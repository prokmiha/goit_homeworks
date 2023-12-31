import os

from classes_homework.actions import add_contact, show_all_contacts, remove_contact, \
	contact_search, remove_only_number, edit_contact, number_search, add_birthday_to_contact, when_birthday, find_all_matches
from classes_homework.classes import AddressBook
from classes_homework.decorators_errors import input_error, Errors


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


# @input_error
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


@input_error
def bd_command(address_book, command):
	try:
		_, name, birthday = command.split()
	except ValueError:
		raise Errors.IncorrectEditCommand
	result = add_birthday_to_contact(name, birthday, address_book)
	print(result)


@input_error
def when_bd_command(address_book, command):
	try:
		_, name = command.split()
	except:
		raise Errors.MissedNameError
	result = when_birthday(name, address_book)
	print(result)


def find_all_command(address_book, command):
	try:
		_, query = command.split()
	except:
		raise Errors.MissedNameError
	find_all_matches(query, address_book)


def hello_command(_):
	print('Hello, how can I help you?')


def exit_command(_):
	print('Good buy!')
	return True


command_actions = {
	"hello": hello_command,
	"show": show_all_command,
	"good": exit_command,
	"close": exit_command,
	"exit": exit_command,
	"add": add_command,
	"birthday": bd_command,
	"when": when_bd_command,
	"edit": edit_command,
	"remove": remove_command,
	"find": search_command,
	"all": find_all_command
}


@input_error
def main():
	if not os.path.exists("address_book.json"):
		address_book = AddressBook()
		address_book.save_to_file("address_book.json")
	else:
		address_book = AddressBook()
		address_book.load_from_file("address_book.json")

	while True:
		command = input("Enter a command: ").strip().lower()
		main_command = command.split()[0]

		if main_command in command_actions:
			action = command_actions[main_command]
			if main_command in ['hello', 'show', 'good', 'close', 'exit']:
				process = action(address_book)
				if process:
					address_book.save_to_file("address_book.json")
					break
			else:
				action(address_book, command)
				address_book.save_to_file("address_book.json")
		else:
			print("Invalid command")


if __name__ == "__main__":
	main()
