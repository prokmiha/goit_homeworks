from setuptools import setup, find_packages

setup(
    name='folder_cleaner_5',
    version='1.0.0',
    description="A tool for classifying and moving files",
    author='Misha',
    author_email='prokmiha@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'folder_cleaner = folder_cleaner_5.homework_module_5:main'
        ]
    },
)
