from collections import UserDict


class Field:
	def __init__(self, value=None):
		self.value = value


class Name(Field):
	pass


class Phone(Field):
	def __init__(self, value):
		super().__init__(value)
		self.validity = self.is_valid(value)
		if not self.validity:
			raise ValueError

	@staticmethod
	def is_valid(number):
		return len(number) == 10 and number.isdigit()


class Record:
	def __init__(self, name, phone=None):
		self.phones = []
		self.name = Name(value=name)
		if phone:
			Phone(value=phone)

	def add_phone(self, phone):
		if Phone.is_valid(phone):
			self.phones.append(Phone(value=phone))
		else:
			if len(self.phones) == 0:
				del self.name
			return False

	def remove_phone(self, phone):
		for target in self.phones:
			if target.value == phone:
				self.phones.remove(target)
				if not self.phones:
					return True

	def edit_phone(self, old_phone, new_phone):
		for target in self.phones:
			if target.value == old_phone:
				print(target.value)
				target.value = new_phone
				break
			else:
				raise ValueError

	def find_phone(self, phone):
		for target in self.phones:
			if target.value == phone:
				return target
		raise ValueError


class AddressBook(UserDict):
	def add_record(self, record):
		try:
			self.data[record.name.value] = [record]
			return True
		except:
			return False

	def find(self, record):
		if record in self.data:
			return self.data[record][0]
		return None

	def delete(self, record):
		try:
			del self.data[record]
		except KeyError:
			return False
