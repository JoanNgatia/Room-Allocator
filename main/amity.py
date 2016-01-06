# import argparse
import sys
import fileinput
from random import random
from employees.model import Staff, Fellow
from rooms.models import Office, LivingSpace

living_space_names = ['Brown', 'Cyan', 'Turquiose', 'White',
                      'Orange', 'Ruby', 'Lilac', 'Sapphire',
                      'Emerald', 'Quartz']
office_names = ['Hogwarts', 'Valhalla', 'Roundtable', 'Quahog',
                'Springfield', 'Krypton', 'Oculus', 'Narnia',
                'Gotham', 'Nowhere']
file = sys.argv[1]


class Amity(object):

    def __init__(self):
        self.fellows_list = []
        self.staff_list = []

    def pre_populate_rooms(self, room_list, room_type):
        if room_type.lower() == 'office':
            room_list = [Office(room_name) for room_name in room_list]
        elif room_type.lower() == 'livingspace':
            room_list = [LivingSpace(room_name) for room_name in room_list]

    # def main(self):
    #     """Read input file from command line"""
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument('infile', type='open')
    #     args = parser.parse_args()
    #     self.inputfile = args.inputfile

    def get_employee_details(self, file):
        """filter employee details from input.txt file"""
        # with open(self.inputfile, 'r') as f:
        # for line in f:
        for line in fileinput.input(sys.argv[1]):
                line = line.split()
                employee_name = " ".join(line[:2])
                employee_type = line[2]
                choice_housing = line[-1]
                if employee_type == "FELLOW":
                    self.fellows_list.append(employee_name + " " + choice_housing)
                else:
                    self.staff_list.append(employee_name)

    def assign_office_space(self, office_names):
        length = len(office_names)

        """assign office to staff randomly"""
        for staff in self.staff_list:
            staff_member = Staff(staff)
            office_index = int(random() * length)
            office_assigned = office_names[office_index]
            office = Office(office_assigned)
            if office.available_space() is True:
                office.add_occupant(staff_member)

        """assign office to fellows randomly"""
        for fellow in self.fellows_list:
            fellow_member = Fellow(fellow, True)
            office_index = int(random() * length)
            office_assigned = office_names[office_index]
            office = Office(office_assigned)
            if office.available_space() is True:
                office.add_occupant(fellow_member)

    def assign_living_space(self, living_space_names):
        length = len(living_space_names)

        """assign living space to fellows"""
        for fellow in self.fellows_list:
            fellow_member = Fellow(fellow, True)
            choice_housing = fellow[-1]
            if choice_housing == 'Y':
                living_space_index = int(random() * length)
                living_space_assigned = living_space_names[living_space_index]
                living_space = LivingSpace(living_space_assigned)
                if living_space.available_space() is True:
                    living_space.add_occupant(fellow_member)
        return living_space_assigned

    def get_unallocated_employees(self):
        """return employees that didn't get office space"""
        self.unallocated_employees = []

        for staff in self.staff_list:
            with open('office_allocation.txt', 'r') as f:
                for line in f:
                    if staff not in line:
                        self.unallocated_employees.append(staff)

        for fellow in self.fellows_list:
            with open('office_allocation.txt', 'r') as f:
                for line in f:
                    if fellow not in line:
                        self.unallocated_employees.append(fellow)
        return self.unallocated_employees

    def get_unallocated_fellows(self):
        self.unallocated_fellows = []

        for fellow in self.fellows_list:
            choice_housing = fellow[-1]
            if choice_housing == 'Y':
                with open('rooms_allocated.txt', 'r') as f:
                    for line in f:
                        if fellow not in line:
                            self.unallocated_fellows.append(fellow)
        return "These guys {} didn't get space".format(self.unallocated_fellows)

# if __name__ == '__main__':
#     amity = Amity()
#     amity.get_employee_details()
#     # fellows = amity.fellows_list
#     # staff = amity.staff_list
#     amity.assign_office_space(office_names)
#     amity.assign_living_space(living_space_names)
#     amity.get_unallocated_employees()
