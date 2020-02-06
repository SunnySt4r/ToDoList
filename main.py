from tkinter import *


def pasteData():
    x = string.get()
    string.set('')
    global countTasks
    countTasks += 1
    vars()['button_' + str(countTasks)] = Button(pole, text="@@@", bg='red', width=5)
    vars()['button_' + str(countTasks)].grid(row=countTasks, column=0)
    vars()['button_' + str(countTasks)].bind('<Button-1>', change)

    vars()['frame_' + str(countTasks)] = Frame()
    vars()['label_' + str(countTasks)] = Label(pole, text=x)
    vars()['label_' + str(countTasks)].grid(row=countTasks, column=1, sticky=W)


def change(event):
    w = event.widget
    if w['text'] == "@@@":
        w.config(text="???", bg='yellow')
    elif w['text'] == "???":
        w.config(text="###", bg='lime')
    else:
        w.config(text="@@@", bg='red')


win = Tk()
win.title("To Do List")

win.geometry("500x500")

# Menu
menuBar = Menu(win)
win.config(menu=menuBar)

fMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fMenu)
fMenu.add_command(label='New File', accelerator='Ctrl + N')
fMenu.add_command(label='Open', accelerator='Ctrl + O')
fMenu.add_command(label='Save', accelerator='Ctrl + S')
fMenu.add_command(label='Save As')
fMenu.add_separator()
fMenu.add_command(label='Copy', accelerator='Ctrl + C')
fMenu.add_command(label='Paste', accelerator='Ctrl + V')

# main frames
countTasks = 0
entryFrame = Frame(win, width=450, height=32)
entryFrame.place(x=0, y=0)
printButtonFrame = Frame(win, width=50, height=32)
printButtonFrame.place(x=450, y=0)
pole = Frame(win, width=500)
pole.place(x=0, y=32)


# frame entryFrame
entryFrame.columnconfigure(0, weight=10)
entryFrame.grid_propagate(False)
string = StringVar()
entry = Entry(entryFrame, textvariable=string)
entry.grid(sticky="we", pady=6)

# frame printButtonFrame
printButtonFrame.columnconfigure(0, weight=10)
printButtonFrame.grid_propagate(False)
entry = Button(printButtonFrame, text="Paste", command=pasteData)
entry.grid(sticky="we", pady=3)


win.mainloop()
