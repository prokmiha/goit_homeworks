import datetime
import re
from collections import UserDict


class Field:
	def __init__(self, value=None):
		self._value = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		self._value = new_value


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

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		if self.is_valid(new_value):
			self._value = new_value
		else:
			raise ValueError


class Birthday(Field):
	def __init__(self, value):
		super().__init__(value)
		self.validity = self.is_valid(value)
		if not self.validity:
			raise ValueError

	@staticmethod
	def is_valid(date):
		date_pattern = r'^\d{1,2}\.\d{1,2}\.\d{4}$'
		if re.match(date_pattern, date):
			day, month, year = map(int, date.split('.'))
			if 1 <= day <= 31 and 1 <= month <= 12 and len(str(year)) == 4:
				return True
		return False

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		if self.is_valid(new_value):
			self._value = new_value
		else:
			raise ValueError


class Record:
	def __init__(self, name, phone=None, birthday=None):
		self.phones = []
		self.name = Name(value=name)
		if phone:
			Phone(value=phone)
		if birthday:
			Birthday(value=birthday)
			self.birthday = birthday

	def add_phone(self, phone):
		if Phone.is_valid(phone):
			self.phones.append(Phone(value=phone))
			return True
		else:
			if len(self.phones) == 0:
				del self.name
			return False

	def add_birthday(self, birthday):
		if Birthday.is_valid(birthday):
			self.birthday = Birthday(value=birthday)

	def remove_phone(self, phone):
		for target in self.phones:
			if target.value == phone:
				self.phones.remove(target)
				if not self.phones:
					return True

	def edit_phone(self, old_phone, new_phone):
		for target in self.phones:
			if target.value == old_phone:
				target.value = new_phone
				break
			else:
				raise ValueError

	def find_phone(self, phone):
		for target in self.phones:
			if target.value == phone:
				return target
		raise ValueError

	def days_to_birthday(self):
		if hasattr(self, 'birthday'):
			today = datetime.date.today()
			current_year = today.year
			day, month, year = map(int, self.birthday.value.split('.'))
			next_birthday = datetime.date(current_year, month, day)

			if next_birthday < today:
				next_birthday = datetime.date(current_year + 1, month, day)

			days_until_birthday = (next_birthday - today).days
			return int(days_until_birthday)
		else:
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

	def iterator(self, count=1):
		records = list(self.data.values())
		total_records = len(records)
		current_index = 0

		while current_index < total_records:
			yield records[current_index:current_index + count]
			current_index += count
