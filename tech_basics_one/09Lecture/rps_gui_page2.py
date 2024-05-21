import tkinter as tk

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

# add a rock button
rock_button = tk.Button(root,
                        text="ROCK",
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