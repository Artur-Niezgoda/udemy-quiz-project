from helper import check_if_numeric


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):

        return self.question_number < len(self.question_list)

    def next_question(self):
        
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {current_question.text}: \n")
        for count, item in enumerate(current_question.options):
            print(str(count+1) + ". " + item +'\n')
        user_answer = input()
        if user_answer in [str(x+1) for x in range(len(current_question.options))]:
            user_answer = check_if_numeric(user_answer, current_question.options)
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} \n")