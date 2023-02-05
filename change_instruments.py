import copy

import mido
from mido import Message, MidiFile, MidiTrack
from times import change_rythm_music
from notes import change_note_music
from texts import name_musique
from dict_instruments import dict_instruments, dict_families


def get_infos(code_musignon):
    """
    Get infos to change on music thanks to the code from the game
    The code is a string containing up to 6 letter+integer like A1B2C3D4E5F6
    """
    code_musignon = code_musignon.upper()
    dict_infos = {}

    dict_infos["instru1"] = 5
    dict_infos["instru2"] = 29
    dict_infos["instru3"] = 41
    dict_infos["instru4"] = 66
    dict_infos["instru5"] = 86
    dict_infos["instru6"] = 115
    dict_infos["change_rythm"] = 1
    dict_infos["change_notes"] = 0

    for i in range(0, 6):
        dict_infos["name_instru{}".format(i+1)] = ""
        dict_infos["name_family{}".format(i+1)] = ""

    for i in range(0, 6):
        try:
            # get the 2 characters of each musignon
            code = code_musignon[2 * i:2 * i + 2]
            # Get the instrument, special cases for Y and Z
            if code == "Y8":
                dict_infos["change_rythm"] = 0.7
                dict_infos["name_instru{}".format(i + 1)] = "ChampDeForce"
                dict_infos["name_family{}".format(i + 1)] = "Y8"
            elif code == "Y9":
                dict_infos["change_rythm"] = 1.3
                dict_infos["name_instru{}".format(i + 1)] = "ChampDeForce"
                dict_infos["name_family{}".format(i + 1)] = "Y9"
            elif code == "Z8":
                dict_infos["change_notes"] = -4
                dict_infos["name_instru{}".format(i + 1)] = "ChampDeForce"
                dict_infos["name_family{}".format(i + 1)] = "Z8"
            elif code == "Z9":
                dict_infos["change_notes"] = 4
                dict_infos["name_instru{}".format(i + 1)] = "ChampDeForce"
                dict_infos["name_family{}".format(i + 1)] = "Z9"
            elif code == "Y0":
                dict_infos["name_instru{}".format(i + 1)] = "ChampDeForce"
                dict_infos["name_family{}".format(i + 1)] = "Y0"
            else:
                dict_infos["instru{}".format(i+1)] = dict_instruments[code[1]]["midi_number"]
                dict_infos["name_instru{}".format(i+1)] = dict_instruments[code[1]]["name"]
                dict_infos["name_family{}".format(i+1)] = dict_families[code[0]]["name"]
        except Exception:
            pass

    return dict_infos


def change_instruments(name_music_input, dict_infos):

    original = MidiFile("music_input/{}.mid".format(name_music_input),
                        clip=True)
    for track in original.tracks:
        for message in track:
            try:
                if message.program == 0:
                    pass
                elif message.program < 27:
                    if "program" in dir(message):
                        message.program = dict_infos["instru1"]
                    if "control" in dir(message):
                        message.control = dict_infos["instru1"]
                elif message.program < 41:
                    if "program" in dir(message):
                        message.program = dict_infos["instru2"]
                    if "control" in dir(message):
                        message.control = dict_infos["instru2"]
                elif message.program < 65:
                    if "program" in dir(message):
                        message.program = dict_infos["instru3"]
                    if "control" in dir(message):
                        message.control = dict_infos["instru3"]
                elif message.program < 73:
                    if "program" in dir(message):
                        message.program = dict_infos["instru4"]
                    if "control" in dir(message):
                        message.control = dict_infos["instru4"]
                elif message.program < 89:
                    if "program" in dir(message):
                        message.program = dict_infos["instru5"]
                    if "control" in dir(message):
                        message.control = dict_infos["instru5"]
                else:
                    if "program" in dir(message):
                        message.program = dict_infos["instru6"]
                    if "control" in dir(message):
                        message.control = dict_infos["instru6"]
            except Exception:
                pass

    new = change_rythm_music(original, dict_infos["change_rythm"])
    new = change_note_music(new, dict_infos["change_notes"])
    new_path = "{}".format(name_musique)
    new.save(new_path)
    return new_path
