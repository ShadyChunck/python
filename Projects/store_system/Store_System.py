import os
play = True
name = input("Write your name: ")

player = {
    "name": name,
    "gold": 25
}

player_inventory = []

# [gold_cost, units]
store_catalog = {
    "Steel Sword": [35, 2],
    "Iron Sword": [25, 3],
    "Shield": [17, 5],
    "Vulnerary": [12, 10],
    "Elixir": [16, 7]
}

def show_catalog():
    print(f"We have this available:\n")
    for k, v in store_catalog.items():
        print(f"{k}: {v[0]} gold | {v[1]} units")
    print("")

def see_inventory():
    if player_inventory == []:
        print(f"You don't have nothing in your inventory. Buy something from the catalog!\n")
    else:
        count = 0
        for obj in player_inventory:
            print(f"{1 + count}.- {obj}")
            count += 1
        print("")

def purchase_object():
    finish = False
    count = 0
    for k, v in store_catalog.items():
        print(f"{1 + count}.- {k}: {v[0]} gold | {v[1]} units")
        count += 1
    while finish != True:
        try:
            items = list(store_catalog.keys()) # Creates a list for the keys of the dictionary
            option = int(input("\nWhich object you want to buy?\n"))
            obj = items[option - 1] # Takes the string from the list the user chooses
            # Compares users gold to the item cost 
            if player["gold"] >= store_catalog[obj][0]:
                player["gold"] -= store_catalog[obj][0]
                player_inventory.append(obj)
                print(f"\n{player_inventory[-1]} bought!\nGold updated: {player["gold"]}")
                finish = True
            else:
                print(f"You don't have enough money to buy the {obj}\n")
                break
        except KeyError:
            print("You must write the same exact name of the object. No numbers allowed.\n")
    
def sell_item():
    if player_inventory == []:
        print("There's nothing in your inventory. Please buy something!\n")

def clear():
    os.system("cls")

print("Welcome to our store. What would you like to do?")
while play:
    try:
        decision = int(input("1- See the store's catalog.\n2- See my inventory.\n3- Purchase an object.\n4- Sell an item.\n5- Exit game.\n"))
        match decision:
                case 1:
                    clear()
                    show_catalog()
                    # play = False
                case 2:
                    clear()
                    see_inventory()
                    # play = False
                case 3:
                    clear()
                    purchase_object()
                    # play = False
                case 4:
                    clear()
                    print("Cuatro")
                    play = False
                case 5:
                    clear()
                    print("Bye bye!")
                    play = False
    except ValueError:
        clear()
        print("You must insert an integer number like 1. Not decimals allowed.\n")
    


