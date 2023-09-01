import re
import json

MORSE_CODE = json.load(
    open("Morse code/morse_code.json")
)  # read the morse_code json file


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    # return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

    list_morse = re.split(
        r"\s{2,}", morse_code.strip()
    )  # ['.... . -.--', '.--- ..- -.. .']
    list_morse_splt = map(
        lambda x: x.split(), list_morse
    )  # [['....', '.', '-.--'], ['.---', '..-', '-..', '.']]
    list_morse_msg = map(
        lambda item: "".join(map(lambda x: MORSE_CODE[x], item)), list_morse_splt
    )  # back to normal message like: ['HEY', 'JUDE']
    msg = " ".join(list_morse_msg)  # join messages
    return msg
