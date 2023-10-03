def smallest(n):
    min_val = [n]
    list_val = list(str(n))
    for index in range(len(list_val)):
        val = list_val.pop(index)
        for position in range(len(list_val)+1):
            list_val2 = list_val.copy()
            list_val2.insert(position, val)
            number = int("".join(list_val2))
            if number < min_val[0]:
                min_val = [number, index, position]
        list_val.insert(index, val)
    return min_val


n = 1000000
n = 261235
n = 209917

res = smallest(n)
print(res)

print("> n", n)
# print("> n_str", n_str)
# print("> n_list", n_list)
# print("> min_indx", min_indx)
# print("> min_val", min_val)


samples = (
    (358557593, [358557539, 0, 8]), # 7
    (631631674410392, [631631674410329, 0, 15]),
    (631631674410392, [631631674410329, 0, 15]),
    (31078807567796495, [31078807567796459, 0, 17]),
    (25230115652581390, [25230115652581309, 0, 17]),
    (53481767546562591, [53481767546562519, 0, 17]),
    (21429757759555492, [21429757759555429, 0, 17]),
    (261235, [126235, 2, 0]),
    (209917, [29917, 0, 1]),
    (285365, [238565, 3, 1]),
    (269045, [26945, 3, 0]),
    (296837, [239687, 4, 1]),
    (1000000, [1, 0, 6]),
)

# for index, (number, exp_result) in enumerate(samples):
#     result = smallest(number)
#     print(
#         ">> n-{} expected: {} Got: {} ===> {}".format(
#             index, exp_result, result, exp_result == result
#         )
#     )
