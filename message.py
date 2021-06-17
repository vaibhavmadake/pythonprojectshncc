from tkinter import*

class MyMessage:
    def __init__(self,root):
        self.f = Frame(root,height=300,width=500)
        self.f.propagate(0)
        self.f.pack()

        self.m = Message(self.f,text="This is a message that has more than one line,also known as multiline",width=200,font=("Roman",20,"bold italic"), fg = "red")
        self.m.pack(side =LEFT)

root = Tk()

obj = MyMessage(root)
root.mainloop()
