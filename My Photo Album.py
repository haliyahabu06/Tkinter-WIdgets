import tkinter as tk
from tkinter import Label, messagebox


window = tk.Tk()
window.title('My Photo Album')
window.geometry('400x420')
window.configure(bg='lightgray')

title_label = tk.Label(window, text='My Photo Album', fg='purple', font=('Arial', 16, 'bold'))
title_label.pack(pady=10)






def show_message():
    messagebox.showinfo('Great!', 'You clicked the photo!')

msg_button = tk.Button(window, text='Click Photo', bg='blue', fg='white', command=show_message)
msg_button.pack(pady=5)

def show_details():
    top = tk.Toplevel()
    top.title('Photo Details')
    top.geometry('240x120')
    
    info = Label(top, text='Taken on November 21, 2026', font=('Arial', 12, 'bold'))
    info.pack(pady=10)
    
    place = Label(top, text='Location: Lagos, Nigeria', font=('Arial', 10))
    place.pack()
    
    top.mainloop()

details_btn = tk.Button(window, text='See Details', bg='green', fg='white', command=show_details)
details_btn.pack(pady=5)

window.mainloop()
