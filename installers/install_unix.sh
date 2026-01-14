#!/bin/bash
echo "--- AssetForge Installer (Linux/Mac) ---"

# Detect script location
DIR="$(cd "$(dirname "$0")" && pwd)"
EXE_NAME="assetforge"

# Case 1: Release (exe is next to script)
if [ -f "$DIR/$EXE_NAME" ]; then
    SOURCE="$DIR/$EXE_NAME"
# Case 2: Dev (exe is in ../dist)
elif [ -f "$DIR/../dist/$EXE_NAME" ]; then
    SOURCE="$DIR/../dist/$EXE_NAME"
else
    echo "[ERROR] '$EXE_NAME' not found."
    echo "Please make sure to run the build script or download the full package."
    exit 1
fi

echo "Source detected: $SOURCE"
echo "Creating symbolic link in /usr/local/bin"
echo "This requires administrator privileges (sudo)."
echo ""

LINK_NAME="/usr/local/bin/$EXE_NAME"

sudo ln -sf "$SOURCE" "$LINK_NAME"

if [ $? -eq 0 ]; then
    echo ""
    echo "[SUCCESS] AssetForge installed correctly."
    echo "You can now use the 'assetforge' command from any terminal."
else
    echo ""
    echo "[ERROR] Failed to create symbolic link."
fi
