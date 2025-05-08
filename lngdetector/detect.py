import os
import magic
import argparse
from collections import defaultdict
from .report import Report
from .mime_lang import mime_to_language
from .extension_lang import extension_to_language


def count_lines_of_code(file_path):
    """Count the number of lines in a file."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return None


def detect_language(file_path):
    """Detect the programming language of a file based on its MIME type and extension."""
    try:
        mime_type = magic.from_file(file_path, mime=True)
        if mime_type in mime_to_language:
            return mime_to_language[mime_type]
        if file_path.endswith(".sample") and ".git/hooks/" in file_path:
            return "Git Hook Script"
        return extension_to_language.get(os.path.splitext(file_path)[1], "Unknown")
    except Exception:
        return None


def analyze_directory(directory):
    """Analyze all files in the given directory recursively and generate a report."""
    languages = defaultdict(lambda: {"count": 0, "lines": 0})
    total_files = 0
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            lines = count_lines_of_code(file_path)
            total_lines += lines or 0
            language = detect_language(file_path)
            languages[language]["count"] += 1
            languages[language]["lines"] += lines or 0

    return languages, total_files, total_lines


def generate_report(directory):
    """Generate a report for the specified directory."""
    languages, total_files, total_lines = analyze_directory(directory)
    return Report(languages, total_files, total_lines)


def get_mime_types():
    """Return a list of all MIME types."""
    return list(mime_to_language.keys())


def main():

    parser = argparse.ArgumentParser(description="Language Detection in a Directory.")
    parser.add_argument("--directory", type=str, help="Directory to analyze", default=os.getcwd())
    args = parser.parse_args()

    report = generate_report(args.directory)
    report.print_pretty_table()

    # Example usage
    # python_data = report.get_language_data('Python')
    # print(f"Python files: {python_data['count']}, lines of code: {python_data['lines']}")


if __name__ == "__main__":
    main()
