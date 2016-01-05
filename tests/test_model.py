import unittest
from employees.model import Staff, Fellow
from rooms.models import Office, LivingSpace
from amity import Amity


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
    """Test room allocation to employees"""
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

    """Test getting the current occupants of a given room"""
    def test_current_occupants(self):
        self.amity = Amity()
        office_name = Office('Gotham')
        living_name = LivingSpace('Emerald')
        self.staff.allocate_office(office_name)
        self.fellow.allocate_livingspace(living_name)
        office_guys = office_name.get_occupants()
        living_guys = living_name.get_occupants()
        self.assertIsNotNone(office_guys)
        self.assertIsNotNone(living_guys)

if __name__ == '__main__':
    unittest.main()
