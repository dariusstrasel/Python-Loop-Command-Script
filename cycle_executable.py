"""
Title: Python Loop Command/Script
Objective: This script is meant to loop an executable command, shell script, or python file for specified intervals of
time, until cancelled via keyboard interrupt.
Author:: Darius Strasel
"""

from sys import argv
import os
import time


def has_three_input_arguments() -> bool:
    if len(argv) == 3:
        return True
    return False


def input_string_is_valid(argument_input):
    """Returns True if input is not a number."""
    try:
        int(argument_input)
        return False
    except ValueError:
        return True


def input_number_is_valid(argument_input):
    """Returns True if the argument_input can cast an integer."""
    try:
        int(argument_input)
        return True
    except (TypeError, ValueError):
        return False


def is_python_file(argument_input):
    """Returns True if the last two character of a string are 'py'"""
    if argument_input[len(argument_input)-2:len(argument_input)] == 'py':
        return True
    return False


def process_loop(timing):
    """Opens a sub-shell based on an input command for 'timing' intervals."""
    if input_number_is_valid(timing):
        timing_as_integer = int(timing)
        print("Looping command '%s' every '%s' seconds. Press 'CTRL' + 'C' to stop execution." % (argv[1], timing))
        while True:
            try:
                if is_python_file(argv[1]):
                    os.system('python ' + str(argv[1]))
                else:
                    os.system(argv[1])
                time.sleep(timing_as_integer)
            except KeyboardInterrupt:
                print("Exiting program loop.")
                exit()


def main():
    """Check if input type is correct before calling functions."""
    expected_argument_format = "cycle_executable.py [command or python file] (string) [Loop Time in seconds] (integer)"
    print("Arguments: %s" % argv)
    if has_three_input_arguments():
        if input_string_is_valid(argv[1]) and input_number_is_valid(argv[2]):
            process_loop(argv[2])
        print("One of the arguments were caught as invalid. Ensure the following is correct:")
        print(expected_argument_format)
    print("Invalid number of arguments: '%s': There should be 3 total." % len(argv))
    print(expected_argument_format)


if __name__ == "__main__":
    main()
