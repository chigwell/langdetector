[![PyPI version](https://badge.fury.io/py/LngDetectoR.svg)](https://badge.fury.io/py/LngDetectoR)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/lngdetector)](https://pepy.tech/project/lngdetector)

# LngDetectoR

LngDetectoR is a Python tool designed to analyze directories and detect the programming languages used in the files. It provides a comprehensive report including the count of files, lines of code, and the percentage of each language present.

## Installation

To install LngDetectoR, you can use pip:

```bash
pip install LngDetectoR
```

## Usage

### As a Command Line Tool

You can use LngDetectoR directly from the command line. The basic usage is as follows:

```bash
lngdetector --directory <path-to-directory>
```

- `--directory`: Specify the directory you want to analyze. If not specified, it uses the current working directory.

### As a Python Module

LngDetectoR can also be used as a Python module in your scripts.

Example:

```python
from lngdetector.main import generate_report

# Generate a report for the current directory
report = generate_report('/path/to/your/project')

# Print the pretty table
report.print_pretty_table()

# Get data for a specific language
python_data = report.get_language_data('Python')
print(f"Python files: {python_data['count']}, lines of code: {python_data['lines']}")
```

## Output Example

When you run LngDetectoR, it outputs a table with the detected languages, the count of files, lines of code, and the percentage. Here is an example output:

```
Total files: 50
Total lines of code: 1200
+------------+------------+---------------+------------+
|  Language  | File Count | Lines of Code | Percentage |
+------------+------------+---------------+------------+
| Python     |     20     |      500      |   41.67%   |
| JavaScript |     15     |      350      |   29.17%   |
| HTML       |     10     |      200      |   16.67%   |
| CSS        |      5     |      150      |   12.50%   |
+------------+------------+---------------+------------+
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/langdetector/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)

