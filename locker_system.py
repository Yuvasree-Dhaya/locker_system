"""
Locker Facility System
Author: Yuvasree Dhaya
"""
import os
import time

"""
Data structures for the lockers
"""
open_chambers = 0
total_chambers = 0
chambers = []
rows = 0
disp = 0
border = ""

class Locker:
	"""
	Class: Locker

	Attributes:
	User can set pin
	Lock set time
	
	Methods:
	__init__() - constructor is used to set locker attributes
	get_type() - retrieve locker type
	get_locker_type() - retrieve locker name
	get_lock_set_time() - retrieve locker set time
	get_Locker() - retrieve locker chamber details
	"""	
    def __init__(self, locker_type, user_pin):
		""" Constructor to initialise the Locker class with locker type, lock set time and user pin """
		self.pin = user_pin
        self.lock_set_time = time.time()

    def get_lock_set_time(self):
		""" 
		Description: retrieve locker set time
		Parameters: Locker object
		Returns: Locker set time
		"""
        return self.lock_set_time

    def get_Locker(self):
		""" 
		Description: retrieve locker chamber details
		Parameters: Locker object
		Returns: Locker type, pin, set_time
		"""
        return self.type, self.pin, self.lock_set_time
		
	def check_pin(self, user_pin):
		""" 
		Description: validates the input user_pin before unlocking the locker
		Parameters: Locker object, user_pin
		Returns: True/False
		"""
		if self.pin != user_pin:
			return False
		else:
			return True
	
		
class Small_Locker(Locker):
	""" 
	class: Small_Locker
	Inherits Parent class Locker
	"""
	def __init__(self, user_pin):
		super().__init__(user_pin)
		self.locker_type = 1
		self.locker_type_name = "Small"
		self.locker_fare = 1
	
	def get_type(self):
		""" 
		Description: retrieve locker type
		Parameters: Locker object
		Returns: Locker type
		"""
        return self.locker_type
		
	def get_fare(self):
		""" 
		Description: retrieve locker fare
		Parameters: Locker object
		Returns: Locker fare
		"""
        return self.locker_fare
		
class Medium_Locker(Locker):
	""" 
	class: Medium_Locker
	Inherits Parent class Locker
	"""
	def __init__(self, user_pin):
		super().__init__(user_pin)
		self.locker_type = 2
		self.locker_type_name = "Medium"
		self.locker_fare = 3
	
	def get_type(self):
		""" 
		Description: retrieve locker type
		Parameters: Locker object
		Returns: Locker type
		"""
        return self.locker_type
		
	def get_fare(self):
		""" 
		Description: retrieve locker fare
		Parameters: Locker object
		Returns: Locker fare
		"""
        return self.locker_fare
	
class Large_Locker(Locker):
	""" 
	class: Large_Locker
	Inherits Parent class Locker
	"""
	def __init__(self, user_pin, space_divider=0):
		super().__init__(user_pin)
		self.locker_type = 3
		self.locker_type_name = "Large"
		self.locker_fare = 5
		self.space_divider = space_divider
		
	def get_type(self):
		""" 
		Description: retrieve locker type
		Parameters: Locker object
		Returns: Locker type
		"""
        return self.locker_type
		
	def get_fare(self):
		""" 
		Description: retrieve locker fare
		Parameters: Locker object
		Returns: Locker fare
		"""
        return self.locker_fare
		
	def set_space_divider(self):
		""" 
		Description: retrieve locker fare
		Parameters: Locker object
		Returns: Locker fare
		"""
		print("The large chamber is split into {} spaces".format(self.space_divider))
		return

class Chamber:
	""" 
	Class: Chamber 

	Attributes:
	Locker object
	Locker Stats(Occupied/Free)

	Methods:
	add_Locker() -> Add a locker object and set it to occupied status
	remove_Locker() -> Remove a Locker object and reset occupied status
	Locker_info() -> Return Locker object
	is_open() -> Return Locker status
	"""
    def __init__(self):
		""" Constructor to initialise the Locker class with locker type, lock set time and user pin """
        self.Locker = None
        self.occupied = False
	
    def add_Locker(self, Locker):
		""" 
		Description: Add a Locker object and set it to occupied status
		Parameters: self, Locker object
		Returns: None
		"""
        self.Locker = Locker
        self.occupied = True

    def remove_Locker(self):
		""" 
		Description: Remove a Locker object and resets occupied status
		Parameters: self
		Returns: Locker object
		"""
		locker_object = self.Locker
		self.Locker = None
        self.occupied = False
        return locker_object

    def Locker_info(self):
		""" 
		Description: Returns Locker object
		Parameters: self
		Returns: Locker object
		"""
        return self.Locker

    def is_open(self):
		""" 
		Description: Returns Locker status
		Parameters: self
		Returns: Locker status
		"""
        return self.occupied

def print_row(row):
	"""
	Description: print_row()
	Parameters: row number
	Returns: console output dump
	"""
    console_dump = ""
    console_dump += "|"
    for s in range(disp * row, disp * (row + 1)):
        if not chambers[s].is_open():
            console_dump += "[ ]"
        else:
            console_dump += "[X]"
        if s < disp * (row + 1) - 1:
            console_dump += " "
    console_dump += "|"
    return console_dump

def display_chambers():
	"""
	Description: Displays open locker chambers
	Parameters: None
	Returns: None
	"""
    global chambers, open_chambers, total_chambers, rows
    console_dump = "AVAILABLE LOCKERS: " + str(open_chambers) + "\n"
    console_dump += border
    for row in range(rows):
        console_dump += print_row(row) + "\n"
    console_dump += border
    print(console_dump)

def display_locker_rows():
	"""
	Description: Displays row numbers of each locker
	Parameters: None
	Returns: None
	"""
    global chambers, open_chambers, total_chambers, rows
    console_dump = "AVAILABLE LOCKERS: " + str(open_chambers) + "\n"
    console_dump += border
    for row in range(rows):
        console_dump += print_row(row)
        console_dump += " <" + str(row) + ">\n"
    console_dump += border
    print(console_dump)

def display_space_selection(row):
	"""
	Description: Displays open lockers in a chosen row
	Parameters: None
	Returns: None
	"""
    global chambers, open_chambers, total_chambers, rows
    console_dump = "VIEWING ROW: " + row + "\n"
    console_dump += border
    console_dump += print_row(int(row)) + "\n"
    console_dump += " "
    for count in range(disp):
        if count < 10:
            console_dump += "<" + str(count) + "> "
        else:
            console_dump += "<" + str(count) + ">"
    console_dump += "\n"
    console_dump += border
    print(console_dump)
    return disp

def Book_Locker(locker_type, lock_pin, row, col):
	"""
	Description: Used to book an available locker
	Parameters: locker_type, lock_pin, row, col
	Returns: Locker object
	"""
    global chambers, open_chambers, total_chambers, rows

    """ if all chambers are booked, return None """
    if open_chambers == 0:
        display_chambers()
        print("All Lockers are booked. Please try again later !!")
        return

    """ Check if the requested Locker is available """
    if chambers[(int(row) * disp) + int(col)].is_open():
        display_space_selection(row)
        print("This Locker is already booked. Please use a different one")
        return -1

    """ Creates the Locker object and books it """
    new_Locker = Locker(locker_type, lock_pin)
    chambers[(int(row) * disp) + int(col)].add_Locker(new_Locker)
    open_chambers -= 1
    display_chambers()
    print("Locker Booked!\n"
          "Start time: " + str(time.strftime('%I:%M %p',
                                             time.localtime(new_Locker.get_lock_set_time()))))
    return new_Locker

def fare_calculator(Locker):
	"""
	Description: Used to calculate the fare of the Locker
	Parameters: Locker object
	Returns: Locker Fare
	"""
    total_time = time.time() - Locker.get_lock_set_time()
    if total_time < 3600:
        hours = 1
    else:
        hours = int(total_time / 3600) + 1
		
    rate = Locker.get_fare() * hours
    fare = "Locker Released!\n" \
		   "Total cost for " + "{:.2f}".format(hours) + " hours is $" + "{:.2f}".format(rate)
    return fare

def remove_lot(row, space):
	"""
	Description: Used to release a Locker
	Parameters: row, space
	Returns: None
	"""
    global open_chambers
    if not chambers[(int(row) * disp) + int(space)].is_open():
        display_space_selection(row)
        print("")
        return

	""" Remove the locker and estimate the fare """
    removed = chambers[(int(row) * disp) + int(space)].remove_Locker()
    open_chambers += 1
    display_chambers()
    print(fare_calculator(removed))

def view_Locker(row, space):
	"""
	Description: Used to display Locker's information
	Parameters: row, space
	Returns: None
	"""
    if not chambers[(int(row) * disp) + int(space)].is_open():
        display_space_selection(row)
        print("Booked Locker! Choose a different one")
    else:
        Locker = chambers[(int(row) * disp) + int(space)].Locker_info()
        display_space_selection(row)
        input("Locker Type: " + Locker.get_locker_type() + "\n"
              "Locker hourly fare: " + Locker.get_fare() + "\n"
              "Entry Time: " + str(time.strftime('%m-%d-%Y %I:%M %p',
              time.localtime(Locker.get_lock_set_time()))) + "\n"
              "\nPress Enter to return to menu")


def locker_operations(command):
	"""
	Description: Handles user operations
	Parameters: command
	Returns: None
	"""
	
	""" Book a Locker """
    if command == "Book":
        while True:
            display_chambers()
            input_type = input("Enter Locker Type:\n"
                             "1 - Small\n"
                             "2 - Medium\n"
                             "3 - Large\n"
                             ">")
            if input_type == "1" or input_type == "2" or input_type == "3":
                break
        display_chambers()
        new_lock_pin = input("Enter New Locker lock_pin Number:\n")
		return_val = -1
        while return_val == -1:
            row, col = input("Enter the row and col of the locker that you would like to book.")
            return_val = Book_Locker(int(input_type), new_lock_pin, row, col)

    """ Unbook a Locker """
    elif command == "Unbook":
        row, col, pin = input("Enter the row, col and pin of the locker that you would like to open.")
        remove_lot(row, col, pin)

	""" View a Locker """
    elif command == "View":
		row, col = input("Enter the row, col of the locker that you would like to check.")
        view_Locker(row, space)

	""" Query Locker Fares """
    elif command == "Fare":
        display_chambers()
        input("Locker Facility per hour fares:\n"
              "Small Locker - ${}/hour\n"
              "Medium Locker - ${}/hour\n"
              "Large Locker - ${}/hour\n"
              "\nPress Enter to return to menu".format(Small_Locker.get_fare, Medium_Locker.get_fare, Large_Locker.get_fare,))

    """ Quit """
    elif command == "Quit":
        return

    """ Invalid Command """
    else:
        print("Please enter a valid command")

def read_config():
	"""
	Description: Parse the locker_configuration.txt file to know the locker parameters.
	Parameters: None
	Returns: None
	"""
    global chambers, total_chambers, open_chambers, rows, disp, border

    file_ptr = open('locker_configuration.txt', 'r')
    while True:
        line = file_ptr.readline()
        if line.find("total_chambers") != -1:
            open_chambers = total_chambers = int(line[13:16])

        elif line.find("rows") != -1:
            rows = int(line[5:7])

        for i in range(total_chambers):
            chambers.append(Space())
			disp = int(total_chambers / rows)
            border = "|"
            for i in range(disp - 1):
                for j in range(4):
                    border += "-"
            border += "---|\n"
            break
    file_ptr.close()

def main():
	"""
	Description: Driver API
	parameters: None
	Returns: None
	"""
	""" Read the config file and intialise the Locker System """
    read_config()
    command = ""
    while command != "Quit":
        display_chambers()
        print("Please Select An Option:\n"
              "Book - Book a Locker\n"
              "Unbook - Release a Locker\n"
              "View - View a booked Locker\n"
              "Rate - Display Locker Rates\n"
              "Quit - Quit Application\n")
        locker_operations(command)

if __name__ == '__main__':
    main()
