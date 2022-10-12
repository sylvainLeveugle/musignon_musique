import mido
from mido import Message, MidiFile, MidiTrack


def change_rythm_music(midi_file, multiplicator):
    """
    From a midi file, multiply all times by a number to get it slower/faster
    """
    for track in midi_file.tracks:
        for message in track:
            try:
                message.time = int(message.time * multiplicator)
            except Exception:
                pass
    return midi_file
