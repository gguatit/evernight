#!/bin/bash
# Linux/Mac에서 실행 파일 빌드 스크립트

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Building executable..."
pyinstaller --onefile --windowed --add-data "assets:assets" --name="DesktopPet" main.py

echo ""
echo "Build complete!"
echo "The executable is in the 'dist' folder."
echo "Run ./dist/DesktopPet to start the desktop pet."
