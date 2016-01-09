import unittest
import nose
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main.amity import Amity
from models.employees import Staff, Fellow
from models.rooms import Office, LivingSpace


class TestModels(unittest.TestCase):
    def setup(self):
        self.office = Office()
        self.livingspace = LivingSpace()
        self.fellow = Fellow('Joan Ngatia', True)
        self.staff = Staff('Anthony Nandaa')

    def test_room_creation(self):
        """Test Room methods and properties"""
        self.office = Office('Krypton')
        self.livingspace = LivingSpace('Lilac')
        office_size = self.office.maximum_members
        livingspace_size = self.livingspace.maximum_members
        self.assertEqual(office_size, 6)
        self.assertEqual(livingspace_size, 4)

    def test_current_room_size(self):
        self.office = Office('Roundtable')
        self.livingspace = LivingSpace('Sapphire')
        self.assertLessEqual(self.office.current_number(), 6)
        self.assertLessEqual(self.livingspace.current_number(), 4)


class TestAllocation(unittest.TestCase):
    """Test room allocation to employees"""

    def test_office_allocation(self):
        """Test office allocation to employees"""
        self.fellow = Fellow('Joan Ngatia', True)
        self.staff = Staff('Anthony Nandaa')
        office_name = Office('Gotham')
        living_name = LivingSpace('Emerald')
        office_allocation = self.staff.allocate_office(office_name)
        living_allocation = self.fellow.allocate_livingspace(living_name)
        office_name.add_occupant(self.staff)
        living_name.add_roomie(self.fellow)

        self.assertIsInstance(office_allocation, Office)
        self.assertIsInstance(living_allocation, LivingSpace)
        self.assertIsNotNone(self.staff.allocate_office(Office))
        self.assertIsNotNone(self.fellow.allocate_livingspace(LivingSpace))
        self.assertTrue(office_name.available_space())
        self.assertTrue(living_name.available_space())

    def test_current_occupants(self):
        """Test getting the current occupants of a given room"""
        self.amity = Amity()
        self.fellow = Fellow('Joan Ngatia', True)
        self.staff = Staff('Anthony Nandaa')
        office_name = Office('Gotham')
        living_name = LivingSpace('Emerald')
        self.staff.allocate_office(office_name)
        self.fellow.allocate_livingspace(living_name)
        office_guys = office_name.get_occupants()
        living_guys = living_name.get_occupants()
        self.assertIsNotNone(office_guys)
        self.assertIsNotNone(living_guys)

    def test_unallocated(self):
        """Test number of unallocated employees if any"""
        self.amity = Amity()
        unallocated_employees = self.amity.get_unallocated()
        self.assertGreaterEqual(len(unallocated_employees), 0)

if __name__ == '__main__':
    nose.run()
