import re


def alphanumeric(password):
    if not password:
        return False
#     if not password or (" " or "_" or "!" or "\"") in password:
#         return False
    regex = "[a-zA-Z0-9]{" + str(len(password)) + "}"
    return bool(re.search(regex, password))
    # if not password or (" " or "_") in password:
    #     return False

    # re
    # if re.search("[a-zA-Z0-9]", password):


passwords = [
    "hello world_",
    "PassW0rd",
    "     ",
    "Y#A",
    "#1BXuZ14",
    "RvlVP}JwW45ctTXHG68Vy",
    "tFPhXKiJM4ZAswT+Suk7A",
    "Xwk4fGBiC0C<yKoa",
    "OxwAvx9GxmWhT0,VqF8nz4XM",
    "76gcHWUCl8HpPXk6VuydT",
    "SIVUidNizt%crn6cXuVwA8hcB",
    "TqvkM7pcSn5DRXszdDJCnX7xi]3U",
    "reihI6^Be4RwPv"
]
password = "hello world_"
# regex = "[a-zA-Z0-9]" + "{" + str(len(password)) +"}"
regex = f"[a-zA-Z0-9]{{len(password)}}"
print(re.search(regex, password))

for password in passwords:
    regex = f"[a-zA-Z0-9]{{len(password)}}"
    print(f">> {password} :: {alphanumeric(password)} ")
    # if not re.search(regex, password):
    #     print(f">> {password} :: {alphanumeric(password)} ")
