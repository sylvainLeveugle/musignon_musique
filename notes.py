import mido
from mido import Message, MidiFile, MidiTrack


def change_note_music(midi_file, addition):
    """
    From a midi file, add addition to all notes, with min and max
    """
    for track in midi_file.tracks:
        for message in track:
            try:
                message.note = max(min(message.note + addition, 127), 0)
            except Exception:
                pass
    return midi_file
