import numpy as np
# def test():
#     i = 0
#     for i in range(5):
#         for i in range(5):
#             yield i
#             i += 1
#         for i in range(2):
#             print("HH")


# for i in test():
#     print(i)


# print('>> {:0.2f}%'.format(7.878787))


def index_generate(C, ls_len):
    end = ls_len-C
    progress = np.array([0]*C)
    ranges = ls_len**C

    # while(progress.sum() < end*C):
    for iter_nbr in range(ranges):
        for index in range(0, end+1):
            yield progress
            progress[-1] += 1

        # if iter_nbr%17:
        # Updates:
        for index in range(C-1, -1, -1):
            if progress[index] > end and index > 0:
                progress[index] = 0
                progress[index-1] = (progress[index-1]+1) % ls_len
                
t = np.array(range(4))          
for i in index_generate(4, 5):
    ii = t + i
    print(ii)      