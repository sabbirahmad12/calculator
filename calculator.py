from tkinter import *

root = Tk()
root.title("Calculator")

# entry section 

entry = Entry(root, width=38, font=("arial",15,"bold"))
entry.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
entry.focus_set()


# Function area

def button_click(number):
    current_click = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current_click) + str(number))

def button_clear():
    entry.delete(0,END)

def button_clear2():
    current_click = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current_click)[:-1])

def button_add():
    first_number = entry.get()
    global f_number
    global math 
    math = 'addition'
    f_number = float(first_number)
    entry.delete(0,END)

def button_subtract():
    first_number = entry.get()
    global f_number
    global math 
    math = 'subtraction'
    f_number = float(first_number)
    entry.delete(0,END)

def button_multiply():
    first_number = entry.get()
    global f_number
    global math 
    math = 'multiplication'
    f_number = float(first_number)
    entry.delete(0,END)

def button_divide():
    first_number = entry.get()
    global f_number
    global math 
    math = 'division'
    f_number = float(first_number)
    entry.delete(0,END)

def button_equal():
    second_number = entry.get()
    entry.delete(0,END)

    if math == 'addition':
        entry.insert(0,float(f_number) + float(second_number))

    elif math == 'subtraction':
        entry.insert(0,float(f_number) - float(second_number))

    elif math == 'multiplication':
        entry.insert(0,float(f_number) * float(second_number))

    elif math == 'division':
        entry.insert(0,float(f_number) / float(second_number))

    else:
        print("Invalid Your Number")



# Button Section 

button1 = Button(root, text = '1', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(1))
button2 = Button(root, text = '2', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(2))
button3 = Button(root, text = '3', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(3))
button4 = Button(root, text = '4', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(4))
button5 = Button(root, text = '5', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(5))
button6 = Button(root, text = '6', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(6))
button7 = Button(root, text = '7', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(7))
button8 = Button(root, text = '8', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(8))
button9 = Button(root, text = '9', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(9))
button0 = Button(root, text = '0', font=("arial",15,"bold"), fg= "#fff", bg = "#2a2d36", padx = 40, pady = 20, command = lambda: button_click(0))

button_add = Button(root, text = '+', font=("arial",15,"bold"), fg= "#fff", bg = "#808080", padx = 38, pady = 20, command = button_add)
button_subtract = Button(root, text = '-', font=("arial",15,"bold"), fg= "#fff", bg = "#808080", padx = 40, pady = 20, command = button_subtract)
button_multiply = Button(root, text = '×', font=("arial",15,"bold"), fg= "#fff", bg = "#808080", padx = 40, pady = 20, command = button_multiply)
button_divide = Button(root, text = '÷', font=("arial",15,"bold"), fg= "#fff", bg = "#808080", padx = 40, pady = 20, command = button_divide)
button_equal = Button(root, text = '=', font=("arial",15,"bold"), fg= "#fff", bg = "#FF9200", padx = 95, pady = 20, command = button_equal)
button_clear = Button(root, text = 'AC', font=("arial",15,"bold"), fg= "#fff", bg= "#3697f5", padx = 85, pady = 20, command = button_clear)
button_clear2 = Button(root, text = 'C', font=("arial",15,"bold"), fg= "#fff", bg = "#808080", padx = 38, pady = 20, command = button_clear2)
button_dot = Button(root, text = '.', font=("arial",15,"bold"), fg= "#fff", bg = "#808080", padx = 42, pady = 20, command = lambda: button_click('.'))

# put the button on the screen

button1.grid(row=4, column=0 )
button2.grid(row=4, column=1 )
button3.grid(row=4, column=2 )

button4.grid(row=3, column=0 )
button5.grid(row=3, column=1 )
button6.grid(row=3, column=2 )

button7.grid(row=2, column=0 )
button8.grid(row=2, column=1 )
button9.grid(row=2, column=2 )

button0.grid(row=5, column=0)
button_dot.grid(row=5, column=1 )
button_clear.grid(row=1, column=1, columnspan = 3)
button_clear2.grid(row=1, column=0)

button_add.grid(row=4, column=4 )
button_subtract.grid(row=3, column=4 )
button_multiply.grid(row=2, column=4 )
button_divide.grid(row=1, column=4 )
button_equal.grid(row=5, column=2, columnspan=3 )


root.mainloop()
