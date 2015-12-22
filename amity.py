from random import random
from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace


class Amity(object):

    def __init__(self):
        living_space_names = ['Brown', 'Cyan', 'Turquiose', 'White', 'Orange',
                              'Ruby', 'Lilac', 'Sapphire', 'Emerald', 'Quartz']
        self.office_names = ['Hogwarts', 'Valhalla', 'Roundtable', 'Quahog',
                        'Springfield', 'Krypton', 'Oculus', 'Narnia',
                        'Gotham', 'Nowhere']
        self.fellows_list = []
        self.staff_list = []

    def get_employee_details(self):
        """filter employee details from input.txt file"""
        with open('input.txt', 'r') as f:
            for line in f:
                line = line.split()
                employee_name = " ".join(line[:2])
                employee_type = line[2]
                if employee_type == "FELLOW":
                    self.fellows_list.append(employee_name)
                else:
                    self.staff_list.append(employee_name)

        print self.fellows_list
        print self.staff_list

    def assign_office_space(self, fellows, staff, office_names):
        """shuffle office indices"""
        length = len(office_names)
        # office_index = range(length)
        # import ipdb; ipdb.set_trace()
        # random.shuffle(office_index)

        """assign office to staff"""
        for staff in staff:
            staff_member = Staff(staff)
            office_index = int(random() * length)
            # office_chosen = office_index.pop()
            office_assigned = office_names[office_index]
            office = Office(office_assigned)
            if office.available_space() is True:
                office.add_occupant(staff_member)
                print office_assigned
            # office_chosen += 1

        """assign office to fellows"""
        for fellow in fellows:
            fellow_member = Fellow(fellow)
            office_index = int(random() * length)
            print 'In the fellows loop!'
            # office_chosen = office_index.pop()
            office_assigned = office_names[office_index]
            office = Office(office_assigned)
            if office.available_space() is True:
                office.add_occupant(fellow_member)
                print office_assigned
            # office_chosen += 1

    def assign_living_space(self, fellows, choice_housing=True):
        """shuffle room indices"""
        living_space_index = list(range(10))
        # random.shuffle(living_space_index)

        """assign living space to fellows"""
        for fellow in fellows:
            if choice_housing:
                living_space_chosen = living_space_index.pop(
                    living_space_index)
                living_space_assigned = living_space_names[living_space_chosen]
                if living_space_assigned.available_space is True:
                    return living_space_assigned
                living_space_chosen += 1


amity = Amity()
# fellows = ['JOAN NGATIA', 'JEE GITHINJI', 'STANLEY NDAGI']
amity.get_employee_details()
fellows = amity.fellows_list
# staff = ['ANTHONY NANDAA']
staff = amity.staff_list
# office_names = ['Hogwarts', 'Valhalla', 'Roundtable', 'Quahog']
office_names = amity.office_names
# print amity.get_employee_details()
print amity.assign_office_space(fellows, staff, office_names)
# # print amity.openfile()
