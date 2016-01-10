"""runs the main allocation program"""
import sys
from main.amity import Amity

living_space_names = ['Brown', 'Cyan', 'Turquiose', 'White',
                      'Orange', 'Ruby', 'Lilac', 'Sapphire',
                      'Emerald', 'Quartz']
office_names = ['Hogwarts', 'Valhalla', 'Roundtable', 'Quahog',
                'Springfield', 'Krypton', 'Oculus', 'Narnia',
                'Gotham', 'Nowhere']

if __name__ == '__main__':
    amity = Amity()
"""Ensure that there is a file specified"""
if len(sys.argv) > 1:
	file_name = sys.argv[1]

if file_name:
    """Prepopulate rooms and offices"""
    amity.pre_populate_rooms(office_names, 'office')
    amity.pre_populate_rooms(living_space_names, 'livingspace')

    """Parse the file to get fellows and staff details"""
    amity.get_employee_details(file_name)

    """randomly allocate room space to employees"""
    amity.assign_officespace()
    amity.assign_livingspace()

    """return list of allocations and print them out"""
    amity.get_allocations_list()
    amity.print_allocations()

    """return a list of unallocated persons"""
    amity.get_unallocated()

else:
	print "Please add an input.txt file to read from"