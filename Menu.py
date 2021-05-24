from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter.messagebox

    
# Menu 보여주는 화면
def home(win):
    for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
        wg.destroy()             # 위젯 제거
    
    #######################################################
    #frame1: 공백
    frame1 = LabelFrame(win, bd='0', height='100')
    frame1.pack(side='top', fill=X)

    #######################################################
    # frame2: 메뉴 버튼들
    frame2 = LabelFrame(win, bd='0')
    frame2.pack(fill=X, expand=TRUE)
    
    from Play import play_game
    bt1 = Button(frame2, text = "Game Start", width ='13', command = partial(play_game, win), bg='#CFFFE5', fg='black', font="default_font 20") # 버튼 생성
    bt1.grid(row=1, column=1, rowspan=1, padx =95, pady=20)

    from addHint import add_HintCode
    bt2 = Button(frame2, text = "Add Hint", width ='13', command = partial(add_HintCode, win), bg='#CFFFE5', fg='black', font="default_font 20") # 버튼 생성
    bt2.grid(row=2, column=1, rowspan=1, pady=20)

    from delHint import del_hintCode
    bt3 = Button(frame2, text = "Delete Hint", width ='13', command = partial(del_hintCode, win), bg='#CFFFE5', fg='black', font="default_font 20") # 버튼 생성
    bt3.grid(row=3, column=1, rowspan=1, pady=20)
    
    from listHint import show_hintList
    bt4 = Button(frame2, text = "Hint Code List", width ='13', command = partial(show_hintList, win), bg='#CFFFE5', fg='black', font="default_font 20") # 버튼 생성
    bt4.grid(row=4, column=1, rowspan=1, pady=20)
    
    #######################################################
    #frame3: 공백
    frame3 = LabelFrame(win, bd='0', height='100')
    frame3.pack(side='bottom', fill=X)
    