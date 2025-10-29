# 이 bat 파일은 evernight-march-7th.gif를 ico로 변환합니다.
# ImageMagick이 설치되어 있어야 합니다.

@echo off
setlocal

set GIF=evernight-march-7th.gif
set ICO=evernight-march-7th.ico

if not exist %GIF% (
    echo %GIF% 파일이 없습니다.
    exit /b 1
)

:: ImageMagick convert 명령어로 ico 생성 (48x48)
convert %GIF% -resize 48x48 %ICO%

if exist %ICO% (
    echo %ICO% 생성 완료.
) else (
    echo 변환 실패.
)

endlocal
pause
