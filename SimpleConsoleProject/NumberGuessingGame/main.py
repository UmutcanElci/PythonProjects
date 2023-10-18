import random
def guessing_game():
    num = random.randint(1,100)
    while(True):
        guess = int(input("What is you guess : "))
        
        if guess == num:
            print(f"Right! The answer is {guess}")
            break
        
        if guess < num:
            print("Number is too low!")
        else:
            print("Number is too high!")
            

guessing_game()       