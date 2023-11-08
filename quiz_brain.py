import random

class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.player_score = 0
        self.question_list = question_list
        random.shuffle(self.question_list)

    def next_question(self):
        random_pick = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f'Q.{self.question_number}: ' + random_pick.question + ' True\False\n')
        if user_input == random_pick.answer:
            print("You've got it right!")
            self.player_score += 1
        else:
            print("The answer is not correct. No worries!")
