from tkinter import *

root = Tk()

root.title('test')
root.geometry('750x450')

address_text = []
pw_text = []

address = Entry(width=40)
popimap = Entry(width=40)
smtp = Entry(width=40)
pw = Entry(width=20)
r_port = Entry(width=10)
s_port = Entry(width=10)

addresslbl = Label(text='Address')
popimaplbl = Label(text='PopServar')
smtplbl = Label(text='SmtpServer')
pwlbl = Label(text='PW')

address.place(x=90, y=70)
popimap.place(x=90, y=120)
r_port.place(x=400, y=120)
smtp.place(x=90, y=170)
s_port.place(x=400, y=170)
pw.place(x=90, y=220)

setaddress = Button(width=10)
setaddress.place(x=400, y=70)

def reset():
    address.delete(0)
    popimap.delete(0)
    smtp.delete(0)
    #text clear
def send():
    outlook = win32com.client.Dispatch("Outlook.Application") # outlookのアプリケーションオブジェクトを作成
    outlook.CreateItem(0)
    #Mail send
def print():
    file = open('test.txt', 'w')
    file.write('test')
    file.close()
    #txt print

root.mainloop()

