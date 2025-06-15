# Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

def displayInventory(inventory):
    total = 0
    for k,v in inventory.items():
        print(k,"->",v)
        total += v
    print("total number of items ->",total)

print(displayInventory(stuff))




