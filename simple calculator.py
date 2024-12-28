from tkinter import *

# The main widget is named root, all the other widgets will be its children
root = Tk()
root.title("Simple calculator") # title

# the text box where we will see the expression
text_input_field = Entry(root, width=25, bg="white", fg="black", borderwidth=4)
text_input_field.grid(row=1, column=1)

# all functions region -------------------

# run to add user input in text box
def button_click(arg):
    previous_inputs = text_input_field.get()
    text_input_field.delete(0, END)
    text_input_field.insert(0, str(previous_inputs) + str(arg))

# run when user input is clear
def button_clear():
    text_input_field.delete(0, END)

# run when user input is '='
def output():
    expression = text_input_field.get()
    text_input_field.delete(0, END)
    try:
        for operator in ('+', '-', '*', '/', '%'):
            if operator in expression:
                two_exp = expression.split(operator)
                if operator == '/' and float(two_exp[1]) == 0:
                    text_input_field.insert(0, "Error: Division by Zero")
                else:
                    text_input_field.insert(0, calculator(float(two_exp[0]), float(two_exp[1]), operator))
                break
    except Exception:
        text_input_field.insert(0, "Error")

# the function which does the calculation-
def calculator(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        return n1 / n2
    elif operator == '%':
        return n1 % n2

# ------------------------------------------------------
# button section, button_selection is a widget which is parent to all buttons, and child of root.

button_section = Label(root, bg="#c0e2e0", width=40, border=15)
button_section.grid(row=2, column=1)
# Buttons-
# variables 
w, h, px, py = 5, 3, 2, 2
# number buttons-

b1 = Button(button_section, text="1", padx=px, pady=py, width=w, height=h, command=lambda: button_click("1"))
b1.grid(row=1, column=1)

b2 = Button(button_section, text="2", padx=px, pady=py, width=w, height=h, command=lambda: button_click("2"))
b2.grid(row=1, column=2)

b3 = Button(button_section, text="3", padx=px, pady=py, width=w, height=h, command=lambda: button_click("3"))
b3.grid(row=1, column=3)

b4 = Button(button_section, text="4", padx=px, pady=py, width=w, height=h, command=lambda: button_click("4"))
b4.grid(row=2, column=1)

b5 = Button(button_section, text="5", padx=px, pady=py, width=w, height=h, command=lambda: button_click("5"))
b5.grid(row=2, column=2)

b6 = Button(button_section, text="6", padx=px, pady=py, width=w, height=h, command=lambda: button_click("6"))
b6.grid(row=2, column=3)

b7 = Button(button_section, text="7", padx=px, pady=py, width=w, height=h, command=lambda: button_click("7"))
b7.grid(row=3, column=1)

b8 = Button(button_section, text="8", padx=px, pady=py, width=w, height=h, command=lambda: button_click("8"))
b8.grid(row=3, column=2)

b9 = Button(button_section, text="9", padx=px, pady=py, width=w, height=h, command=lambda: button_click("9"))
b9.grid(row=3, column=3)

b0 = Button(button_section, text="0", padx=px, pady=py, width=w, height=h, command=lambda: button_click("0"))
b0.grid(row=4, column=2)

# function buttons-

b_add = Button(button_section, text="+", padx=px, pady=py, width=w, height=h, command=lambda: button_click("+"))
b_add.grid(row=1, column=4)

b_sub = Button(button_section, text="-", padx=px, pady=py, width=w, height=h, command=lambda: button_click("-"))
b_sub.grid(row=2, column=4)

b_mul = Button(button_section, text="*", padx=px, pady=py, width=w, height=h, command=lambda: button_click("*"))
b_mul.grid(row=3, column=4)

b_div = Button(button_section, text="/", padx=px, pady=py, width=w, height=h, command=lambda: button_click("/"))
b_div.grid(row=4, column=4)

b_mod = Button(button_section, text="%", padx=px, pady=py, width=w, height=h, command=lambda: button_click("%"))
b_mod.grid(row=5, column=4)

b_dot = Button(button_section, text=".", padx=px, pady=py, width=w, height=h, command=lambda: button_click("."))
b_dot.grid(row=5, column=2)

b_equ = Button(button_section, text="=", padx=px, pady=py, width=w, height=h, command=output)
b_equ.grid(row=4, column=3)

b_clr = Button(button_section, text="Clear", padx=px, pady=py, width=w, height=h, command=button_clear)
b_clr.grid(row=4, column=1)

# The End of button section----------------------------

# the below line will tell to continuously loop through the code, so that any updates made by the user (button clicks, animations) can be shown in real time.

root.mainloop()
