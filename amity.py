import random
from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace


class Amity(object):
    living_space_names = ['Brown', 'Cyan', 'Turquiose', 'White', 'Orange',
                          'Ruby', 'Lilac', 'Sapphire', 'Emerald', 'Quartz']
    office_names = ['Hogwarts', 'Valhalla', 'Roundtable', 'Quahog',
                    'Springfield', 'Krypton', 'Oculus', 'Narnia',
                    'Gotham', 'Nowhere']
    fellows = []
    staff = []

    def get_employee_details(self):
        """get employee details from input.txt file"""
        with open(input.txt, 'r') as f:
            for line in f:
                line = line.split()
                employee_name = " ".join([line[:2]])
                employee_type = line[2]
                if employee_type == "FELLOW":
                    self.fellows.append(employee_name)
                print self.fellows
                self.staff.append(employee_name)
                print self.staff

    def assign_office_space(self, fellows, staff, office_names):
        """shuffle office indices"""
        office_index = list(range(10))
        random.shuffle(office_index)

        """assign office to staff"""
        for staff in staff:
            office_chosen = office_index.pop(office_index)
            office_assigned = office_names[office_chosen]
            if office_chosen.available_space is True:
                return office_assigned
            office_chosen += 1


amity = Amity()
# print amity.get_employee_details()
# print amity.pre_populate_livingspace()
# print amity.openfile()
