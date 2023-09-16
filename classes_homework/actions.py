from classes_homework.classes import Record


def add_contact(name, number, address_book):
	if name in address_book.data:
		result = add_to_contact(name, number, address_book)
		return result
	record = Record(name)
	if not record.add_phone(number):
		return 'Invalid phone number'
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