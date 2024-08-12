# Task 2 :- Calculator
from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="darkgray")  # Background color set to dark gray
    gui.title("Simple Calculator")
    gui.geometry("470x460")  # Adjusted size of the window

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=('arial', 20, 'bold'), bd=10, relief=SUNKEN, bg='lightgray')
    expression_field.grid(columnspan=4, ipadx=70, ipady=15, padx=5, pady=10)

    button_bg = 'gray'
    button_fg = 'black'
    button_font = ('arial', 16, 'bold')  # Adjusted font size for better visibility

    # Number buttons
    button1 = Button(gui, text='1', fg=button_fg, bg=button_bg,
                     command=lambda: press(1), height=2, width=5, font=button_font)
    button1.grid(row=2, column=0, padx=1, pady=1)

    button2 = Button(gui, text='2', fg=button_fg, bg=button_bg,
                     command=lambda: press(2), height=2, width=5, font=button_font)
    button2.grid(row=2, column=1, padx=1, pady=1)

    button3 = Button(gui, text='3', fg=button_fg, bg=button_bg,
                     command=lambda: press(3), height=2, width=5, font=button_font)
    button3.grid(row=2, column=2, padx=1, pady=1)

    button4 = Button(gui, text='4', fg=button_fg, bg=button_bg,
                     command=lambda: press(4), height=2, width=5, font=button_font)
    button4.grid(row=3, column=0, padx=1, pady=1)

    button5 = Button(gui, text='5', fg=button_fg, bg=button_bg,
                     command=lambda: press(5), height=2, width=5, font=button_font)
    button5.grid(row=3, column=1, padx=1, pady=1)

    button6 = Button(gui, text='6', fg=button_fg, bg=button_bg,
                     command=lambda: press(6), height=2, width=5, font=button_font)
    button6.grid(row=3, column=2, padx=1, pady=1)

    button7 = Button(gui, text='7', fg=button_fg, bg=button_bg,
                     command=lambda: press(7), height=2, width=5, font=button_font)
    button7.grid(row=4, column=0, padx=1, pady=1)

    button8 = Button(gui, text='8', fg=button_fg, bg=button_bg,
                     command=lambda: press(8), height=2, width=5, font=button_font)
    button8.grid(row=4, column=1, padx=1, pady=1)

    button9 = Button(gui, text='9', fg=button_fg, bg=button_bg,
                     command=lambda: press(9), height=2, width=5, font=button_font)
    button9.grid(row=4, column=2, padx=1, pady=1)

    button0 = Button(gui, text='0', fg=button_fg, bg=button_bg,
                     command=lambda: press(0), height=2, width=5, font=button_font)
    button0.grid(row=5, column=0, columnspan=1, padx=1, pady=1)

    # Operator buttons
    plus = Button(gui, text='+', fg=button_fg, bg=button_bg,
                  command=lambda: press("+"), height=2, width=5, font=button_font)
    plus.grid(row=2, column=3, padx=1, pady=1)

    minus = Button(gui, text='-', fg=button_fg, bg=button_bg,
                   command=lambda: press("-"), height=2, width=5, font=button_font)
    minus.grid(row=3, column=3, padx=1, pady=1)

    multiply = Button(gui, text='*', fg=button_fg, bg=button_bg,
                      command=lambda: press("*"), height=2, width=5, font=button_font)
    multiply.grid(row=4, column=3, padx=1, pady=1)

    divide = Button(gui, text='/', fg=button_fg, bg=button_bg,
                    command=lambda: press("/"), height=2, width=5, font=button_font)
    divide.grid(row=5, column=3, padx=1, pady=1)

    # Special buttons
    equal = Button(gui, text='=', fg=button_fg, bg='gray',
                   command=equalpress, height=2, width=5, font=button_font)
    equal.grid(row=5, column=2, padx=1, pady=1)

    clear = Button(gui, text='Clear', fg='black', bg='orange',
                   command=clear, height=2, width=11, font=button_font)
    clear.grid(row=10, column=1, columnspan=2, padx=1, pady=1)

    Decimal = Button(gui, text='.', fg=button_fg, bg=button_bg,
                     command=lambda: press('.'), height=2, width=5, font=button_font)
    Decimal.grid(row=5, column=1, padx=1, pady=1)

    gui.mainloop()
