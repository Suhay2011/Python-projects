# parent class
class Bird:

    def __init__(self):
        print("Bird is readdy")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim Faster!")

# child class
class Penguin(Bird):

    def __init__(self):
        super().__init__()