
# def rgb(*args):
#     return map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args)

def rgb(r, g, b):
    rgb = [r, g, b]
    for i in rgb:
        if i < 0:
            rgb[rgb.index(i)] = "00"
        elif 0 <= i < 16:
            rgb[rgb.index(i)] = "0"+str(hex(i)[2:])
        elif i > 255:
            rgb[rgb.index(i)] = hex(255)[2:]
        else:
            rgb[rgb.index(i)] = hex(i)[2:]
    return f"{rgb[0]}{rgb[1]}{rgb[2]}".upper()


values = [
    [0, 0, 0],
    [255, 255, 255],
    [-20, 2, 299]
]

for r, g, b in values:
    result = rgb(r, g, b)
    print(type(result), list(result))


# for r, g, b in values:
#     r = hex(r)[2:] if r > 0 else hex(r)[3:] if hex(r) < 255 else 0
#     g = hex(g)[2:] if g > 0 else hex(g)[3:]
#     b = hex(b)[2:] if b > 0 else hex(b)[3:]
#     print(f"{r} {g} {b}".upper())


# test = "{} : {} : {}".format(hex(r)[2:],
#                              hex(g)[2:],
#                              hex(b)[2:]).upper()
# print(test)
