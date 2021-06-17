from tkinter import*

root = Tk()

def myClick():
    myLabel = Label(root, text = "You Clicked ME!!")
    myLabel.pack()


myButton = Button(root, text = "Click Me!", command = myClick, fg="blue", bg= "black")
myButton.pack()



root.mainloop()
