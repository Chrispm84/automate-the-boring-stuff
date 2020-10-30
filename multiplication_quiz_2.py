'''
Giving up on this. It's possible, but overly complicated.
It's not really worth the time investment.
Author has certainly proved the usefulness of his pyinputplus module.
'''

import time

problem_num = 0
print(problem_num)

def problem():
    tries = 1
    rand_num1 = random.randint(0, 9)
    rand_num2 = random.randint(0, 9)
    
    if tries <= 3:
        answer = int(input(f"Problem #{problem_num}: {rand_num1} X {rand_num2} = ?...\n"))
        if problem_num1 * problem_num2 == answer:
            return "Correct!"
            time.sleep(1)
        else:
            return "Wrong, try again!"
            tries += 1
    else:
        return "You've run out of tries..."
        continue

while problem_num <= 10:
    problem_num += 1

    try:
        print(problem())
    except:
        print("Please only use whole numbers.")