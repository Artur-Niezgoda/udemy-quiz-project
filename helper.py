from random import sample

def check_if_numeric(inputs, categories):
    for i in range(len(categories)):
        if inputs == str(i+1):
            inputs = list(categories)[i]
    return inputs

def randomize_questions(question_data, max_no_of_questions):
    randomlist = sample(range(0, len(question_data)), max_no_of_questions)
    new_question_data = []
    for item in randomlist:
        new_question_data.append(question_data[item])
    return new_question_data

def choose_category(print_message, question_data):
    categories = question_data.keys()
    print(print_message)
    for count, item in enumerate(categories):
        print(str(count+1) + ". " + item +'\n')

    while True:
        choice = input().lower()
        if choice in [str(x+1) for x in range(len(categories))]:
            choice = check_if_numeric(choice, categories)
        if choice in categories:
            break
        print("Please choose correct category. \n") 
    return question_data[choice]