from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You have completed the quiz.\n")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

