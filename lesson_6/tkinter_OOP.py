from tkinter import *


class Block:
    def __init__(self, master, func):
        # конструктор класса
        self.txt = Entry(master, width=40)
        # создание виджетов
        self.btn = Button(master, text="КН-1")
        self.lbl = Label(master, width=40)
        self.btn["command"] = getattr(self, func)
        # привязка команды к кнопке
        self.txt.pack()
        self.btn.pack()
        self.lbl.pack()

    def text_same_label(self):
        # функция класса без сортировки
        s = self.txt.get()
        # забрать значение из текстового поля
        self.lbl["text"] = s

    def text_sort_label(self):
        # функция класса с сортировкой
        s = self.txt.get().split()
        s.sort()
        self.lbl["text"] = " ".join(s)


root = Tk()
# создать окно класса
root.title("TK и ООП")
b1 = Block(root, "text_same_label")
# создать объект класса
b2 = Block(root, "text_sort_label")
b3 = Block(root, "text_sort_label")
root.mainloop()
