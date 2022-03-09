class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list

    def next_question(self):
        qs = self.question_list[self.question_number]
        answer = input(f'Q.{self.question_number+1}: {qs} (True or False)')