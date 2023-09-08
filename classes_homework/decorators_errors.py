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
remove [name]
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


def input_error(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except MissedNameOrNumber as e:
			if len(args[1].split()) == 1:
				return e.missed_info()
			elif len(args[1].split()) == 2:
				return e.wrong_format()
		except UnknownContact as e:
			return e.unknown_contact()
		except UnknownCommandError as e:
			return e.unknown_command()
		except ContactNotFoundError as e:
			return e.comtact_not_found()
		except MissedNameError as e:
			return e.missed_name()
		except MissedCriteriaError as e:
			return e.missed_criteria()
		except KeyboardInterrupt:
			print('\nGood buy!')

	return wrapper
