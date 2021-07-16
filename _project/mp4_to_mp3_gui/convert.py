import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from moviepy.editor import *

screen = tk.Tk()
 
style = ttk.Style(screen)
style.theme_use("clam")
 
 
def convert():
    rep = filedialog.askopenfilenames(
    	initialdir='/',
    	filetypes=[
    		("MP4", "*.mp4")])
    print(rep)
    mp4_file = rep[0]
    filename = mp4_file.split("/")
    mp3_file = f'./{filename[2]}.mp3'
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
 
ttk.Button(screen, text="Open files", command=convert).grid(row=1, column=0, padx=4, pady=4, sticky='ew')

screen.mainloop()
