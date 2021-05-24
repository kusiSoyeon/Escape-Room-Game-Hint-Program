from tkinter import *
from tkinter import ttk
from functools import partial
from Hint import hintList
   
#힌트 코드 목록을 보여주는 창
def show_hintList(win):
    for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
        wg.destroy()             # 위젯 제거
        
    h_list = ""
    
    for key in hintList.keys():
    	h_list = h_list + key + '\n\n'
    
    #############################################################
    # frame0: 공백
    frame0 = LabelFrame(win, bd='0', height='20')
    frame0.pack(side='top', fill=X)
    
    #############################################################
    #frame1: 힌트 코드 목록
    frame1 = LabelFrame(win, pady = 10, text="Using Hint Code", labelanchor='n', font="default_font 25")
    frame1.pack(fill=BOTH, expand=1)
    
    lb1 = Label(frame1, text=h_list, width = '32')
    lb1.grid(row = 1, column = 1, padx=10, pady=10, ipadx=10, ipady=10)
    
    #############################################################
    #frame2: Menu로 이동하는 버튼
    frame2 = LabelFrame(win, bd='0')
    frame2.pack(side='bottom', fill=X)
    
    from Menu import home
    bt1 = Button(frame2, text = 'Menu', command = partial(home, win), bg = '#CFFFE5')
    bt1.grid(row=1, column=1, rowspan=1, padx =155, pady =20)

    
    