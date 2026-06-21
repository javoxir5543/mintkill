# MintKill — Universal Force Quit App

[English](#english) | [Русский](#русский) | [O‘zbek](#ozbek)

---

## English

A tiny, cross-desktop utility to forcefully kill frozen applications on any Linux distribution.  
It detects your session type (X11 or Wayland) and adapts automatically:

- **X11** – cursor turns into a skull, click the frozen window to kill it (uses `xkill`).
- **Wayland** – a dialog asks for the process name and runs `killall -9`.

### Installation

```bash
git clone https://github.com/yourusername/mintkill.git
cd mintkill
chmod +x install.sh
./install.sh
