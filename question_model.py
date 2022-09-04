"""Creates a question object for the quiz.

Classes:

    Question
"""


class Question:
    """This is a class for creating a question for quiz.

    Attributes:
        text (string): The string containing the question
        answer (string): The string containing the answer
    """

    def __init__(self, q_text: str, q_answer: str):
        """The constructor for Question class.

        :param q_text: The string containing the question
        :param q_answer: The string containing the answer
        """
        self.text = q_text
        self.answer = q_answer
