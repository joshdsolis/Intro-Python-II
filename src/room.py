# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []

    def __str__(self):
        returnString = f"------------\n\n{self.title}\n\n  {self.description}\n\n ------------"
        returnString += f"\nItems:\n{self.items}"
        return returnString
        