from tkinter import *
from PIL import Image, ImageTk
import os
import win

root = win.getWindow()

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'images.png')
photo = PhotoImage(file=image_path)

btn = Button(root, image=photo)  # root라는 창에 버튼을 생성

btn.config(width=photo.width(), height=photo.height()) 
# 버튼의 크기 설정 ( 버튼 크기 고정 )
btn.config(padx=20, pady=20) 
# 버튼의 크기 절정 ( 글자 수에 따라 크기 달라짐 값은 글자와 버튼 테두리 사이의 거리 값)
btn.config(text="버튼")
# 버튼의 내용 설정
btn.config(fg="red", bg="yellow")
# 버튼의 글자색(fg)과 배경색(bg) 설정

btn.pack()          # 만든 버튼을 창에 배치


root.mainloop()