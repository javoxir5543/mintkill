#!/usr/bin/env python3
"""
MintKill – Universal dastur o‘ldirgich
X11 da: sichqoncha bilan oynani chertib o‘ldiradi (xkill)
Wayland da: jarayon nomini kiritib o‘ldiradi (killall)
Barcha Linux distributivlarida ishlaydi.
"""

import os
import sys
import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

def x11_kill():
    """X11 muhitida xkill ishga tushiriladi."""
    if subprocess.call(['which', 'xkill'], stdout=subprocess.DEVNULL) == 0:
        subprocess.run(['xkill'])
    else:
        messagebox.showerror("Xatolik",
            "xkill topilmadi.\nIltimos, 'sudo apt install x11-utils' (yoki paket menejeringiz) orqali o‘rnating.")
        sys.exit(1)

def wayland_kill():
    """Wayland muhitida jarayon nomi so‘raladi va killall -9 orqali o‘ldiriladi."""
    root = tk.Tk()
    root.withdraw()  # asosiy oynani yashirish
    proc_name = simpledialog.askstring("Majburiy yopish",
                                       "Jarayon nomini kiriting (masalan, firefox, libreoffice):")
    if proc_name:
        try:
            subprocess.run(['killall', '-9', proc_name], check=True)
            messagebox.showinfo("Bajarildi", f"'{proc_name}' majburan yopildi.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Xatolik", f"'{proc_name}' nomli jarayon topilmadi yoki o‘ldirib bo‘lmadi.")
    root.destroy()

if __name__ == '__main__':
    # Qaysi grafik muhitda ekanligimizni aniqlaymiz
    session_type = os.environ.get('XDG_SESSION_TYPE', 'x11').lower()

    if session_type == 'wayland':
        wayland_kill()
    else:
        # X11 yoki noma’lum holatda xkill ga tayanamiz
        x11_kill()
