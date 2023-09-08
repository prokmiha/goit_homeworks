from collections import UserDict


class Field:
	def __init__(self, value=None):
		self.value = value


class Name(Field):
	pass


class Phone(Field):
	pass


class Record:
	def __init__(self, name, phone=None):
		self.name = Name(value=name)
		self.phones = []
		if phone:
			self.add_phone_number(phone)

	def add_phone_number(self, phone):
		self.phones.append(Phone(value=phone))


class AddressBook(UserDict):
	def add_record(self, record):
		self.data[record.name.value] = [record]

	def change_record(self, record):
		pass

	def add_more_numbers(self, record):
		pass
