import tkinter as tk
import tkinter.messagebox as msg

string = ""
screen = tk.Tk()
screen.geometry('400x270')
screen.title('Calculator')

def backspace(field):
    global string
    string = ''.join(string[:-1])
    field.set(string)
def input_num(num, field):
    global string
    string = string + str(num)
    field.set(string)
def clear_input():
    global string
    string = ""
    field.set("")
def answer(field):
    global string
    try:
        result = str(float((eval(string))))
        field.set(result)
    except:
        msg.showerror("Error", "Something Wrong!")

field = tk.StringVar()
input_frame = tk.Entry(screen, textvariable=field)
input_frame.place(height=50)
input_frame.grid(columnspan=6, ipadx=100, ipady=6)
zero = tk.Button(screen, text='0', fg='white', command=lambda:input_num(0,field), height=2, width=7)
zero.grid(row=5, column=1)
one = tk.Button(screen, text='1', fg='white', command=lambda:input_num(1, field), height=2, width=7)
one.grid(row=4, column=0)
two = tk.Button(screen, text='2', fg='white', command=lambda:input_num(2, field), height=2, width=7)
two.grid(row=4, column=1)
three = tk.Button(screen, text='3', fg='white', command=lambda:input_num(3, field), height=2, width=7)
three.grid(row=4, column=2)
four = tk.Button(screen, text='4', fg='white', command=lambda:input_num(4, field), height=2, width=7)
four.grid(row=3, column=0)
five = tk.Button(screen, text='5', fg='white', command=lambda:input_num(5, field), height=2, width=7)
five.grid(row=3, column=1)
six = tk.Button(screen, text='6', fg='white', command=lambda:input_num(6, field), height=2, width=7)
six.grid(row=3, column=2)
seven = tk.Button(screen, text='7', fg='white', command=lambda:input_num(7, field),height=2, width=7)
seven.grid(row=2, column=0)
eight = tk.Button(screen, text='8', fg='white', command=lambda:input_num(8, field), height=2, width=7)
eight.grid(row=2, column=1)
nine = tk.Button(screen, text='9', fg='white', command=lambda:input_num(9, field), height=2, width=7)
nine.grid(row=2, column=2)
plus = tk.Button(screen, text='+', fg='white', command=lambda:input_num('+', field), height=2, width=7)
plus.grid(row=4, column=3)
minus = tk.Button(screen, text='-', fg='white', command=lambda:input_num('-', field), height=2, width=7)
minus.grid(row=3, column=3)
multiply = tk.Button(screen, text='*', fg='white', command=lambda:input_num('*', field), height=2, width=7)
multiply.grid(row=2, column=3)
divide = tk.Button(screen, text='/', fg='white', command=lambda:input_num('/', field), height=2, width=7)
divide.grid(row=1, column=3)
delete = tk.Button(screen, text='<-', fg='white', command=lambda:backspace(field), height=2, width=7)
delete.grid(row=1, column=2)
clear = tk.Button(screen, text='C', fg='white', command=lambda:clear_input(), height=2, width=7)
clear.grid(row=1, column=1)
result = tk.Button(screen, text='=', fg='white', command=lambda:answer(field), height=2, width=7)
result.grid(row=5, column=3)
dot = tk.Button(screen, text='.', fg='white', command=lambda:input_num('.',field), height=2, width=7)
dot.grid(row=5, column=2)
modulo = tk.Button(screen, text='%', fg='white', command=lambda:input_num('%', field), height=2, width=7)
modulo.grid(row=5, column=0)

screen.mainloop()
