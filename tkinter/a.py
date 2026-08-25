from tkinter import *

window = Tk()
window.title("my user card")
window.geometry("400x400")
title = Label(window, text="text my profile", fg="white", bg="purple", width=40)
title.grid(row=0, column=0, columnspan=2, padx=5, pady=10)


# -------------------------------------------------------

# PART 3 - Add Name and Hobby Labels and Entry boxes

# -------------------------------------------------------

name_label = Label(window, text='Name:', fg='black', bg='white')

name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg='blue', bg='lightyellow', width=25)

name_entry.grid(row=1, column=1, padx=10, pady=5)

hobby_label = Label(window, text='Hobby:', fg='black', bg='white')

hobby_label.grid(row=2, column=0, padx=10, pady=5)

hobby_entry = Entry(window, fg='blue', bg='lightyellow', width=25)

hobby_entry.grid(row=2, column=1, padx=10, pady=5)

# -------------------------------------------------------

# PART 4 - Add a Frame with an About Me Text box inside

# -------------------------------------------------------

about_frame = Frame(window, relief=RAISED, borderwidth=3)

about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text='About Me:')

about_label.pack()

window.mainloop()