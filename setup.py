from setuptools import setup

setup(
    name='senf - student environment',
    version='0.1',
    py_modules=['senf'],
    install_requires=[
            'click',
            ],
    entry_points='''
        [console_scripts]
        senf=senf:cli
        ''',
        )
