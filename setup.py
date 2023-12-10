from setuptools import setup, find_packages

setup(
    name='LangDetectoR',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'prettytable',
        'python-magic',
    ],
    entry_points={
        'console_scripts': [
            'langdetector = langdetector.main:main',
        ],
    },
    author='Evgenii Evstafev',
    author_email='chigwel@gmail.com',
    description='A tool to detect programming languages in a directory.',
    keywords='language detection programming report',
    url='https://github.com/chigwell/langdetector',  # Replace with your actual URL
)
