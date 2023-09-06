def line_start(line=8):
    start, val_sum = 1, 0
    for i in range(1, line):
        val_sum += 2
    start += val_sum
    return start


line = 1
def row_sum_odd_numbers(n):
    start = sum(range(0, n * 2, 2)) + 1
    return sum(range(start, start + n*2, 2))


# def row_sum_odd_numbers(n):
#     def start(s):
#         if s == 1:
#             return 1;
#         else:
#             return start(n-1) + 2 * (n-1)
#     summ = start(n)
#     return sum([summ + 2 for i in range(n)])


samples = ((1, 1), (2, 8), (13, 2197), (19, 6859), (41, 68921))

for index, (number, exp_result) in enumerate(samples):
    result = row_sum_odd_numbers(number)
    print(
        ">> n-{} expected: {} Got: {} ===> {}".format(
            index, exp_result, result, exp_result == result
        )
    )
