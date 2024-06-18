import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()
# give your gui a title
root.title("Place image")

# define size of screen and the image
screen_height = 450
screen_width = 850
image_width = screen_width
image_height = screen_height

# cerate screen
root.minsize(height=screen_height, width=screen_width)


# definition to place a background image
# this includes options to resize and place the image on specific coordinates
def set_background(root, image_file_path, width, height, x, y):
    img = Image.open(image_file_path)
    # code for resizing the image
    resize_img = img.resize((width, height))
    photo = ImageTk.PhotoImage(resize_img)
    label = tk.Label(root, image=photo)
    label.image = photo  # places the image on the gui
    label.place(x=x, y=y)


# place the first image on the screen
# this is the same size as the screen
image_file_path = "images/store.jpeg"
set_background(root, image_file_path, image_width, image_height, 0, 0)

# create a definition to add a second image
# adjust information accordingly
def add_second_image():
    global image_width, image_height

    image_file_path = "images/store.jpeg"
    image_width = round(image_width*0.9)
    image_height = round(image_height*0.9)
    set_background(root, image_file_path, image_width, image_height, 20, 20)


def add_third_image():
    global image_width, image_height

    image_file_path = "images/store.jpeg"
    image_width = round(image_width * 0.9)
    image_height = round(image_height * 0.9)

    set_background(root, image_file_path, image_width, image_height, 40, 40)


root.after(2000, add_second_image) # specify the amount of time to place second image
# the time is in milliseconds
root.after(4000, add_third_image) # specify the amount of time to place third image

# code to execute the code
root.mainloop()