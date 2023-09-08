from classes_homework.actions import add_contact, edit_contact, add_to_contact, show_all_contacts, remove_contact, \
	contact_search
from classes_homework.classes import AddressBook
from classes_homework.decorators_errors import MissedNameOrNumber, input_error, ContactNotFoundError, MissedNameError


@input_error
def add_command(address_book, command):
	try:
		_, name, number = command.split()
	except:
		raise MissedNameOrNumber
	result = add_contact(name, number, address_book)
	print(result)


@input_error
def change_commands(address_book, contact):
	try:
		_, name, number = contact.split()
	except:
		raise MissedNameOrNumber

	if name in address_book.data:
		update_info = input(
			'If you want to change current contact, please type "edit"\nIf you want to add another number, please type "add"\n')
		if update_info == 'edit':
			result = edit_contact(name, number, address_book)
			print(result)
		elif update_info == 'add':
			result = add_to_contact(name, number, address_book)
			print(result)
		else:
			print("Invalid command. Please type 'edit' or 'add'.")
	else:
		raise ContactNotFoundError


def show_all_command(address_book):
	result = show_all_contacts(address_book)
	print(result)


@input_error
def remove_command(address_book, command):
	try:
		_, name = command.split()
	except:
		raise MissedNameError
	if name in address_book.data:
		result = remove_contact(name, address_book)
		print(result)
	else:
		raise ContactNotFoundError


def search_command(address_book, criteria):
	try:
		_, value = criteria.split()
	except:
		raise MissedNameError
	result = contact_search(value, address_book)
	print(result)

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
	"change": change_commands,
	"remove": remove_command,
	"search": search_command
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
