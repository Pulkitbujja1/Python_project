def addToInventory(inventory, addedItems):
    for Items in addedItems:
            inventory.setdefault(Items,0)
            inventory[Items] += 1
    print(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
