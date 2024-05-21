import tkinter as tk
import webbrowser

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Meow 🐱")

# set the background colour of the window
root.configure(background='orange')

# code to configure the size
# option 1
root.geometry("650x450")


# option 2
# root.minsize(height=450, width=650)

def launch_cat_video():
    url = "https://youtube.com/shorts/3bhkYoMWTFE?si=Oxg3u_BYbcUzRD82"
    webbrowser.open(url)


# place a button
# create button with text 1
meow_button = tk.Button(root,
                        text="CLICK HERE TO SEE 🐱🐱🐱",
                        # adjust the colour and font
                        fg="blue",
                        font="arial 16 bold",
                        # windows user can also change the background colour of the button
                        bg="red",
                        # mac users
                        highlightbackground="pink",
                        # you can also adjust the height and width of the button
                        height=5,
                        width=25,
                        command=launch_cat_video
                        )
# place button with text MEOW, centered
meow_button.place(relx=0.5, rely=0.5, anchor="center")

# code to execute the code
root.mainloop()
