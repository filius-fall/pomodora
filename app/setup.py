from setuptools import setup,find_packages

setup(
    name = 'pomodora',
    version = '0.1',
    py_modules = ['pomodora'],
    install_requires = ['Click'],
    entry_points = '''
        [console_scripts]
        pomodora = pomodora:timer
        pp = pomodora:csv_reader
    
     ''',
)