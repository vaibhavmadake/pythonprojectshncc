from tkinter import*
root = Tk()

c = Canvas (root,height=700,width=1200,bg="white")

id = c.create_arc (100,100,400,300,width=3,start=270,extent=180,outline="red",style="arc")

id = c.create_arc (500,100,800,300,width=3,start=90,extent=180,outline="red",style="arc")

id = c.create_arc (100,400,400,600,width=3,start=0,extent=180,outline="red",style="arc")

id = c.create_arc (500,400,800,600,width=3,start=270,extent=180,outline="red",style="arc")

id = c.create_arc (700,100,1200,600,width=3,start=90,extent=90,outline="red",style="arc")

c.pack()

root.mainloop()
