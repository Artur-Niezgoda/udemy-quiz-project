from question_model import Question
from data import question_data


question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

print(question_bank)