import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Rezize image")

# code to configure the size
# define the screen width and height
screen_height = 1450
screen_width = 1850
# you can also define the image width and height
# if you want it to be the same size as the screen, set the image width and height
image_width = screen_width
image_height = screen_height

root.minsize(height=screen_height, width=screen_width)


# definition to place a background image
def set_background(root, image_file_path, width, height):
    img = Image.open(image_file_path)
    # code for resizing the image
    resize_img = img.resize((width, height))
    photo = ImageTk.PhotoImage(resize_img)
    label = tk.Label(root, image=photo)
    label.image = photo  # places the image on the gui
    label.place(x=0, y=0, relwidth=1, relheight=1)


# place an image on the gui
image_file_path = "images/store.jpeg"
set_background(root, image_file_path, image_width, image_height)


# code to execute the code
root.mainloop()
