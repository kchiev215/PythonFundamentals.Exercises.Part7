from typing import Dict
import math
import random

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: "English", 2: "Spanish", 3: "Portuguese"}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?', 2: '¿Cómo te llamas?', 3: 'Qual é o seu nome?'}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = [["Hello"], ["Hola"], ["Olá"]]


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    # pass  # remove pass statement and implement me
    print('Please choose a language: ')
    for key, value in lang_options.items():
        print(f'{key}: {value}')



def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    # pass  # remove pass statement and implement me
    user_input = int(input("What language would you like to pick?"))
    return user_input


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    # pass  # remove pass statement and implement me
    if lang_choice in lang_options:
        return True
    else:
        return False



def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    # pass  # remove pass statement and implement me
    return name_prompt_options.get(lang_choice)



def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    # pass  # remove pass statement and implement me
    name = input(name_prompt)
    return name

def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    # pass  # remove pass statement and implement me
    print(random.choice(greetings_dict[lang_choice-1]), name)

def choose_mode():
    print("Would you like to enter admin or user mode?")
    print("1. admin mode    2. user mode")
    user_input = int(input(">> "))
    if user_input == 1:
        print("Entering admin mode...")
        admin_mode()
    elif user_input == 2:
        print("Entering user mode...")
    else:
        print("That's not an option. Continuing on.")

def admin_mode():
    print("Do you want to add a new language or edit a current one?")
    print("1. Add new language  2. Edit an existing language    3. Quit")
    user_input = int(input(">> "))
    if user_input == 1:
        add_language()
    elif user_input == 2:
        update_existing_language()
    else:
        print("Switching to user mode...")

def add_language():
    print("What language will you be adding?")
    new_language = input(">> ")
    new_key = len(lang_dict) + 1
    lang_dict[new_key] = new_language
    print("Write 'What's your name' in the language you're adding.")
    new_name_prompt = input(">> ")
    name_prompt_dict[new_key] = new_name_prompt
    print("Write 'Hello' in the language you're adding.")
    new_greeting = input(">> ")
    greetings_dict[new_key] = new_greeting

def update_existing_language():
    print("Which language are you updating?")
    print_language_options(lang_dict)
    language_option = int(input(">> "))
    language_option = language_option - 1
    print("What is your new greeting?")
    new_greeting = input(">> ")
    greetings_dict[language_option].append(new_greeting)
    print(greetings_dict)


    









if __name__ == '__main__':
    choose_mode()
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
