import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()
# give your gui a title
root.title("My Pencil Store")
# code to configure the size
# option 1
#root.geometry("650x450")
# option 2
width = 650
height = 450
root.minsize(height=450, width=650)


def set_background(root, image_file_path, width, height):
    img = Image.open(image_file_path)
    # code for resizing the image
    resize_img = img.resize((width, height))
    photo = ImageTk.PhotoImage(resize_img)
    label = tk.Label(root, image=photo)
    label.image = photo  # places the image on the gui
    label.place(x=0, y=0, relwidth=1, relheight=1)


# this definition clear everything you just created
def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()


def second_page(root, width, height):
    # clear widgets
    clear_widgets(root)

    # place background image
    image_file_path = "images/pencils.jpeg"
    set_background(root, image_file_path, width, height)

    # place a label
    welcome_label = tk.Label(root,
                             text="WELCOME TO MY ETHICALLY SOURCED PENCIL STORE",
                             font=('Comic Sans MS', 20, 'bold'),
                             fg="black",
                             # this could help with getting colour matches: https://imagecolorpicker.com/
                             bg="#f0c101")

    welcome_label.place(relx=0.5, rely=0.1, anchor="center")

    # place a homepage button
    homepage_button = tk.Button(root,
                                text="🏠",
                                command=lambda: home_page(root, width, height))
    homepage_button.place(relx=0.5, rely=0.9, anchor="center")


def home_page(root, width, height):
    # clear any widgets that were created
    clear_widgets(root)

    # place the background image
    image_file_path = "images/store.jpeg"
    set_background(root, image_file_path, int(width / 1.1), int(height / 1.1))
    #set_background(root, image_file_path, width-20, height-20)
    # place a button on top of the background image
    enter_button = tk.Button(root,
                             text="Click here to enter",
                             command=lambda: second_page(root, width, height))
    enter_button.place(relx=0.5, rely=0.35, anchor="center")


# creating your home page
home_page(root, width, height)

# code to execute the window
root.mainloop()