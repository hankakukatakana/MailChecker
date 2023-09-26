from tkinter import *
#メソッド呼び出し時のオブジェクト名Tk.を省略
root = Tk()

root.title('test')
root.geometry('750x450')
#xはエックスです
address = Entry(width=40)
popimap = Entry(width=40)
smtp = Entry(width=40)
pw = Entry(width=20)

address.place(x=90, y=70)
popimap.place(x=90, y=120)
smtp.place(x=90, y=170)

root.mainloop()