import os
from lngdetector.detect import detect_language


def test_mime_type_detection():
    curr_dir = os.getcwd()
    assert detect_language(curr_dir + "/setup.py") == "Python"
