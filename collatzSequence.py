def collatz(number):
    while number >= 1:
        if number % 2 == 0:
            print(number)
            number = number // 2
        elif number % 2 == 1 and number != 1:
            print(number)
            number = 3 * number + 1
        elif number == 1:
            print(number)
            break
try:
    collatz(int(input()))
except ValueError:
    print("That's not a number, dummy")
