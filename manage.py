# runs the main allocation program
from main.amity import Amity

living_space_names = ['Brown', 'Cyan', 'Turquiose', 'White',
                      'Orange', 'Ruby', 'Lilac', 'Sapphire',
                      'Emerald', 'Quartz']
office_names = ['Hogwarts', 'Valhalla', 'Roundtable', 'Quahog',
                'Springfield', 'Krypton', 'Oculus', 'Narnia',
                'Gotham', 'Nowhere']

if __name__ == '__main__':
    amity = Amity()
    amity.get_employee_details(file)
    # fellows = amity.fellows_list
    # staff = amity.staff_list
    amity.assign_office_space(office_names)
    amity.assign_living_space(living_space_names)
    amity.get_unallocated_employees()
