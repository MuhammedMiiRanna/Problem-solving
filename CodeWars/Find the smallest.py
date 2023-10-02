def smallest(n):
    # your code
    n_str = str(n)
    n_list = list(n_str)
    pass


n = 1000000
n = 261235
n = 209917
n_str = str(n)
n_list = list(n_str)

while "0" in n_list:
    n_list.remove("0")

min_val = (
    min(n_list)
    if min(n_list) != n_list[0]
    else min(n_list[1:])
    if len(n_list) > 1
    else n_list[0]
)
min_indx = n_list.index(min_val)

n_list.remove(min_val)

if min_indx == 0:
    
for val in n_list:
    pass

print("> n", n)
print("> n_str", n_str)
print("> n_list", n_list)
print("> min_indx", min_indx)
print("> min_val", min_val)


samples = (
    (261235, [126235, 2, 0]),
    (209917, [29917, 0, 1]),
    (285365, [238565, 3, 1]),
    (269045, [26945, 3, 0]),
    (296837, [239687, 4, 1]),
    (1000000, [0000001, 0, 6]),
)

# for index, (number, exp_result) in enumerate(samples):
#     result = smallest(number)
#     print(
#         ">> n-{} expected: {} Got: {} ===> {}".format(
#             index, exp_result, result, exp_result == result
#         )
#     )
