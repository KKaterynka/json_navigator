"""
Module that ONLY browses
through cats.json file
"""

import json
import pandas as pd
import fontstyle

# extracting data from .json file
with open('json_files/cats.json', 'r') as fdata:
    decoded_students = json.load(fdata)


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


def dictionary_parser(dict_obj):
    """
    Function to manimize code.
    Extracts keys from dictionary.
    """
    print(fontstyle.apply("""The current object is a dictionary.
        It consists of these keys:""", 'bold/Italic/purple'))
    for i in dict_obj.keys():
        print(fontstyle.apply("        * " + i, 'bold/Italic/purple'))

    print(fontstyle.apply("Please, write the full name of key!", 'bold/Italic/purple'))


def greeting():
    """
    Function that greets the user.
    """
    print(fontstyle.apply("Hello, what's your name?", 'bold/Italic/purple'))
    user_name = input(">>> ")
    # check if user entered name
    while user_name == "":
        print(fontstyle.apply("Please, type in your name!", 'bold/Italic/red/BLACK_BG'))
        user_name = input(">>> ")
    print(fontstyle.apply(f"So, {user_name}, I guess you are here to look at my .json file",
                          'bold/Italic/purple'))


def key_validation(validation_range):
    """
    General validator for user inputs.
    """
    user_key = input(">>> ")
    # check if user answer is correct
    while user_key.strip() not in validation_range:
        print(fontstyle.apply("Wrong answer. Try again!", 'bold/Italic/red/BLACK_BG'))
        user_key = input(">>> ")

    return user_key.strip()


def say_goodbye():
    """
    Function that says
    goodbye to user.
    """
    print(fontstyle.apply("Hope you got the needed information!", 'bold/Italic/red/BLACK_BG'))
    print(fontstyle.apply("Still, do you want to see the whole data?", 'bold/Italic/red/BLACK_BG'))
    print(fontstyle.apply('Just type in "yes" or "no"', 'bold/Italic/red/BLACK_BG'))
    user_ent = input(">>> ")
    if user_ent.lower().startswith("y"):
        raw_data = decoded_students["data"]
        result_table = user_table(raw_data, ['state', 'conversation_id', 'created_at', 'id', 'lang', 'public_metrics',
                                             'referenced_tweets', 'reply_settings', 'source', 'text'])
        print(fontstyle.apply(result_table, 'faint/Italic/blue'))

    print("Okay, do you need to browse through the file one more time?")
    print(fontstyle.apply('Just type in "yes" or "no"', 'bold/Italic/red/BLACK_BG'))
    user_one_mt = input(">>> ")
    if user_one_mt.lower().startswith("y"):
        interact_with_user()

    print("Goodbye, JSON explorer!")


def interact_with_user():
    """
    Main function.
    Navigates user through .json file.
    """
    # name validation
    greeting()

    dictionary_parser(decoded_students)
    user_key = key_validation(["meta", "data"])

    if user_key == "data":
        print(
            fontstyle.apply(
                """Value of "data" is a list of dictionary object

                Actually, you have two options:
                1. Do you want to see a specific object in a list of dictionary?
                2. Do you want to see the whole data list of dictionary?

                Just type in 1 or 2.
            """.strip(), 'bold/Italic/purple'))

        data_option = key_validation(["1", "2"])
        if data_option == "2":
            # whole list
            raw_data = decoded_students["data"]
            result_table = user_table(raw_data,
                                      ['state', 'conversation_id', 'created_at', 'id', 'lang', 'public_metrics',
                                       'referenced_tweets', 'reply_settings', 'source', 'text'])
            print(fontstyle.apply(result_table, 'faint/Italic/blue'))

        elif data_option == "1":
            # specific data option
            print(fontstyle.apply("So, which exactly element do you want to see?", 'bold/Italic/purple'))
            print(fontstyle.apply("(Type in the number from 0 to 19)", 'bold/Italic/purple'))
            user_num_data = int(key_validation(["0", "1", "2", "3", "4", "5", "6", "7", "8",
                                                "9", "10", "11", "12", "13",
                                                "14", "15", "16", "17", "18", "19"]))

            print(fontstyle.apply(
                """Okay, now you should say me:

                1. Do you need all information about object #%s?
                2. Do you need specific data about object #%s?

                Just type in 1 or 2.""" % (user_num_data, user_num_data),
                'bold/Italic/purple'))

            whether_full_object = key_validation(["1", "2"])
            if whether_full_object == "1":

                raw_data = decoded_students["data"][user_num_data]
                result_table = user_table(raw_data,
                                          ['state', 'conversation_id', 'created_at', 'id', 'lang', 'public_metrics',
                                           'referenced_tweets', 'reply_settings', 'source', 'text'])
                print(fontstyle.apply(result_table, 'faint/Italic/blue'))
            else:
                data_keys = [i for i in decoded_students["data"][user_num_data].keys()]
                dictionary_parser(decoded_students["data"][user_num_data])
                user_data_key = key_validation(data_keys)

                if user_data_key == "public_metrics":
                    public_metrics_keys = [i for i in
                                           decoded_students["data"][user_num_data][user_data_key.strip()].keys()]
                    dictionary_parser(decoded_students["data"][user_num_data][user_data_key.strip()])
                    user_public_metrics_key = key_validation(public_metrics_keys)

                    print(fontstyle.apply(
                        decoded_students["data"][user_num_data]["public_metrics"][user_public_metrics_key],
                        'bold/Italic/purple'))

                elif user_data_key == "referenced_tweets":
                    referenced_tweets_keys = [i for i in
                                              decoded_students["data"][user_num_data][user_data_key.strip()][0].keys()]
                    dictionary_parser(decoded_students["data"][user_num_data][user_data_key.strip()][0])
                    user_referenced_tweets_key = key_validation(referenced_tweets_keys)
                    print(fontstyle.apply(
                        decoded_students["data"][user_num_data]["referenced_tweets"][0][user_referenced_tweets_key],
                        'bold/Italic/purple'))

                else:
                    print(fontstyle.apply(decoded_students["data"][user_num_data][user_data_key], 'bold/Italic/purple'))

    elif user_key == "meta":
        print(fontstyle.apply(
            """Actually, you have two options:

            1. Do you need all the information from "meta"?
            2. Do you need a specific information from "meta"?

            Type in 1 or 2.
            """, 'bold/Italic/purple'))
        user_meta_info = key_validation(["1", "2"])
        meta_keys = [i for i in decoded_students["meta"].keys()]
        if int(user_meta_info) == "1":
            raw_data = decoded_students["meta"]
            result_table = user_table(raw_data,
                                      ['newest_id', 'next_token', 'oldest_id', 'result_count'])
            print(fontstyle.apply(result_table, 'faint/Italic/blue'))
        else:
            dictionary_parser(decoded_students["meta"])
            user_meta_key = key_validation(meta_keys)
            print(fontstyle.apply(decoded_students["meta"][user_meta_key], 'bold/Italic/purple'))

    say_goodbye()


interact_with_user()
