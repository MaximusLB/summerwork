#Imports the libraries 
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector as sql
from datetime import date

#Connects the database
conn = sql.connect(
  host="localhost",
  user="root",
  password="RootPass",
  database="cardbase"
)
conn.autocommit = True
cur = conn.cursor()


#Sets a fram variable
def show_frame(frame):
  frame.tkraise()


#setting the program wide details
root = tk.Tk()
root.state('zoomed')
root.title('NyahaGifts')
root.geometry("1080x1920")
root.bg="#cae3e1"

#sets the top left icon 
ico1 = PhotoImage(file ='nyaicon.gif')
root.iconphoto(True, ico1)
logo1 = PhotoImage(0,0, file = "nyaicon.gif")


#Sets or and collumn weight
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

#Sets all frames to root settings
for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
  frame.grid(row=0,column=0,sticky='nsew')
  tk.Frame(master=root,bg="#FFFFFF")
  label = tk.Label(master=root, text=frame1)

#Imports images
#logo = ImageTk.PhotoImage(Image.open("nyalogo.jpg"))


#Defining variables and their scopes
global username
global password
global usname
global psword
global message
global rusername
global rpassword
global rmessage
global raccess
global basket
global recmessage
global UID
username = StringVar()
password = StringVar()
usname = StringVar()
psword = StringVar()
message = StringVar()
rusername = StringVar()
rpassword = StringVar()
rmessage = StringVar()
productnumber = StringVar()
recmessage = StringVar()
totalID = StringVar()
totalItems = StringVar()
basket = list()
basketprice = list()
baskettext = list()
totalID = ' '.join(basket)
totalItems = baskettext[:]
totalPrice = StringVar()
updatebaskettext = tk.StringVar()
updatebasketprice = tk.StringVar()

#Creates lists for the basket (WIP)
#def basketap(self,item):
  #basket.append(item)

#def basketapprice(self,cost):
 # basketprice.append(cost)

#def basketaptext(self,text):
 # basket.append(text)


#==================================login code
def login():
  usname = username.get()
  psword = password.get()
  statement = f"SELECT username from user WHERE username='{usname}' AND Password = '{psword}';"
  cur.execute(statement)
  if not cur.fetchone():
    message.set("Login failed")
  else:
    message.set("Login success"),show_frame(frame4)


#==================================Register code
def register():
  rusname = rusername.get()
  rpsword = rpassword.get()
  raccess = "Customer"
  if len(rusname)<5 or len(rusname)>12 or len(rpsword)<5 or len(rpsword)>12:
    rmessage.set("Both fields must be between 5 to 12 characters")
    register()
  else:
    rstatement = f"SELECT username from user WHERE username='{rusname}';"
    cur.execute(rstatement)
    if not cur.fetchone():
      rstatement2 = "INSERT INTO user (username, password, access) VALUES (%s, %s, %s)"
      values = (rusname, rpsword, raccess)
      cur.execute(rstatement2, values)
      rmessage.set("Register success"),show_frame(frame4)
    else:
      rmessage.set("Username in use")



#==================================Basket append
def basketap(productNumber,productPrice,productName):
  basket.append(productNumber)
  basketprice.append(productPrice)
  baskettext.append(productName)

def basketPrints():
  print("IDs: ",basket[:])
  print("Prices: ",basketprice[:])
  print("Items: ",baskettext[:])
  totalPrice = str(sum(basketprice))
  print("Total = £",totalPrice)
  totalItems = str("\n".join(baskettext))
  updatebaskettext.set (totalItems)
  updatebasketprice.set (totalPrice)
 

#===================================Receipt gen
def Receipt():
    show_frame(frame8)
    recstatement = f"SELECT UserID from user WHERE username='{usname}';"
    cur.execute(recstatement)
    UID = cur.fetchone()
    recdate = date.today()
    str(totalPrice)
    str(totalID)
    recstatement2 = "INSERT INTO sales (UserID,CardIDs,Price) VALUES (%s,%s,%s)"
    recvalues = (UID, totalID, totalPrice)
    cur.execute(recstatement2, recvalues)
    recmessage.set("Receipt added to database")

  

#==================================Frame 1 code

frame1_title= tk.Label(frame1, text='~NyahaGifts~\nChoose Login or Register',font=('Helvetica bold',24),height="5",bg="#fadadd")
frame1_title.pack(fill='x')

frame1_photo= tk.Label(frame1, image= logo1,height="20",width="300")
frame1_photo.pack(anchor="nw")

frame1_btn = tk.Button(frame1,text='Login',height="5",width="75",bg="#fadadd",command=lambda:show_frame(frame2))
frame1_btn.pack(padx=15, pady=60)

frame1_btn_skip = tk.Button(frame1,text='Register',height="5",width="75",bg="#fadadd",command=lambda:show_frame(frame3))
frame1_btn_skip.pack(padx=15, pady=10)

#==================================Frame 2 code

frame2_title= tk.Label(frame2, text='Login Page',bg="#fadadd")
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

frame2_btn = tk.Button(frame2, text='Enter',height="2",width="30",bg="#fadadd",command=login,)
frame2_btn.pack()

#==================================Frame 3 code
frame3_title= tk.Label(frame3, text='Register Page',bg="#fadadd")
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

frame3_btn = tk.Button(frame3, text='Enter',height="2",width="30",bg="#fadadd",command=register,)
frame3_btn.pack()


#================================Frame 4
frame4_title= tk.Label(frame4, text='Welcome to MXCardShop',bg="#fadadd")
frame4_title.pack(fill='x')

frame4_btn = tk.Button(frame4,text='Catalogue',height="2",width="30",bg="#fadadd",command=lambda:show_frame(frame5))
frame4_btn.pack()

frame4_btn_basket= tk.Button(frame4,text='Basket',height="2",width="30",bg="#fadadd",command=lambda:show_frame(frame6))
frame4_btn_basket.pack()

#================================Frame 5
frame5_title= tk.Label(frame5, text='Welcome to MXCardShop catalogue',bg="#fadadd")
frame5_title.pack(fill='x')

frame5_btn_basket= tk.Button(frame5,text='Basket',height="1",width="15",bg="#fadadd",command=lambda:show_frame(frame6))
frame5_btn_basket.pack()


frame5_btn_c1 = tk.Button(frame5,text='1.Blue Birthday Card \n £2.99',height="2",width="30",bg="#fadadd", command=lambda:[basketap(1,float(2.99),"Blue Birthday Card")])
frame5_btn_c1.pack()

frame5_btn_c2= tk.Button(frame5,text='2.Red Birthday Card \n £2.99',height="2",width="30",bg="#fadadd", command=lambda:[basketap(2,2.99,"Red Birthday Card")])
frame5_btn_c2.pack()

frame5_btn_c3= tk.Button(frame5,text='3.Green Birthday Card \n £2.99',height="2",width="30",bg="#fadadd", command=lambda:[basketap(3,2.99,"Green Birthday Card")])
frame5_btn_c3.pack()

frame5_btn_c4= tk.Button(frame5,text='4.White Anniversary \n £5',height="2" ,width="30",bg="#fadadd", command=lambda:[basketap(4,5.00,"White Anniversary")])
frame5_btn_c4.pack()

frame5_btn_c5= tk.Button(frame5,text='5.Purple Congratulations \n £4',height="2",width="30",bg="#fadadd", command=lambda:[basketap(5,4.00,"Purple Congratulations")])
frame5_btn_c5.pack()

frame5_btn_c6= tk.Button(frame5,text='6.Orange Congratulations \n £4',height="2",width="30",bg="#fadadd", command=lambda:[basketap(6,4.00,"Orange Congratulations")])
frame5_btn_c6.pack()

frame5_btn_c7= tk.Button(frame5,text='7.Red Valentines \n £3.50',height="2",width="30",bg="#fadadd", command=lambda:[basketap(7,3.50,"Red Valentines")])
frame5_btn_c7.pack()

frame5_btn_c8= tk.Button(frame5,text='8.Pink Valentines \n £3.50',height="2",width="30",bg="#fadadd", command=lambda:[basketap(8,3.50,"Pink Valentines")])
frame5_btn_c8.pack()

frame5_btn_c9= tk.Button(frame5,text='9.Dark Red Valentines \n £3.50',height="2",width="30",bg="#fadadd", command=lambda:[basketap(9,3.50,"Dark Red Valentines")])
frame5_btn_c9.pack()

frame5_btn_out= tk.Button(frame5,text='output list',height="2",width="30",bg="#fadadd", command=lambda:[basketPrints()])
frame5_btn_out.pack()
#===============================Frame 6

frame6_title= tk.Label(frame6, text='Basket',bg="#fadadd")
frame6_title.pack(fill='x')

frame6_listtitle=tk.Label(frame6, text="Items", bg="#fadadd")
frame6_listtitle.pack()

frame6_list=tk.Label(frame6, textvariable=updatebaskettext,)
frame6_list.pack()

frame6_listtitleprice=tk.Label(frame6, text="Price £", bg="#fadadd")
frame6_listtitleprice.pack()

frame6_listprice=tk.Label(frame6, textvariable=updatebasketprice,)
frame6_listprice.pack()

frame6_btn_update = tk.Button(frame6,text='Update Basket',height="2",width="30",bg="#fadadd",command=lambda:basketPrints())
frame6_btn_update.pack()

frame6_btn = tk.Button(frame6,text='Catalogue',height="2",width="30",bg="#fadadd",command=lambda:show_frame(frame5))
frame6_btn.pack()

frame6_btn_pay = tk.Button(frame6,text='Pay',height="2",width="30",bg="#fadadd",command=lambda:show_frame(frame7))
frame6_btn_pay.pack()

#===============================Frame 7

frame7_title= tk.Label(frame7, text='Checkout',bg="#fadadd")
frame7_title.pack(fill='x')


frame7_btn = tk.Button(frame7,text='Proccess payment',height="2",width="30",bg="#fadadd",command=lambda:Receipt())
frame7_btn.pack()

#===============================Frame 7

frame8_title= tk.Label(frame8, text='Receipt',bg="#fadadd")
frame8_title.pack(fill='x')

frame8_feedback = tk.Label(frame8, text="",textvariable=recmessage)
frame8_feedback.pack()

frame8_btn = tk.Button(frame8,text='Return to Catalogue',height="2",width="30",bg="#fadadd",command=lambda:show_frame(frame4))
frame8_btn.pack()




#Runs the program

show_frame(frame1)

root.mainloop()
