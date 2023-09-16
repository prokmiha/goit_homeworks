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