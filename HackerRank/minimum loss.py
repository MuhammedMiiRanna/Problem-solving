
# Problem link: https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true
# PS: Thanx for "Amit Yadav" for his hint
# the previous solutions showed 'Time limit exceeded' error :3
# his profile: https://www.hackerrank.com/Coder_AMiT?hr_r=1

def minimumLoss(price):
    # Write your code here
    sorted_price = sorted(price)
    min_loss = sorted_price[-1]
    for index in range(len(sorted_price)-1):
        if min_loss > sorted_price[index+1]-sorted_price[index] > 0 and \
                price.index(sorted_price[index+1]) < price.index(sorted_price[index]):
            min_loss = sorted_price[index+1]-sorted_price[index]

    return min_loss


prices = [
    [[20, 7, 8, 2, 5], 2],
    [[5, 10, 3], 2],
]

for index, (price, answer) in enumerate(prices):
    result = minimumLoss(price)
    print(
        f'>> Result Number-{index+1} is {result == answer} ===> Expected: {answer} Result: {result} ')


# history:

    # tbh idk when did i wrote this and how
    # price_len = len(price)
    # min_loss = max(price)-min(price)

    # for first_year in range(price_len-1):
    #     for sec_year in range(first_year+1, price_len):
    #         loss = price[first_year] - price[sec_year]
    #         if min_loss > loss > 0:
    #             min_loss = loss
    # return min_loss


# def minimumLoss(price):
#     min_loss = max(price)
#     for index in range(len(price)-1):
#         loss = price[index] - min(price[index+1:])
#         if min_loss > loss > 0:
#             min_loss = loss
#         if loss == 1:
#             return min_loss
#     return min_loss

# def minimumLoss(price):
#     min_loss = max(price)
#     for index in range(len(price)-1):
#         px = price[index]
#         price_left = price[index:]
#         sorted_price_left = sorted(price_left)
#         min_price = sorted_price_left[sorted_price_left.index(px)-1]

#         loss = px - min_price
#         if min_loss > loss > 0:
#             min_loss = loss
#         if loss == 1:
#             return min_loss
#     return min_loss
