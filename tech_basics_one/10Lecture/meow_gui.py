import pygame as pg
import tkinter as tk

# code to create the gui window
root = tk.Tk()
# give your gui a title
root.title("Meow 🐱")
# set the background colour of the window
root.configure(background='orange')
# code to configure the size
root.geometry("650x450")

# initialize pygame library
pg.init()


def stop_cat_music():
    # stop the music
    pg.mixer.music.stop()
    # configure the button
    meow_button.configure(text="CLICK HERE TO PLAY AGAIN",
                          command=play_cat_music,
                          fg="blue")


def play_cat_music():
    # load the music and add -1 to play on repeat
    pg.mixer.music.load("music/Cats-loud-meow-sound-clip.mp3")
    pg.mixer.music.play(-1)
    # configure the button to update the text and stop the music
    meow_button.configure(text="PLEASE STOP THE MADNESS",
                          command=stop_cat_music,
                          fg="red")


# place a button
# create button with text 1
meow_button = tk.Button(root,
                        text="CLICK HERE TO HEAR 🐱🐱🐱",
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
                        command=play_cat_music
                        )
# place button with text MEOW, centered
meow_button.place(relx=0.5, rely=0.5, anchor="center")

# code to execute the code
root.mainloop()
