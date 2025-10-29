@echo off
REM Windows에서 폴더 형태로 빌드 (더 작은 크기)

echo Installing dependencies...
python -m pip install -r requirements.txt

echo Building executable (folder mode)...
python -m PyInstaller --onedir --windowed --add-data "assets;assets" --name="DesktopPet" main.py

echo.
echo Build complete! 
echo The executable folder is in 'dist/DesktopPet/'
echo Share the entire 'dist/DesktopPet' folder.
echo Run dist/DesktopPet/DesktopPet.exe to start.
pause
