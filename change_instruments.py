import copy

import mido
from mido import Message, MidiFile, MidiTrack
from times import change_rythm_music
from texts import name_musique


def change_instruments(name_music_input, instru1, instru2, instru3, change_rythm = 1, change_notes = 0):
    instru1 = int(instru1)
    instru2 = int(instru2)
    instru3 = int(instru3)
    original = MidiFile("music_input/{}.mid".format(name_music_input),
                        clip=True)
    for message in original.tracks[0]:
        try:
            if message.program == 0:
                pass
            elif message.program < 20:
                message.program = instru1
            elif message.program < 40:
                message.program = instru2
            else:
                message.program = instru3
        except Exception:
            pass

    new = change_rythm_music(original, change_rythm)
    new_path = "{}".format(name_musique)
    new.save(new_path)
    return new_path
