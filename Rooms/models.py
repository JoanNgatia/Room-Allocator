class Room(object):
    def __init__(self, room_names):
        self.list = room_names
        self.occupiers = []

    def occupiers_names(self):
        """Gives the list of current occupiers of a room"""
        occupiers = [occupier.name for occupier in self.occupiers]
        return occupiers

    def current_number(self):
        """checks for current occupancy of a room"""
        return len(self.occupiers)

    def available_space(self):
        """Checks if room is at maximum capacity"""
        """returns true if space is available"""
        if self.current_number() < self.maximum_members():
            return True
        else:
            return False


class Office(Room):
    maximum_members = 6
    room_type = 'office'


class LivingSpace(Room):
    maximum_members = 4
    room_type = 'living'
