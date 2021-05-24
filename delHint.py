from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter.messagebox
from Hint import hintList

def del_hintCode(win):
    for wg in win.pack_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
        wg.destroy()             # 위젯 제거
    
    #############################################################
    # frame1: 공백
    frame1 = LabelFrame(win, bd='0', height='150')
    frame1.pack(side='top', fill=X)
    
    #############################################################
    # frame2: 힌트 코드 입력
    frame2 = LabelFrame(win,text='Hint Code', labelanchor='n', font="default_font 25")
    frame2.pack(side='top',fill=X)
    
    #공백 라벨
    lb_empty1 = Label(frame2)
    lb_empty1.grid(row = 1, column = 0)
    
    #공백 라벨
    lb_empty2 = Label(frame2)
    lb_empty2.grid(row = 1, column = 1)
    
    #힌트코드 입력폼
    global del_hint_code
    del_hint_code = Entry(frame2, font="default_font 25", width=15)
    del_hint_code.grid(row = 1, column = 2, padx = 10, pady = 10)
    
    #힌트코드 삭제 버튼
    use = Button(frame2, text = '삭제', command = partial(del_hint, win), bg = '#CFFFE5', width = 3)
    use.grid(row = 1, column = 3, padx = 10, pady = 10)
    
    #############################################################
    # frame3: 뒤로가기 버튼
    frame3 = LabelFrame(win, bd='0', height='50')
    frame3.pack(side='bottom', fill=X)
    
    from Menu import home
    bt1 = Button(frame3, text = '←', command = partial(home, win), bg = '#CFFFE5')
    bt1.grid(row=1, column=1, columnspan=1, padx =20, pady =20)
    
#힌트를 리스트에서 삭제 연산 하는 기능
def del_hint(win):
    hintCode_del = del_hint_code.get()
    MsgBox = tkinter.messagebox.askquestion ('힌트 삭제', "[" + str(hintCode_del) + "]" + '를 정말 삭제하시겠습니까?')
    if hintCode_del in hintList:
        if MsgBox == 'yes':
            hintList.pop(hintCode_del)
            tkinter.messagebox.showinfo("삭제 완료", "힌트가 삭제되었습니다.")

        else: #No 클릭 시 힌트 다시 힌트 입력 화면으로
            del_hintCode(win)
            
    else:
        tkinter.messagebox.showinfo("오류", "존재하지 않는 힌트코드입니다. 다시 입력하세요.")
        del_hintCode(win)
