from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='LngDetectoR',
    version='0.15',
    packages=find_packages(),
    install_requires=[
        'prettytable',
        'python-magic',
    ],
    entry_points={
        'console_scripts': [
            'lngdetector = lngdetector.main:main',
        ],
    },
    author='Evgenii Evstafev',
    author_email='chigwel@gmail.com',
    description='A tool to detect programming languages in a directory.',
    keywords='language detection programming report',
    url='https://github.com/chigwell/langdetector',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
