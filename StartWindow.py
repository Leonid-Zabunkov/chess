from tkinter import *


class ChessSettings:
    def __init__(self, master: Tk):
        self.__master = master
        self.__master.title("Настройки игры")
        self.__master.geometry("300x300")
        self.__master.resizable(False, False)
        # сохраняем данные для main
        self.__result = None

        self.__mode = StringVar(value="standard")
        self.__white_name = StringVar(value="Max")
        self.__black_name = StringVar(value="Leon")

        Label(master, text="Set mode", font=("Arial", 10, "bold")).pack(pady=5)

        self.__mode_frame = Frame(master)
        self.__mode_frame.pack(side=TOP, fill=X)

        #  variable=self.mode Сколько угодно кнопок, но выбрать можно только 1
        Radiobutton(
            self.__mode_frame,
            text="Standard",
            variable=self.__mode,
            value="standard",
            command=self.__toggle_mode,
        ).pack(side=LEFT, padx=15)

        Radiobutton(
            self.__mode_frame,
            text="Fisher Chess",
            variable=self.__mode,
            value="fisher",
            command=self.__toggle_mode,
        ).pack(side=LEFT, padx=5)

        # Radiobutton(
        #     mode_frame,
        #     text="Puzzle",
        #     variable=self.__mode,
        #     value="puzzle",
        #     command=self.toggle_mode,
        # ).pack(side=LEFT, padx=15)

        self.__last_radio = Radiobutton(
            self.__mode_frame,
            text="Puzzle",
            variable=self.__mode,
            value="puzzle",
            command=self.__toggle_mode,
        )
        self.__last_radio.pack(side=LEFT, padx=5)

        # 3. Фрейм для ввода ID пазла (по умолчанию на пакуется)
        self.__puzzle_frame = Frame(master)
        Label(self.__puzzle_frame, text="Puzzle`s ID").pack(side=LEFT)
        self.__puzzle_id = Entry(self.__puzzle_frame, width=5)
        self.__puzzle_id.insert(0, "1")
        self.__puzzle_id.pack(side=LEFT)

        Label(
            master, text="Players settings:", font=("Times New Roman", 10, "bold")
        ).pack(pady=(15, 0))

        # Настройка белых
        f_w = Frame(master)
        f_w.pack(pady=2)
        Label(f_w, text="White").pack(side=LEFT)
        Entry(f_w, textvariable=self.__white_name, width=10).pack(side=LEFT)
        Label(f_w, text=" Time:").pack(side=LEFT)
        self.__time_w = Entry(f_w, width=5)
        self.__time_w.insert(0, "500")
        self.__time_w.pack(side=LEFT)

        # Настройка чёрных
        f_b = Frame(master)
        f_b.pack(pady=2)
        Label(f_b, text="Black ").pack(side=LEFT)
        Entry(f_b, textvariable=self.__black_name, width=10).pack(side=LEFT)
        Label(f_b, text=" Time:").pack(side=LEFT)
        self.__time_b = Entry(f_b, width=5)
        self.__time_b.insert(0, "200")
        self.__time_b.pack(side=LEFT)

        btn_frame = Frame(master)
        btn_frame.pack(side=BOTTOM, pady=(0, 15))

        Button(
            master, text="Play", bg="green", fg="white", command=self.__start_game
        ).pack(fill=X, padx=20, pady=20)

        Button(btn_frame, text="Clear all", command=self.clear).pack(
            side=LEFT,
            padx=5,
            ipadx=20,  # Увеличит ширину кнопки внутри
            ipady=1,  # Увеличит высоту кнопки внутри
        )

        Button(btn_frame, text="  Exit  ", command=self.exit_app).pack(
            side=LEFT,
            padx=5,
            ipadx=20,  # Увеличит ширину кнопки внутри
            ipady=1,  # Увеличит высоту кнопки внутри
        )

    def __start_game(self):
        self.__result = {
            "mode": self.__mode.get(),
            "white": self.__white_name.get(),
            "black": self.__black_name.get(),
            "time_w": int(self.__time_w.get()),
            "time_b": int(self.__time_b.get()),
            "puzzle_id": int(self.__puzzle_id.get()),
        }
        self.__master.destroy()

    def __toggle_mode(self):
        # Если выбрали пазл - показываем поле ID, иначе прячем
        if self.__mode.get() == "puzzle":
            # Рисуем под блоком режимов
            self.__puzzle_frame.pack(after=self.__mode_frame, pady=5)
        else:
            # Удаляет с экрана, но не выкидывает из памяти
            self.__puzzle_frame.pack_forget()

    def clear(self):

        self.__mode.set("standard")
        self.__white_name.set("Max")
        self.__black_name.set("Leon")

        self.__time_w.delete(0, END)
        self.__time_w.insert(0, "500")

        self.__time_b.delete(0, END)
        self.__time_b.insert(0, "200")

        self.__puzzle_id.delete(0, END)
        self.__puzzle_id.insert(0, "1")

        self.__toggle_mode()

    def exit_app(self):
        self.__master.destroy()

    def get_data(self):
        return self.__result
