import tkinter as tk

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Simple Calculator")

# set the background colour of the window
root.configure(background='orange')

# code to configure the size
# option 1
root.geometry("650x450")

# option 2
# root.minsize(height=450, width=650)

# code to execute the code
root.mainloop()
