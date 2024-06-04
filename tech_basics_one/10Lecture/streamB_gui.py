import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()
# give your gui a title
root.title("Knowledge Check")

# code to configure the size
# option 2
screen_height = 450
screen_width = 850
image_width = screen_width - 20
image_height = screen_height - 20

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


def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()


def home_page(root, width, height):
    clear_widgets(root)

    # place an image on the gui
    image_file_path = "images/store.jpeg"
    set_background(root, image_file_path, width, height)

    # create a button
    enter_button = tk.Button(root,
                             text="Click here to enter",
                             command=lambda: second_page(root, image_width, image_height))
    enter_button.place(relx=0.5, rely=0.3, anchor="center")


def second_page(root, width, height):
    # clears any widgets that were created
    clear_widgets(root)
    # place a background image
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
    # add a home page button
    home_button = tk.Button(root,
                            text="🏠",
                            command=lambda: home_page(root, width, height))
    home_button.place(relx=0.5, rely=0.9, anchor="center")


# call the definition to create the home page
home_page(root, screen_width, screen_height)
# code to execute the code
root.mainloop()
