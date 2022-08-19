from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

def choose_category(print_message):
    categories = question_data.keys()
    print(print_message)
    for count, item in enumerate(categories):
        print(str(count+1) + ". " + item +'\n')

    while True:
        choice = input()
        if choice in categories:
            break
        print("Please choose correct category. \n") 
    return question_data[choice]

def randomize_questions(question_data, max_no_of_questions):
    randomlist = random.sample(range(0, len(question_data)), max_no_of_questions)
    new_question_data = []
    for item in randomlist:
        new_question_data.append(question_data[item])
    return new_question_data

question_data = choose_category("Welcome in a QuizBrain. Please choose one of the following categories: ")
question_data = choose_category("Now please choose the difficulity level: ")
max_no_of_questions = input("Please choose number of questions for this round: \n")
question_data = randomize_questions(question_data, max_no_of_questions)

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.\n")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")