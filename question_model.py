from random import sample

class Question:

    def __init__(self, q_text, q_answer, q_wrong):
        self.text = q_text
        self.answer = q_answer
        self.options = sample(q_wrong +[q_answer], len(q_wrong +[q_answer]))