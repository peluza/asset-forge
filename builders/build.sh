#!/bin/bash
cd "$(dirname "$0")/.."
echo "--- Installing dependencies ---"
pip install -r requirements.txt

echo "--- Building Executable with PyInstaller ---"
python -m PyInstaller --noconfirm --onefile --console --name "assetforge" --hidden-import="PIL" --hidden-import="rembg" --hidden-import="vtracer" asset_forge.py

echo ""
echo "--- PROCESS COMPLETED ---"
echo "The executable is located in: dist/assetforge"
echo ""
