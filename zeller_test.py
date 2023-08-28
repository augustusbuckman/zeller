import os.path
import sys
from unittest import TestCase

from zeller import main
from tud_test_base import *
def test_zeller():
    try:
        exist = os.path.exists("zeller.py")
        assert exist == True
    except:
        sys.exit()

    set_keyboard_input(['April',1,1999])
    main()
    output = get_display_output()
    assert output == [
        "Enter the month (for example, January, February, etc.): ",
        "Enter the day (an integer): ",
        "Enter the year (an integer): ",
        "The day of the week is Thursday."
    ]