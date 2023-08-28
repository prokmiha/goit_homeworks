from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
	today = date.today()
	week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	final = {day: [] for day in week_days}

	for user in users:
		name = user['name'].split()[0]
		birthday = user['birthday']
		next_bd = birthday.replace(year=today.year)

		if next_bd < today:
			next_bd = next_bd.replace(year=today.year + 1)

		days_to_bd = (next_bd - today).days
		day_name = next_bd.strftime('%A')

		if days_to_bd <= 7:
			if day_name in week_days:
				final[day_name].append(name)
			else:
				final['Monday'].append(name)

	final = {day: result for day, result in final.items() if result}

	return final


if __name__ == "__main__":
	users = [
		{"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
	]

	result = get_birthdays_per_week(users)
	print(result)
	# Виводимо результат
	for day_name, names in result.items():
		print(f"{day_name}: {', '.join(names)}")
