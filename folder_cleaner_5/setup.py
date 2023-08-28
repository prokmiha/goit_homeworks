from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='folder_cleaner_5',
    version='0.1.2',
    description="A tool for classifying and moving files",
    author='Misha',
    author_email='prokmiha@gmail.com',
    packages=find_packages(),
    install_requires=[
        'transliterate',
    ],
    setup_requires=[
        'transliterate',
    ],
    entry_points={
        'console_scripts': [
            'folder_cleaner = folder_cleaner_5.folder_cleaner:main'
        ]
    },
)
