import json
from re import split
from math import ceil


# That said, your task is to implement two functions:

# Function decodeBits(bits):
# - find out the transmission rate of the message
# - decode the message to dots ., dashes - and spaces (one between characters, three between words)
# - return those as a string.
# Note: some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them.
# Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.

# 2. Function decodeMorse(morseCode):
# - would take the output of the previous function and return a human-readable string.

# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

# The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).
# Eg:
#  morseCodes(".--") // to access the morse translation of ".--"

# All the test strings would be valid to the point that they could be reliably decoded as described above,
# so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

MORSE_CODE = json.load(
    open("Morse code/morse_code.json")
)  # read the morse_code json file


def rate(bits):
    n1 = bits.index("0") if "0" in bits else len(bits)
    n0 = (
        len(
            bits[bits.index("0") : bits.index("0") + bits[bits.index("0") :].index("1")]
        )
        if "0" in bits
        else 0
    )

    if n1 % 2 == 0:
        rate = 2
    elif n0 == n1:
        rate = n1
    elif n0 == 1:
        rate = 1
    # elif n1 in (1, 3):
    #     rate = 3
    else:
        rate = n1

    return rate


def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    # bits = bits[bits.index('1'):len(bits)-bits[::-1].index('1')] # remove the zeros from the beginning and the end of bits
    bits = bits.strip("0")  # remove the zeros from the beginning and the end of bits
    rate_val = rate(bits)
    rate_val = 6

    morse_msg = ""
    binary_to_morse = {
        "1": ".",
        "111": "-",
        "0": "",
        "000": " ",
        "0000000": "   ",
    }

    bits_list = list()
    bit1, bit0 = "", ""

    for bit in bits:
        if bit == "1":
            bit1 += "1"
            if bit0:
                bits_list.append(bit0)
                bit0 = ""
        else:
            bit0 += "0"
            if bit1:
                bits_list.append(bit1)
                bit1 = ""

    # adding last set of bits
    if bit1:
        bits_list.append(bit1)
    if bit0:
        bits_list.append(bit0)

    for bit in bits_list:
        temp = bit[0] * (len(bit) // rate_val)

        # if len(temp) % 7 == 0:
        #     temp = bit[0] * 7
        # if len(temp) % 3 == 0:
        #     temp = bit[0] * 3
        morse_msg += binary_to_morse[temp]

    return morse_msg
    # return (
    #     bits.replace("111", "-").replace("000", " ").replace("1", ".").replace("0", "").replace("0000000", "   ")
    # )


def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    list_morse = split(
        r"\s{2,}", morseCode.strip()
    )  # ['.... . -.--', '.--- ..- -.. .']
    list_morse_splt = map(
        lambda x: x.split(), list_morse
    )  # [['....', '.', '-.--'], ['.---', '..-', '-..', '.']]
    list_morse_msg = map(
        lambda item: "".join(map(lambda x: MORSE_CODE[x], item)), list_morse_splt
    )  # back to normal message like: ['HEY', 'JUDE']
    msg = " ".join(list_morse_msg)  # join messages
    return msg


# 111 => E
# 1110111 => M
# 111000111 => I
# 1111111 => E
# 111110000011111 => I
# decoded_bits = decode_bits(bits)
# Example from description:
bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
bits = "111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111"
bits = "1110001010101000100000001110111010111000101011100010100011101011101000111010111000000011101010100010111010001110111011100010111011100011101000000010101110100011101110111000111010101110000000101110111011100010101110001110111000101110111010001010100000001110111011100010101011100010001011101000000011100010101010001000000010111010100010111000111011101010001110101110111000000011101010001110111011100011101110100010111010111010111"
msg = "HEY JUDE"


# TODO: check how to check for the len of every element

decoded_bits = decode_bits(bits)
decoded_msg = decode_morse(decoded_bits)
print(decoded_msg)