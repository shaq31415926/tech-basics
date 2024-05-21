import tkinter as tk
from PIL import Image, ImageTk

# launch the gui window
root = tk.Tk()
root.title("ROCK PAPER SCISSORS PAGE 1")
root.minsize(height=450, width=850)


# definition to set the background image
def set_background(root, image_file_path):
    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)


# image file path
image_file_path = "image/rps.jpeg"
# call the definition
set_background(root, image_file_path)

# place a label widget
welcome_label = tk.Label(root,
         text="WELCOME TO THE MOST EPIC GAME EVER",
         font="arial 15 bold",
         fg="white",
         bg="black")
welcome_label.place(relx=0.5, rely=0.1, anchor="center")
#welcome_label.place(x=10, y=10)
name_label = tk.Label(root,
         text="What is your name?",
         font="arial 15 bold",
         fg="white",
         bg="black")
name_label.place(relx=0.5, rely=0.2, anchor="center")

# place an entry box so the user can enter their name
name = tk.StringVar()
name_box = tk.Entry(root,
                    textvar=name,
                    font="arial 15 bold")
name_box.place(relx=0.5, rely=0.3, anchor="center")


root.mainloop()
