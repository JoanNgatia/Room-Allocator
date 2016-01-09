class Employee(object):
    """this class represents employee at amity"""
    def __init__(self, name):
        self.name = name
        self.office = None

    def allocate_office(self, office):
        """assign office to employee"""
        self.office = office
        return self.office

    def __repr__(self):
        return "{0}".format(self.name)        


class Fellow(Employee):
    """Fellow inherits from Employee class
       fellow has choice of housing within Amity"""
    def __init__(self, name, wants_housing='N'):
        self.name = name
        self.living_space = None
        self.wants_housing = True if wants_housing == 'Y' else False

    def allocate_livingspace(self, room):
        self.living_space = room
        return self.living_space


class Staff(Employee):
    """staff inherits from the Employee class"""
    pass
