from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

rock = Item("rock", "This is a rock")
room['outside'].items.append(rock)
sword = Item("sword", "Golden sword forged by elves")
room['foyer'].items.append(sword)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? "), 100, 'outside')
print(player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    '''
    if move =="N":
        josh.current_room = room[josh.current_room].n_to
        print(room[josh.current_room].description)
    elif move == "S":
        josh.current_room = room[josh.current_room].s_to
    elif move == "E":
        josh.current_room = room[josh.current_room].e_to
    
    '''

    def get_item(item_name, player, room):
        for item in room.items:
            if item.name == item_name:
                player.items.append(item)
                room.items.remove(item)
                print(f"{player.name} now has {item}")
        return None
    
    def drop_item(item_name, player, room):
        for item in player.items:
            if item.name == item_name:
                player.items.remove(item)
                room.items.append(item)
                print(f"{item.name} is now in {room.name}")
        return None

    def travel(player, dir):
        try:
            if getattr(room[player.current_room], f'{dir}_to').title.lower().split(" ")[0] == 'grand':
                player.current_room = getattr(room[player.current_room], f'{dir}_to').title.lower().split(" ")[1]
            else:
                player.current_room = getattr(room[player.current_room], f'{dir}_to').title.lower().split(" ")[0]
        except AttributeError:
            print('\n')
            print(f'There is no path in that direction, {player.name}.')

    print(room[player.current_room])

    pick_up = input("Would you like to pick up an item? (Y/N): ")


    if pick_up == "Y" and room[player.current_room].items:
        get_item(input("Which item would you like to pick up? "), player, room[player.current_room])
    
    move = input("Which direction would you like to go? N, S, E, or W?: ")

    if len(player.items) > 0:
        drop = input("Would you like to drop an item? (Y/N): ")
        if drop == "Y" and player.items:
            drop_item(input("Which item would you like to drop? "), player, room[player.current_room])    

    if move not in ["N", "S", "E", "W", "n", "s", "e", "w"]:
        input("Please enter a valid direction: N, S, E, W: ")
    move = move.lower()

    travel(player, move)
    print("\n")
    print(player)