import tkinter as tk

root = tk.Tk()
# root.configure(background='black')
root.geometry('400x600')

textbox = tk.Text(root, background='black', foreground='green')
textbox.pack(fill='both', expand=True)

root.mainloop()