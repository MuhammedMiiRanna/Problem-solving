

import json
from re import split, findall

# https://github.com/MuhammedMiiRanna/Problem-solving/tree/main/CodeWars/Morse%20code

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
    # Cheking for the min length of seq of each char ("1", "0")
    ones = len(min(filter(lambda x: bool(x), bits.split("0"))))
    zeroes = len(min(filter(lambda x: bool(x), bits.split("1")))) if "0" in bits else 99
    
    return min(ones, zeroes)
    # bunch of test, made them after analysing
    # the values and outliers for so long
    if zeroes == ones:
        rate = ones
    elif ones % 2 == 0:
        rate = 2
    elif zeroes == 1:
        rate = 1
    else:
        rate = ones

    return rate


def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip("0")  # remove the zeros from the beginning and the end of bits
    rate_val = rate(bits)  # calculating the rate

    # # bits_list # #
    # bits_list = list()  # list that contains the sequences
    # ones, zeroes = "", ""  # var to collect ones and zeroes
    # # Here we will iterate over the string of bits
    # # to seperate between "0" and "1"
    # for bit in bits:
    #     if ones == "1":
    #         ones += "1"  # add "1" to the ones seq
    #         if zeroes:  # if there is zeroes
    #             bits_list.append(zeroes)
    #             zeroes = ""
    #     else:
    #         zeroes += "0"
    #         if ones:
    #             ones.append(ones)
    #             ones = ""

    # # adding last set of bits
    # if ones:
    #     bits_list.append(ones)
    # if zeroes:
    #     bits_list.append(zeroes)
    # # bits_list # #
    # we can do this, inside the "bits_list" comment,

    # or this 2 lines using 'findall' functiong from regex lib (took me a while to finds that xD):
    bits_list = findall(
        r"0+|1+", bits
    )  # separating the sequence into list of ones and zeroes
    # PS: we can merge the rate func with this line, to work with "bits_list", somehow

    # getting the morse message
    morse_msg = ""
    # dict with (binary_code: morse_code) values pair
    binary_to_morse = {
        "1": ".",
        "111": "-",
        "0": "",
        "000": " ",
        "0000000": "   ",
    }
    for bit in bits_list:
        # bit[0]: gives u '1' or '0'
        # (len(bit) // rate_val):  dividing the length of the seq by the rate_value
        # so we're removing the rate effect, by dividing
        # the length of the seq by the rate_value
        morse_msg += binary_to_morse[bit[0] * (len(bit) // rate_val)]

    return morse_msg


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


# some outlier examples:
# 111 => E
# 1111111 => E
# 1110111 => M
# 111000111 => I
# 111110000011111 => I
# decoded_bits = decode_bits(bits)
# Example from description:
bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
bits = "111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111"
msg = "HEY JUDE"
bits = "1110001010101000100000001110111010111000101011100010100011101011101000111010111000000011101010100010111010001110111011100010111011100011101000000010101110100011101110111000111010101110000000101110111011100010101110001110111000101110111010001010100000001110111011100010101011100010001011101000000011100010101010001000000010111010100010111000111011101010001110101110111000000011101010001110111011100011101110100010111010111010111"
msg = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

# Her's some (value, rate) key pairs to test the rate with
samples = {
    "111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111": 6,
    "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011": 2,
    "1110001010101000100000001110111010111000101011100010100011101011101000111010111000000011101010100010111010001110111011100010111011100011101000000010101110100011101110111000111010101110000000101110111011100010101110001110111000101110111010001010100000001110111011100010101011100010001011101000000011100010101010001000000010111010100010111000111011101010001110101110111000000011101010001110111011100011101110100010111010111010111": 1,
    "111000111": 3,
    "111": 3,
    "1110111": 1,
    "111110000011111": 5,
    "1111111": 7,
    "10001": 1,
}

decoded_bits = decode_bits(bits)
decoded_msg = decode_morse(decoded_bits)
print(">> Decoded msg:", decoded_msg)
print(">> The message:", msg)
print(">>", decoded_msg == msg)


# testing the rate func
a = "00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110"
# (value, rate) key pairs
samples = {
    "111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111": 6,
    "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011": 2,
    "1110001010101000100000001110111010111000101011100010100011101011101000111010111000000011101010100010111010001110111011100010111011100011101000000010101110100011101110111000111010101110000000101110111011100010101110001110111000101110111010001010100000001110111011100010101011100010001011101000000011100010101010001000000010111010100010111000111011101010001110101110111000000011101010001110111011100011101110100010111010111010111": 1,
    "111000111": 3,
    "111": 3,
    "1110111": 1,
    "111110000011111": 5,
    "1111111": 7,
    "10001": 1,
}

for index, (value, result) in enumerate(samples.items()):
    rate_val = rate(value)
    print(
        ">> n-{} expected: {} Got: {} ===> {}".format(
            index, result, rate_val, result == rate_val
        )
    )


# Result
# >> n-0 expected: 6 Got: 6 ===> True
# >> n-1 expected: 2 Got: 2 ===> True
# >> n-2 expected: 1 Got: 1 ===> True
# >> n-3 expected: 3 Got: 3 ===> True
# >> n-4 expected: 3 Got: 3 ===> True
# >> n-5 expected: 1 Got: 1 ===> True
# >> n-6 expected: 5 Got: 5 ===> True
# >> n-7 expected: 7 Got: 7 ===> True
# >> n-8 expected: 1 Got: 1 ===> True

# Draft:
# bits = bits[bits.index('1'):len(bits)-bits[::-1].index('1')] # remove the zeros from the beginning and the end of bits


# rate = (bits.index("0")
#     # len(
#     #     bits[bits.index("0") : bits.index("0") + bits[bits.index("0") :].index("1")]
#     # )
#     if "0" in bits
#     else len(bits)
# )
# rate = 1
# rate = 2 if rate % 2 == 0 else 1 if rate in (1, 3) else rate


# bits = "1100011001"
# bits = "11111000011111001"
# res = bits[bits.index("0") : bits.index("0") + bits[bits.index("0") :].index("1")]
