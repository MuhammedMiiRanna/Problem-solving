from test import fact, removeDuplicate
import random
import test
import re

gene = "GAAATAAA"
gene = "ACTGAAAG"
gene = "ACTGCATTACGGCGCATCTAATTAAACAACAGAGTCTATATCAAGGGAATAAATTCCATGATCCGCCTCATCAACATAGAAGGAAACAACAGCCAAACATCCCGCCTTACCTAGTGAAAAACCCCAACATAACCATAAATTCCCTACAAGGAGGAATATTAAAAGTTCAAACTCATCCGCCCAAAATAGGTGGAAAAGAATGTCAGAATCAAAGGCCACACGCATATTTCTATTGACTATAACGTAGTACGGTACAGCGGGAAAAGTTGTAGTTCAAGCAATATTTAGTAATCCTGGAGCCAGAAATTCAGCAGAAATACTAGCCCCAACCAATCACAGCAAATACGCCAGCAAGAATTTATTTATGGAGGCAATCCAATCGACTCCCAACGAGTGCAATGTACTCAAGTGATCTAAGGCAGCATACACTGCCAAAACCTAACCTGTTCATCATTCTAAGTCTTCACCAAGACCCCACCGGTAAGCAGCA"
gene = "ATAGATAACGTATGTAACAAGTAAACAATCGAGCGGGACGATCGTAAGGTAATGAGACATTAAAAAAAATAGGAATAAGAGGTTCCGAGGTGTATCTACTCCGATGAAAATTTGGTGAGAGTCAGGCGATCAAAAAATGAAGGGCTTATAAAAAAGATCTGTTCTAACTAATGTTAGACGACGAAATAGCAATAACAACCTGTTGTCCCAAAGACAATGAAAAATAATCAAATCAGAATCGCTGTCGGGGGATCATCTGGCGTATTATGGAATTTCAAACCATAGGAAATATTGACCACCACAACCAATTGAAGAACAAGACACTCTCTATATAACTGACAAACGAGAGAATGAATATACGTATCGACGAAATAAATAAATAAATGCCGCGCTAATACAGAACAGTAGACCATAATATAAAAAACGGAATGAGTAGTGTACACGGAAAA"
gene = "AAACCGCCAAACGCCACAGCGGGAAACGCAATATTGGGAGGTAGAAGCAGCTATAGAAATCTCAACACAAAGGACGATGGTGAGGCAACTATTACAGACAGATACGAGCTGAACATACATAATTAATTGGTATAGAAAGACTGTTTAAATCAGCTTCTATT"
genelength = len(gene)
level = genelength/4
tcag = {"C": 0,
        "G": 0,
        "T": 0,
        "A": 0}


for i in gene:
    tcag[i] += 1

overLevelChar = []
underLevelChar = []

for key, value in tcag.items():
    if value > level:
        # overLevelChar.append([key, value-level])
        for i in range(int(value-level)):
            overLevelChar.append([key, value-level])

    elif value < level:
        # underLevelChar.append([key, level-value])
        for i in range(int(level-value)):
            underLevelChar.append([key, level-value])


possMissChComb = []


# overLevelChar = [["1"], ["2"], ["3"], ["4"]]
# overLevelChar = [["1"], ["2"]]
# overLevelChar = [["1"]]
# overLevelChar = [["1"], ["2"], ["3"]]
# for _ in range(0, fact(len(overLevelChar))):
for i in range(0, len(overLevelChar)):
    lineCombination = []
    for j in range(0, len(overLevelChar)):
        # comb = overLevelChar[i][0]
        # if i != j:
        #     comb += overLevelChar[j][0]
        comb = ""
        comb = overLevelChar[i][0]
        if j != i:
            for y in range(0, len(overLevelChar), 1):
                comb += overLevelChar[(j+y) % len(overLevelChar)][0]
                lineCombination.append(comb)
                pass

            for y in range(0, len(overLevelChar), -1):
                comb += overLevelChar[(j+y) % len(overLevelChar)][0]
                lineCombination.append(comb)
                pass

    possMissChComb.append(lineCombination)

for i in range(len(possMissChComb)):
    possMissChComb[i] = sorted(
        removeDuplicate(
            possMissChComb[i]))

print(possMissChComb)
print("overLevelChar", overLevelChar)
print("ششششششششششششششششششششششششششششششششششششششششششششش")
print("underLevelChar", underLevelChar)
print("ششششششششششششششششششششششششششششششششششششششششششششش")
print("tcag", tcag)
print("ششششششششششششششششششششششششششششششششششششششششششششش")


for i in possMissChComb:
    for j in i:
        x=(re.findall("A[a-zA-Z]*A[a-zA-Z]*A", j))

print(x)
# x = re.search("^The.*Spain$", txt)
# x = re.findall("ai", txt)


# Habiit nahii les list li m3awdiin
# i=0
# while i < len(possMissChComb):
#     duplicate = possMissChComb.count(i)
#     if duplicate > 1:
#         possMissChComb.pop(i)
#     i+=1


# for cc in range(len(possMissChComb)):
#     i=0
#     while i < len(possMissChComb[cc]):
#         if len(i) < len(overLevelChar):
#             possMissChComb[cc].pop(i)
#         i+=1
 



# max = 0
# charMax = []
# for key, value in actg.items():
#     if value > max:
#         max = value
#         charMax.append(key)
#     print(key, ":", value)
# print(actg)
# test = "CCCC"
# print(test)
# test = test.replace("C", "b", 1)
# print(test)
