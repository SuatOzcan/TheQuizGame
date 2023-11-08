import random

class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.player_score = 0
        self.question_list = question_list
        random.shuffle(self.question_list)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        random_pick = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f'Q.{self.question_number}: ' + random_pick.question + ' True\False\n')
        self.user_answer(random_pick, user_input)

    def user_answer(self, random_pick, user_input):
        if user_input.lower() == random_pick.answer.lower():
            self.player_score += 1
            print(f"You've got it right!. Your point is: {self.player_score} \ {self.question_number}")            
        else:
            print(f"The answer is not correct. No worries! Your point is: {self.player_score} \ {self.question_number}")
