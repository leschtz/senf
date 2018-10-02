from setuptools import setup

setup(
    name='senf - student environment',
    version='0.2',
    py_modules=['senf'],
    install_requires=[
            'click',
            'colorama',
            ],
    entry_points='''
        [console_scripts]
        senf=senf:cli
        ''',
        )
