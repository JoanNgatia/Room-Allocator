[![Build Status](https://travis-ci.org/andela-jngatia/Room-Allocator.svg?branch=develop)](https://travis-ci.org/andela-jngatia/Room-Allocator)
# Room-Allocator

##Description
This is a system to allocate offices and living spaces to employees at Amity.

##How it works
1. Simply clone the repo by running
		`git clone https://github.com/andela-jngatia/Room-Allocator.git`.
2. Install dependencies as per the requirements.txt file within your virtual environment.
		`pip install -r requirements.txt`.
3. Run the allocation program
		`python manage.py <inputfile>`.
4. To view the allocations, 
	open `office_allocation.txt` for office allocation or 
	`livingrooms_allocation.txt` for living spaces allocated.
    The allocations will  also be printed to the console.

##Running tests
1.	Navigate to project directory.
2.	Run `python tests/test_model.py` to test the system.
3.	Run `coverage run tests/test_model.py` to check coverage.

###Author
###### [Joan Ngatia](https://github.com/andela-jngatia)
