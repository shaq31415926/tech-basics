import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Rock Paper Scissors - Page1")

# code to configure the size
# option 1
# root.geometry("750x450")

# option 2
height = 450
width = 850
root.minsize(height=height, width=width)


# place a background image
def set_background(root, image_file_path):
    """
    You need to specify the variable that creates the gui frame and the file path of the image
    """

    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)


image_file_path = "image/rps.jpeg"
set_background(root, image_file_path)


# code to execute the code
root.mainloop()
