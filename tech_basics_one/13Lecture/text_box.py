import tkinter as tk

root = tk.Tk()
root.configure(background="pink")
root.geometry("400x400")

# create the text box
text_box = tk.Text(root,
                   bg="blue",
                   fg="white")
text_box.place(x=20, y=20, relwidth=0.9, relheight=0.9)  # these attributes ensure it takes up the entire screen


def save_entry():
    entry = text_box.get(1.0, tk.END)
    print(entry)

# save button
save_button = tk.Button(text="save",
                        command=save_entry)
save_button.place(x=200, y=200)
root.mainloop()