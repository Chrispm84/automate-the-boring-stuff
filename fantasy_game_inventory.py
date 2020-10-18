inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def print_items(storage):
    print("Inventory:")
    items_total = 0
    for k, v in storage.items():
        print(str(v) + ' ' + k)
        items_total += v
    print("Total number of items: " + str(items_total))

print_items(inventory)