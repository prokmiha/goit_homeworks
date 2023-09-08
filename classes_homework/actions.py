from classes_homework.classes import Record


def add_contact(name, number, address_book):
	record = Record(name)
	record.add_phone_number(number)
	address_book.add_record(record)
	return "Contact added successfully"


def edit_contact(name, number, address_book):
	for record in address_book.data[name]:
		for phone in record.phones:
			phone.value = number
	return "Phone number updated"


def add_to_contact(name, number, address_book):
	for record in address_book.data[name]:
		record.add_phone_number(number)
	return "Phone number added"


def remove_contact(name, address_book):
	del address_book[name]
	return f"Contact {name} successfully removed"


def contact_search(criteria, address_book):
	for key, value in address_book.data.items():
		if criteria in key:
			contact = value[0]
			phones = ", ".join([phone.value for phone in contact.phones])
			return f"I found contact {key} with numbers: {phones}"
		for record in value:
			if any(criteria in phone.value for phone in record.phones):
				phones = ", ".join([phone.value for phone in record.phones])
				return f"I found contact {record.name.value} with numbers: {phones}"
	return 'Contact not found'


def show_all_contacts(address_book):
	if not address_book.data:
		return "No contacts available"

	result = []
	for name, records in address_book.data.items():
		for record in records:
			phone_numbers = [phone.value for phone in record.phones]
			result.append(f"{name}: {', '.join(phone_numbers)}")

	return "\n".join(result)
