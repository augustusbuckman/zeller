import unittest
import zeller
import tud_test_base as tud


def expected_weekday(month, day, year):

    if month == "January":
        month_number = 13
        year -= 1
    elif month == "February":
        month_number = 14
        year -= 1
    elif month == "March":
        month_number = 3
    elif month == "April":
        month_number = 4
    elif month == "May":
        month_number = 5
    elif month == "June":
        month_number = 6
    elif month == "July":
        month_number = 7
    elif month == "August":
        month_number = 8
    elif month == "September":
        month_number = 9
    elif month == "October":
        month_number = 10
    elif month == "November":
        month_number = 11
    else:
        month_number = 12

    variation_in_days_per_month = (13 * (month_number + 1)) // 5

    leap_year_days = (year // 4) + (year // 400)

    century_days = year // 100

    total_days = (
        day
        + variation_in_days_per_month
        + year
        + leap_year_days
        - century_days
    )

    day_of_week = total_days % 7

    if day_of_week == 0:
        return "Saturday"
    elif day_of_week == 1:
        return "Sunday"
    elif day_of_week == 2:
        return "Monday"
    elif day_of_week == 3:
        return "Tuesday"
    elif day_of_week == 4:
        return "Wednesday"
    elif day_of_week == 5:
        return "Thursday"
    else:
        return "Friday"


class TestZeller(unittest.TestCase):

    def verify_case(self, month, day, year):

        tud.set_keyboard_input(
            [month, str(day), str(year)]
        )

        zeller.main()

        output = tud.get_display_output()

        expected = [
            "Enter the month (for example, January, February, etc.): ",
            "Enter the day (an integer): ",
            "Enter the year (an integer): ",
            f"The day of the week is {expected_weekday(month, day, year)}."
        ]

        self.assertEqual(output, expected)

    # Assignment examples

    def test_assignment_example(self):
        self.verify_case("April", 1, 1999)

    def test_example_1(self):
        self.verify_case("July", 31, 1929)

    def test_example_2(self):
        self.verify_case("January", 3, 1988)

    def test_example_3(self):
        self.verify_case("March", 1, 2000)

    # Additional tests

    def test_january(self):
        self.verify_case("January", 15, 2005)

    def test_february(self):
        self.verify_case("February", 28, 2020)

    def test_march(self):
        self.verify_case("March", 15, 2010)

    def test_april(self):
        self.verify_case("April", 10, 1998)

    def test_may(self):
        self.verify_case("May", 20, 2012)

    def test_june(self):
        self.verify_case("June", 30, 1985)

    def test_july(self):
        self.verify_case("July", 4, 1776)

    def test_august(self):
        self.verify_case("August", 25, 1995)

    def test_september(self):
        self.verify_case("September", 1, 2001)

    def test_october(self):
        self.verify_case("October", 31, 2024)

    def test_november(self):
        self.verify_case("November", 11, 2011)

    def test_december(self):
        self.verify_case("December", 25, 2025)

    # Bulk tests to prevent hardcoding

    def test_multiple_dates(self):

        dates = [
            ("January", 1, 1900),
            ("February", 29, 2000),
            ("March", 15, 1950),
            ("April", 30, 1975),
            ("May", 12, 1988),
            ("June", 8, 1999),
            ("July", 21, 2005),
            ("August", 17, 2017),
            ("September", 9, 2021),
            ("October", 13, 2030),
            ("November", 5, 2040),
            ("December", 31, 2099)
        ]

        for month, day, year in dates:
            with self.subTest(month=month, day=day, year=year):
                self.verify_case(month, day, year)


if __name__ == "__main__":
    unittest.main()
