import random  #inporting module
playing = True #initilise
number = str(random.randint(10,20)) #random in-built function

print("I will generate a random number from 0 to 9 and you have to guess the number one diget at a time")
print("The game ends when you find 1 hero!")
#iterate loop untill it is true
while playing:
    guess = input("Give me your best guess /n")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break

    else:
        print("Your guess isnt quite right try again. /n" )