from Employees.model import Staff, Fellow


class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []

    def occupant_names(self):
        """Gives the list of current occupiers of a room"""
        occupants = [occupant.name for occupant in self.occupants]
        return occupants

    def current_number(self):
        """checks for current occupancy of a room"""
        return len(self.occupants)

    def available_space(self):
        """Checks if room is at maximum capacity"""
        """returns true if space is available"""
        if self.current_number() < self.maximum_members:
            return True
        else:
            return False


class Office(Room):
    maximum_members = 6

    def add_occupant(self, employee):
        "adds an employees name to list of office occupants"
        if self.available_space() is True:
            # import ipdb; ipdb.set_trace()
            if isinstance(employee, Staff) or isinstance(employee, Fellow):
                self.occupants.append(employee)
                with open('office_allocation.txt', 'a') as f:
                    f.write(employee.name + " " + self.room_name + "\n")
            return self.occupants

class LivingSpace(Room):
    maximum_members = 4

    def add_occupant(self, Fellow):
        if self.available_space is True:
            self.accupants.append(Fellow)
        return self.occupants
