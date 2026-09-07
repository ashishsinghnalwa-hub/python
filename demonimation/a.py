from tkinter import *
from tkinter import messagebox

# ---------------- Main Window ----------------

root = Tk()

root.title('Denomination Counter')

root.configure(bg='light blue')

root.geometry('650x400')

label1 = Label(root,text="Hey User! Welcome to Denomination Counter Application.",bg='light blue')

label1.place(relx=0.5, y=340, anchor=CENTER)

# ---------------- Message Function ----------------

def msg():

    MsgBox = messagebox.showinfo("Alert","Do you want to calculate the denomination count?")

    if MsgBox == 'ok':

        topwin()

# Button

button1 = Button(root,text="Let's get started!",command=msg,bg='brown',fg='white')

button1.place(x=260, y=360)

# ---------------- Top Window ----------------

def topwin():
    top = Toplevel(root)
    top.title('Denomination Counter')
    top.geometry('650x400')
    top.configure(bg='light blue')     #configure means to set the background color of the window

    label = Label(top,text="Enter the amount to calculate the denomination count.",bg='light blue')
    entry = Entry(top)


    lbl = Label(top,text="here is the denomination count",bg='light blue')

    l1 = Label(top,text="2000 : ",bg='light blue')
    l2 = Label(top,text="500 : ",bg='light blue')
    l3 = Label(top,text="100 : ",bg="light blue")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:                      #try means to try the code and if there is an error it will go to except block
            amount = int(entry.get())
            note2000 = amount // 2000 #// means to divide the amount by 2000 and get the quotient
            amount = amount % 2000 #% means to divide the amount by 2000 and get the remainder
            amount = amount // 500
            note500 = amount % 500
            note100 = amount // 100 
            note100 = amount % 100

            t1.delete(0, END) #delete means to delete the previous value in the entry box
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(note2000)) #insert means to insert the value in the entry box
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))
        except ValueError: #except means to catch the error and show the messagebox
            messagebox.showerror("Error", "Please enter a valid amount.")


    btn = Button(top,text="Calculate",command=calculate,bg='brown',fg='white')   #command means to call the function when the button is clicked


    label.place(x=150, y=50)
    entry.place(x=200, y=80)
    btn.place(x=250, y=120)
    lbl.place(x=200, y=160)

    l1.place(x=200, y=200)
    l2.place(x=200, y=230)
    l3.place(x=200, y=260) #place means to place the widget in the window at the specified x and y coordinates

    t1.place(x=300, y=200)
    t2.place(x=300, y=230)
    t3.place(x=300, y=250)

root.mainloop() #mainloop means to keep the window open until the user closes it