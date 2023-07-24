


def increment_string(strng):
    if not strng:
        return "1"
    
    int_part = ''
    str_list = list(strng)

    for i in range(len(str_list)):
        try:
            int(str_list[i])
        except ValueError:
            pass
        else:
            length = f":0{len(str_list[i:])}d"

            # int_part = "{:09d}".format(int(''.join(str_list[i:])) +1)
            int_part = "{0101} {int(''.join(str_list[i:])) +1}".format(length)
            break

    str_part = ''.join(str_list[:i])
    # try:
    #     str_list[-1] = str(int(str_list[-1]) + 1)
    # except ValueError:
    #     str_list.append("1")
    
    # strng = "".join(str_list)
    return str_part + int_part



tests = {
    "foo": "foo1",
    "foobar001": "foobar002",
    "foobar1": "foobar2",
    "foobar00": "foobar01",
    "foobar99": "foobar100",
    "foobar099": "foobar100",
    "": "1"
}

for key, value in tests.items():
    if value != increment_string(key):
        print(f"===>> {key} === {value} ::: {increment_string(key)} ")
