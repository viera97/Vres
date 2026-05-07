# 🎬 Vres - Video Resolution Analyzer

**Vres** is a command-line (CLI) tool written in Python that analyzes and classifies video file resolutions using **FFmpeg**.

## 📋 Features

- 🔍 **Fast analysis** of video resolutions
- 📁 **Folder support** with recursive scanning option
- 🎯 **Automatic classification** into resolution categories
- 🎞️ **Multiple formats** supported
- ⚡ **Lightweight and portable** (can be compiled as a standalone executable)

## 📦 Supported Formats

| Format | Extension |
|---------|-----------|
| AVI     | `.avi`    |
| MPEG    | `.mpg`    |
| MP4     | `.mp4`    |
| MKV     | `.mkv`    |
| VOB     | `.vob`    |

## 🏷️ Resolution Classifications

| Category | Minimum Resolution |
|----------|-------------------|\n| 8K       | 7680 × 4320       |
| 4K       | 3840 × 2160       |
| 2K       | 2560 × 1440       |
| FHD      | 1920 × 1080       |
| HD       | 1280 × 720        |
| SD       | < 854 × 480       |

## 🚀 Installation

### Prerequisites

- Python 3.13+
- FFmpeg (must be installed and in system PATH)

### Install from source code

```bash
# Clone the repository
git clone <repository-url>
cd vres

# Install dependencies with uv
uv sync

# Install FFmpeg (Ubuntu/Debian)
sudo apt install ffmpeg

(Arch)
sudo pacman -Sy ffmpeg

(Fedora)
sudo dnf install -S ffmpeg

# Install FFmpeg (macOS)
brew install ffmpeg

# Install FFmpeg (Windows)
# Download from https://ffmpeg.org/download.html
```

## 💻 Usage

### Basic usage

```bash
# Analyze current folder
python Vres.py

# Analyze a specific folder
python Vres.py /path/to/videos

# Recursive analysis (includes subfolders)
python Vres.py /path/to/videos -r
python Vres.py /path/to/videos --recursive
```

### Output example

```
Title: ./videos/movie.mkv
FHD

Title: ./videos/documentary.mp4
4K

Title: ./videos/clip.avi
SD
```

## 🔧 Compile as Executable

The project includes **PyInstaller** configuration to generate a standalone executable.

```bash
# Install PyInstaller
pip install pyinstaller

# Compile
pyinstaller Vres.spec

# The executable will be in dist/Vres
./dist/Vres
```

## 📁 Project Structure

```
vres/
├── Vres.py          # Main analysis script
├── Vres.spec        # PyInstaller configuration
├── main.py          # Alternative entry point
├── pyproject.toml   # Project configuration (uv)
└── README.md        # This file
```

## 🛠️ Development

### Dependency management with uv

```bash
# Add new dependency
uv add <package-name>

# Sync environment
uv sync

# List dependencies
uv pip list
```

## 📝 Dependencies

- **ffmpeg-python**: Python wrapper for FFmpeg
- **pyinstaller**: Compile to standalone executable (development)

## 📄 License

This project is available for free use.

## 🤝 Contributing

Contributions are welcome. Please feel free to submit pull requests or open issues to report bugs or request new features.

---

⭐ If you find it useful, don't forget to star the project!
