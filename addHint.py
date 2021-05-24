from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter.messagebox
from Hint import hintList



#힌트 코드 추가 입력창        
def add_HintCode(win):
        for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
            wg.destroy()             # 위젯 제거
        
        #############################################################
        # frame1: 공백
        frame1 = LabelFrame(win, bd='0', height='150')
        frame1.pack(side='top', fill=X)
        
        #############################################################
        # frame2: 힌트코드 입력
        frame2 = LabelFrame(win,text='Hint Code', labelanchor='n', font="default_font 25")
        frame2.pack(side='top',fill=X)
        
        #공백 라벨
        lb_empty1 = Label(frame2)
        lb_empty1.grid(row = 1, column = 0)
        
        #공백 라벨
        lb_empty2 = Label(frame2)
        lb_empty2.grid(row = 1, column = 1)
        
        #힌트코드 입력폼
        global add_hint_code
        add_hint_code = Entry(frame2, font="default_font 25", width=15)
        add_hint_code.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        #힌트코드 저장 버튼
        use = Button(frame2, text = '저장', command = partial(check_hint, win), bg = '#CFFFE5', width = 3)
        use.grid(row = 1, column = 3, padx = 10, pady = 10)
        
        #############################################################
        # frame3: 뒤로가기 버튼
        frame3 = LabelFrame(win, bd='0', height='50')
        frame3.pack(side='bottom', fill=X)
        
        from Menu import home
        bt1 = Button(frame3, text = '←', command = partial(home, win), bg = '#CFFFE5')
        bt1.grid(row=1, column=1, columnspan=1, padx =20, pady =20)
    
#힌트 내용 추가 입력창
def add_HintSentence(win, hintCode_add):
        for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
            wg.destroy()             # 위젯 제거
        
        #############################################################
        # frame1: 공백 프레임
        frame1 = LabelFrame(win, bd='0', height='100')
        frame1.pack(side='top', fill=X)
        
        #############################################################
        # frame2: 힌트 내용 입력   
        frame2 = LabelFrame(win, pady = 10, text="힌트 내용", labelanchor='n', font="default_font 25")
        frame2.pack(side='top', fill=BOTH, expand=1)
        useHintCode = frame2.cget('text')
       
        #힌트코드 표시 라벨
        lb_empty2 = Label(frame2, text=hintCode_add, width = '31', bd='0')
        lb_empty2.grid(row = 1, column = 1, ipadx=10, ipady=10)
        
        hintCode_add = lb_empty2.cget('text') #라벨에 있는 힌트코드 다시 저장
        
        #힌트 내용 입력폼
        global add_hint_sentence
        add_hint_sentence = Text(frame2, font="default_font 15", width='32', height='10')
        add_hint_sentence.grid(row = 2, column = 1, padx=20, pady=20)
        
        #############################################################
        # frame3: (Menu로)돌아가기 버튼 / 힌트 내용 저장 버튼 / 힌트 추가 입력 버튼
        frame3 = LabelFrame(win, bd='0', height='50')
        frame3.pack(side='bottom', fill=X)
        
        from Menu import home
        bt1 = Button(frame3, text = 'Menu', command = partial(home, win), bg = '#CFFFE5')
        bt2 = Button(frame3, text = '저장', command = partial(add_hint, win, hintCode_add), bg = '#CFFFE5')
        bt3 = Button(frame3, text = '+힌트', command = partial(add_HintCode, win), bg = '#CFFFE5')

        bt1.grid(row=1, column=1, columnspan=1, padx =50, pady =50)
        bt2.grid(row=1, column=2, columnspan=1, padx =0, pady =50)
        bt3.grid(row=1, column=3, columnspan=1, padx =50, pady =50)
        
        
#힌트 리스트에 힌트 추가하는 기능
def add_hint(win, hintCode_add):
    hintSentence_add = add_hint_sentence.get("1.0","end")
    hintList.setdefault(hintCode_add, hintSentence_add) #힌트 리스트에 힌트코드:힌트내용 저장         
    tkinter.messagebox.showinfo("저장 완료", "힌트가 저장되었습니다.")
    
    
#힌트코드가 이미 사용되고 있는지 검사하는 기능
def check_hint(win):
        hintCode_add = add_hint_code.get()
        if hintCode_add in hintList:
                tkinter.messagebox.showerror( "Hint Code", "이미 존재하는 힌트코드입니다.")
                add_HintCode(win) #힌트코드 입력으로 되돌아가기
        else: #힌트 내용 입력으롱 이동
                add_HintSentence(win, hintCode_add)