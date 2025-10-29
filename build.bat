@echo off
setlocal
REM Windows에서 EXE 파일 빌드 스크립트 (GIF->ICO 변환 포함)

where python >nul 2>nul
if errorlevel 1 (
    echo Python이 설치되어 있지 않습니다. winget으로 Python을 설치합니다...
    winget install -e --id Python.Python.3
    echo Python 설치가 완료되면 창을 닫지 말고 아무 키나 누르세요.
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

REM evernight-march-7th.gif -> evernight-march-7th.ico 변환 (ImageMagick 필요)
if exist evernight-march-7th.gif (
    if not exist evernight-march-7th.ico (
        echo GIF를 ICO로 변환 중...
        convert evernight-march-7th.gif -resize 48x48 evernight-march-7th.ico
        if exist evernight-march-7th.ico (
            echo evernight-march-7th.ico 생성 완료.
        ) else (
            echo evernight-march-7th.ico 변환 실패. (ImageMagick 설치 및 PATH 확인)
        )
    )
)

REM 빌드
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
