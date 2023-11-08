from main import question_list
import random

class QuizBrain():
    def __init__(self):
        self.question_number = 0
        self.player_score = 0
        self.question_list = question_list
        random.shuffle(self.question_list)

    def next_question(self):
        for i in range(len(self.question_list)):
            random_pick = self.question_list[i]
            user_input = input(random_pick.question + ' True\False\n')
            if user_input == random_pick.answer:
                self.player_score += 1
            print(f'Your score is {player_question.player_score}.')
        print('Game over.')

player_question = QuizBrain()
player_question.next_question()
