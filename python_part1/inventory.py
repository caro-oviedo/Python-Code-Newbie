def display_inventory (inventory):
    """Displays a player's inventory."""
    
    print("Inventory: ")

    total_items = 0 
    for item, total in inventory.items():
        print(f"{total} {item} ")
        total_items += total 
    print(f"Total number of items: {total_items}")


def add_to_inventory(inventory, added_items):
    """Receives a list of items and add them to the player's inventory. """
    
    updated_inventory = inventory
    for item in added_items: 
        updated_inventory.setdefault(item,0)
        updated_inventory[item] += 1

    return updated_inventory
    



inventory = { 
    'rope': 1,
    'torch': 6,
    'gold coin':42, 
    'dagger': 1,
    'arrow': 12,
} 

dragon_loot = ['gold chain', 'dagger', 'gold coin', 'ruby']

display_inventory(inventory)
new_inventory =(add_to_inventory(inventory, dragon_loot))
display_inventory(new_inventory)
