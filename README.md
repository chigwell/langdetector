[![PyPI version](https://badge.fury.io/py/LngDetectoR.svg)](https://badge.fury.io/py/LngDetectoR)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/lngdetector)](https://pepy.tech/project/lngdetector)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# LngDetectoR

LngDetectoR is a Python tool designed to analyze directories and detect the programming languages used within files. It generates a comprehensive report detailing the count of files, lines of code, and the percentage of each language present.

## Installation

To install LngDetectoR, you can use pip:

```bash
pip install LngDetectoR
```

## Usage

### As a Command Line Tool

LngDetectoR can be utilized directly from the command line. Basic usage is as follows:

```bash
lngdetector --directory <path-to-directory>
```

- `--directory`: Specifies the directory to analyze. If not specified, it defaults to the current working directory.

### As a Python Module

LngDetectoR can also be used within your Python scripts.

Example:

```python
from lngdetector.detect import generate_report

# Generate a report for the specified directory
report = generate_report('/path/to/your/project')

# Display the report in a pretty table format
report.print_pretty_table()

# Retrieve data for a specific language
python_data = report.get_language_data('Python')
print(f"Python files: {python_data['count']}, lines of code: {python_data['lines']}")
```

## Output Example

When you run LngDetectoR, it generates a table with the detected languages, file counts, lines of code, and their percentage contributions. Here's an example of what the output might look like:

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

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/langdetector/issues) for a list of proposed features (and known issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
