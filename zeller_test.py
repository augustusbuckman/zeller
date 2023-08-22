import os.path
import sys
from unittest import TestCase

from easter_date import main
from tud_test_base import *

def test_zeller():
    try:
        exists = os.path.exists("zeller.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input(['April'])
    set_keyboard_input([1])
    set_keyboard_input([1999])
    main()
    output = get_display_output()
    assert output == [
        "Enter the month (for example, January, February, etc.): ",
        "Enter the day (an integer): ",
        "Enter the year (an integer): ",
        "The day of the week is Thursday."
    ]