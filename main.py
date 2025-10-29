#!/usr/bin/env python3
"""
Desktop Invasion - Prank Program
화면에 캐릭터가 계속 증식하는 장난 프로그램 🎭
경고: 친구들에게만 사용하세요!
"""

import tkinter as tk
from tkinter import Canvas, messagebox
from PIL import Image, ImageTk
import random
import os
import sys
import threading
import time

# 전역 윈도우 리스트
all_windows = []
spawn_active = True
secret_code = []  # Konami 코드 같은 비밀 종료 키


class DesktopInvader:
    def __init__(self, image_path, spawn_more=True):
        self.root = tk.Tk()
        self.root.title("Don't Close Me! :)")
        self.spawn_more = spawn_more
        
        # 이미지 로드
        try:
            self.original_image = Image.open(image_path)
            self.original_image = self.original_image.convert("RGBA")
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            sys.exit(1)
        
        # 랜덤 크기 (더 다양하게)
        size = random.choice([80, 100, 120, 150, 180, 200, 250])
        self.image_size = (size, size)
        self.image = self.original_image.resize(self.image_size, Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        
        # 화면 크기
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 랜덤 위치
        x = random.randint(0, max(0, screen_width - self.image_size[0]))
        y = random.randint(0, max(0, screen_height - self.image_size[1]))
        
        # 윈도우 설정
        self.root.geometry(f"{self.image_size[0]}x{self.image_size[1]}+{x}+{y}")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        
        # 투명도
        try:
            self.root.attributes('-transparentcolor', 'white')
            self.root.config(bg='white')
        except:
            pass
        
        # 캔버스
        self.canvas = Canvas(
            self.root,
            width=self.image_size[0],
            height=self.image_size[1],
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
        # 이벤트 바인딩
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<Double-Button-1>", self.on_double_click)
        self.root.bind("<Key>", self.on_key_press)
        
        # 닫기 시도 감지
        self.root.protocol("WM_DELETE_WINDOW", self.on_close_attempt)
        
        # 랜덤 움직임 시작
        self.moving = random.choice([True, False])
        if self.moving:
            self.start_random_movement()
        
        # 전역 리스트에 추가
        all_windows.append(self)
    
    def on_click(self, event):
        """클릭하면 도망가기"""
        self.escape()
        if self.spawn_more and random.random() < 0.3:  # 30% 확률로 증식
            threading.Thread(target=spawn_new_window, daemon=True).start()
    
    def on_right_click(self, event):
        """우클릭하면 더 많이 생성!"""
        if self.spawn_more:
            for _ in range(random.randint(2, 4)):
                threading.Thread(target=spawn_new_window, daemon=True).start()
    
    def on_double_click(self, event):
        """더블클릭 = 폭발적 증식"""
        if self.spawn_more:
            messagebox.showwarning("Oops!", "왜 더블클릭을 했어요? 😈")
            for _ in range(random.randint(3, 6)):
                threading.Thread(target=spawn_new_window, daemon=True).start()
    
    def on_close_attempt(self):
        """창 닫기 시도 시"""
        if self.spawn_more:
            # 닫으려 하면 더 많이 생성!
            messages = [
                "안 돼요! 😭",
                "나를 닫지 마세요!",
                "친구가 되어줘요!",
                "좀만 더 놀아요!",
                "닫으면 친구 데려올거에요! 👯"
            ]
            messagebox.showinfo("Please Don't!", random.choice(messages))
            
            for _ in range(random.randint(2, 5)):
                threading.Thread(target=spawn_new_window, daemon=True).start()
        else:
            self.root.destroy()
    
    def on_key_press(self, event):
        """비밀 종료 코드: ESC 5번"""
        global secret_code
        secret_code.append(event.keysym)
        if len(secret_code) > 10:
            secret_code.pop(0)
        
        # ESC를 5번 연속 누르면 종료
        if secret_code[-5:] == ['Escape'] * 5:
            self.emergency_shutdown()
    
    def emergency_shutdown(self):
        """긴급 종료"""
        global spawn_active
        spawn_active = False
        messagebox.showinfo("해방!", "축하합니다! 비밀 코드를 발견했어요! 🎉")
        for window in all_windows:
            try:
                window.root.destroy()
            except:
                pass
    
    def escape(self):
        """다른 위치로 도망"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = random.randint(0, max(0, screen_width - self.image_size[0]))
        y = random.randint(0, max(0, screen_height - self.image_size[1]))
        
        try:
            self.root.geometry(f"+{x}+{y}")
        except:
            pass
    
    def start_random_movement(self):
        """랜덤하게 움직이기"""
        def move():
            while True:
                try:
                    if not self.root.winfo_exists():
                        break
                    time.sleep(random.uniform(2, 5))
                    self.escape()
                except:
                    break
        
        threading.Thread(target=move, daemon=True).start()
    
    def run(self):
        """실행"""
        self.root.mainloop()


def spawn_new_window():
    """새 창 생성"""
    global spawn_active
    if not spawn_active or len(all_windows) >= 50:  # 최대 50개로 제한 (너무 많으면 위험)
        return
    
    time.sleep(random.uniform(0.1, 0.5))  # 약간의 딜레이
    
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    image_path = os.path.join(base_path, "assets", "character.png")
    
    try:
        invader = DesktopInvader(image_path, spawn_more=True)
        threading.Thread(target=invader.run, daemon=True).start()
    except:
        pass


def show_welcome():
    """시작 메시지"""
    root = tk.Tk()
    root.withdraw()
    
    response = messagebox.askyesno(
        "경고! ⚠️",
        "이 프로그램은 장난용 프로그램입니다.\n\n"
        "실행하면 화면에 캐릭터가 증식합니다!\n"
        "닫으려 하면 더 많이 생깁니다! 😈\n\n"
        "비밀 종료 방법: ESC 키를 5번 연속 누르세요\n\n"
        "정말 실행하시겠습니까?"
    )
    
    root.destroy()
    return response


if __name__ == "__main__":
    # 사용자 동의 확인
    if not show_welcome():
        sys.exit(0)
    
    # 이미지 경로
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    image_path = os.path.join(base_path, "assets", "character.png")
    
    # 초기 창 3개 생성
    initial_count = random.randint(3, 5)
    for i in range(initial_count):
        if i == 0:
            # 첫 번째는 메인 스레드에서
            invader = DesktopInvader(image_path, spawn_more=True)
        else:
            # 나머지는 별도 스레드에서
            threading.Thread(target=spawn_new_window, daemon=True).start()
        time.sleep(0.3)
    
    # 자동 증식 스레드
    def auto_spawn():
        """자동으로 가끔 새 창 생성"""
        while spawn_active:
            time.sleep(random.uniform(5, 15))  # 5~15초마다
            if spawn_active and len(all_windows) < 30:
                spawn_new_window()
    
    threading.Thread(target=auto_spawn, daemon=True).start()
    
    # 메인 루프 실행
    invader.run()
ㅇ