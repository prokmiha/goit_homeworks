from classes_homework.classes import Record


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
	result = address_book.delete(name)
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
			if hasattr(record, 'birthday'):
				birthday = record.birthday.value
				result.append(f"{name}: {', '.join(phone_numbers)}\n{birthday}")
			else:
				result.append(f"{name}: {', '.join(phone_numbers)}")

	return "\n".join(result)


def add_birthday_to_contact(name, birthday, address_book):
	if name in address_book.data:
		records = address_book.data[name]
		for record in records:
			if not hasattr(record, 'birthday'):
				record.add_birthday(birthday)
			else:
				record.birthday.value = birthday
		return f"Birthday added/updated for {name}"
	else:
		return f'Contact {name} not found'


def when_birthday(name, address_book):
	if name in address_book.data:
		records = address_book.data[name]
		for record in records:
			result = record.days_to_birthday()
			if isinstance(result, int):
				return f"There is {result} days to {name}'s birthday"
	else:
		return 'Contact not found'


def find_all_matches(query, address_book):
	matching_contacts = address_book.find_all_matches(query)

	if matching_contacts:
		print("Matching contacts:")
		for contact in matching_contacts:
			print(contact.name.value)
			for phone in contact.phones:
				print(f"Phone: {phone.value}")
			if hasattr(contact, 'birthday'):
				print(f"Birthday: {contact.birthday.value}")
			print()
	else:
		print("No matching contacts found.")
