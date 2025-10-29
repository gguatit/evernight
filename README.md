# Desktop Invasion - 장난 프로그램

화면에 캐릭터가 계속 증식하는 재미있는 프랭크(prank) 프로그램입니다!

**경고**: 이것은 장난용 프로그램입니다. 친구들에게만 사용하세요!

## 기능

- 화면에 캐릭터가 랜덤하게 증식
- 클릭하면 도망가고 새 친구를 데려옴
- 우클릭하면 더 많이 증식
- 더블클릭하면 폭발적으로 증식
- 닫으려 하면 더욱 많이 생성
- 일부는 스스로 움직임
- 투명 배경 (Windows)
- 항상 최상위 표시
- **비밀 종료 코드**: ESC 키 5번 연속

## 빠른 시작

### 1. 이미지 준비

첨부된 캐릭터 이미지를 다음 위치에 저장하세요:
```
assets/character.png
```

PNG 또는 GIF 형식의 투명 배경 이미지를 권장합니다.

### 2-A. Python으로 직접 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 프로그램 실행
python main.py
```

### 2-B. EXE 파일로 빌드 (Windows)

**옵션 1: 단일 파일 (추천)**
```cmd
# build.bat 실행
build.bat

# 생성된 EXE 실행
dist\DesktopPet.exe
```

특징:
- Python 설치 불필요
- 파일 하나만 있으면 됨
- 어떤 Windows PC에서도 실행 가능
- 크기: 약 10~20MB

**옵션 2: 폴더 형태 (더 작은 용량)**
```cmd
# build_folder.bat 실행
build_folder.bat

# 폴더 전체를 공유하고 실행
dist\DesktopPet\DesktopPet.exe
```

특징:
- 전체 폴더를 공유해야 함
- 더 작은 용량

### 2-C. 실행 파일 빌드 (Linux/Mac)

```bash
# 실행 권한 부여
chmod +x build.sh

# 빌드
./build.sh

# 실행
./dist/DesktopPet
```

## 동작 방식

| 동작 | 결과 |
|------|------|
| **클릭** | 도망가고 30% 확률로 증식 |
| **우클릭** | 2~4개 증식 |
| **더블클릭** | 3~6개 폭발적 증식 |
| **창 닫기 시도** | 2~5개 증식 + 메시지 |
| **자동 증식** | 5~15초마다 자동으로 1개 추가 |
| **ESC 5번 연속** | 비밀 종료 코드 - 모든 창 닫기 |

## 안전 기능

- 최대 50개로 제한 (시스템 부하 방지)
- 시작 시 경고 메시지 표시
- 비밀 종료 코드 제공 (ESC x5)

## 커스터마이징

### 증식 속도 조절

`main.py`에서 다음 값들을 수정하세요:

```python
# 클릭 시 증식 확률 (현재: 30%)
if random.random() < 0.3:

# 우클릭 시 증식 개수 (현재: 2~4개)
for _ in range(random.randint(2, 4)):

# 더블클릭 시 증식 개수 (현재: 3~6개)
for _ in range(random.randint(3, 6)):

# 자동 증식 간격 (현재: 5~15초)
time.sleep(random.uniform(5, 15))

# 최대 개수 (현재: 50개)
if not spawn_active or len(all_windows) >= 50:
```

### 비밀 종료 코드 변경

```python
# ESC 5번 대신 다른 키/횟수로 변경
if secret_code[-5:] == ['Escape'] * 5:
# 예: 'q' 키 3번
if secret_code[-3:] == ['q'] * 3:
```

## 빌드 결과물

### 단일 파일 빌드 (build.bat)

```
dist/
  └── DesktopPet.exe    ← 이 파일 하나만!
```

**특징:**
- ✅ Python 설치 **완전히 불필요**
- ✅ 모든 라이브러리 **내장**
- ✅ 이미지 파일 **포함**
- ✅ 어떤 Windows PC에서도 실행
- 📦 크기: 약 10~20MB
- 🚀 **이 파일만 공유하면 끝!**

### 폴더 빌드 (build_folder.bat)

```
dist/
  └── DesktopPet/
      ├── DesktopPet.exe
      ├── _internal/        ← 필요한 파일들
      └── ...
```

**특징:**
- 📁 전체 폴더를 공유해야 함
- 💾 각 파일이 작아서 관리 용이
- 📦 총 크기는 비슷함

## 💻 시스템 요구사항

### 빌드할 때 (개발자)
- Python 3.8 이상
- Windows / Linux / macOS
- 메모리: 최소 100MB

### 실행할 때 (사용자)
- ✅ **Python 설치 불필요!**
- Windows 7 이상 / Linux / macOS
- 메모리: 최소 50MB
- **그냥 EXE 더블클릭만 하면 됨!**

### 이미지를 찾을 수 없음
```
Error: Image not found at assets/character.png
```
→ `assets/character.png` 파일이 있는지 확인하세요.

### 너무 많이 생겨서 멈출 수 없어요!
→ **ESC 키를 5번 연속으로 누르세요!** (비밀 종료 코드)

### 투명도가 작동하지 않음
- Windows 7/10/11에서는 `-transparentcolor` 속성으로 흰색 배경이 투명하게 처리됩니다.
- Linux에서는 컴포지터(Compositor)가 필요할 수 있습니다.

### 프로그램이 응답하지 않음
- 작업 관리자(Ctrl+Shift+Esc)로 Python 프로세스 종료
- 또는 `taskkill /F /IM DesktopPet.exe` (Windows CMD)

## 추천 이미지 설정

- 형식: PNG (투명 배경)
- 크기: 200x200 ~ 500x500 픽셀
- 애니메이션: GIF도 지원 가능 (추가 코드 필요)

## 📄 라이선스

MIT License - 자유롭게 수정하고 배포할 수 있습니다.

## 사용 시나리오

### 친구 컴퓨터에서 (장난)
1. EXE 파일을 친구 컴퓨터로 전송
2. 친구가 실행
3. 웃으며 ESC 5번 알려주기

### 선물용 (재미)
1. 재미있는 캐릭터 이미지 준비
2. 빌드 후 선물
3. 비밀 코드도 함께 알려주기

### 스트리밍/영상용
1. 방송 중 실행
2. 시청자들과 함께 즐기기
3. ESC x5로 마무리

---

**경고**: 책임 있게 사용하세요! 이 프로그램은 교육 및 오락 목적입니다.

## 라이선스

MIT License - 자유롭게 수정하고 배포할 수 있습니다.
