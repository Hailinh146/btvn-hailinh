d = {"apple": 15, "bananas": 35, "grapes": 12}

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
}
print(inventory)
print("*******************************")

inventory['pocket'] = ['seashell','strange berry','lint']
print(inventory)
print("*******************************")

inventory['backpack'].sort()
print(inventory)
print("*******************************")

del (inventory['backpack'][1])
print(inventory)
print("*******************************")

inventory['gold'] += 50
print(inventory)
