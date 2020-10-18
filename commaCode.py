def print_list(list):
        for i in range(len(list) - 1):
            print(list[i] + ', ', end='')
        print('and ' + list[i + 1])

spam = []

while True:
    item = input("What would you like to add to the list?\n")
    if item is not '':
        spam.append(item)
    else:
        break

print_list(spam)