import pyinputplus as pyip

"""
This is bad
Real bad. 
Sorry to anyone who sees this, lol.
"""

prices = {'White': .62, 'Wheat': .73, 'Sourdough': .85, 'Chicken': 1.58, 'Turkey': 2.03, 'Ham': 1.25, 'Tofu': .01,
          'Cheddar': .56, 'Swiss': .81, 'Mozzarella': .65, 'Mayo': .01, 'Mustard': .32, 'Lettuce': .19, 'Tomato': .56}

total = 0.00

if pyip.inputYesNo(prompt="Would you like to buy a sandwich? ",) == 'yes':
    bread = pyip.inputMenu(['White', 'Wheat', 'Sourdough'], prompt="What kind of bread would you like?\n", numbered=True)
    total += prices[bread]
    protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt="What protein do you want?\n", numbered=True)
    total += prices[protein]

    if pyip.inputYesNo(prompt="Would you like cheese on that? ") == 'yes':
        cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt="What type of cheese?\n", numbered=True)
        total += prices[cheese]
    
    if pyip.inputYesNo(prompt="Would you like Mayo on that? ") == 'yes':
        mayo = 'Mayo'
        total += prices[mayo]
    
    if pyip.inputYesNo(prompt="Do you want mustard on it? ") == 'yes':
        mustard = 'Mustard'
        total += prices[mustard]
    
    if pyip.inputYesNo(prompt="How about a bit of lettuce? ") == 'yes':
        lettuce = 'Lettuce'
        total += prices[lettuce]
    
    if pyip.inputYesNo(prompt="And how about tomatoes? ") == 'yes':
        tomato = 'Tomato'
        total += prices[tomato]
    
    num_of_sandwiches = pyip.inputInt(prompt="How many of these sandwiches would you like? ", greaterThan=1)
    total *= num_of_sandwiches
    total = round(total, 2)

    print(f"Ok, your total comes to ${total}.\nThanks for coming to Samiches R Us for all your samich needs!")

else:
    print("Ok, maybe next time then.")