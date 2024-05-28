import tkinter as tk
import random

# launch the gui window
root = tk.Tk()
root.title("Rock Paper Scissors Page 2")
root.minsize(height=450, width=850)
root.configure(background="black")

# initialise variables
user_selection_label = tk.Label()
comp_selection_label = tk.Label()
message = tk.Label()
user_score = 0
comp_score = 0

def press(user_selects):
    global user_selection_label, comp_selection_label, message, user_score, comp_score

    user_selection_label.destroy()
    comp_selection_label.destroy()
    message.destroy()


    user_selection_label = tk.Label(text=f"You selected {user_selects}")
    user_selection_label.place(relx=0.5, rely=0.6, anchor="center")

    # computer selection
    options = ["Rock", "Paper", "Scissors"]
    computer_selection = random.choice(options)

    comp_selection_label = tk.Label(text=f"The computer selected {computer_selection}")
    comp_selection_label.place(relx=0.5, rely=0.7, anchor="center")

    # write an if-else-if statement
    if user_selects == computer_selection:
        message = tk.Label(text="TRY AGAIN")
    elif user_selects == "Rock" and computer_selection == "Scissors":
        message = tk.Label(text="Rock smashes scissors. YOU WIN")
        user_score += 1
    elif user_selects == "Scissors" and computer_selection == "Paper":
        message = tk.Label(text="Scissor cuts paper. YOU WIN")
        user_score += 1
    elif user_selects == "Paper" and computer_selection == "Rock":
        message = tk.Label(text="Paper cover rocks. YOU WIN")
        user_score += 1
    else:
        message = tk.Label(text="The computer wins")
        comp_score += 1

    message.place(relx=0.5, rely=0.8, anchor="center")

    # user score label
    user_score_label = tk.Label(text=f"User score: {user_score}",
             relief=tk.RAISED,
             bg='#4834DF',
             fg="#ffffff",
             borderwidth=5,
             width=12
             )
    user_score_label.place(x=5, y=60)
    # computer score label
    comp_score_label = tk.Label(text=f"Computer score: {comp_score}",
                                relief=tk.RAISED,
                                bg='#4834DF',
                                fg="#ffffff",
                                borderwidth=5,
                                width=12
                                )
    comp_score_label.place(x=5, y=100)

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
                        text="🪨",
                        font=('Comic Sans MS', 20, 'bold'),
                        fg="blue",
                        # windows user can also change the background colour of the button
                        bg="red",
                        # mac users
                        #highlightbackground="pink",
                        # you can also adjust the height and width of the button
                        height=1,
                        width=4,
                        command=lambda: press("Rock")
                        )
rock_button.place(relx=0.5, rely=0.3, anchor="center")

# add a paper button
paper_button = tk.Button(root,
                         text="📄",
                         font=('Comic Sans MS', 20, 'bold'),
                         fg="blue",
                         # windows user can also change the background colour of the button
                         bg="red",
                         # mac users
                         #highlightbackground="pink",
                         # you can also adjust the height and width of the button
                         height=1,
                         width=4,
                         command=lambda: press("Paper"))
paper_button.place(relx=0.5, rely=0.4, anchor="center")

# add a scissors button
scissors_button = tk.Button(root,
                            text="✂️",
                            font=('Comic Sans MS', 20, 'bold'),
                            fg="blue",
                            # windows user can also change the background colour of the button
                            bg="red",
                            # mac users
                            #highlightbackground="pink",
                            # you can also adjust the height and width of the button
                            height=1,
                            width=4,
                            command=lambda: press("Scissors"))
scissors_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
