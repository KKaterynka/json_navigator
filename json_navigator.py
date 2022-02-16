"""
Module that gives you an opportunity
to browse through .json file.
"""

import sys
import os
import pandas as pd
import json


def greeting():
    """
    Function that greets the user.
    """
    print("Hello, what's your name?")
    user_name = input(">>> ")
    # check if user entered name
    while user_name == "":
        print("Please, type in your name!")
        user_name = input(">>> ")
    print(f"So, {user_name}, I guess you are here to browse through your .json file")
    print(f"{user_name}, please type in the correct path to your .json file")
    return user_name


def get_path():
    """
    Function that extracts a path.
    Checks if it exists.
    """
    while True:
        path = input(">>> ")
        # check if user path exists
        if os.path.exists(path):
            return path
        print('Wrong path! Try again.')


def get_file():
    """
    Function that extract information
    from file.
    """

    # greet the user
    greeting()

    # extract data from .json file
    path = get_path()
    with open(path, mode='r', encoding='utf-8') as fdata:
        data = json.load(fdata)
    return data


def key_validation(validation_range):
    """
    General validator for user inputs.
    """
    user_key = input(">>> ")
    # check if user answer is correct
    while user_key.strip() not in validation_range:
        print("Wrong answer. Try again!")
        user_key = input(">>> ")

    return user_key.strip()


def user_table(raw_data, meta_data):
    """
    Function that creates a full dataset
    in a table form.
    """

    # setting features of table
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    return pd.json_normalize(raw_data,
                             meta=meta_data)


def json_navi():
    """
    Main function.
    Navigates user through .json file.
    """
    data = get_file()

    print("Do you want to see full dataset or some element?")
    print('Please, just type in "dataset" or "element".')
    what_display = key_validation(["dataset", "element"])

    if what_display == "element":

        while True:
            if isinstance(data, list):

                print('The current object is a list.', f"So, which exactly element do you want to see?\n"
                      , f"(Type in the number from 0 to {len(data) - 1})")
                user_obj = int(input(">>> "))
                # checking if user number is in range
                while user_obj not in range(0, len(data)):
                    print("Element out of range! Try again.")
                    user_obj = int(input(">>> "))
                # adding to history of browsing
                data = data[user_obj]

            elif isinstance(data, dict):
                keys = list(data.keys())
                print('The current object is a list.', f"\nNumber of elements in this dictionary {len(keys)}:")
                for i in keys:
                    print("        * " + i)
                print("Choose right for you.")
                user_key = key_validation(keys)
                data = data[user_key]

            else:
                print('Here is required information:')
                print(data)
                break

    else:
        # creating full dataset
        if len(data) > 1 and isinstance(data, dict):
            # check if there are more than 1 dictionary
            keys = list(data.keys())
            print("This dictionary consists of these keys: ")
            for i in keys:
                print("        * " + i)
            print("Choose for which you want get full dataset.")
            user_key = key_validation(keys)
            raw_data = data[user_key]
            if isinstance(raw_data, list):
                result_table = user_table(raw_data, list(raw_data[0].keys()))
            else:
                result_table = user_table(raw_data, list(raw_data.keys()))
            print(result_table)
        else:
            try:
                raw_data = data
                result_table = user_table(raw_data, list(raw_data[0].keys()))
                print(result_table)
            except:
                print("Sorry, can not display for these type of object")
                sys.exit()

    print("\nGoodbye, JSON explorer!")


json_navi()
