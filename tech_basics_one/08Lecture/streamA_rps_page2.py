import tkinter as tk
import random

# launch the window
root = tk.Tk()
root.title("ROCK PAPER SCISSORS PAGE 2")
root.minsize(height=450, width=850)
root.configure(background="black")

# add a welcome label
welcome_label = tk.label = tk.Label(root,
                                    text="WELCOME PLAYER! LET THE BATTLE BEGIN",
                                    #font="Helvetica 15 bold",
                                    font=('Comic Sans MS', 20, 'bold'),
                                    fg="white",
                                    bg="black")

welcome_label.place(relx=0.5, y=20, anchor="center")

selection_label = tk.label = tk.Label(root,
                                    text="SELECT YOUR CHOICE - ROCK, PAPER, SCISSORS....",
                                    #font="Helvetica 15 bold",
                                    font=('Comic Sans MS', 20, 'bold'),
                                    fg="white",
                                    bg="black")

selection_label.place(relx=0.5, y=80, anchor="center")

# this definition is activated when the user clicks on the buttons
def press(user_selects):
    global user_selection_label

    user_selection_label.destroy()

    user_selection_label = tk.Label(root,
             text=f"You selected {user_selects}",
             bg="black",
             fg="white",
             font="Arial 15 bold"
             )
    user_selection_label.place(relx=0.5, y=300, anchor="center")


# initialise a user and computer selection variable
user_selection_label = tk.Label()

# add some buttons
# rock
rock_button = tk.Button(root,
                        text="🪨",
                        command=lambda:press("Rock"),
                        font=('Comic Sans MS', 20, 'bold'),
                        fg="blue",
                        # windows user can also change the background colour of the button
                        bg="red",
                        # mac users
                        #highlightbackground="pink",
                        # you can also adjust the height and width of the button
                        height=1,
                        width=4)
rock_button.place(relx=0.5, y=120, anchor="center")
# paper
paper_button = tk.Button(root,
                        text="🧻",
                        command=lambda:press("Paper"),
                        font=('Comic Sans MS', 20, 'bold'),
                        fg="blue",
                        # windows user can also change the background colour of the button
                        bg="red",
                        # mac users
                        #highlightbackground="pink",
                        # you can also adjust the height and width of the button
                        height=1,
                        width=4)
paper_button.place(relx=0.5, y=180, anchor="center")
# scissors
scissors_button = tk.Button(root,
                        text="✂️",
                        command=lambda:press("Scissors"),
                        font=('Comic Sans MS', 20, 'bold'),
                        fg="blue",
                        # windows user can also change the background colour of the button
                        bg="red",
                        # mac users
                        #highlightbackground="pink",
                        # you can also adjust the height and width of the button
                        height=1,
                        width=4)
scissors_button.place(relx=0.5, y=240, anchor="center")


root.mainloop()
