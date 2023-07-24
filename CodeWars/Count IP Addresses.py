# # Version 1
# def count(first_adr, second_adr):
#     first_adr = first_adr.split('.')
#     second_adr = second_adr.split('.')
#     adr_rang = list()
#     for index in range(0, len(first_adr)):
#         adr_rang.append(int(second_adr[index])-int(first_adr[index]))
#         # adr_rang.append(abs(first_adr[index]-second_adr[index]))

# ip_adr_results = [50, 256, 246]
# ip_adr_results = [50, 256, 246]


# def count(first_adr, second_adr):
#     first_adr = first_adr.split('.')
#     second_adr = second_adr.split('.')
#     nbr_adr = 0
#     for index in range(len(first_adr)-1, -1, -1):
#         nbr_adr += abs(int(first_adr[index]) -
#                        int(second_adr[index])) * pow(256, index)
#     return nbr_adr

# def concat(elements):
#     word = ""
#     word

def count(first_adr, second_adr, printing=False):
    first_adr = first_adr.split('.')
    second_adr = second_adr.split('.')
    if printing:
        print('>>', first_adr)
        print('>>', second_adr)
    # first_adr = "{0:08d}{0:08d}{0:08d}{0:08d}".format(int(bin(int(first_adr[0]))[2:]), int(bin(int(first_adr[1]))[2:]),
    #                                                   int(bin(int(first_adr[2]))[2:]), int(bin(int(first_adr[3]))[2:]))
    # second_adr = "{0:08d}{0:08d}{0:08d}{0:08d}".format(int(bin(int(second_adr[0]))[2:]), int(bin(int(second_adr[1]))[2:]),
    #                                                    int(bin(int(second_adr[2]))[2:]), int(bin(int(second_adr[3]))[2:]))
    st1 = "{0:08d}".format(int(bin(int(first_adr[0]))[2:]))
    nd2 = "{0:08d}".format(int(bin(int(first_adr[1]))[2:]))
    rd3 = "{0:08d}".format(int(bin(int(first_adr[2]))[2:]))
    rd4 = "{0:08d}".format(int(bin(int(first_adr[3]))[2:]))
    # first_adr = st1 + nd2 + rd3 + rd4
    first_adr = "".join([st1, nd2, rd3, rd4])
    st1 = "{0:08d}".format(int(bin(int(second_adr[0]))[2:]))
    nd2 = "{0:08d}".format(int(bin(int(second_adr[1]))[2:]))
    rd3 = "{0:08d}".format(int(bin(int(second_adr[2]))[2:]))
    rd4 = "{0:08d}".format(int(bin(int(second_adr[3]))[2:]))
    # second_adr = st1 + nd2 + rd3 + rd4
    second_adr = "".join([st1, nd2, rd3, rd4])
    if printing:
        print('>>', first_adr)
        print('>>', second_adr)
    first_adr = '0b'+first_adr
    second_adr = '0b'+second_adr
    nbr_adr = (int(second_adr, 2) - int(first_adr, 2))
    if printing:
        print(nbr_adr, type(nbr_adr))
        print('*'*35)
    # nbr_adr = [nbr_adr[index:index+9] for index in range(0, 32, 8)]

    return nbr_adr


ip_adresses = [
    ["10.0.0.0", "10.0.0.50", "50"],
    ["10.0.0.0", "10.0.1.0", "256"],
    ["20.0.0.10", "20.0.1.0", "246"]
]

for index, (first_adr, second_adr, res) in enumerate(ip_adresses):
    nbr_adr = count(first_adr, second_adr, False)
    # if nbr_adr != ip_adr_results[index]:
    print("   >> adr range N-{} state is {}, ===> result: {:<10}  -  real number: {:<10}".format(
        index+1, nbr_adr == int(res), nbr_adr, res))
