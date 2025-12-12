from tkinter import *

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "%", "<-", "C", "=",
            "1/x", "X^2", "sqrtx", "/",
            "1", "2", "3", "*",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "."
        ]

        x = 10
        y = 90
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15), command=com).place(x=x, y=y, width=80, height=60)
            x += 80
            if x > 250:
                x = 10
                y += 81

        # Привязываем клавиши к функции
        self.bind_keys()

    def bind_keys(self):
        keys = {
            '1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9',
            '0': '0', '+': '+', '-': '-',
            '*': '*', '/': '/', '(': '(',
            ')': ')', '.': '.', 'Return': '=', 
            'BackSpace': '<-', 'c': 'C', 'C': 'C'
        }

        for key, value in keys.items():
            self.master.bind(key, lambda event, val=value: self.logicalc(val))

        # Привязываем F1 к функции для открытия нового окна
        self.master.bind('<F1>', self.show_info)

    def show_info(self, event=None):
        info_window = Toplevel(self.master)
        info_window.title("Информация")
        info_window.geometry("500x200")
        
        label = Label(info_window, text="Это калькулятор на Tkinter от (С)tukan4ek, 2024.\n Спасибо маме и папе за всё!\nНажмите F1 для этой информации(Да,это бесполезная подказка).", font=("Times New Roman", 12))
        label.pack(pady=20)

        button_close = Button(info_window, text="Закрыть", command=info_window.destroy)
        button_close.pack(pady=10)

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "<-":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            try:
                self.formula = str(eval(self.formula))
            except Exception:
                self.formula = "Ошибка"
        elif operation == "%":
            self.formula = str(eval(self.formula) / 100)
        elif operation == "1/x":
            try:
                self.formula = str(1 / (eval(self.formula)))
            except Exception:
                self.formula = "Ошибка"
        elif operation == "sqrtx":
            try:
                self.formula = str(eval(self.formula) ** 0.5)
            except Exception:
                self.formula = "Ошибка"
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("340x570+200+200")
    root.iconbitmap("calc.ico")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
