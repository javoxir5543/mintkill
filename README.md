English / Русский / O‘zbek (Bitta matnda)
MintKill – a tiny, cross‑desktop utility to forcefully kill frozen applications on any Linux distribution.
MintKill – миниатюрная кроссплатформенная утилита для принудительного завершения зависших приложений в любом дистрибутиве Linux.
MintKill – har qanday Linux distributivida muzlab qolgan dasturlarni majburan yopish uchun mo‘ljallangan kichik dastur.

It automatically detects your session type: X11 or Wayland.
Он автоматически определяет тип сеанса: X11 или Wayland.
U sessiya turini avtomatik aniqlaydi: X11 yoki Wayland.

On X11 – the cursor turns into a skull, simply click the frozen window to kill it (uses xkill).
В X11 – курсор превращается в череп, достаточно щёлкнуть по зависшему окну, чтобы закрыть его (используется xkill).
X11 da – sichqoncha ko‘rsatkichi bosh suyagiga aylanadi, muzlagan oynani cherting ( xkill ishlatiladi).

On Wayland – a dialog asks for the process name (e.g., firefox, libreoffice) and forcefully kills it (killall -9).
В Wayland – появляется диалог, введите имя процесса (например, firefox, libreoffice) и он будет принудительно завершён (killall -9).
Wayland da – dialog oynasiga jarayon nomini (masalan, firefox, libreoffice) kiriting, u majburan yopiladi (killall -9).

Installation / Установка / O‘rnatish

git clone https://github.com/javoxir5543/mintkill.git
cd mintkill
chmod +x install.sh
./install.sh

Or manually (или вручную, yoki qo‘lda):

sudo cp mintkill.py /usr/local/bin/
sudo chmod +x /usr/local/bin/mintkill.py
sudo cp mintkill.desktop /usr/share/applications/


Requirements / Зависимости / Talablar
Python 3

Tkinter (python3-tk, python3-tkinter or tk)

X11 only / только для X11 / faqat X11 uchun: x11-utils (provides xkill)

Wayland: no extra packages / дополнительных пакетов не требуется / qo‘shimcha paketlar kerak emas (built‑in killall).

Usage / Использование / Ishlatish
Launch MintKill from your applications menu.
Запустите MintKill из меню приложений.
Ilovalar menyusidan MintKill ni ishga tushiring.

On X11, click the frozen window.
В X11 щёлкните по зависшему окну.
X11 bo‘lsa, muzlagan oynani cherting.

On Wayland, type the process name (e.g., firefox) and press Enter.
В Wayland введите имя процесса (например, firefox) и нажмите Enter.
Wayland bo‘lsa, jarayon nomini (masalan, firefox) yozing va Enter bosing.

License / Лицензия / Litsenziya
MIT – free to use, modify, and distribute.
Свободное использование, модификация и распространение.
Erkin foydalanish, o‘zgartirish va tarqatish.
