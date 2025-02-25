import random

class FruitQuiz:
    def __init__(self):
        self.fruits={
            'apple':'red',
            'banana':'yellow',
            'watermelon':'green',
            'orange':'orange','grape':'purple','pineapple':'yellow','grapefruit':'yellow','tangerine':'tangerine',
            'dregonfruit':'pink','zukini':'purple','blueberries':"blue"

        }
    def quiz(self):
        while (True):
            fruit, colour = random.choice(list(self.fruits.items()))
            print("What is the colour of",fruit)
            user_answer = input()

            if(user_answer.lower() == colour):
              print("Correct answer")
            else:
                 print("Wrong answer")

            option = int(input("Enter 0 , if you want to play again otherwise enter 1"))
            if (option==1):
             break

print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()