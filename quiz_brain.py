"""The module responsible for running the quiz.

Classes:
    
    QuizBrain

Methods:

    still_has_questions() -> Boolean
        Check if there are still questions left
    next_question() -> String
        Take next Question object
    check_answer(string) -> Boolean
        Check user's answer
"""
from html import unescape


class QuizBrain:
    """This is a Class for displaying questions and checking the answers for Quiz Brain program.

    Attributes:
        question_number (int): enumerates the current question
        question_list (list): list of dictionaries holding question text (key)
                               and the correct answer (value)
        score (int): score standing for the number of correctly answered questions
        current_question (object): object of Question class, containing question '.text' and '.answer' as its attributes
    """

    def __init__(self, q_list: list):
        """The constructor for the QuizBrain class.

        :param q_list: list of Question class objects
        """

        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def still_has_questions(self) -> bool:
        """Check if there are still questions left

        :return: returns True if number of the current question is lower than the length
                     of the question _list, False otherwise.
        """

        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Take next Question object and return its text attribute as a string

        :return: text of the question with the number of the current question
        """

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {unescape(self.current_question.text)}"

    def check_answer(self, user_answer: str) -> bool:
        """
        Check if user's answer is correct by comparing it to the correct answer.

        :param user_answer: String containing user's answer
        :return: True if the answer is correct, False otherwise
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
