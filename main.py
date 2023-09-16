from collections import UserDict

from classes_homework.decorators_errors import input_error


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
			return True
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


class Errors:
	class UnknownCommandError(Exception):
		@staticmethod
		def unknown_command():
			print("Please type 'edit' or 'add'")

	class MissedNameError(Exception):
		@staticmethod
		def missed_name():
			print("Give me contact name")

	class MissedCriteriaError(Exception):
		@staticmethod
		def missed_criteria():
			print("Give me something to search")

	class MissedNameOrNumber(Exception):
		@staticmethod
		def missed_info():
			print("Give me name and phone please")

		@staticmethod
		def wrong_format():
			print("""
	Input format:
	
	add [name] [phone]
	change [name] [phone]
	search [criteria]
	""")

	class ContactNotFoundError(Exception):
		@staticmethod
		def comtact_not_found():
			print("Contact not found")

	class UnknownContact(Exception):
		@staticmethod
		def unknown_contact():
			print("Wrong name")

	class IncorrectRemoveRequest(Exception):
		@staticmethod
		def incorrect_request():
			print("Please, type correct request")

	class IncorrectEditCommand(Exception):
		@staticmethod
		def incorrect_edit_command():
			print('If you want to edit contact type "edit [name] [old number] [new number]"')


def input_error(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Errors.MissedNameOrNumber as e:
			if len(args[1].split()) == 1:
				return e.missed_info()
			elif len(args[1].split()) == 2:
				return e.wrong_format()
		except Errors.UnknownContact as e:
			return e.unknown_contact()
		except Errors.UnknownCommandError as e:
			return e.unknown_command()
		except Errors.ContactNotFoundError as e:
			return e.comtact_not_found()
		except Errors.MissedNameError as e:
			return e.missed_name()
		except Errors.MissedCriteriaError as e:
			return e.missed_criteria()
		except Errors.IncorrectRemoveRequest as e:
			return e.incorrect_request()
		except Errors.IncorrectEditCommand as e:
			return e.incorrect_edit_command()
		except KeyboardInterrupt:
			print('\nGood buy!')

	return wrapper


@input_error
def add_command(address_book, command):
	try:
		_, name, number = command.split()
	except:
		raise Errors.MissedNameOrNumber
	result = add_contact(name, number, address_book)
	print(result)


@input_error
def edit_command(address_book, command):
	try:
		_, name, old_number, new_number = command.split()
	except ValueError:
		raise Errors.IncorrectEditCommand
	result = edit_contact(name, old_number, new_number, address_book)
	print(result)


def show_all_command(address_book):
	result = show_all_contacts(address_book)
	print(result)


@input_error
def remove_command(address_book, command):
	try:
		_, name = command.split()
	except:
		raise Errors.MissedNameError
	try:
		request = input(
			'Write "del", if you want to delete contact, or type a number, if you want remove it\n')
		if request.isdigit():
			result = remove_only_number(name, request, address_book)
			print(result[0])
			if result[1]:
				remove_contact(name, address_book)

		elif request == 'del':
			result = remove_contact(name, address_book)
			print(result)
	except:
		raise Errors.IncorrectRemoveRequest


@input_error
def search_command(address_book, criteria):
	try:
		_, value = criteria.split()
	except:
		raise Errors.MissedNameError
	if value.isdigit():
		result = number_search(value, address_book)
		if result:
			print(f"I found these contacts with number {value}:")
			for item in result:
				print(item)

	else:
		result = contact_search(value, address_book)
		print(result)


def hello_command(_):
	print('Hello, how can I help you?')


def exit_command(_):
	print('Good buy!')
	return True


def add_contact(name, number, address_book):
	if name in address_book.data:
		result = add_to_contact(name, number, address_book)
		return result
	record = Record(name)
	result = record.add_phone(number)
	if not result:
		return 'Invalid phone number'
	else:
		address_book.add_record(record)
		return "Contact added successfully"


def add_to_contact(name, number, address_book):
	for record in address_book.data[name]:
		if not record.add_phone(number):
			return 'Invalid phone number'
	return "Phone number added"


def edit_contact(name, old_phone, new_phone, address_book):
	if name in address_book.data:
		records = address_book.data[name]
		for record in records:
			record.edit_phone(old_phone, new_phone)
		return f"Contact {name}'s numbers changed from {old_phone} to {new_phone}"
	else:
		return f'Contact {name} not found'


def remove_contact(name, address_book):
	record = Record(name)
	result = address_book.delete(record)
	if result:
		return f"Contact {name} successfully removed"
	return None


def remove_only_number(name, phone, address_book):
	for contact, numbers in address_book.data.items():
		result = []
		for record in numbers:
			result.append([phone.value for phone in record.phones])
		if phone not in result[0]:
			break
		records = address_book.data[name]
		for record in records:
			record.remove_phone(phone)
		return f"Phone number {phone} removed from {name}'s record.", result
	return f"{name} doesn't have number {phone}", False


def contact_search(criteria, address_book):
	name = Record(criteria)
	result = address_book.find(name)
	if result is not None:
		return result
	return None


def number_search(criteria, address_book):
	try:
		result = []
		for name, phone in address_book.data.items():
			for record in phone:
				numbers = ([phone.value for phone in record.phones])
				if criteria in numbers:
					result.append(f'{name}: {criteria}')
		return result
	except ValueError:
		print('I can\'t find this')


def show_all_contacts(address_book):
	if not address_book.data:
		return "No contacts available"

	result = []
	for name, records in address_book.data.items():
		for record in records:
			phone_numbers = [phone.value for phone in record.phones]
			result.append(f"{name}: {', '.join(phone_numbers)}")

	return "\n".join(result)


command_actions = {
	"hello": hello_command,
	"show": show_all_command,
	"good": exit_command,
	"close": exit_command,
	"exit": exit_command,
	"add": add_command,
	"edit": edit_command,
	"remove": remove_command,
	"find": search_command
}


@input_error
def main():
	address_book = AddressBook()

	while True:
		command = input("Enter a command: ").strip().lower()
		main_command = command.split()[0]

		if main_command in command_actions:
			action = command_actions[main_command]
			if main_command in ['hello', 'show', 'good', 'close', 'exit']:
				process = action(address_book)
				if process:
					break
			else:
				action(address_book, command)
		else:
			print("Invalid command")


if __name__ == "__main__":
	main()
