from tkinter import *
import tkinter.font as font         #imports font module and being imported as font. It helps to define a specfic font style
import random

win = Tk()                          #creates the window
win.title('ATM')
win.geometry('400x390')             #sets the dimension of the window

tim40 = font.Font(family='Times', size=40, weight='bold', slant='italic', underline=1)            #Font is an instance which contains parameter as
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
saving = Button(rightframe,text='Savings',font=cour15,bg='skyblue',fg='red')
saving.pack(padx=10,pady=10)
current = Button(rightframe,text="Current",font=cour15,bg='skyblue',fg='red')
current.pack(padx=10,pady=10)

win.mainloop()