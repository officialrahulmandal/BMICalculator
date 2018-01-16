# importing packages
from tkinter import *
import tkinter.messagebox

# creating the main window and setting its properties
mainwindow = Tk()
mainwindow.geometry('400x300+300+100')
mainwindow.title('BMI Calculator')


# making a function to calculate BMI
def convert_this():
    # taking the input entered by the user
    myvar1 = var1.get()
    myvar2 = var2.get() / 100
    # Validator that checks there must be a valid input(NON ZERO)
    if myvar1 != 0 and myvar2 != 0:
        height_square = myvar2 * myvar2
        bmi = str(myvar1 / height_square)
        result_label = Label(mainwindow, text='Result :-' + str(bmi))
        result_label.grid(row=5, column=2)
        normal_bmi = Label(mainwindow, text="*******************************\n*   Normal Weight = 19-24.9 *\n*         "
                                            "Overweight = 25-29.9  *\n*    Obesity level 1 = 30-34.9  *\n*      Obesity "
                                            "level 2= 35-39.9  *\n*    Obesity level 3 >= 40         *\n***************"
                                            "****************")
        normal_bmi.grid(row=6, column=2)
    # if the input is zero then a message box pop up
    else:
        tkinter.messagebox.showinfo('Value Error', 'Zero is not acceptable')

# defining variable
var1 = DoubleVar()
var2 = DoubleVar()
# Top heading
top_heading = Label(mainwindow, text='BMI Calculator', font='Helvetica 18 bold')
top_heading.grid(row=1, column=2)
# input labels
height_label = Label(mainwindow, text='Enter your height')
height_label.grid(row=2, column=1)
weight_label = Label(mainwindow, text='enter your weight :-')
weight_label.grid(row=3, column=1)
# Input from users
height_input = Entry(mainwindow, textvariable=var2, width=30)
height_input.delete(1, END)
height_input.grid(row=2, column=2)
weight_input = Entry(mainwindow, textvariable=var1, width=30)
weight_input.delete(1, END)
weight_input.grid(row=3, column=2)
# button for showing the result
convert_button = Button(mainwindow, text='CALCULATE BMI', command=convert_this)
convert_button.grid(row=4, column=2)

mainwindow.mainloop()
