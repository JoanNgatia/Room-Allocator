import sys
import fileinput
from random import random, shuffle
from models.employees import Staff, Fellow
from models.rooms import Office, LivingSpace


class Amity(object):

    def __init__(self):
        self.fellows_list = []
        self.staff_list = []
        self.room_list = {
            'office': [],
            'livingspace': []
        }
        self.allocated = []
        self.unallocated = []

    def pre_populate_rooms(self, room_list, room_type):
        for room_name in room_list:
            room = Office(room_name) if room_type.lower() == 'office' else LivingSpace(room_name)
            self.room_list[room_type.lower()].append(room)

    def get_employee_details(self, file):
        """filter employee details from input.txt file"""
        for line in fileinput.input(file):
            line = line.split()
            employee_name = " ".join(line[:2])
            employee_type = line[2]
            if employee_type == "FELLOW":
                wants_housing = line[-1]
                self.fellows_list.append(Fellow(employee_name, wants_housing))
            else:
                self.staff_list.append(Staff(employee_name))

    def assign_office_space(self):
        # length = len(office_names)
        shuffle(self.room_list['office'])

        """assign office to staff randomly"""
        employee_list = self.fellows_list + self.staff_list
        shuffle(employee_list)
        employee_pos = 0
        # for employee in employee_list:
        while employee_pos < len(employee_list):
            for employee in employee_list:
                office_list = self.room_list['office']
                length = len(office_list)
                office_allocated_index = int(random() * length)
                office_allocated = office_list[office_allocated_index]
                # for employee in employee_list:
                if office_allocated.available_space() is True:
                    employee.allocate_office(office_allocated)
                    office_allocated.add_occupant(employee)
                    self.allocated.append(office_allocated)
                    office_allocated_index += 1
                else:
                    self.unallocated.append(employee)

            employee_pos += 1

    def assign_living_space(self, living_space_names):
        shuffle(self.room_list['livingspace'])

        length = len(living_space_names)

        """assign living space to fellows"""
        shuffle(self.fellows_list)
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

    def get_allocations_list(self):
        """return a list of allocated employees"""
        return self.allocated

    def print_allocations(self):
        """print a list of allocations"""
        for room in self.allocated:
            print "%s (%s)" % (room.room_name, room.room_type)
            for occupant in room.occupants:
                print occupant.name
            print "\n"

    def get_unallocated(self):
        """return a list of unallocated employees"""
        return self.unallocated
