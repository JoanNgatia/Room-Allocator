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
    def __init__(self, name, choice_housing):
        self.name = name
        self.living_space = None
        self.type = type
        self.choice_housing = False

    def chooses_housing(self, choice_housing):
        if choice_housing == 'Y' or choice_housing is True:
            self.choice_housing = True

    def allocate_living_space(self, room):
        self.living_space = room
        return self.living_space


class Staff(Employee):
    """staff inherits from the Employee class"""
    pass


# class Emp_type:
#     type_of = {'fellow': Fellow, 'staff': Staff}
