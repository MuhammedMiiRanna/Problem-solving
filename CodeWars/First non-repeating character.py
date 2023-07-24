
def char_count(string, char):
    if char.lower() != char.upper():
        return string.count(char.lower()) + string.count(char.upper())
    return string.count(char)


def first_non_repeating_letter(string):
    # old_string = string
    # string = zip(string, countFunction)
    # str_dict = {char.lower(), string.count(char.lower()) + string.count(char.upper()) for char in string}
    # string = list(string)
    str_dict = {char.lower(): char_count(string, char) for char in string}

    for char, occ in str_dict.items():
        if occ == 1:
            break
    else:
        return ""

    if char.lower() in string:
        return char.lower() 
    return char.upper()
    # your code here


tests = {
    'a' : 'a',
    'stress' : 't',
    'moonmen' : 'e',
    '' : '',
    'abba' : '',
    'aa' : '',
    '~><#~><' : '#',
    'hello world, eh?' :  'w',
    'sTreSS' : 'T',
    'Go hang a salami, I\'m a lasagna hog!' : ','
}

for key, value in tests.items():
    result = first_non_repeating_letter(key)
    if result != value:
        print(f">> {key} ==> should be <<<< {value} >>>> :: u return <<<< {result} >>>>")

#############################################################################

# def first_non_repeating_letter(string):
#     singles = [i for i in string if string.lower().count(i.lower()) == 1]
#     return singles[0] if singles else ''


# from collections import Counter
# def first_non_repeating_letter(string):
#     cnt = Counter(string.lower())
#     for letter in string:
#         if cnt[letter.lower()] == 1:
#             return letter
#     return ''

# def first_non_repeating_letter(string):
#     string_lower = string.lower()
#     for i, letter in enumerate(string_lower):
#         if string_lower.count(letter) == 1:
#             return string[i]
            
#     return ""



#############################################################################