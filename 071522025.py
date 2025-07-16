import os 
from midiutil import MIDIFile


note_to_midi = {
    'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65, 'F#': 66,
    'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71
}

midi = MIDIFile(1)  # Create a single-track MIDI file
midi.addTempo(0, 0, 157)

chords = [
    ['D', 'F#', 'A'],
    ['D', 'F#', 'A', 'C#'],
    ['C#', 'E', 'G#'],
    ['D', 'F#', 'A', 'C#']
]

start_time = 0
duration = 4

for chord in chords:
    for note in chord:
        midi.addNote(0, 0, note_to_midi[note], start_time, duration, 100)
    start_time += duration

with open("hello_world.mid", "wb") as output_file:
    midi.writeFile(output_file)

