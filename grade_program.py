#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 01, 2023
# This function, calc_mark, takes a level as input and returns the corresponding mark.


def calc_mark(level):
    mark = level  # Initialize mark with the user's input level

    # Check different level cases and assign corresponding marks
    if "-1" in level:
        mark = 50
    elif "1" == level:
        mark = 56
    elif "+1" == level:
        mark = 59
    elif "-2" == level:
        mark = 62
    elif "2" == level:
        mark = 66
    elif "+2" == level:
        mark = 69
    elif "-3" == level:
        mark = 72
    elif "3" == level:
        mark = 76
    elif "+3" == level:
        mark = 79
    elif "-4" == level:
        mark = 86
    elif "4" == level:
        mark = 94
    elif "+4" == level:
        mark = 100

    return mark  # Return the calculated mark


# This is the main function where the user inputs their level and the program calculates and prints the mark.
def main():
    user_level = input("Enter your level: ")  # Get user input for the level

    # Calculate and print the mark using the calc_mark function
    mark = calc_mark(user_level)
    print(f"Your mark is: {mark}% ")


if __name__ == "__main__":
    main()
