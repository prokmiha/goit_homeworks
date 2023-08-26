

def worktime_decorator(need_print: bool):
	def inner(func):
		def wrapper(*args, **kwargs):
			from time import time

			start = time()
			func(*args, **kwargs)
			end = time()
			total_time = (end - start)
			if need_print:
				print(f'Def {func.__name__} finish her work in {total_time}sec')
			return total_time

		return wrapper

	return inner


def log_decorator(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		print(f"{args}\ndef {func.__name__}" )
		return result

	return wrapper
