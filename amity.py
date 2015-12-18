from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace


class Amity(object):
    def pre_populate_Office(self):
        Office = []
        a = ['Hogwarts', 'Valhalla', 'Roundtable', 'Krypton', 'Oculus']
        for item in a:
            Office.append(item)
        return Office

    def pre_populate_livingspace(self):
        LivingSpace = []
        b = ['Brown', 'Cyan', 'Turquiose', 'White', 'Orange']
        for item in b:
            LivingSpace.append(item)
        return LivingSpace

    def assign_office(self, Office, Staff, Fellow):
        room = Rooms()
        room.available_space()

amity = Amity()
print amity.pre_populate_Office()
print amity.pre_populate_livingspace()
