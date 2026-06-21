import sys
import os
import ctypes
import subprocess

# ---------- Administrator huquqi ----------
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

if not is_admin():
    run_as_admin()

# ---------- Asosiy dastur ----------
import tkinter as tk
import win32gui
import win32process

def kill_window_at_cursor():
    """Kursor ostidagi oynaning jarayon daraxtini butunlay yo‘q qilish."""
    x, y = win32gui.GetCursorPos()
    hwnd = win32gui.WindowFromPoint((x, y))
    if hwnd:
        class_name = win32gui.GetClassName(hwnd)
        if class_name not in ("Progman", "Shell_TrayWnd", "WorkerW"):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            if pid and pid != os.getpid():
                subprocess.run(['taskkill', '/F', '/PID', str(pid), '/T'],
                               capture_output=True)

def on_click(event):
    """Chap tugma bosilganda: avval oynani yashir, keyin o‘ldir, so‘ng dasturni yop."""
    root.withdraw()
    root.update_idletasks()
    kill_window_at_cursor()
    root.destroy()

# ---------- Dim effect bilan to‘liq ekran oyna ----------
root = tk.Tk()

# Alt+Tab va Taskbarda ko‘rinmaydigan qilish
root.overrideredirect(True)

# Ekran o‘lchamini qo‘lda o‘rnatamiz
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Oynani eng tepaga olib chiqamiz
root.attributes('-topmost', True)

# *** DIM EFFECT ***
# Shaffoflik 40% – ekran sezilarli qorayadi, lekin ostidagi dasturlar ko‘rinadi
root.attributes('-alpha', 0.4)

# Orqa fonni qora qilamiz (shaffoflik orqali qoraytirish)
root.configure(bg='black')

# Kursor xoch (+) bo‘ladi
root.config(cursor='crosshair')

# Hodisalarni bog‘lash
root.bind('<Button-1>', on_click)                # chap tugma → o‘ldirish
root.bind('<Button-3>', lambda e: root.destroy()) # o‘ng tugma → bekor qilish
root.bind('<Escape>', lambda e: root.destroy())   # Esc → bekor qilish

root.mainloop()