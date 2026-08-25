from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title("my photo album")
window.geometry("400x400")


title = Label(window, text="my photo album", fg="white", bg="purple", width=40)
title.pack(pady = 10)
img_file = Image.open("image.jpg")
img_file = img_file.resize((300, 300))   #resize means to change the size of the image
img = ImageTk.PhotoImage(img_file)
pic = Label(window, image=img)
pic.pack(pady = 10)

def show_message():
    top = Toplevel()    #toplevel means to create a new window
    top.title("photo details")
    top.geometry("300x200")     #geometry means to set the size of the window
    info = Label(top, text="taken on: 21 june")
    info.pack()
    top.mainloop()     #mainloop means to keep the window open until the user closes it
    details_btn = Button(window, text="see details" , bg="indigo" , fg="black" , command=show_message) #command means to call the function when the button is clicked
    details_btn.pack(pady=5)


window.mainloop()
    
