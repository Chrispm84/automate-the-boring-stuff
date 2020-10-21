#! python3

def print_table():
    col_widths = [0] * len(table_data)
    
    for i in table_data[0]:
        if len(i) > col_widths[0]:
            col_widths[0] = len(i)
    #print(col_widths[0])
    
    for i in table_data[1]:
        if len(i) > col_widths[1]:
            col_widths[1] = len(i)
    #print(col_widths[1])
    
    for i in table_data[2]:
        if len(i) > col_widths[2]:
            col_widths[2] = len(i)
    #print(col_widths[2])

    for i in range(4):
        x = 0
        for i_i in range(3):
            print((table_data[i_i][i].rjust(col_widths[x]) + " "), end='')
            x = x + 1
        print('')

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table()