import os
from langdetector.main import generate_report


report = generate_report(os.getcwd())
report.print_pretty_table()
python_data = report.get_language_data('Python')
print(f"Python files: {python_data['count']}, lines of code: {python_data['lines']}")