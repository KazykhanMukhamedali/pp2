from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os


class MP:
    def __init__(self, win):
        # создаем окно с помощью ткинтера
        win.geometry('600x100')
        win.title('Music Player')
        win.resizable(0, 0)

        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        # настройки баттонов
        load_button = Button(win, text='Load', width=10, font=('Arial', 15), command=self.load)
        load_button.place(x=50, y=40)

        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 15), command=self.play)
        play_button.place(x=150, y=40)

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 15), command=self.pause)
        pause_button.place(x=250, y=40)

        previous_button = Button(win, text='Previous', width=10, font=('Arial', 15), command=self.previous_track)
        previous_button.place(x=350, y=40)

        next_button = Button(win, text='Next', width=10, font=('Arial', 15), command=self.next_track)
        next_button.place(x=450, y=40)

        self.music_files = []
        self.current_track_index = 0
        self.playing_state = False

    def load(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.music_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.mp3')]
            print("Loaded: ", self.music_files)
            self.play_restart.set('Play')

    def play(self):
        if self.music_files:
            mixer.init()
            mixer.music.load(str(self.music_files[self.current_track_index]))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        mixer.music.stop()

    def previous_track(self):
        if self.music_files:
            self.current_track_index = (self.current_track_index - 1) % len(self.music_files)
            self.play()

    def next_track(self):
        if self.music_files:
            self.current_track_index = (self.current_track_index + 1) % len(self.music_files)
            self.play()


root = Tk()
MP(root)
root.mainloop()