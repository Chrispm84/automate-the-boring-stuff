def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
        return inventory

def print_items(inventory):
    print("Inventory:")
    items_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        items_total += v
    print("Total number of items: " + str(items_total))

inv = {'gold coin': 42, 'rope': 1}
print(inv) #Test
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(dragon_loot) #Test
inv = add_to_inventory(inv, dragon_loot)
print(inv) #Test
print_items(inv)