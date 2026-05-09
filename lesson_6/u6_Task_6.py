from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Графич. калькулятор")
        self.calc_frame = Frame(master)

        # 1. Сначала переменные (логика)
        self.mode = StringVar(value="calc")
        self.calc_sum, self.calc_sub = BooleanVar(), BooleanVar()
        self.calc_mul, self.calc_div = BooleanVar(), BooleanVar()
        self.rect_perim, self.rect_area = BooleanVar(), BooleanVar()

        # 2. Выбор режима
        Radiobutton(
            master,
            text="Калькулятор",
            variable=self.mode,
            value="calc",
            command=self.toggle_mode,
        ).pack()
        Radiobutton(
            master,
            text="Прямоугольник",
            variable=self.mode,
            value="rect",
            command=self.toggle_mode,
        ).pack()

        # 3. Поля ввода
        Label(master, text="Arg 1:").pack()
        self.ent1 = Entry(master)
        self.ent1.pack()
        Label(master, text="Arg 2:").pack()
        self.ent2 = Entry(master)
        self.ent2.pack()

        # 4. Рамки для операций
        Label(master, text="Операции:").pack()

        # 2. Создаем ПЕРВУЮ строку (рамку) внутри основной
        row1 = Frame(self.calc_frame)
        row1.pack()  # Она ляжет сверху
        Checkbutton(row1, text="Сумма", variable=self.calc_sum).pack(side=LEFT, padx=5)
        Checkbutton(row1, text="Разность", variable=self.calc_sub).pack(
            side=LEFT, padx=5
        )

        # 3. Создаем ВТОРУЮ строку (рамку) внутри основной
        row2 = Frame(self.calc_frame)
        row2.pack()  # Она ляжет под первой
        Checkbutton(row2, text="Умножение", variable=self.calc_mul).pack(
            side=LEFT, padx=5
        )
        Checkbutton(row2, text="Деление", variable=self.calc_div).pack(
            side=LEFT, padx=5
        )

        self.rect_frame = Frame(master)
        Checkbutton(self.rect_frame, text="Периметр", variable=self.rect_perim).pack(
            side=LEFT
        )
        Checkbutton(self.rect_frame, text="Площадь", variable=self.rect_area).pack(
            side=LEFT
        )

        # Показываем начальную рамку
        self.calc_frame.pack()

        # justify=LEFT выравнивает строки по левому краю
        # anchor="w" (West/Запад) прижимает текст к левой границе метки
        self.lbl_res = Label(
            master, text="----", fg="blue", font=("Arial", 10, "bold"), justify=LEFT
        )

        self.lbl_res.pack(pady=10)

        # Кнопка расчета (на всю ширину)
        Button(master, text="Рассчитать", command=self.calculate).pack(
            fill=X, padx=20, pady=5
        )

        # Кнопка обмена (можно тоже на всю ширину или обычную)
        Button(master, text="Поменять местами", command=self.swap).pack(
            fill=X, padx=20, pady=5
        )

        btn_frame = Frame(master)
        btn_frame.pack(pady=10)
        Button(btn_frame, text="Очистить", command=self.clear).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Выход", command=self.exit_app).pack(side=LEFT, padx=5)

    # --- 4. Методы логики ---

    def toggle_mode(self):
        if self.mode.get() == "calc":
            self.rect_frame.pack_forget()  # Прячем прямоугольник
            # Говорим: "Встань ПЕРЕД меткой результата"
            self.calc_frame.pack(before=self.lbl_res)
        else:
            self.calc_frame.pack_forget()  # Прячем калькулятор
            # Говорим: "Встань ПЕРЕД меткой результата"
            self.rect_frame.pack(before=self.lbl_res)

    def calculate(self):
        try:
            # Сбор данных
            a = float(self.ent1.get())
            b = float(self.ent2.get())
            results = []

            if self.mode.get() == "calc":
                # Проверяем каждую галочку калькулятора
                if self.calc_sum.get():
                    results.append(f"Сумма: {round(a + b, 2)}")
                if self.calc_sub.get():
                    results.append(f"Разность: {round(a - b, 2)}")
                if self.calc_mul.get():
                    results.append(f"Произв.: {round(a * b, 2)}")
                if self.calc_div.get():
                    if b != 0:
                        results.append(f"Частное: {round(a / b, 2)}")
                    else:
                        results.append("Частное: На 0 делить нельзя!")

            elif self.mode.get() == "rect":
                # Проверка на положительные числа для прямоугольника
                if a <= 0 or b <= 0:
                    self.lbl_res["text"] = "Ошибка: Стороны должны быть > 0"
                    return

                # Проверяем галочки прямоугольника
                if self.rect_perim.get():
                    results.append(f"Периметр: {round(2 * (a + b), 2)}")
                if self.rect_area.get():
                    results.append(f"Площадь: {round(a * b, 2)}")

            # Соединяем все найденные результаты через пробел или новую строку
            if results:
                self.lbl_res["text"] = "\n".join(results)
            else:
                self.lbl_res["text"] = "Выберите хотя бы одну операцию"

            if results:
                self.lbl_res.config(text="\n".join(results), justify=LEFT)
            else:
                self.lbl_res.config(text="Выберите операцию", justify=CENTER)

        except ValueError:
            self.lbl_res["text"] = "Ошибка: введите числа!"

    def swap(self):
        v1 = self.ent1.get()
        v2 = self.ent2.get()
        self.ent1.delete(0, END)
        self.ent1.insert(0, v2)
        self.ent2.delete(0, END)
        self.ent2.insert(0, v1)

    def clear(self):
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.lbl_res.config(text="---", justify=CENTER)

    def exit_app(self):
        self.master.destroy()


# --- А вот эта часть запускает всё приложение ---
root = Tk()  # Создаем системное окно
root.geometry("300x450")  # Можно задать размер
app = App(root)  # Передаем окно в твой класс
root.mainloop()  # Запускаем бесконечный цикл (чтобы окно не закрылось сразу)
