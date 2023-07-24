
overLevelChar = [["C", 4],
                 ["T", 2],
                 ["A", 2],
                 ["G", 3]]

possMissChComb = []


for y in range(0, len(overLevelChar)):
    for i in range(0, len(overLevelChar)):
        comb = overLevelChar[y][0]
        for j in range(0, len(overLevelChar)):
            if j != i:
                comb += overLevelChar[j][0]

        possMissChComb.append(comb)

    print(possMissChComb)
