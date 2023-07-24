import numpy as np
from time import time
from os import system
# int("".join(map(str, indexes)))
# [0, 1, 2, 3] ==> 123

# list('{:04d}'.format(123))
# 123 ==> [0, 1, 2, 3]


def index_generate(C, ls_len):
    end = ls_len-C
    progress = np.array([0]*C)
    ranges = ls_len**C
    big_break = False

    # while(progress.sum() < end*C):
    for iter_nbr in range(ranges):
        _ = system('cls')
        print('>> {:.2f}%'.format((iter_nbr*100)/ranges))
        for index in range(0, end+1):
            if end in progress:
                big_break = True
                break
            yield progress
            progress[-1] += 1
        # if big_break:
        #     big_break = False
        #     break
        # if iter_nbr%17:
        # Updates:
        for index in range(C-1, -1, -1):
            if progress[index] > end and index > 0:
                progress[index-1] = (progress[index-1]+1) % ls_len
                progress[index] = progress[index-1]


start = time()
c = 4
tmax = 230
indexes = np.array([0, 1, 2, 3])
max_distance = np.array([-1])
ls = np.array([100, 76, 56, 44, 89, 73, 68, 56, 64,
              123, 2333, 144, 50, 132, 123, 34, 89])


for progress in index_generate(c, ls.size):

    # index_progress = indexes+progress
    # index_progress_sum = ls[indexes+progress].sum()
    # index_progress_array = ls[indexes+progress]
    if max_distance.sum() < ls[indexes+progress].sum() <= tmax:
        max_distance = ls[indexes+progress]
    if max_distance.sum() == tmax:
        break

end = time()
print(f'>> Time: {end-start}Seconds')
print('>> The Distances:', max_distance)
print('>> The Distance:', max_distance.sum())
