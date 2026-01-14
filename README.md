# ⚒️ AssetForge

> **Professional asset optimization for web and games.**
> *No dependencies. No hassle. Ready to use.*

AssetForge is a command-line tool (CLI) designed for developers, designers, and technical artists. It automates batch image processing, optimizing workflows for **Flutter, Unity, Unreal Engine, and Web** projects.

## ✨ Key Features

- **🖼️ Background Removal (AI)**: Automatically remove backgrounds from sprites, products, or icons using CPU-safe AI.
- **📐 Vectorization (Bitmap to SVG)**: Convert pixelated logos or sketches into high-quality scalable SVG vectors.
- **⚡ WebP Optimization**: Automatically generate `1x`, `2x`, and `3x` variants for high-performance mobile and web apps.
- **🎥 WebM Video**: Convert `.mp4`, `.mov`, `.avi` to efficient `.webm` format for the web.
- **🚀 Total Portability**: No Python installation or external libraries required. Works on Windows, Linux, and MacOS.

---

## 📥 Download & Installation (End Users)

You don't need to know how to code to use AssetForge. Just download the installer.

1.  Go to the **[Releases](../../releases)** section of this repository.
2.  Download the `.zip` (Windows) or `.tar.gz` (Linux/Mac) file for your system.
3.  **Unzip** the downloaded file.
4.  Run the included automatic installer:

### 🪟 Windows
Double-click the `install.bat` file (included in release). 
*(Or run `installers\install_windows.bat` from source).*

### 🐧 Linux / 🍎 Mac
Open a terminal in the unzipped folder and run:
```bash
chmod +x install.sh
./install.sh
```
*(Or run `installers/install_unix.sh` from source).*

---

## 🛠️ Usage

Once installed, open any terminal (PowerShell, CMD, Bash) and use the `assetforge` command.

### 1. Remove Background
Clean all `.png` or `.jpg` images in a folder.
```bash
# Process current folder
assetforge remove-bg .

# Process specific folder
assetforge remove-bg "C:/My Projects/Assets/Icons"
```

### 2. Create SVGs
Convert images to vectors.
```bash
assetforge svg .
```

### 3. Generate WebP Assets
Create optimized mobile versions (1x, 2x, 3x assets).
```bash
assetforge webp .
```

### 4. Convert to WebM (Video)
Convert mp4/mov/avi videos to WebM.
```bash
assetforge webm .
```

### 5. Web Aggressive Optimization
Convert images to WebP and videos to WebM, **deleting the originals** (backups are created).
```bash
assetforge web .
```

---

## 👨‍💻 Developer Zone (Source Code)

If you are a developer and want to contribute or run the project from source (Python):

### Requirements
- Python 3.8 or higher.
- `pip` installed.

### Local Installation (Editable Mode)
```bash
# Clone repository
git clone git@github.com:peluza/asset-forge.git
cd asset-forge/scripts

# Install dependencies and link command
pip install -e .
```

### Direct Execution
```bash
python asset_forge.py --help
```

### Build Executables
If you want to generate your own `.exe` binaries:

- **Windows**: Run `builders\build.bat`.
- **Linux/Mac**: Run `builders/build.sh`.

Artifacts will be generated in the `dist/` folder.

---

## 📄 License

This project is **Open Source** and distributed under the **MIT License**.
You are free to use, modify, and distribute it in personal or commercial projects.

```text
MIT License
Copyright (c) 2026 editech.dev
```

---
<p align="center">
  Made with ❤️ by <b>editech.dev</b>
</p>
