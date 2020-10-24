import re

# check_date checks whether the entered date is valid.
# 31 - January, March, May, July, August, October, December
# 30 - April, June, September, November
# 28 - Februrary (29 in leap year)

def check_date(month, day, year):
    if year in range(1000, 3000):
        if month in range(1, 13):
            if day in range(1, 32) and month in [1, 3, 5, 7, 8, 10, 12]:
                print("Date entered is valid!")
            elif day in range(1, 31) and month in [4, 6, 9, 11]:
                print("Date entered is valid!")
                if day == 1 and month == 11 and year == 1984:
                    print("...And it's Chris' birthday!")
            elif day in range(28, 30) and month == 2:
                if day == 29:
                    print("Checking if date entered is a leap year.")
                    if year % 4 == 0:
                        if year % 100 == 0:
                            if year % 400 == 0:
                                print("Date entered is valid! It's also a leap year!")
                            else:
                                print("Date entered is invalid! Please enter a valid date.")
                    else:
                        print("Date entered is invalid! Please enter a valid date.")
                else:
                    print("Date entered is valid!")
            else:
                print("Date entered is invalid! Please enter a valid date.")
        else:
            print("Invalid month! Please enter a valid date.")
    else:
        print("Invalid year! Please enter a valid date.")

date = input("Please enter date (MM/DD/YYYY)\n")

date_regex = re.compile(r'(\d\d)/?(\d\d)/?(\d\d\d\d)')
mo = date_regex.search(date)
month, day, year = mo.groups()

print("Month is: " + str(month) + '\n' + "Day is: " + str(day) + '\n' + "Year is: " + str(year))
check_date(int(month), int(day), int(year))