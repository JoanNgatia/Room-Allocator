import unittest
from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace


class TestModels(unittest.TestCase):
    def setup(self):
        self.office = Office()
        self.livingspace = LivingSpace()
        self.f = self.Employee('Joan Ngatia', 'fellow', choice_housing=True)
        self.f = self.Employee('Anthony Nandaa', 'staff')

    def test_room_creation(self):
        """Test room methods and properties"""
        self.office = Office('Krypton')
        self.livingspace = LivingSpace('Lilac')
        office_size = self.office.maximum_members
        livingspace_size = self.livingspace.maximum_members
        self.assertEqual(office_size, 6)
        self.assertEqual(livingspace_size, 4)
