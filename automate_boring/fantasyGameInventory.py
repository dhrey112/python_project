def display_inventory(inventory):
    total_items = 0
    print("Inventory")
    for k, v in inventory.items():
        print(str(v), " ", k)
        total_items += v
    print("Total number of items: ", total_items)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)
