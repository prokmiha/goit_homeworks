from setuptools import setup, find_packages

setup(
    name='folder_cleaner_5',
    version='0.1.7',
    description="A tool for classifying and moving files",
    author='Misha',
    author_email='prokmiha@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'transliterate>=1.0.0',  # Указываем диапазон версий
        'six>=1.10.0',  # Пример для другой зависимости
    ],

    entry_points={
        'console_scripts': [
            'folder_cleaner = folder_cleaner_5.homework_module_5:main'
        ]
    },
)
