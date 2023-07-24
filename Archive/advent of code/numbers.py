
with open('advent of code/numbers.txt') as numbers:
    br_count = 0
    lists, temp = dict(), []

    for index, val in enumerate(numbers.readlines()):
        if val != '\n':
            temp.append(int(val[:2]))
        else:
            lists[br_count] = temp
            br_count += 1
            temp = []
            
    lists = list(lists.values())
    lists.append(temp)

print(lists)
print(">> DONE!!")
# [lists[br_count] = lists[br_count].get(br_count, []).append(int(val)) if val != '\n' for val, index in enumerate(numbers.readlines())]

# effort #1:
# with open('advent of code/numbers.txt') as numbers:
# numbers = [list(block) for block in"".join(numbers.readlines()).split('\n')]
# print(numbers)
