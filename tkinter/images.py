from tkinter import*
from PIL import ImageTk,Image

root = Tk()

myImage = ImageTk.PhotoImage(Image.open("cat.jpg"))
myLabel = Label(image=myImage)
myLabel.pack()







root.mainloop()
