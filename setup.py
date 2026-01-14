from setuptools import setup, find_packages

setup(
    name="asset-forge",
    version="1.0.0",
    description="AssetForge: Professional Asset Optimization Tool",
    author="editech.dev",
    author_email="contact@editech.dev",
    url="https://editech.dev",
    packages=find_packages(),
    # py_modules removed in favor of find_packages detecting 'core'
    py_modules=["asset_forge"],
    install_requires=[
        "rembg[cpu]", # Force CPU version for broader compatibility in portable builds
        "Pillow",
        "vtracer",
        "pyinstaller",
        "imageio",
        "imageio-ffmpeg" 
    ],
    entry_points={
        "console_scripts": [
            "assetforge=asset_forge:main",
        ],
    },
)
