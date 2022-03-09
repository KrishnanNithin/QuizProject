from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
score = 0

for info in question_data:
    newq = Question(info['text'], info['answer'])
    question_bank.append(newq)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was {brain.score}/{brain.question_number}")