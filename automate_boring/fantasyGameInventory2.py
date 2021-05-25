def add_to_inventory(inventory, added_items):
    new_inventory = {}
    for k, v in inventory.items():
        for i in added_items:
            if i == k:
                new_inventory = inventory + i.get()
                return new_inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)

print(inv)
