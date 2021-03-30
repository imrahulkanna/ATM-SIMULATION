from tkinter import *
import tkinter.font as font         #imports font module and being imported as font. It helps to define a specfic font style
import random

win = Tk()                          #creates the window
win.title('ATM')
win.geometry('400x390')             #sets the dimension of the window


def enter_pin():

    new_win = Toplevel(win)
    new_win.geometry('400x390')

    text_entry = StringVar()

    def setInputText(text):
        entry_box.insert('end',text)            #insert allows to enter(display on entry box) the text at the end(if we replace end with 0 the text is placed at front)

    def text_delete():
        entry_box.delete(0)                     #we have another function called delete which deletes text from the given range(.delete(0,'end') deletes the entire text

    lbl = Label(new_win, text='Enter your PIN',font=cour20,fg='red')
    lbl.pack(pady=20)

    entry_box = Entry(new_win, font=cour15, show='*', justify='center')  #show parameter display the input text as *(we can use any other element also
    entry_box.pack()

    bf = Frame(new_win)
    bf.pack(side=BOTTOM)

    bf0 = Frame(new_win)
    bf0.pack(side=BOTTOM)

    bf1 = Frame(new_win)
    bf1.pack(side=BOTTOM)

    bf2 = Frame(new_win)
    bf2.pack(side=BOTTOM)

    bf3 = Frame(new_win)
    bf3.pack(side=BOTTOM)

    bf4 = Frame(new_win)
    bf4.pack(side=BOTTOM)

    rf = Frame(new_win)
    rf.pack(side=RIGHT)

    btn1 = Button(bf4,text='1',font=cour15, command=lambda:setInputText('1'))
    btn1.pack(side=LEFT, pady=10)

    btn2 = Button(bf4, text='2', font=cour15, command=lambda:setInputText('2'))
    btn2.pack(side=LEFT,padx=10)

    btn3 = Button(bf4, text='3', font=cour15, command=lambda:setInputText('3'))
    btn3.pack(side=LEFT)

    btn4 = Button(bf3, text='4', font=cour15, command=lambda:setInputText('4'))
    btn4.pack(side=LEFT)

    btn5 = Button(bf3, text='5', font=cour15, command=lambda:setInputText('5'))
    btn5.pack(side=LEFT,padx=10)

    btn6 = Button(bf3, text='6', font=cour15, command=lambda:setInputText('6'))
    btn6.pack(side=LEFT)

    btn7 = Button(bf2, text='7', font=cour15, command=lambda:setInputText('7'))
    btn7.pack(side=LEFT,pady=10)

    btn8 = Button(bf2, text='8', font=cour15, command=lambda:setInputText('8'))
    btn8.pack(side=LEFT, padx=10)

    btn9 = Button(bf2, text='9', font=cour15, command=lambda:setInputText('9'))
    btn9.pack(side=LEFT)

    btn = Button(bf1, text=' ', font=cour15)
    btn.pack(side=LEFT)

    btn0 = Button(bf1, text='0', font=cour15, command=lambda:setInputText('0'))
    btn0.pack(side=LEFT, padx=10)

    btn_ = Button(bf1, text=' ', font=cour15)
    btn_.pack(side=LEFT)

    enter_btn = Button(bf0, text='ENTER', font=cour15,fg='green')
    enter_btn.pack(side= LEFT, pady=10,padx=10)

    exit_btn = Button(bf0, text='EXIT', font=cour15, fg='red', command=lambda:new_win.destroy())
    exit_btn.pack(side=RIGHT, padx=10)

    clear_btn = Button(bf0,text='CLEAR', font=cour15, fg='orange',command=text_delete)
    clear_btn.pack(side=LEFT)

    note = Label(bf, text='Note:Enter pin either from keyboard or keypad', fg='red')
    note.pack()



tim40 = font.Font(family='Times', size=40, weight='bold', slant='italic', underline=1)      #Font is an instance which contains parameter as
                                                                                            #family(the font style), size, weight(bold,normal)
                                                                                            #slant(italic,roman(non-italic)), underline(1-yes,0-no),
                                                                                            #overstrike(1-yes,0-no) and many more

title_label = Label(win, text='ATM', font=tim40, fg='red')              #Label is smthg similar to a label which displays text on the window
title_label.pack(pady=10)                                               #pady gives vertical distance both above and below where as padx gives
                                                                        #horizontal distance
#displaying some introduction
user_id = random.randrange(1000,10000)
cour20 = font.Font(family='Courier', size=20, weight='bold')
intro = Label(win, text='\nWelcome User '+str(user_id), font=cour20, fg='green')
intro.pack()
cour15 = font.Font(family='Courier', size=15, weight='bold')
option_label = Label(win, text='\nSelect your account type', font=cour15, fg='grey')
option_label.pack()

rightframe = Frame(win)
rightframe.pack(side=RIGHT)
saving = Button(rightframe,text='Savings',font=cour15,bg='skyblue',fg='red', command=enter_pin)
saving.pack(padx=10,pady=10)
current = Button(rightframe,text="Current",font=cour15,bg='skyblue',fg='red', command=enter_pin)
current.pack(padx=10,pady=10)

win.mainloop()