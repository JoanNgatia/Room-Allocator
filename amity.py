from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace

office_rooms = ['yellow', 'Turquiose', 'White']


class Amity(object):
    def print_rooms(self):
        office = Office.prepopulate()
        print office
