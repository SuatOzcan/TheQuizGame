from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for dictionary in question_data:
    question = dictionary['text']
    answer = dictionary['answer']
    question_list.append(Question(question, answer))

QuizBrain(question_list)
