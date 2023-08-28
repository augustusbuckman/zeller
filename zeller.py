# File: zeller.py
# Description: <A DESCRIPTION OF YOUR PROGRAM>
# Assignment Number: 3
#
# Name: <YOUR NAME>
# SID:  <YOUR EID>
# Email: <YOUR EMAIL>
# Grader: <YOUR GRADER'S NAME Carolyn OR Emma OR Ahmad>
# Slip days used this assignment: <#>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student. .

def main():
    month_name = input("Enter the month (for example, January, February, etc.): ")
    day = int(input("Enter the day (an integer): "))
    year = int(input("Enter the year (an integer): "))

    if month_name == "January":
        month_number = 13
    elif month_name == "February":
        month_number = 14
    elif month_name == "March":
        month_number = 3
    elif month_name == "April":
        month_number = 4
    elif month_name == "May":
        month_number = 5
    elif month_name == "June":
        month_number = 6
    elif month_name == "July":
        month_number = 7
    elif month_name == "August":
        month_number = 8
    elif month_name == "September":
        month_number = 9
    elif month_name == "October":
        month_number = 10
    elif month_name == "November":
        month_number = 11
    elif month_name == "December":
        month_number = 12

    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = year // 4 + year // 400
    century_days = year // 100
    total_days = day + variation_in_days_per_month + year + leap_year_days - century_days
    day_of_week = total_days % 7
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week_name = days_of_week[day_of_week]

    print("The day of the week is " + day_of_week_name + ".")


if __name__ == "__main__":
    main()