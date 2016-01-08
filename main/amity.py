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

    def assign_officespace(self):
        # length = len(office_names)
        shuffle(self.room_list['office'])

        """assign office to staff randomly"""
        employee_list = self.fellows_list + self.staff_list
        shuffle(employee_list)
        employee_pos = 0
        # for employee in employee_list:
        if employee_pos < len(employee_list):
            for employee in employee_list:
                office_list = self.room_list['office']
                # print office_list
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

    def assign_livingspace(self):
        shuffle(self.room_list['livingspace'])
        # print self.room_list
        livingspace_list = self.room_list['livingspace']
        length = len(livingspace_list)

        shuffle(self.fellows_list)
        fellow_pos = 0
        """assign living space to fellows"""
        if fellow_pos < len(self.fellows_list):
            for fellow in self.fellows_list:
                if fellow.wants_housing:
                    livingspace_allocated_index = int(random() * length)
                    livingspace_allocated = livingspace_list[livingspace_allocated_index]

                    if livingspace_allocated.available_space() is True:
                        fellow.allocate_livingspace(livingspace_allocated)
                        livingspace_allocated.add_roomie(fellow)
                        self.allocated.append(livingspace_allocated)
                        livingspace_allocated_index += 1
                    else:
                        self.unallocated.append(fellow)

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
