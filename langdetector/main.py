import os
import magic
from prettytable import PrettyTable
from collections import defaultdict

class Report:
    def __init__(self, languages, total_files, total_lines):
        self.languages = languages
        self.total_files = total_files
        self.total_lines = total_lines

    def print_pretty_table(self):
        table = PrettyTable()
        table.field_names = ["Language", "File Count", "Lines of Code", "Percentage"]

        sorted_languages = sorted(self.languages.items(), key=lambda x: x[1]['lines'], reverse=True)

        for language, data in sorted_languages:
            percentage = (data['lines'] / self.total_lines) * 100 if self.total_lines > 0 else 0
            table.add_row([language, data['count'], data['lines'], f'{percentage:.2f}%'])

        print(f"Total files: {self.total_files}")
        print(f"Total lines of code: {self.total_lines}")
        print(table)

    def get_language_data(self, language):
        return self.languages.get(language, {'count': 0, 'lines': 0})

    def get_total_files(self):
        return self.total_files

def count_lines_of_code(file_path):
    """Count the number of lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception:
        return None

def detect_language(file_path):
    """Detect the programming language of a file based on its MIME type and extension."""
    try:
        mime_type = magic.from_file(file_path, mime=True)
        mime_to_language = {
            'application/x-python-code': 'Python',
            'application/javascript': 'JavaScript',
            'text/html': 'HTML',
            'text/css': 'CSS',
            'text/markdown': 'Markdown',
            'application/json': 'JSON',
            'text/plain': 'Text',
            'application/xml': 'XML',
            'application/x-yaml': 'YAML',
            'application/x-shellscript': 'Shell',
            'application/x-bat': 'Batch',
            'application/x-powershell': 'PowerShell',
            'text/x-java-source': 'Java',
            'text/x-c': 'C',
            'text/x-c++': 'C++',
            'text/x-csharp': 'C#',
            'text/x-go': 'Go',
            'application/x-httpd-php': 'PHP',
            'application/x-ruby': 'Ruby',
            'text/rust': 'Rust',
            'text/x-swift': 'Swift',
            'text/x-kotlin': 'Kotlin',
            'text/x-clojure': 'Clojure',
            'text/x-scala': 'Scala',
            'text/x-perl': 'Perl',
            'application/x-julia': 'Julia',
            'text/x-r-source': 'R',
            'application/dart': 'Dart',
            'text/x-lua': 'Lua',
            'text/coffeescript': 'CoffeeScript',
            'text/x-vb': 'Visual Basic',
            'application/typescript': 'TypeScript',
            'text/x-haskell': 'Haskell',
            'text/x-erlang': 'Erlang',
            'application/x-elixir': 'Elixir',
            'application/x-elm': 'Elm',
            'text/x-pascal': 'Pascal',
            'text/x-lisp': 'Lisp',
            'text/x-scheme': 'Scheme',
            'text/x-common-lisp': 'Common Lisp',
            'text/x-ocaml': 'OCaml',
            'text/x-fsharp': 'F#',
            'text/x-coq': 'Coq',
            'application/x-isabelle': 'Isabelle',
            'application/x-racket': 'Racket',
        }
        extension_to_language = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.html': 'HTML',
            '.css': 'CSS',
            '.md': 'Markdown',
            '.json': 'JSON',
            '.txt': 'Text',
            '.xml': 'XML',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.sh': 'Shell',
            '.bat': 'Batch',
            '.ps1': 'PowerShell',
            '.java': 'Java',
            '.c': 'C',
            '.cpp': 'C++',
            '.h': 'C++',
            '.cs': 'C#',
            '.go': 'Go',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.rs': 'Rust',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.clj': 'Clojure',
            '.scala': 'Scala',
            '.pl': 'Perl',
            '.jl': 'Julia',
            '.r': 'R',
            '.dart': 'Dart',
            '.lua': 'Lua',
            '.coffee': 'CoffeeScript',
            '.vb': 'Visual Basic',
            '.ts': 'TypeScript',
            '.hs': 'Haskell',
            '.erl': 'Erlang',
            '.ex': 'Elixir',
            '.elm': 'Elm',
            '.pas': 'Pascal',
            '.lisp': 'Lisp',
            '.scm': 'Scheme',
            '.cl': 'Common Lisp',
            '.ml': 'OCaml',
            '.fs': 'F#',
            '.fsi': 'F#',
            '.v': 'Coq',
            '.thy': 'Isabelle',
            '.ml4': 'OCaml',
            '.rkt': 'Racket',
            '.exs': 'Elixir',
            '.pyc': 'Python Bytecode',
            '.iml': 'PyCharm Project File',
        }
        # First try to detect based on MIME type
        if mime_type in mime_to_language:
            return mime_to_language[mime_type]
        # Special handling for Git hook scripts
        if file_path.endswith('.sample') and '.git/hooks/' in file_path:
            return 'Git Hook Script'
        # Fallback to extension if MIME type is not conclusive
        return extension_to_language.get(os.path.splitext(file_path)[1], 'Unknown')
    except Exception:
        return None


def analyze_directory(directory):
    """Analyze all files in the given directory recursively and generate a report."""
    languages = defaultdict(lambda: {'count': 0, 'lines': 0})
    total_files = 0
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            lines = count_lines_of_code(file_path)
            total_lines += lines or 0
            language = detect_language(file_path)
            languages[language]['count'] += 1
            languages[language]['lines'] += lines or 0
            #if language == 'Unknown':
            #    print(file_path)

    return languages, total_files, total_lines

def generate_report(directory):
    """Generate a report for the specified directory."""
    languages, total_files, total_lines = analyze_directory(directory)
    return Report(languages, total_files, total_lines)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Language Detection in a Directory.')
    parser.add_argument('--directory', type=str, help='Directory to analyze', default=os.getcwd())
    args = parser.parse_args()

    report = generate_report(args.directory)
    report.print_pretty_table()

    # Example usage
    # python_data = report.get_language_data('Python')
    # print(f"Python files: {python_data['count']}, lines of code: {python_data['lines']}")

if __name__ == '__main__':
    main()
