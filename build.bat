
@echo off
setlocal
REM Windows EXE build script (GIF->ICO conversion included, English messages)

where python >nul 2>nul
if errorlevel 1 (
    echo Python not found. Installing with winget...
    winget install -e --id Python.Python.3
    echo After install, press any key to continue.
    pause
)

echo Installing dependencies...
python -m pip install -r requirements.txt

echo Checking assets folder...
if not exist "assets" (
    echo Creating assets folder...
    mkdir assets
    echo WARNING: Please add your character image to assets\character.png
    echo You can add it later and rebuild.
)

REM Convert evernight-march-7th.gif to evernight-march-7th.ico (ImageMagick required)
if exist evernight-march-7th.gif (
    if not exist evernight-march-7th.ico (
        echo Converting GIF to ICO...
        magick evernight-march-7th.gif -resize 48x48 evernight-march-7th.ico
        if exist evernight-march-7th.ico (
            echo evernight-march-7th.ico created.
        ) else (
            echo evernight-march-7th.ico conversion failed. (Check ImageMagick install and PATH)
        )
    )
)

REM Build
echo Building executable...
set "ICON="
if exist evernight-march-7th.ico set "ICON=--icon=evernight-march-7th.ico"
python -m PyInstaller --onefile --windowed --add-data "assets;assets" --name="DesktopPet" %ICON% main.py

echo.
echo Build complete!
echo The executable is in the 'dist' folder.
echo.
echo IMPORTANT: Make sure assets\character.png exists before running!
echo Run dist\DesktopPet.exe to start the desktop pet.
endlocal
pause
