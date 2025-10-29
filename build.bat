@echo off
REM Windows에서 EXE 파일 빌드 스크립트

echo Installing dependencies...
pip install -r requirements.txt

echo Building executable...
pyinstaller --onefile --windowed --add-data "assets;assets" --icon=assets/character.png --name="DesktopPet" main.py

echo.
echo Build complete! 
echo The executable is in the 'dist' folder.
echo Run dist\DesktopPet.exe to start the desktop pet.
pause
