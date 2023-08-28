def input_error(func):
	def wrapper(*args, **kwargs):
		command_parts = args[1].split()
		try:
			return func(*args, **kwargs)
		except ValueError:
			if len(command_parts) == 1:
				return "Give me name and phone please"
			elif len(command_parts) == 2:
				return """
Input format:

add [name] [phone]
change [name] phone
phone [name]"""

		except KeyError:
			return "Wrong name"

	return wrapper


@input_error
def add_contact(contacts, command):
	_, name, phone = command.split(" ", 2)
	contacts[name] = phone
	return "Contact added successfully"


@input_error
def change_phone(contacts, command):
	_, name, phone = command.split(" ", 2)
	if name in contacts:
		contacts[name] = phone
		return "Phone number updated"
	else:
		raise KeyError


def get_phone(contacts, command):
	_, name = command.split(" ", 1)
	if name in contacts:
		return name, contacts[name]
	else:
		raise KeyError


def show_all_contacts(contacts):
	if not contacts:
		return "No contacts available"
	return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


# @input_error
def main():
	contacts = {}

	while True:
		command = input("Enter a command: ").strip().lower()

		if command == "hello":
			print("How can I help you?")
		elif command.startswith("add"):
			result = add_contact(contacts, command)
			print(result)

		elif command.startswith("change"):
			result = change_phone(contacts, command)
			print(result)
		elif command.startswith("phone"):
			try:
				result = get_phone(contacts, command)
				print(f"{result[0]}'s phone number is {result[1]}")
			except KeyError:
				print("Contact not found")
		elif command == "show all":
			result = show_all_contacts(contacts)
			print(result)
		elif command in ("good bye", "close", "exit"):
			print("Good bye!")
			break
		else:
			print("Invalid command")


if __name__ == "__main__":
	main()
