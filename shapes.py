from tkinter import*

root = Tk()

c =  Canvas(root,width=700,height=900,bg="blue",cursor="pencil")
c.pack ()

id = c.create_line (50,50,200,50,200,150,50,150,50,50,width=3,fill="white")

id = c.create_oval(50,200,250,300,width=5,fill="yellow",outline="red",activefill="green")

id = c.create_polygon(50,310,200,500,300,500,width=3,fill="green",outline="pink",smooth="1",activefill="orange")

id = c.create_rectangle(50,550,300,650,width=2,fill="gray",outline="black",activefill="AliceBlue")

fnt= ('Times',40,'bold italic underline')
id = c.create_text(500,100,text="Assingment",font=fnt,fill="yellow",activefill="green")
