import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from mutagen.mp3 import MP3

import pygame
import time 
import os
import pygame.mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x400")  # Increased height for better layout

        self.music_files = []
        self.current_index = 0
        self.paused = False
        self.volume = 0.5

        self.create_widgets()
        pygame.mixer.init()  # Initialize the pygame mixer

    def create_widgets(self):
        # Song selection frame
        self.song_selection_frame = tk.Frame(self.root, bg="lightgray")
        self.song_selection_frame.pack(fill=tk.X, pady=10)

        self.select_button = tk.Button(self.song_selection_frame, text="Select Music", command=self.select_music)
        self.select_button.pack(side=tk.LEFT, padx=10)

        self.music_listbox = tk.Listbox(self.song_selection_frame, width=60, height=10, bg="lightgray")
        self.music_listbox.pack(side=tk.LEFT, fill=tk.X, padx=10)
        self.music_listbox.bind("<<ListboxSelect>>", self.play_selected_song)

        # Control buttons frame
        self.control_frame = tk.Frame(self.root, bg="lightgray")
        self.control_frame.pack(pady=10)

        self.prev_button = tk.Button(self.control_frame, text="Prev", command=self.play_prev, state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play_pause_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.control_frame, text="Next", command=self.play_next, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=10)

        # Song information and progress bar
        self.song_label = tk.Label(self.root, text="Currently playing: None", wraplength=400)
        self.song_label.pack(pady=5)

        self.time_label = tk.Label(self.root, text="00:00", width=5)
        self.time_label.pack(side=tk.LEFT, padx=10)

        self.progress_bar = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.pack(pady=5)

        self.current_time_label = tk.Label(self.root, text="00:00", width=5)
        self.current_time_label.pack(side=tk.RIGHT, padx=10)

        # Volume control
        self.volume_label = tk.Label(self.root, text="Volume:", bg="lightgray")
        self.volume_label.pack(pady=5)

        self.volume_scale = ttk.Scale(self.root, from_=0, to=1, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=5)

    def play_pause_music(self):
        if self.music_files:
            if pygame.mixer.music.get_busy() and not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
                self.play_button.config(text="Play")
            else:
                if self.paused:
                    pygame.mixer.music.unpause()
                    self.paused = False
                else:
                    pygame.mixer.music.load(self.music_files[self.current_index])
                    pygame.mixer.music.play()
                    self.update_song_label()
                    self.update_progress_bar()
                self.play_button.config(text="Pause")
    def stop_music(self):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                self.paused = False
                self.play_button.config(text="Play")
                self.update_song_label()

    def play_prev(self):
            if self.music_files:
                self.current_index = (self.current_index - 1) % len(self.music_files)
                pygame.mixer.music.load(self.music_files[self.current_index])
                pygame.mixer.music.play()
                self.update_song_label()

    def play_next(self):
            if self.music_files:
                self.current_index = (self.current_index + 1) % len(self.music_files)
                pygame.mixer.music.load(self.music_files[self.current_index])
                pygame.mixer.music.play()
                self.update_song_label()

    def select_music(self):
            music_files = filedialog.askopenfilenames(title="Select Music", filetypes=[("MP3 Files", "*.mp3")])
            if music_files:
                self.music_files = music_files
                self.music_listbox.delete(0, tk.END)
                for music_file in music_files:
                    self.music_listbox.insert(tk.END, music_file)
                self.play_button.config(state=tk.NORMAL)
                self.prev_button.config(state=tk.NORMAL)
                self.next_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.NORMAL)

    def play_selected_song(self, event):
            selected_index = self.music_listbox.curselection()[0]
            self.current_index = selected_index
            pygame.mixer.music.load(self.music_files[self.current_index])
            pygame.mixer.music.play()
            self.update_song_label()
            self.update_progress_bar()

    def update_song_label(self):
            music= (self.music_files[self.current_index]).split("/")[-1]
            if self.music_files:
                self.song_label.config(text=f"Currently playing: {music}")

    def update_progress_bar(self):
        if self.music_files:
            song_mute = MP3(str(self.music_files[self.current_index]))
            song_length = song_mute.info.length
            
            current_time = pygame.mixer.music.get_pos()
            self.progress_bar['value'] = (current_time // 1000) / song_length * 100

            # Update time labels
            self.time_label.config(text=f"{time.strftime('%M:%S', time.gmtime(round(song_length)))}")
            self.current_time_label.config(text=f"{time.strftime('%M:%S',  time.gmtime(current_time // 1000))}")
            if int(round(song_length)) != current_time // 1000:
                self.root.after(1000, self.update_progress_bar)


    def set_volume(self, volume):
        self.volume = float(volume)
        pygame.mixer.music.set_volume(self.volume)

# Start the main loop
root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()
