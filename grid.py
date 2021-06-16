from tkinter import*

root = Tk()

b1 = Button (text="Submit",fg="red")
b1.grid(row=0,column=0,padx=10,pady=15)
b2 = Button (text="Cancle",fg="blue")
b2.grid(row=0,column=1,padx=10,pady=15)
b3 = Button (text="Update",fg="black")
b3.grid(row=1,column=0,padx=10,pady=15)
b4 = Button (text="Delete",fg="green")
b4.grid(row=1,column=1,padx=10,pady=15)
