question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
correct = 0
import random

class Question:
    def __init__(self, question, answer, correct):
        self.question = question
        self.answer = answer
        self.correct = 0

    def check_answer(self, questions):
        if questions.lower() == (self.answer).lower():
            self.correct += 1
            print(f"You are correct! Your score is now {self.correct}")
        else:
            print(f"Sorry, that's incorrect. Your score remains {self.correct}")
        print(f"your current score is {self.correct}/{question_number}")





question_number = 1
is_done = False
while is_done == False:
    number = random.randint(1, len(question_data)-1)
    question_asking = Question(question_data[number]["text"], question_data[number]["answer"], correct)
    questions = input(f"{question_number}) {question_asking.question}\nAnswer 'True' or 'False': ").title()
    question_asking.check_answer(questions)
    question_data.remove(question_data[number])
    if len(question_data) == 0:
        is_done = True
    else:
        is_done = False
