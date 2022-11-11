import tkinter
from tkinter import *
import pytube

def load():
    video_link = Entry.clipboard_get(enter_link)
    yt = pytube.YouTube(video_link)
    streams = yt.streams
    video_best = streams.order_by('resolution').desc().first()
    audio_best = streams.filter(only_audio=True).desc().first()
    print(audio_best)
    path = Entry.clipboard_get(enter_save)
    video_best.download(path)
    audio_best.download(path)

def start():
    global enter_link
    global enter_save
    
    window = Tk()
    window.title('загрузка')
    window.geometry('400x240')
    window.columnconfigure(index=0, weight=50)
    window.columnconfigure(index=1, weight=250)
    link = Label(window, text='Введите ссылку для скачивания')
    link.grid(row=0, column=0, sticky = 'e')
    save = Label(window, text='Введите путь для сохранения')
    save.grid(row=1, column=0, sticky = 'e')  
    enter_link = Entry(window) 
    enter_link.grid(row=0, column=1, sticky = 'w')
    enter_save = Entry(window)  
    enter_save.grid(row=1, column=1, sticky = 'w')

    btn = Button(window, text='скачать',command = load)
    btn.grid(row=4, columnspan=2)
    window.mainloop()

