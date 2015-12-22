class Employee(object):
    """docstring for Employee"""
    def __init__(self, name):
        self.name = name
        self.office = None

    def allocate_office(self, office):
        """assign office to employee"""
        self.office = office
        return self.office


class Fellow(Employee):
    """Fellow inherits from Employee class
       fellow has choice of housing within Amity"""
    def __init__(self, name):
        self.name = name
        self.choice_housing = True
        self.living_space = None

    def living_space(self, living_space, choice_housing):
        self.choice_housing = True
        """assigns living space to fellow"""
        if self.choice_housing:
            self.living_space = living_space
        else:
            print "You did not choose to live within Amity"


class Staff(Employee):
    """staff inherits from the Employee class"""
    pass
