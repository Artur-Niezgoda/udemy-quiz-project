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

    def __init__(self, q_text, q_answer):
        """The constructor for Question class.

        Args:
            q_text (string): The string containing the question
            q_answer (string): The string containing the answer
        """
        self.text = q_text
        self.answer = q_answer