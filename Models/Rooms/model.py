class Room(object):
    def __init__(self, room_names):
        self.list = room_names
        self.occupiers = []

    def occupiers_names(self):
        """Gives the list of current occupiers of a room"""
        occupiers_list = [occupiers.name for occupier in self.occupiers]
        return occupiers_list

    def prepopulate(self):
        roomname_list = []
        for i in self.list:
            roomname_list.append(i)
            return roomname_list


class Office(Room):
    maximum_members = 6


class LivingSpace(Room):
    maximum_members = 4
