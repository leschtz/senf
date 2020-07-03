from setuptools import setup

setup(
    name='senf - student environment',
    author="Lukas Schuetz",
    author_email="leschtz@icloud.com",
    version='0.2',
    py_modules=['senf'],
    install_requires=[
            'click',
            'colorama',
            ],
    scripts=["senf.sh"],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        senf=senf:cli
        ''',
        )
