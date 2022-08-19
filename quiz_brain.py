"""The module responsible for running the quiz.

Classes:
    
    QuizBrain

Methods:

    still_has_questions(object) -> Boolean
    next_question(object)
    check_answer(object, string, string)
"""


class QuizBrain:
    """This is a Class for displaying questions and checking the answers for Quiz Brain program. 

    Attributes:
        question_number (int): enumerates the current question
        question_list (list): list of dictionaries holding question text (key) 
                               and the correct answer (value)
        score (int): score standing for the number of correctly answered questions
    """

    def __init__(self, q_list):
        """The constructor for the QuizBrain class.

        Args:
            q_list (list): list of dictionaries holding question text (key) 
                               and the correct answer (value)
        """

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Function checking if there are still questions left

        Returns:
            Boolean: returns True if number of question is lower than the length 
                     of the question, False otherwise.
        """

        return self.question_number < len(self.question_list)

    def next_question(self):
        """Function that asks the user next question. Controls the number of 
        the question, asks for answer and sends the input, together with 
        the correct answer to the check_answer function.
        """

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Function that checks if user's answer is correct by comparing it to the correct answer.

        Args:
            user_answer (string): String containing users answer
            correct_answer (string): String containing correct answer
        """

        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} \n")