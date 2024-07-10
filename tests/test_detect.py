'''
This file is a part of 'LngDetectoR', a tool to detect programming languages in a directory.
It contains the implementation of the function 'detect_language' which determines
the programming language of a given file based on its MIME type and extension. It uses Python's magic library for this.
The 'mime_to_language' dictionary is used to map certain MIME types to their corresponding languages.
'''
   }

import os
from lngdetector.detect import detect_language, count_lines_of_code

def test_mime_type_detection():
    curr_dir = os.getcwd()
    assert detect_language(curr_dir + "/setup.py") == 'Python'
