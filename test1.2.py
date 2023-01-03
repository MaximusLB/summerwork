import tkinter as tk
from tkinter import *
import mysql.connector as sql

conn = sql.connect(
  host="localhost",
  user="root",
  password="RootPass",
  database="cardbase"
)
#import urllib.request (error 1)

#imgURL = "https://drive.google.com/file/d/1ifP4TG2Jk1gnEmbsZr61mSiTwbi3pzdI/view?usp=sharing" (error 1)
#ringico=urllib.request.urlretrieve(imgURL, "My Drive/ring.ico") (error 1)

def show_frame(frame):
  frame.tkraise()


#setting the program wide details
root = tk.Tk()
root.state('normal')
root.title('MXCardShop')
root.geometry("300x250")
root.bg="#cae3e1"
#sets the top left icon 
#root.iconbitmap(r'ringico')(error 1)

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)


#frame roots to set background colours
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
frame6 = tk.Frame(root)
frame7 = tk.Frame(root)
frame8 = tk.Frame(root)

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
  frame.grid(row=0,column=0,sticky='nsew')
  tk.Frame(master=root,)
  label = tk.Label(master=root, text=frame1)

global username
global password
global message
global rusername
global rpassword
global rmessage
global productnumber
global basket
username = StringVar()
password = StringVar()
message = StringVar()
rusername = StringVar()
rpassword = StringVar()
rmessage = StringVar()
productnumber = StringVar()
basket = [0]


#==================================login code
def login():
  usname = username.get()
  psword = password.get()
  if usname=='' or psword=='':
    message.set("fill the empty field!!!")
  else:
    if usname=="Admin" and psword=="Secret":
      message.set("Login success"),show_frame(frame4)
    else:
      message.set("Invalid username or password")

#==================================Register code
def register():
  rusname = rusername.get()
  rpsword = rpassword.get()
  if rusname=='' or rpsword=='':
    message.set("fill the empty field!!!")
  else:
    if rusname==rusname and rpsword==rpsword:
      rmessage.set("Register success"),show_frame(frame4)
    else:
      rmessage.set("Invalid username or password")

#==================================Basket append
def basketap():
  basket.append(productnumber)

#==================================Frame 1 code
frame1_title= tk.Label(frame1, text='Choose Login or Register',bg="#defcfa")
frame1_title.pack(fill='x')

frame1_btn = tk.Button(frame1,text='Login',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame2))
frame1_btn.pack()

frame1_btn_skip = tk.Button(frame1,text='Register',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame3))
frame1_btn_skip.pack()

#==================================Frame 2 code

frame2_title= tk.Label(frame2, text='Login Page',bg="#defcfa")
frame2_title.pack(fill='x')

frame2_ulabel= tk.Label(frame2, text="Username",height="2",width="30")
frame2_ulabel.pack()

frame2_uentry = tk.Entry(frame2, textvariable = username)
frame2_uentry.pack()

frame2_plabel= tk.Label(frame2, text="Password",height="2",width="30")
frame2_plabel.pack()

frame2_pentry = tk.Entry(frame2, textvariable = password)
frame2_pentry.pack()

frame2_feedback = tk.Label(frame2, text="",textvariable=message)
frame2_feedback.pack()

frame2_btn = tk.Button(frame2, text='Enter',height="2",width="30",bg="#defcfa",command=login,)
frame2_btn.pack()

#==================================Frame 3 code
frame3_title= tk.Label(frame3, text='Register Page',bg="#defcfa")
frame3_title.pack(fill='x')

frame3_ulabel= tk.Label(frame3, text="Username",height="2",width="30")
frame3_ulabel.pack()

frame3_uentry = tk.Entry(frame3, textvariable = rusername)
frame3_uentry.pack()

frame3_plabel= tk.Label(frame3, text="Password",height="2",width="30")
frame3_plabel.pack()

frame3_pentry = tk.Entry(frame3, textvariable = rpassword)
frame3_pentry.pack()

frame3_feedback = tk.Label(frame3, text="",textvariable=rmessage)
frame3_feedback.pack()

frame3_btn = tk.Button(frame3, text='Enter',height="2",width="30",bg="#defcfa",command=register,)
frame3_btn.pack()


#================================Frame 4
frame4_title= tk.Label(frame4, text='Welcome to MXCardShop',bg="#defcfa")
frame4_title.pack(fill='x')

frame4_btn = tk.Button(frame4,text='Catalogue',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame5))
frame4_btn.pack()

frame4_btn_basket= tk.Button(frame4,text='Basket',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame6))
frame4_btn_basket.pack()

#================================Frame 5
frame5_title= tk.Label(frame5, text='Welcome to MXCardShop catalogue',bg="#defcfa")
frame5_title.pack(fill='x')

frame5_btn_basket= tk.Button(frame5,text='Basket',height="1",width="15",bg="#defcfa",command=lambda:show_frame(frame6))
frame5_btn_basket.pack()


frame5_btn_c1 = tk.Button(frame5,text='Card 1',height="2",width="30",bg="#defcfa", command=lambda:[productnumber.set("1"),basketap()])
frame5_btn_c1.pack()

frame5_btn_c2= tk.Button(frame5,text='Card 2',height="2",width="30",bg="#defcfa", command=lambda:[productnumber.set("2"),basketap()])
frame5_btn_c2.pack()

frame5_btn_c3= tk.Button(frame5,text='Card 3',height="2",width="30",bg="#defcfa", command=lambda:[productnumber.set("3"),basketap()])
frame5_btn_c3.pack()

frame5_btn_c4= tk.Button(frame5,text='Card 4',height="2"
                         ,width="30",bg="#defcfa", command=lambda:[productnumber.set("4"),basketap()])
frame5_btn_c4.pack()

frame5_btn_c5= tk.Button(frame5,text='Card 5',height="2",width="30",bg="#defcfa", command=lambda:[productnumber.set("5"),basketap()])
frame5_btn_c5.pack()

frame5_btn_c6= tk.Button(frame5,text='Card 6',height="2",width="30",bg="#defcfa", command=lambda:[productnumber.set("6"),basketap()])
frame5_btn_c6.pack()


#===============================Frame 6

frame6_title= tk.Label(frame6, text='Basket',bg="#defcfa")
frame6_title.pack(fill='x')

frame6_list=tk.Label(frame6, text=print(basket[:]), bg="#defcfa")
frame6_list.pack()

frame6_btn = tk.Button(frame6,text='Catalogue',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame4))
frame6_btn.pack()

frame6_btn_pay = tk.Button(frame6,text='Pay',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame7))
frame6_btn_pay.pack()

#===============================Frame 7

frame7_title= tk.Label(frame7, text='Checkout',bg="#defcfa")
frame7_title.pack(fill='x')


frame7_btn = tk.Button(frame7,text='Proccess payment',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame8))
frame7_btn.pack()

#===============================Frame 7

frame8_title= tk.Label(frame8, text='Receipt',bg="#defcfa")
frame8_title.pack(fill='x')


frame8_btn = tk.Button(frame8,text='Return to Catalogue',height="2",width="30",bg="#defcfa",command=lambda:show_frame(frame4))
frame8_btn.pack()




#Runs the program

show_frame(frame1)

root.mainloop()
