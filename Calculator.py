""" Calculator
-------------------------------------------------
"""


from tkinter import *

expression = ""  #globally declares the expression variable

# Function to update expression in the text entry box
def press(num):
    global expression   # point out the global expression variable
    expression = expression + str(num)  # concatenation of string
    equation.set(expression)  # update the expression by using set method

# Function to evaluate the final expression
def equalpress():
    # Handling the errors like zero division error etc. 
    try:
        global expression
        # eval function evaluates the expression and str function convert the result into string 
        total = str(eval(expression))
        equation.set(total)
        expression = ""  # initialize expression variable by empty string

    # If error is generated then the except block handles it
    except:
        equation.set("error")
        expression = ""
    
# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("") 

# Main driver code
if __name__=="__main__":
    gui = Tk()  # Creates a GUI window
    gui.configure(background="#555555")  # Background colour
    gui.title("Calculator")  # Title of window
    gui.geometry("340x185") # Configuration of window
    equation = StringVar() # StringVar() is the variable class, we create an instance of this class 
    expression_field = Entry(gui, textvariable=equation)  # create the text entry box for showing the expression.
    expression_field.grid(columnspan = 4, ipadx=70)  # grid method is used for placing 
    # the widgets at respective positions in table like structure 
    equation.set('Enter your expression')
    # create Buttons and place at a particular location inside the root window . 
    # when user press the button, the command or function affiliated to that button is executed . 
    button1 = Button(gui, text='1', fg='white', bg='#343434', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='2', fg='white', bg='#343434', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='3', fg='white', bg='#343434', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    plus = Button(gui, text='+', fg='black', bg='#343434', command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3)

    button4 = Button(gui, text='4', fg='white', bg='#343434', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='5', fg='white', bg='#343434', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='6', fg='white', bg='#343434', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    
    minus= Button(gui, text='-', fg='black', bg='#343434', command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3)

    button7 = Button(gui, text='7', fg='white', bg='#343434', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='8', fg='white', bg='#343434', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='9', fg='white', bg='#343434', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    multiply = Button(gui, text='*', fg='black', bg='#343434', command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3)

    button0 = Button(gui, text='0', fg='black', bg='#343434', command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0)

    clear = Button(gui, text='Clear', fg='black', bg='#343434', command=clear, height=1, width=7) 
    clear.grid(row=5, column=1)

    equal = Button(gui, text='=', fg='black', bg='#343434', command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2)

    divide = Button(gui, text='/', fg='black', bg='#343434', command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3)

    decimal = Button(gui, text='.', fg='black', bg='#343434', command=lambda: press("."), height=1, width=7) 
    decimal.grid(row=6, column=0)
    
    gui.mainloop()  # Start the gui