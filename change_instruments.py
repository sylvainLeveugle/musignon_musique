import copy

import mido
from mido import Message, MidiFile, MidiTrack
from times import change_rythm_music
from notes import change_note_music
from texts import name_musique


def change_instruments(name_music_input, instru1, instru2, instru3, change_rythm=0, change_notes=0):
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
    new = change_note_music(new, change_notes)
    new_path = "{}".format(name_musique)
    new.save(new_path)
    return new_path


def change_instruments_control(name_music_input, instru1, instru2, instru3, change_rythm=0, change_notes=0):
    instru1 = int(instru1)
    instru2 = int(instru2)
    instru3 = int(instru3)
    original = MidiFile("music_input/{}.mid".format(name_music_input),
                        clip=True)
    for message in original.tracks[0]:
        try:
            if message.control == 0:
                pass
            elif message.control < 20:
                message.control = instru1
            elif message.control < 40:
                message.control = instru2
            else:
                message.control = instru3
        except Exception:
            pass

    new = change_rythm_music(original, change_rythm)
    new = change_note_music(new, change_notes)
    new_path = "{}".format(name_musique)
    new.save(new_path)
    return new_path
