import numpy as np


def index_generate(c, end):
    for index in range(int(str(c)*c)+1):
        if max(map(int, str(index))) > end:
            continue
        yield('{:04d}'.format(index))
    # if len(set(str(index)))<len(str(index)):
    #     continue

# int("".join(map(str, indexes)))
# [0, 1, 2, 3] ==> 123

# list('{:04d}'.format(123))
# 123 ==> [0, 1, 2, 3]


indexes = [0, 1, 2, 3]
ls = np.array([100, 76, 56, 44, 89, 73, 68, 56, 64,
              123, 2333, 144, 50, 132, 123, 34, 89])
c = 4
tmax = 230

max_distance = np.array([-1])
for index in index_generate(c, ls.size):
    progress = np.array(list(map(int, list('{:04d}'.format(int(index))))))

    index_progress = indexes+progress
    index_progress_sum = ls[indexes+progress].sum()
    index_progress_array = ls[indexes+progress]

    if max_distance.sum() < ls[indexes+progress].sum() <= tmax:
        max_distance = ls[indexes+progress]

print('>> The Distances:', max_distance)
print('>> The Distance:', max_distance.sum())
