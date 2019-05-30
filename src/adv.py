from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
josh = Player('josh', 100, None, 'outside')
print(josh)
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
    print(josh.current_room)
    print(room[josh.current_room].description)

    move = input("Which direction would you like to go? N, S, E, or W?: ")

    if move not in ["N", "S", "E", "W", "n", "s", "e", "w"]:
        input("Please enter a valid direction: N, S, E, W: ")
    '''
    if move =="N":
        josh.current_room = room[josh.current_room].n_to
        print(room[josh.current_room].description)
    elif move == "S":
        josh.current_room = room[josh.current_room].s_to
    elif move == "E":
        josh.current_room = room[josh.current_room].e_to
    
    '''
    move = move.lower()
    print(move)

## travel not working yet
    def travel(player, dir):
        try:
            if getattr(room[player.current_room], f'{dir}_to').title.lower().split(" ")[0] == 'grand':
                player.current_room = getattr(room[player.current_room], f'{dir}_to').title.lower().split(" ")[1]
            else:
                player.current_room = getattr(room[player.current_room], f'{dir}_to').title.lower().split(" ")[0]
        except AttributeError:
            print('\n')
            print(f'There is no path in that direction, {player.name}.')

    travel(josh, move)
    print("\n")
    print(josh.current_room)