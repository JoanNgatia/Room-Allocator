class Employee(object):
    """docstring for Employee"""
    def __init__(self, name):
        return self.name


class Fellow(Employee):
    """Fellow inherits from Employee class
       has aother defined attributes"""
    def __init__(self, name, choice_housing):
        self.choice_housing = choice_housing
        super(Fellow, self).__init__(name)
        pass


class Staff(Employee):
    """staff inherits from the Employee class"""
    pass
