from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter.messagebox


#게임 시작 버튼 화면
def play_game(win):
    for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
        wg.destroy()             # 위젯 제거
        
    # Button : 게임 시작 버튼(전체화면)
    frame1 = LabelFrame(win)
    frame1.pack(fill=BOTH, expand=TRUE)
    
    bt_gameStart = Button(frame1, text = "게임 시작", command = partial(input_hintCode, win), bg='#CFFFE5', fg='black', font="default_font 30") # 버튼 생성
    bt_gameStart.pack(fill=BOTH, expand=TRUE)


#힌트 입력하는 화면
def input_hintCode(win):
    for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
        wg.destroy()             # 위젯 제거  
    
    #############################################################
    # frame1: 공백
    frame1 = LabelFrame(win, bd='0', height='150')
    frame1.pack(side='top', fill=X)
    
    #############################################################
    #frame2: Hint Code 입력
    frame2 = LabelFrame(win,text='Hint Code', labelanchor='n', font="default_font 25")
    frame2.pack(side='top',fill=X)
    
    #공백 라벨
    lb_empty1 = Label(frame2)
    lb_empty1.grid(row = 1, column = 0)
    
    lb_empty2 = Label(frame2)
    lb_empty2.grid(row = 1, column = 1)
    
    #힌트코드 입력폼
    global useHint
    useHint = Entry(frame2, font="default_font 25", width=15)
    useHint.grid(row = 1, column = 2, padx = 10, pady = 10)
    
    #힌트 사용 버튼
    bt1 = Button(frame2, text = 'Use', command = partial(search_hint, win), bg = '#CFFFE5', width = 3)
    bt1.grid(row = 1, column = 3, padx = 10, pady = 10)
    
    #############################################################
    # frame3: 뒤로가기 버튼
    frame3 = LabelFrame(win, bd='0', height='50')
    frame3.pack(side='bottom', fill=X)
    
    from Menu import home
    bt1 = Button(frame3, text = '←', command = partial(home, win), bg = '#CFFFE5')
    bt1.grid(row=1, column=1, columnspan=1, padx =20, pady =20)

    

#힌트 알려주는 화면
def output_hint(win, useHintCode):
    for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
        wg.destroy()             # 위젯 제거
    
    #############################################################
    # frame1: 공백
    frame1 = LabelFrame(win, bd='0', height='100')
    frame1.pack(side='top', fill=X)
    
    #############################################################
    # frame2: 힌트 내용 표시 
    frame2 = LabelFrame(win, pady = 10, text=useHintCode, labelanchor='n', font="default_font 25")
    frame2.pack(side='top', fill=BOTH, expand=1)
    
    #힌트 내용 표시 라벨
    from Hint import hintList
    showHint = Label(frame2, text = hintList[useHintCode], font="default_font 15", wraplength='350')
    showHint.grid(padx = 30, pady = 30)
    showHint.pack(fill=BOTH, expand=1)
    
    useHintCode = frame2.cget('text')
    #############################################################
    # frame3: (Menu로) 돌아가기 버튼 / 힌트코드 입력으로 돌아가기 버튼
    frame3 = LabelFrame(win, bd='0', height='50')
    frame3.pack(side='bottom', fill=BOTH, expand=1)   
    
    from Menu import home
    bt1 = Button(frame3, text = 'Menu', command = partial(home, win), bg = '#CFFFE5')
    bt2 = Button(frame3, text = '←', command = partial(input_hintCode, win), bg = '#CFFFE5')

    bt1.grid(row=1, column=1, columnspan=1, padx =77, pady =50)
    bt2.grid(row=1, column=3, columnspan=1, padx =77, pady =50)
    
    
#힌트리스트에 있는 힌트 코드를 입력했는지 검사하는 기능
def search_hint(win):
    useHintCode = useHint.get()
    
    from Hint import hintList
    if useHintCode in hintList:
        output_hint(win, useHintCode)
    else: #잘못된 힌트 코드를 입력했을 때, 경고창
        tkinter.messagebox.showerror( "Hint Code", "잘못된 코드입니다. 다시 입력하세요.")
        input_hintCode(win) #힌트 입력으로 되돌아가기