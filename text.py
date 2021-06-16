from tkinter import*

root = Tk()

fnt = ('Verdana',14,'bold')

t = Text(root, width = 30, height = 10, font = fnt, fg = 'blue', bg = 'white')

t.insert (INSERT, 'Widget Example \n')
t.insert (END, 'Text widget \nThis is an example\n First line\n Second line \n Last Line')

t.tag_add('start','1.0','1.14')
t.tag_config('start',background = 'red', foreground = 'white', font = ('Time',20,'bold italic'))

t.tag_add('next','2.0','2.11')
t.tag_config('next',background = 'purple', foreground = 'white', font = ('Courier',20,'bold italic'))

t.pack (side = LEFT)

root.geometry('300x400+250+250')

root.mainloop()
