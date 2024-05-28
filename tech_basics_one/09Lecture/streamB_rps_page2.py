import tkinter as tk
import random

# launch the gui window
root = tk.Tk()
root.title("Rock Paper Scissors Page 2")
root.minsize(height=450, width=850)
root.configure(background="black")

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

# initialize labels when you start the game
user_selection_label = tk.Label()
comp_selection_label = tk.Label()
message = tk.Label()
user_score = 0
comp_score = 0


def press(user_selects):
    global user_selection_label, comp_selection_label, message, user_score, comp_score

    # destroy any historical widgets that were created
    user_selection_label.destroy()
    comp_selection_label.destroy()
    message.destroy()

    user_selection_label = tk.Label(root,
                                    text=f"You selected {user_selects}",
                                    bg="black",
                                    fg="white",
                                    font=("Papyrus", 20, "bold")
                                    )
    user_selection_label.place(relx=0.5, rely=0.7, anchor="center")

    # call the definition that selects an option randomly
    options = ['Rock', 'Paper', 'Scissors']
    comp_selects = random.choice(options)

    comp_selection_label = tk.Label(root,
                                    text=f"The computer selected {comp_selects}",
                                    bg="black",
                                    fg="white",
                                    font=("Papyrus", 20, "bold")
                                    )
    comp_selection_label.place(relx=0.5, rely=0.8, anchor="center")

    # write our winning logic -
    if user_selects == comp_selects:
        message = tk.Label(root,
                           text="THEY TIE",
                           bg="black",
                           fg="white",
                           font=("Papyrus", 20, "bold"))
    elif user_selects == "Rock" and comp_selects == "Scissors":
        message = tk.Label(root,
                           text="Rock smashes scissors. You win!",
                           bg="black",
                           fg="white",
                           font=("Papyrus", 20, "bold"))
        user_score += 1
    elif user_selects == "Paper" and comp_selects == "Rock":
        message = tk.Label(root,
                           text="Paper cover rocks. You win!",
                           bg="black",
                           fg="white",
                           font=("Papyrus", 20, "bold"))
        user_score += 1
    elif user_selects == "Scissors" and comp_selects == "Paper":
        message = tk.Label(root,
                           text="Scissor cuts Paper. You win!",
                           bg="black",
                           fg="white",
                           font=("Papyrus", 20, "bold"))
        user_score += 1
    else:
        message = tk.Label(root,
                           text="THE COMPUTER WINS",
                           bg="black",
                           fg="white",
                           font=("Papyrus", 20, "bold"))
        comp_score += 1

    message.place(relx=0.5, rely=0.9, anchor="center")

    user_score_label = tk.Label(root,
                                text=f"User score: {user_score}",
                                relief=tk.RAISED,
                                fg="#ffffff",
                                bg="#4834DF",
                                borderwidth=5,
                                width=10
                                )
    user_score_label.place(x=5, y=80)
    comp_score_label = tk.Label(root,
                                text=f"Computer score: {comp_score}",
                                relief=tk.RAISED,
                                fg="#ffffff",
                                bg="#4834DF",
                                borderwidth=5,
                                width=10
                                )
    comp_score_label.place(x=5, y=120)

# add a rock button
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
rock_button.place(relx=0.5, rely=0.3, anchor="center")

# add a paper button
paper_button = tk.Button(root,
                        text="📄",
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
paper_button.place(relx=0.5, rely=0.4, anchor="center")

# add a scissors button
scissors_button = tk.Button(root,
                        command=lambda:press("Scissors"),
                        text="✂️",
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