from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from helper import check_if_numeric, choose_category, randomize_questions
import random



if __name__ == '__main__':
    question_data = choose_category("Welcome in a QuizBrain. Please choose one of the following categories: ", question_data)
    question_data = choose_category("\n Now please choose the difficulity level: ", question_data)
    max_no_of_questions = int(input("\n Please choose number of questions for this round: \n"))
    question_data = randomize_questions(question_data, max_no_of_questions)

    question_bank = []
    for item in question_data:
        question_bank.append(Question(item["question"], item["correct_answer"], item["incorrect_answers"]))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz.\n")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")