


def smallest(n):
    s = str(n)
    min1, from1, to1 = n, 0, 0
    for i in range(len(s)):
        removed = s[:i] + s[i+1:]
        for j in range(len(removed)+1):
            num = int(removed[:j] + s[i] + removed[j:])
            if (num < min1):
                min1, from1, to1 = num, i, j
    return [min1, from1, to1]


n = 1000000
n = 261235
n = 209917

res = smallest(n)
print(res)
# import signal
# TIMEOUT = 5  # number of seconds your want for timeout


# def interrupted(signum, frame):
#     "called when read times out"
#     print('interrupted!')


# signal.signal(signal.SIGALRM, interrupted)


# def input():
#     try:
#         print('You have 5 seconds to type in your stuff...')
#         foo = raw_input()
#         return foo
#     except:
#         # timeout
#         return


# # set alarm
# signal.alarm(TIMEOUT)
# s = input()
# # disable the alarm after success
# signal.alarm(0)
# print('You typed', s)


############################################################


