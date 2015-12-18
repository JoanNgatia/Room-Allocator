class Room(object):
    def __init__(self, room_names):
        self.list = room_names
        self.occupiers = []

    def occupiers_names(self):
        """Gives the list of current occupiers of a room"""
        occupiers_list = [occupiers.name for item in self.occupiers]
        return occupiers_list

    def populate(self):
        """Creates a list of room names"""
        roomname_list = []
        for i in self.list:
            roomname_list.append(i)
            return roomname_list

    def current_number(self):
        """checks for current occupancy of a room"""
        return len(self.occupiers)

    def available_space(self):
        """Checks if room is at maximum capacity"""
        """returns true if space is available"""
        if self.current_number() <= self.maximum_members():
            return True
        else:
            return False


class Office(Room):
    maximum_members = 6


class LivingSpace(Room):
    maximum_members = 4
