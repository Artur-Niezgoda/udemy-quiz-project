"""Module contatining usefull functions for quiz program.

Functions:
    change_if_numeric(int, list) -> string
    randomize_questions(list, int) -> list
    choose_category(list) -> list
"""

from random import sample

def change_if_numeric(inputs, categories):
    """Function that changes numeric answer to corresponding string

    Args:
        inputs (int): a number corresponding to given answer by user
        categories (dict_keys): dict_keys containing list of keys

    Returns:
        string: string corresponding to chosen numer representing the answer
    """

    for i in range(len(categories)):
        if inputs == str(i+1):
            inputs = list(categories)[i]
    return inputs

def randomize_questions(question_data, max_no_of_questions):
    """Function that chooses randomly a given number or questions

    Args:
        question_data (list): list containing dictionaries of questions
        max_no_of_questions (int): number of questions in a round

    Returns:
        list: list containing only given number of questions, chosen randomly
    """
    randomlist = sample(range(0, len(question_data)), max_no_of_questions)
    new_question_data = []
    for item in randomlist:
        new_question_data.append(question_data[item])
    return new_question_data

def choose_category(print_message, question_data):
    """Function that preserves only questions from given category 
    or level of difficulity.

    Args:
        print_message (string): a message printed when asking user for input
        question_data (dict): dictionary of questions

    Returns:
        dictionary/list: returns dictionary if user is choosing category
                         or list if level of difficulty 
    """
    
    categories = question_data.keys()
    print(print_message)
    for count, item in enumerate(categories):
        print(str(count+1) + ". " + item +'\n')

    while True:
        choice = input().lower()
        if choice in [str(x+1) for x in range(len(categories))]:
            choice = change_if_numeric(choice, categories)
        if choice in categories:
            break
        print("Please choose correct category. \n") 
    return question_data[choice]