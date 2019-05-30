# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, health, current_room):
        self.name = name
        self.health = health
        self.current_room = current_room
        self.items = []
    
    def __str__(self):
        return f"The player's name is {self.name}, currently has {self.health} health, these items: {self.items}, and is in this room: {self.current_room}"