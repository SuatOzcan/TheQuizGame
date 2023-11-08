from data import question_data
from question_model import Question

question_list = []

for dictionary in question_data:
    question = dictionary['text']
    answer = dictionary['answer']
    question_list.append(Question(question, answer))

for item in question_list:
    print(item.question, item.answer)

print(type(question_list[0].answer))

