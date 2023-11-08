from data import question_data

class Question(): #Initializes with a question attribute and a boolean attribute.
    def __init__(self, question: str, answer: bool):
        self.question = question
        self.answer = answer

question_list = []

for dictionary in question_data:
    question = dictionary['text']
    boolean_answer = dictionary['answer']
    question_list.append(Question(question, boolean_answer))

for item in question_list:
 print(item.question, item.answer)

