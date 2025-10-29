@echo off
REM Windows에서 EXE 파일 빌드 스크립트

echo Installing dependencies...
python -m pip install -r requirements.txt

echo Building executable...
python -m PyInstaller --onefile --windowed --add-data "assets;assets" --name="DesktopPet" main.py

echo.
echo Build complete! 
echo The executable is in the 'dist' folder.
echo Run dist\DesktopPet.exe to start the desktop pet.
pause
