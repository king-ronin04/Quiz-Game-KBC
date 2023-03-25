from tkinter import *

root = Tk()
root.geometry('1270x652+0+0')
root.title('One Piece')
root.config(bg='black')

leftframe=Frame(root)
leftframe.grid(row=0,column=0)

topframe=Frame(leftframe)
topframe.grid(row=0,column=0)

centerframe=Frame(leftframe)
centerframe.grid(row=1,column=0)

bottomframe=Frame(leftframe)
bottomframe.grid(row=2,column=0)

rightframe=Frame(root)
rightframe.grid(row=0,column=1)

root.mainloop()
