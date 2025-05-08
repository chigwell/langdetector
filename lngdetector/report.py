from prettytable import PrettyTable


class Report:
    def __init__(self, languages, total_files, total_lines):
        self.languages = languages
        self.total_files = total_files
        self.total_lines = total_lines

    def sort_languages(self):
        return sorted(self.languages.items(), key=lambda x: x[1]["lines"], reverse=True)

    def print_pretty_table(self):
        table = PrettyTable()
        table.field_names = ["Language", "File Count", "Lines of Code", "Percentage"]

        sorted_languages = self.sort_languages()

        for language, data in sorted_languages:
            percentage = (data["lines"] / self.total_lines) * 100 if self.total_lines > 0 else 0
            table.add_row([language, data["count"], data["lines"], f"{percentage:.2f}%"])

        print(f"Total files: {self.total_files}")
        print(f"Total lines of code: {self.total_lines}")
        print(table)

    def get_report(self):
        report = {}
        report["total_files"] = self.total_files
        report["total_lines"] = self.total_lines

        sorted_languages = self.sort_languages()
        for language, data in sorted_languages:
            percentage = (data["lines"] / self.total_lines) * 100 if self.total_lines > 0 else 0
            report[language] = {
                "count": data["count"],
                "lines": data["lines"],
                "percentage": f"{percentage:.2f}%",
            }

        return report

    def get_language_data(self, language):
        return self.languages.get(language, {"count": 0, "lines": 0})

    def get_total_files(self):
        return self.total_files
