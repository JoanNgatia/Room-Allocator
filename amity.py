from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace


class Amity(object):
    living_space = ['Brown', 'Cyan', 'Turquiose', 'White', 'Orange']
    office = ['Hogwarts', 'Valhalla', 'Roundtable', 'Krypton', 'Oculus']

    # def assign_space(self):
    #     opendfile = open('input.txt', 'r')
    #     for line in opendfile:
    #         lastChar = line[-1:]
    #         if lastChar == "Y":
                

            


amity = Amity()
print amity.pre_populate_Office()
print amity.pre_populate_livingspace()
print amity.openfile()
