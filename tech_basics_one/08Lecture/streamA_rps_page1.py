import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("ROCK PAPER SCISSORS PAGE 1")
root.minsize(height=450, width=850)


def set_background(root, image_file_path):
    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)


# image file path
image_file_path = "image/rps.jpeg"
set_background(root, image_file_path)

root.mainloop()
