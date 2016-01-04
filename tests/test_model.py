import unittest
from Employees.model import Staff, Fellow
from Rooms.models import Office, LivingSpace


class TestModels(unittest.TestCase):
    def setup(self):
        self.office = Office()
        self.livingspace = LivingSpace()
        self.fellow = self.Employee('Joan Ngatia', 'fellow', choice_housing=True)
        self.staff = self.Employee('Anthony Nandaa', 'staff')

    def test_room_creation(self):
        """Test Room methods and properties"""
        self.office = Office('Krypton')
        self.livingspace = LivingSpace('Lilac')
        office_size = self.office.maximum_members
        livingspace_size = self.livingspace.maximum_members
        self.assertEqual(office_size, 6)
        self.assertEqual(livingspace_size, 4)


class TestAllocation(unittest.TestCase):
    """test room allocation to employees"""
    def test_office_alloaction(self):
        self.fellow = self.Employee('Joan Ngatia', 'fellow', choice_housing=True)
        self.staff = self.Employee('Anthony Nandaa', 'staff')
        office_name = Office('Gotham')
        living_name = LivingSpace('Emerald')
        office_allocation = self.staff.allocate_office(office_name)
        living_allocation = self.fellow.allocate_livingspace(living_name)
        office_name.add_occupant(self.staff)
        living_name.add_occupant(self.fellow)

        self.assertIsInstance(office_allocation, Office)
        self.assertIsInstance(living_allocation, LivingSpace)
        self.assertIsNotNone(self.staff.allocate_office())
        self.assertIsNotNone(self.felllow.allocate_livingspace())
        self.assertFalse(office_name.available_space())
        self.assertFalse(living_name.available_space())
