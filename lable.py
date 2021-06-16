from tkinter import*

root = Tk()

fnt = ('Courier',-30,'bold underline')

lbl = Label (root,text="Assignment In Progress....",fg="blue",bg="white",font=fnt)
lbl.pack(side=LEFT)

root.geometry("600x500")

root.mainloop()
