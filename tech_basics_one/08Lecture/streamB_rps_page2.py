import tkinter as tk
import random

# launch the gui window
root = tk.Tk()
root.title("Rock Paper Scissors Page 2")
root.minsize(height=450, width=850)
root.configure(background="black")

# initialize the labels
user_selection_label = tk.Label()


def generate_computer_selection():
    options = ['Rock', 'Paper', 'Scissors']
    computer_selection = random.choice(options)

    return computer_selection


def press(user_selects):
    global user_selection_label

    # destroy any historical widgets that were created
    user_selection_label.destroy()

    user_selection_label = tk.Label(root,
                                    text=f"You selected {user_selects}",
                                    bg="black",
                                    fg="white",
                                    font=("Papyrus", 20, "bold")
                                    )
    user_selection_label.place(relx=0.5, rely=0.7, anchor="center")

    # call the definition that selects an option randomly
    comp_selects = generate_computer_selection()
    comp_selection_label = tk.Label(root,
                                    text=f"The computer selected {comp_selects}",
                                    bg="black",
                                    fg="white",
                                    font=("Papyrus", 20, "bold")
                                    )
    comp_selection_label.place(relx=0.5, rely=0.8, anchor="center")


# add a welcome label
welcome_label = tk.Label(
    text="WELCOME TO THE ROCK PAPER SCISSORS GAME",
    font=("Papyrus", 25, "bold"),
    fg="green",
    bg="black"
)
welcome_label.place(relx=0.5, rely=0.1, anchor="center")

selection_label = tk.Label(
    text="PLEASE SELECT...",
    font=("Papyrus", 25, "bold"),
    fg="green",
    bg="black"
)
selection_label.place(relx=0.5, rely=0.2, anchor="center")

# add a rock button
rock_button = tk.Button(root,
                        command=lambda: press("Rock"),
                        text="🪨",
                        font=('Comic Sans MS', 20, 'bold'),
                        fg="blue",
                        # windows user can also change the background colour of the button
                        bg="red",
                        # mac users
                        #highlightbackground="pink",
                        # you can also adjust the height and width of the button
                        height=1,
                        width=4)
rock_button.place(relx=0.5, rely=0.3, anchor="center")

# add a paper button
paper_button = tk.Button(root,
                         command=lambda: press("Paper"),
                         text="📄",
                         font=('Comic Sans MS', 20, 'bold'),
                         fg="blue",
                         # windows user can also change the background colour of the button
                         bg="red",
                         # mac users
                         #highlightbackground="pink",
                         # you can also adjust the height and width of the button
                         height=1,
                         width=4)
paper_button.place(relx=0.5, rely=0.4, anchor="center")

# add a scissors button
scissors_button = tk.Button(root,
                            text="✂️",
                            command=lambda: press("Scissors"),
                            font=('Comic Sans MS', 20, 'bold'),
                            fg="blue",
                            # windows user can also change the background colour of the button
                            bg="red",
                            # mac users
                            #highlightbackground="pink",
                            # you can also adjust the height and width of the button
                            height=1,
                            width=4)
scissors_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
