import tkinter as tk
import random
import string

def generate_random_text():
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choices(valid_chars, k=random.randint(8, 45)))
    return random_string

def custom_close_protocol():
    global task_id
    textbox.config(foreground='red', font=('Helvetica', 18))
    if task_id is not None:
        root.after_cancel(task_id)
        task_id = None
    textbox.insert('end', 'ERROR !!! ERROR !!!\n')
    textbox.insert('end', '!!!! COMPUTER CORRUPTED !!!!\n')
    textbox.insert('end', 'ERROR !!! ERROR !!!')
    textbox.see('end')
    root.after(5000, root.destroy)

def initial_update_text():
    textbox.insert('end', 'Accessing Kernel...\n')
    textbox.insert('end', 'Scanning Operating System....\n')
    textbox.insert('end', 'Checking Windows Files.....\n')
    textbox.insert('end', 'Injecting Trojan H1X32 into System Event Viewers....')
    
def update_text():
    global task_id
    random_string = generate_random_text()
    textbox.insert('end', random_string+"\n")
    textbox.see('end')
    task_id = root.after(80, update_text)

root = tk.Tk()
root.geometry('400x600')

textbox = tk.Text(root, background='black', foreground='green')
textbox.pack(fill='both', expand=True)

root.protocol("WM_DELETE_WINDOW", custom_close_protocol)

initial_update_text()
update_text()

root.mainloop()