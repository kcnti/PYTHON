from tkinter import *
from tkinter import filedialog
from moviepy import *
import tkinter.messagebox as msg

screen = Tk()
screen.geometry('500x500')
screen.title('Converter')

def browseFile():
    filename = filedialog.askopenfile(initialdir = ".",
                                        title = "Select a File",
                                        filetypes = [("MP4", "*.mp4")]) 
    label_file_explorer.configure(text=f'File Opened: {filename[0]}')


label_file_explorer = Label(screen, text="File", width=100,
                            height=4, fg="blue")
button_explore = Button(screen, text="Browse", command=browseFile)
button_exit = Button(screen, text="Exit", command=exit)

label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_exit.grid(column=1, row=3)

screen.mainloop()
