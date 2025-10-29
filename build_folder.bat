@echo off
REM Windows에서 폴더 형태로 빌드 (더 작은 크기)

echo Installing dependencies...
python -m pip install -r requirements.txt

echo Checking assets folder...
if not exist "assets" (
    echo Creating assets folder...
    mkdir assets
    echo WARNING: Please add your character image to assets\character.png
    echo You can add it later and rebuild.
)

echo Building executable (folder mode)...
python -m PyInstaller --onedir --windowed --add-data "assets;assets" --name="DesktopPet" main.py

echo.
echo Build complete! 
echo The executable folder is in 'dist/DesktopPet/'
echo Share the entire 'dist/DesktopPet' folder.
echo.
echo IMPORTANT: Make sure assets\character.png exists before running!
echo Run dist/DesktopPet/DesktopPet.exe to start.
pause
