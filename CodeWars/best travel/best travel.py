

# def choose_best_distance(tmax, c, ls):
# max_distance, citys, distances


def choose_best_sum(tmax, c, ls):
    pass


# INITIALISATION
all_distances_list = [
    [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89],
    [50, 55, 57, 58, 60],
    [50, 55, 56, 57, 58],
    [91, 74, 73, 85, 73, 81, 87]
]
distances = all_distances_list[0]
# max_distance = 174
# citys = 3

# expected_result = []
parameters = [
    ((230, 4, distances), 230),
    ((430, 5, distances), 430),
    ((430, 8, distances), None),
    ((174, 3, all_distances_list[1]), 173),
    ((163, 3, all_distances_list[2]), 163),
    ((230, 3, all_distances_list[3]), 228)
]
# parameters = [((173, 3, all_distances_list[1]), 174)]

all_printed_result = []
for index, ((max_distance, citys, distances), expected_result) in enumerate(parameters):
    possible_distance = choose_best_distance(max_distance, citys, distances)
    print('#'*60)
    print('>> distances:', distances)
    print(">> Sample N-{:<2} result: {:<6}\n>>     Max distance is: {:<4}\n>>     Expected is: {:<4}\n>>     Result is: {:<4}".format(
        index+1, bool(possible_distance == expected_result), max_distance, str(expected_result), str(possible_distance)))
    print('#'*60)
    all_printed_result.append("""{}
>> distances: {}
>> Sample N-{:<2} result: {:<6}
>>     Max distance is: {:<4}
>>     Expected is: {:<4}
>>     Result is: {:<4}
{}
""".format(
        '#'*60,
        distances, index+1,
        bool(possible_distance == expected_result),
        max_distance,
        str(expected_result),
        str(possible_distance),
        '#'*60
    ))


print(*all_printed_result)


########################################################################
# Comments:
# per_max: permanent max
# poss_dist: possible distance


# # V1:
# def choose_best_distance(tmax, c, ls):
#     # max_distance, citys, distances
#     poss_dist = None
#     ls.sort()
#     for i in range(len(ls)-c):
#         per_max = 0
#         for j in range(c):
#             per_max += ls[i]
#         # poss_dist = per_max if per_max <= tmax else poss_dist = None
#         if per_max < tmax:
#             poss_dist = per_max
#         elif per_max == tmax:
#             poss_dist = per_max
#             break
#     return poss_dist


# # V2:
# def choose_best_sum(tmax, c, ls):
#     ls.sort()
#     rec_perm = 0
#     poss_dist = None
#     R = len(ls)-c+1
#     for i in range(R):
#         # nb, r = i+c-1, len(ls)
#         i2 = i+c-1
#         sum_ls = sum(ls[i:i2])
#         R2 = i+c-1
#         for j in range(R2, len(ls)):
#             per_max = sum_ls + ls[j]
#             if rec_perm < per_max <= tmax:
#                 poss_dist = per_max
#                 rec_perm = per_max
#     return poss_dist


# # V2:
# def choose_best_distance(tmax, c, ls):
#     # max_distance, citys, distances
#     ls = list(set(ls))
#     ls.sort()
#     rec_perm = 0
#     poss_dist = None
#     R = len(ls)-c+1
#     for i in range(R):
#         # nb, r = i+c-1, len(ls)
#         i2 = i+c-1
#         sum_ls = sum(ls[i:i2])
#         R2 = i+c-1
#         print('tmax:', tmax, ls)
#         for j in range(R2, len(ls)):
#             per_max = sum_ls + ls[j]
#             if rec_perm < per_max <= tmax:
#                 print('TRIUUEEEE')
#                 poss_dist = per_max
#                 rec_perm = per_max
#             print('{} - {:<8} ==> {}'.format(ls[i:i2], ls[j], per_max))
#         print('*'*45)
#     return poss_dist
