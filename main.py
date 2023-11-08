from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for dictionary in question_data:
    question = dictionary['text']
    answer = dictionary['answer']
    question_list.append(Question(question, answer))

player_game = QuizBrain(question_list)

for i in range(len(question_list)):
    player_game.next_question()

print(f'Your score is {player_game.player_score}.')
print('Game over.')
