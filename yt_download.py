from __future__ import unicode_literals
import youtube_dl
from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("Youtube Downloader")
root.geometry('900x500')
user_input = tk.StringVar(root)

def download():
	ydl_opts = {
		'format' : 'beastaudio/best',
		'postprocessors':
		[{
			'key' : 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([user_input.get()])


l1=Label(root,
	 text='Copy the "URL" from youtube and past it down here',
	 fg = 'black',
	 font = 'Times')

l1.config(anchor=CENTER)
l1.pack()

t1= tk.Entry(root,textvariable = user_input)
t1.pack(ipadx = 100,ipady = 10)

b1 = Button(root, text = "Download",command= download)
b1.pack(ipadx = 30, ipady = 10)


root.mainloop()