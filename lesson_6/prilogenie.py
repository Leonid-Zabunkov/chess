from tkinter import *

from tkinter import ttk

root = Tk()

root.title("Проверка кнопок")

root.geometry("300x250")

lbn = Label(root, text="hello")

txt = Entry(root, width=20)

btn1 = Button(root, text="КН-1")
# кнопка стандарт

btn2 = ttk.Button(root, text="КН-2")
# кнопка ttk

btn1.pack()  # разместить кнопку в окне

btn2.pack()  # разместить кнопку в окне

lbn.pack()

txt.pack()


def test(event):

    s = txt.get()
    lbn["text"] = s


btn1.bind("<Button-1>", test)
# связать вызов функции с событием

root.mainloop()
