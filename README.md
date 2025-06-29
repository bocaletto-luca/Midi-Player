# MIDI Player

**Author:** Bocaletto Luca

**Language:** Python

## Description

**MIDI Player** is a desktop application that allows users to load and play MIDI files. The application provides an intuitive user interface to select a MIDI file, control playback, manage MIDI devices, and monitor the current playback time.

![Screenshot 2023-10-18 144139](https://github.com/elektronoide/Midi-Player/assets/134635227/f650f32d-52ad-47bc-84d6-ff03c28d2bbf)

![Screenshot 2023-10-18 144121](https://github.com/elektronoide/Midi-Player/assets/134635227/5f4a934e-027e-464a-be3d-9265a79efe20)

## Key Features

- **MIDI File Playback**: Users can open and play MIDI files by selecting the desired file using the "Open MIDI File" button.

- **Playback Control**: The application offers a "Play" button to start playback or pause it if the MIDI file is already playing. The "Stop" button allows users to stop playback and reset the playback position.

- **MIDI Device Selection**: Users can select the destination MIDI device through a combo box labeled "Select Device." This allows routing MIDI output to the desired device.

- **MIDI File Display**: The application displays the name of the currently selected MIDI file in the "File" label and the current playback time at the bottom of the window.

- **MIDI Note Display**: During playback, the application displays the current MIDI notes in the center of the window.

- **MIDI Volume Control**: Users can adjust the MIDI volume using a horizontal scrollbar, enabling them to vary the sound intensity during playback.

- **Error Handling**: The application is capable of handling errors during playback and displays any error messages at the bottom of the window.

## Usage

1. Launch the "MIDI Player" application.
2. Select a destination MIDI device from the "Select Device" dropdown list.
3. Load a MIDI file using the "Open MIDI File" button.
4. Use the "Play" button to start or pause playback.
5. Use the "Stop" button to halt playback.
6. Adjust the volume using the scrollbar.
7. During playback, the current MIDI notes are displayed in the window.

## Notes

- The application utilizes the Tkinter and Mido libraries for the user interface and MIDI file management.
- You can select a destination MIDI device for output.
- The application provides volume control to adjust sound intensity during playback.
- Any errors during playback are managed and displayed in the application window.

**MIDI Player** is a valuable tool for those who want to play MIDI files and have flexible playback control while offering a range of options for managing MIDI devices and volume control.

---

**Maintainer Update**

All legacy projects from the old `@Elektronoide` GitHub account are now officially maintained by **@bocaletto-luca**. Please direct any issues, pull requests, and stars to **@bocaletto-luca** for all future updates.

---
