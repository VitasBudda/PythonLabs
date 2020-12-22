import math
from tkinter import *

class Form:
    def __init__(self, parent):
        Label(parent, width=20, text=' Перше число:', pady=10).pack()
        self.entry1 = Entry(parent, width=20)
        self.entry1.pack()

        Label(parent, width=20, text='Друге число:', pady=10).pack()
        self.entry2 = Entry(parent, width=20)
        self.entry2.pack()

        Label(parent, width=20, text='Третє число:', pady=10).pack()
        self.entry3 = Entry(parent, width=20)
        self.entry3.pack()        

        self.perimetr = BooleanVar()
        Radiobutton(parent, width=10, text="Периметр", pady=10, variable=self.perimetr, value=1).pack()
        Radiobutton(parent, width=10, text="Площа", pady=10, variable=self.perimetr, value=0).pack()

        self.calcBtn = Button(parent, text="ОК", pady=10)
        self.calcBtn['command'] = self.calculate
        self.calcBtn.pack()

        self.resultLabel = Label(parent, width=40, pady=20, text='Результат')
        self.resultLabel.pack()

    def calculate(self):
        val1 = self.entry1.get()
        val2 = self.entry2.get()
        val3 = self.entry3.get()
        is_perimetr = self.perimetr.get()

        if not val1 or not val2 or not val3:
            self.resultLabel['text'] = 'Поля є обов\'язковими'
            return

        if not val1.isnumeric() or not val2.isnumeric() or not val3.isnumeric():
            self.resultLabel['text'] = 'Поля мають містити лише числа'
            return

        a = int(val1)
        b = int(val2)
        c = int(val3)

        res = (a + b > c and b + c > a and c + a > b)

        if res:
            res = 'Можна'
            P = a + b + c
            p = P / 2

            if is_perimetr:
                res += '\nПериметр: '
                res += str(P)
            else:
                res += '\nПлоща: '
                S = math.sqrt(p*(p-a)*(p-b)*(p-c))
                res += str(S)
        else:
            res = 'Не можна'

        self.resultLabel['text'] = f'Результат: {res}'

root = Tk()
root.title('Варіант 21')
root.resizable(False, False)

main = Form(root)

root.mainloop()