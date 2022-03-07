from __future__ import unicode_literals
import pytube
import youtube_dl
import tkinter as tk
from tkinter import Entry
from tkinter import *


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("400x400")
root.title("Youtube Video İndirici")

e = Entry(root, width=50)
e.pack()
e.focus_set()


def mp4():
    link = e.get()
    yt = pytube.YouTube(link)

    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download(filename='video')
    print("Download completed!!")
    var.set("Video indi!")


def mp3():
    # instead of using yt, we'd use ydl
    link = e.get()
    of = {
        'format': 'bestaudio/best',
        'postprocessors': [{

            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(of) as ydl:
        ydl.download([link])
    var.set("Ses indi!")


# buttons for mp4 and mp3
button = tk.Button(frame, text="mp4", command=mp4)
button.pack(side=tk.LEFT)
button2 = tk.Button(frame, text="mp3", command=mp3)
button2.pack(side=tk.LEFT)

# label for the link
var = tk.StringVar()
label = tk.Label(root, textvariable=var, relief=tk.RAISED)
var.set("Linki gir, mp4 mu mp3 mu sec insin.")


label.pack()
root.mainloop()
