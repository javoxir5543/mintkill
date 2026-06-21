#!/bin/bash
set -e

echo "============================================"
echo "  MintKill - Universal Force Quit Installer"
echo "============================================"
echo ""

# 1. Detect package manager
if command -v apt &> /dev/null; then
    PKG_MGR="apt"
    INSTALL_CMD="sudo apt update && sudo apt install -y"
elif command -v dnf &> /dev/null; then
    PKG_MGR="dnf"
    INSTALL_CMD="sudo dnf install -y"
elif command -v pacman &> /dev/null; then
    PKG_MGR="pacman"
    INSTALL_CMD="sudo pacman -S --noconfirm"
else
    echo "No supported package manager found. Please install dependencies manually."
    exit 1
fi

echo "Detected package manager: $PKG_MGR"
echo ""

# 2. Check and install required packages
MISSING=""

if ! command -v xkill &> /dev/null; then
    MISSING+="x11-utils "
fi

if ! python3 -c "import tkinter" &> /dev/null; then
    MISSING+="python3-tk"
fi

if [ -n "$MISSING" ]; then
    echo "Installing missing packages: $MISSING"
    if [ "$PKG_MGR" = "apt" ]; then
        eval "$INSTALL_CMD x11-utils python3-tk"
    elif [ "$PKG_MGR" = "dnf" ]; then
        eval "$INSTALL_CMD xkill python3-tkinter"
    elif [ "$PKG_MGR" = "pacman" ]; then
        eval "$INSTALL_CMD xorg-xkill tk"
    fi
else
    echo "All dependencies are already installed."
fi

echo ""

# 3. Copy files
echo "Copying program files..."
sudo cp mintkill.py /usr/local/bin/
sudo chmod +x /usr/local/bin/mintkill.py

sudo cp mintkill.desktop /usr/share/applications/

# Copy icon if present
if [ -f icon.png ]; then
    sudo mkdir -p /usr/share/icons/hicolor/128x128/apps/
    sudo cp icon.png /usr/share/icons/hicolor/128x128/apps/mintkill.png
    sudo gtk-update-icon-cache -f /usr/share/icons/hicolor/ 2>/dev/null || true
fi

# 4. Update desktop database
if command -v update-desktop-database &> /dev/null; then
    sudo update-desktop-database /usr/share/applications/ 2>/dev/null || true
fi

echo ""
echo "============================================"
echo "  MintKill installed successfully!"
echo "  Find 'MintKill' in your application menu."
echo "============================================"
