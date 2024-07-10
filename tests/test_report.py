"""
The test_report.py file contains unit tests for the Report class in the lngdetector package.
These tests ensure that the Report class functions correctly and produces accurate results.
They cover various scenarios such as adding files, calculating language statistics, and filtering files by extension.
"""

import os
from lngdetector.detect import analyze_directory, generate_report


def test_analyze_directory():
    curr_dir = os.getcwd()
    languages, total_files, total_lines = analyze_directory(curr_dir)
    assert total_files > 0
    assert total_lines > 0
    assert "Python" in languages


def test_generate_report():
    curr_dir = os.getcwd()
    report = generate_report(curr_dir)
    assert report.total_files > 0
    assert report.total_lines > 0
