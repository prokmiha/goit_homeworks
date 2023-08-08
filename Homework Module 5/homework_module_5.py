import os
import re
import shutil
from transliterate import translit


def contains_cyrillic(text):
	return bool(re.search('[а-яА-Я]', text))


def normalize(name):
	if contains_cyrillic(name):
		name = translit(name, reversed=True)
	if any(char.isupper() for char in name):
		name = name.lower()
	name = name.replace(' ', '_')

	return name


def classify_and_move_file(file_path):
	name, extension = os.path.splitext(os.path.basename(file_path))
	normalized_name = normalize(name) + extension

	file_ext = extension[1:].upper()
	if file_ext in ('JPEG', 'PNG', 'JPG', 'SVG'):
		target_folder = 'images'
	elif file_ext in ('AVI', 'MP4', 'MOV', 'MKV'):
		target_folder = 'video'
	elif file_ext in ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'):
		target_folder = 'documents'
	elif file_ext in ('MP3', 'OGG', 'WAV', 'AMR'):
		target_folder = 'audio'
	elif file_ext in ('ZIP', 'GZ', 'TAR'):
		target_folder = 'archives'
		target_path = os.path.join(os.path.dirname(file_path), target_folder)
		archive_folder_name = os.path.splitext(os.path.basename(file_path))[0]
		archive_folder_path = os.path.join(target_path, archive_folder_name)
		os.makedirs(archive_folder_path, exist_ok=True)
		shutil.unpack_archive(file_path, archive_folder_path)
		os.remove(file_path)
		return

	else:
		target_folder = 'unknown'

	target_path = os.path.join(os.path.dirname(file_path), target_folder)
	os.makedirs(target_path, exist_ok=True)
	os.rename(file_path, os.path.join(target_path, normalized_name))


def process_folder(path):
	files = []
	folders = []

	for item in os.listdir(path):
		item_path = os.path.join(path, item)

		if os.path.isfile(item_path):
			files.append(item_path)
		elif os.path.isdir(item_path):
			folders.append(item_path)

	for file in files:
		classify_and_move_file(file)

	for folder in folders:
		folder_path = os.path.join(path, folder)
		process_folder(folder_path)
		if not os.listdir(folder_path):
			os.rmdir(folder_path)


def main():
	initial_path = 'E:/Other'
	process_folder(initial_path)


if __name__ == "__main__":
	main()
