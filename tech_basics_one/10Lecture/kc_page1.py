import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Knowledge Check")

# code to configure the size
# option 1
# root.geometry("850x450")

# option 2
height = 450
width = 850
root.minsize(height=height, width=width)


# definition to place a background image
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


# place an image on the gui
image_file_path = "images/store.jpeg"
set_background(root, image_file_path, width, height)

# place a button that will activate a button that will clear all the widgets
enter_button = tk.Button(text="Click here to enter store",
                         fg="blue",
                         font=("Lucida", 15, "bold"),
                         height=2,
                         width=20,
                         command=lambda: clear_widgets(root))
enter_button.place(relx=0.5, rely=0.3, anchor="center")

# code to execute the code
root.mainloop()
