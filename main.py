from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for dictionary in question_data:
    question = dictionary['text']
    answer = dictionary['answer']
    question_list.append(Question(question, answer))

player_game = QuizBrain(question_list)

while player_game.still_has_questions():
    player_game.next_question()

print(f"\nYou've gone through all the questions. Your score is {player_game.player_score} \ {player_game.question_number}.")
print('Game Over.\n')
