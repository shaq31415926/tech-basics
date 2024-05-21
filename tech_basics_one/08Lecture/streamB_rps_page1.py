import tkinter as tk
from PIL import Image, ImageTk

# launch the gui window
root = tk.Tk()
root.title("Rock Paper Scissors Page 1")
root.minsize(height=450, width=850)


# this definitions set a background image
def set_background(root, image_file_path):
    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)


image_file_path = "image/rps.jpeg"  # variable that contains the file path of our background image
set_background(root, image_file_path)

welcome_label = tk.Label(root,
                         text="WELCOME TO THE ROCK PAPER SCISSORS GAME",
                         #font="Arial 15 bold",
                         font=("Comic Sans MS", 15, "bold"),
                         bg="black",
                         fg="white")
welcome_label.place(relx=0.5, y=20, anchor="center")

name_label = tk.Label(root,
                      text="PLEASE ENTER YOUR NAME?!",
                      font="Arial 15 bold",
                      bg="black",
                      fg="white")
name_label.place(relx=0.5, y=70, anchor="center")

# create an entry box that accepts the user name
name = tk.StringVar()
name_box = tk.Entry(root,
                    textvar=name,
                    font="Arial 15 bold",
                    fg="blue"
                    )
name_box.place(relx=0.5, y=110, anchor="center")

root.mainloop()
