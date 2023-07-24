from math import floor

rows, columns = 4, 4

for row in range(2, rows+1):
    for column in range(1, columns+1):
        print('*'*15)
        result = ((column+1)//2) * ((row+1)//2)
        f_result = (column+1)//2 * (row+1)//2
        # result = ((row+1)*(column+1))/2
        print('>> normal expression:', (column+1)//2, (row+1)//2)
        print('>> second expression:', ((column+1)//2), ((row+1)//2))
        print('>>               row:', row)
        print('>>            column:', column)
        print('>>           Results:', result, f_result)
    print()
