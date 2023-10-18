# Name: Player Midi
# Author: Bocaletto Luca
# Web Site: https://www.elektronoide.it
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import mido
import threading
import time

class MidiPlayer:
    def __init__(self, app):
        self.app = app
        self.playing = False
        self.paused = False
        self.port = None
        self.file_path = None
        self.available_ports = mido.get_output_names()
        self.current_time = tk.StringVar(value="0:00")  # Variable for current time
        self.note_display = tk.Label(app.root, text="")  # Label for note display
        self.volume = 64  # Added volume control with a default value

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MIDI Files", "*.mid")])
        if file_path:
            self.file_path = file_path
            self.app.update_file_label()  # Update the selected file name

    def select_port(self, selected_port):
        if self.playing:
            return
        if selected_port:
            self.port = mido.open_output(selected_port)

    def play(self):
        if self.playing:
            self.paused = not self.paused
            self.app.update_play_button_text()
        else:
            try:
                if not self.port:
                    self.port = mido.open_output()
                if not self.file_path:
                    return
                self.playing = True
                self.app.update_play_button_text()
                self.play_thread = threading.Thread(target=self.play_midi)
                self.play_thread.start()
            except OSError as e:
                self.stop()
                self.app.update_status(f"Error during MIDI playback: {str(e)}")

    def play_midi(self):
        try:
            with mido.MidiFile(self.file_path) as midi_file:
                start_time = time.time()
                for msg in midi_file.play():
                    if not self.playing:
                        break
                    while self.paused:
                        time.sleep(0.1)
                    if msg.type == "control_change":
                        msg_with_volume = msg.copy()
                        msg_with_volume.control = 7  # MIDI volume control number
                        msg_with_volume.value = self.volume  # Set the volume value
                        self.port.send(msg_with_volume)
                    else:
                        self.port.send(msg)
                    current_time = time.time() - start_time
                    self.current_time.set(self.format_time(current_time))
                    if msg.type == "note_on":
                        self.note_display.config(text=f"Note: {msg.note}")
                    time.sleep(msg.time)
        except OSError as e:
            self.stop()
            self.app.update_status(f"Error during MIDI playback: {str(e)}")

    def stop(self):
        self.playing = False
        if self.port:
            self.port.reset()
        self.port = None
        self.app.update_play_button_text()

        # Reset note and time values
        self.current_time.set("0:00")
        self.note_display.config(text="")

    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes}:{seconds:02}"

class MidiPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MIDI Player")
        self.player = MidiPlayer(self)

        self.play_button = tk.Button(root, text="Play", command=self.player.play)
        self.stop_button = tk.Button(root, text="Stop", command=self.player.stop)
        self.open_button = tk.Button(root, text="Open MIDI File", command=self.player.open_file)

        self.port_label = tk.Label(root, text="Select Device")
        self.port_combobox = ttk.Combobox(root, values=self.player.available_ports, state="readonly")
        self.port_combobox.bind("<<ComboboxSelected>>", self.select_port)

        # Add a label for the selected file name
        self.file_label = tk.Label(root, text="File: None")

        # Add a label for displaying the current time
        self.time_label = tk.Label(root, textvariable=self.player.current_time)

        self.status_label = tk.Label(root, text="")

        # Add volume control
        self.volume_label = tk.Label(root, text="Volume")
        self.volume_scale = ttk.Scale(root, from_=0, to=127, variable=self.player.volume, orient="horizontal")

        self.play_button.pack()
        self.stop_button.pack()
        self.open_button.pack()
        self.port_label.pack()
        self.port_combobox.pack()
        self.file_label.pack()
        self.time_label.pack()
        self.player.note_display.pack()
        self.status_label.pack()

        # Display the volume control
        self.volume_label.pack()
        self.volume_scale.pack()

    def select_port(self, event):
        selected_port = self.port_combobox.get()
        self.player.select_port(selected_port)

    def update_play_button_text(self):
        if self.player.playing:
            self.play_button.config(text="Pause" if not self.player.paused else "Resume")
        else:
            self.play_button.config(text="Play")

    def update_file_label(self):
        if self.player.file_path:
            file_name = self.player.file_path.split("/")[-1]
            self.file_label.config(text="File: " + file_name)
        else:
            self.file_label.config(text="File: None")

    def update_status(self, text):
        self.status_label.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MidiPlayerApp(root)
    root.mainloop()
