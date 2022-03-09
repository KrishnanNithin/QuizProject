from question_model import Question
from data import question_data

question_bank = []
for info in question_data:
    newq = Question(info['text'], info['answer'])
    question_bank.append(newq)

