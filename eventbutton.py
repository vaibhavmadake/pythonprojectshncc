from tkinter import*

class MyButtons:
    def __init__(self,root):
        self.f = Frame(root,height=300,width=500)
        self.f.propagate(0)
        self.f.pack()

        self.b1= Button(self.f,text="Click Me",width=15,height=2,command=self.buttonClick)
        
        self.b2= Button(self.f,text="Close",width=15,height=2,command=quit)

        self.b1.grid(row=0,column=1)
        self.b2.grid(row=0,column=2)

    def buttonClick(self):
        self.fnt = ('Courier',-30,'bold italic underline')
        self.lbl = Label(self.f,text="Welcome To Python",width=20,height=2,font=self.fnt,fg='blue')

        self.lbl.grid(row=2,column=0)


root = Tk()

obj = MyButtons(root)
root.mainloop()
