from tkinter import*


def buttonClick():
    print("Submit Button Click")

root = Tk()

root.title("My Frame")

f = Frame(root, height = 400, width = 500,bg="gray",cursor="cross")

f.propagate(0)
btn = Button(f,text="Submit",height=5,width=10,bg="white",fg="red",command = buttonClick)
btn.pack()


f.pack()

root.mainloop()
