def input_error(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except IndexError:
			if len(args[0]) == 1:
				return "Give me name and phone please"
			elif len(args[0]) == 2:
				return """
Input format:

add [name] [phone]
change [name] phone
phone [name]"""

		except KeyError:
			return "Wrong name"

	return wrapper


contacts = {}


@input_error
def add_contact(command):
	contacts[command[1]] = command[2]
	return "Contact added successfully"


@input_error
def change_phone(command):
	if command[1] in contacts:
		contacts[command[1]] = command[2]
		return "Phone number updated"
	else:
		raise KeyError


def get_phone(command):
	try:
		if command[1] in contacts:
			return command[1], contacts[command[1]]
	except:
		raise ValueError
	raise KeyError


def show_all_contacts():
	if not contacts:
		return "No contacts available"
	return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def hello_command():
	print("How can I help you?")


def add_command(contact_info):
	result = add_contact(contact_info)
	print(result)


def change_command(contact_info):
	result = change_phone(contact_info)
	print(result)


def phone_command(contact_info):
	try:
		result = get_phone(contact_info)
		print(f"{result[0]}'s phone number is {result[1]}")
	except KeyError:
		print("Contact not found")

	except ValueError:
		print("Please, write contact name")


def show_all_command():
	result = show_all_contacts()
	print(result)


def exit_command():
	print("Good bye!")
	return True


command_actions = {
	"hello": hello_command,
	"add": add_command,
	"change": change_command,
	"phone": phone_command,
	"show": show_all_command,
	"good": exit_command,
	"close": exit_command,
	"exit": exit_command
}


def main():
	while True:
		command = input("Enter a command: ").strip().lower().split()
		main_command = command[0]

		if main_command in command_actions:
			action = command_actions[main_command]
			if main_command in ['hello', 'show', 'good', 'close', 'exit']:
				process = action()
				if process:
					break
			else:
				action(command)
		else:
			print("Invalid command")


if __name__ == "__main__":
	main()
