# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, health, items, current_room):
        self.name = name
        self.health = health
        self.items = items
        self.current_room = current_room
    
    def __str__(self):
        return f"This player's name is {self.name}, currently has {self.health} health, these items: {self.items}, and is in this room: {self.current_room}"