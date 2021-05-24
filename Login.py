from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from functools import partial


win = Tk() # 창 만들기

win.title("ESCAPE ROOM") # 창 제목 변경
win.geometry("400x550") # 창 크기 변경
win.option_add("*Font","default_font 15") # 창 내에 생기는 위젯의 폰트 설정

# 사용자 id와 password를 저장하는 변수 생성
user_id, password = StringVar(), StringVar()
    
# 사용자 id와 password가 맞는지 비교하는 기능
def check_admin():
    if user_id.get() == "admin" and password.get() == "admin":
        from Menu import home
        home(win) #홈화면 호출
    else:
        tkinter.messagebox.showerror("계정 오류", "계정이 일치하지 않습니다. 다시 입력하세요.")
        id.delete(0, END)
        pw.delete(0, END)


#######################################################
# frame1: 배너
frame1 = LabelFrame(win, bd = '0')
frame1.pack(side="top", fill=BOTH, expand=TRUE)

title = Label(frame1, text='ESCAPE ROOM', fg='black', font="default_font 30")
title.pack(side='bottom', fill=BOTH, expand=TRUE)

#######################################################
# frame2: ID, PW 부분
frame2 = LabelFrame(win, bd = '0')
frame2.pack(fill=BOTH, expand=TRUE)

#공백 라벨
empty1 = Label(frame2)
empty1.grid(row = 0, column = 0, padx = 10, pady = 10)

#ID 라벨
id_login = Label(frame2, text = "ID : ")
id_login.grid(row = 3, column = 1, padx = 10, pady = 10)

#PW 라벨
pw_login = Label(frame2, text = "PW : ")
pw_login.grid(row = 4, column = 1, padx = 10, pady = 10)

#ID 입력
id = Entry(frame2, textvariable = user_id)
id.grid(row = 3, column = 2, padx = 10, pady = 10)

#PW 입력
pw = Entry(frame2, textvariable = password)
pw.grid(row = 4, column = 2, padx = 10, pady = 10)

#로그인 버튼
Button(frame2, text = "Login", command = partial(check_admin), bg='#CFFFE5').grid(row = 5, column = 2, ipadx = 20, padx = 10, pady = 10)



win.mainloop()