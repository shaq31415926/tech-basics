import tkinter as tk

# List of improvements to the calculator
# TODO: On division by zero the calculator does not work
# fixed - Does not display x or division sign (check line 291-295)
# TODO: The expression can contain multiple operators
# TODO: Keep track of the total - but you can find this is stream B code
# TODO: add a delete button

# code to create the gui window
root = tk.Tk()
# change the title
root.title("My First Calculator")
# change the background colour
root.configure(background="orange")
# change the size - width x height
root.geometry("410x175")

# creating our display box
equation = tk.StringVar()
expression_box = tk.Entry(root, textvariable=equation)
expression_box.grid(columnspan=4, ipadx=110)

# writing the code so we can keep track what the user enters
expression_display = ""


def press(value):
    global expression_display

    expression_display = expression_display + str(value)
    equation.set(expression_display)


# create button with text 1
button1 = tk.Button(root,
                    text=" 1 ",
                    command=lambda: press(1),
                    # adjust the colour and font
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    # you can also adjust the height and width of the button
                    height=1,
                    width=7
                    )
# place button with text 1
button1.grid(row=2, column=0)

# place button with text 2
button2 = tk.Button(root,
                    text=" 2 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(2)
                    )
button2.grid(row=2, column=1)

# place button with text 3
button3 = tk.Button(root,
                    text=" 3 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(3)
                    )
button3.grid(row=2, column=2)

# place button with text 4
button4 = tk.Button(root,
                    text=" 4 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(4)
                    )
button4.grid(row=3, column=0)

# place button with text 5
button5 = tk.Button(root,
                    text=" 5 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(5)
                    )
button5.grid(row=3, column=1)

# place button with text 6
button6 = tk.Button(root,
                    text=" 6 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(6)
                    )
button6.grid(row=3, column=2)

# place button with text 7
button7 = tk.Button(root,
                    text=" 7 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(7)
                    )
button7.grid(row=4, column=0)

# place button with text 8
button8 = tk.Button(root,
                    text=" 8 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(8)
                    )
button8.grid(row=4, column=1)

# place button with text 9
button9 = tk.Button(root,
                    text=" 9 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(9)
                    )
button9.grid(row=4, column=2)

# place button with text 0
button0 = tk.Button(root,
                    text=" 0 ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(0)
                    )
button0.grid(row=5, column=0)

# place button with text .
decimal = tk.Button(root,
                    text=" . ",
                    fg="blue",
                    font="arial 15 bold",
                    # windows user can also change the background colour of the button
                    bg="red",
                    # mac users
                    highlightbackground="pink",
                    height=1,
                    width=7,
                    command=lambda: press(".")
                    )
decimal.grid(row=5, column=1)

# place button with text +
plus = tk.Button(root,
                 text=" + ",
                 fg="blue",
                 font="arial 15 bold",
                 # windows user can also change the background colour of the button
                 bg="red",
                 # mac users
                 highlightbackground="pink",
                 height=1,
                 width=7,
                 command=lambda: press("+")
                 )
plus.grid(row=2, column=3)

# place button with text minus
minus = tk.Button(root,
                  text=" - ",
                  fg="blue",
                  font="arial 15 bold",
                  # windows user can also change the background colour of the button
                  bg="red",
                  # mac users
                  highlightbackground="pink",
                  height=1,
                  width=7,
                  command=lambda: press("-")
                  )
minus.grid(row=3, column=3)

# place button with text divide
divide = tk.Button(root,
                   text=" ÷ ",
                   fg="blue",
                   font="arial 15 bold",
                   # windows user can also change the background colour of the button
                   bg="red",
                   # mac users
                   highlightbackground="pink",
                   height=1,
                   width=7,
                   command=lambda: press("÷")
                   )
divide.grid(row=5, column=3)

# place button with text multiply
multiply = tk.Button(root,
                     text=" x ",
                     fg="blue",
                     font="arial 15 bold",
                     # windows user can also change the background colour of the button
                     bg="red",
                     # mac users
                     highlightbackground="pink",
                     height=1,
                     width=7,
                     command=lambda: press("x")
                     )
multiply.grid(row=4, column=3)


def clear_display():
    global expression_display

    expression_display = ""
    equation.set("")


# place a clear button
clear = tk.Button(root,
                  text=" AC ",
                  fg="blue",
                  font="arial 15 bold",
                  # windows user can also change the background colour of the button
                  bg="red",
                  # mac users
                  highlightbackground="pink",
                  height=1,
                  width=7,
                  command=clear_display
                  )
clear.grid(row=1, column=0)


def press_equal():
    global expression_display

    # this replaces the signs with cross and divides
    for char in expression_display:
        if char == "x":
            expression_display = expression_display.replace("x", "*")
        if char == "÷":
            expression_display = expression_display.replace("÷", "/")

    total = str(eval(expression_display))
    equation.set(total)


# place a equal button
equals = tk.Button(root,
                   text=" = ",
                   fg="blue",
                   font="arial 15 bold",
                   # windows user can also change the background colour of the button
                   bg="red",
                   # mac users
                   highlightbackground="pink",
                   height=1,
                   width=7,
                   command=press_equal
                   )
equals.grid(row=5, column=2)

# you need to add this at the end to launch the window
root.mainloop()
