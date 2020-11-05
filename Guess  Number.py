
# Guess The Number

n=25
num_of_guess=1
print(" Guess Number Game:")
print("num of guesses is limited to only 5 times")
while(num_of_guess<=5):
    guess_number = int(input("Guess the Number:\n"))
    if guess_number<25:
        print("your number is smaller than Guess")
    elif guess_number>25:
        print("your number is bigger than num")
    else:
        print("Congrest you Win the Game")
        print(num_of_guess,"No of Guesses he tooked to finish")
        break
    print(5-num_of_guess,"no of Guesses left")
    num_of_guess=num_of_guess+1
if(num_of_guess>5):
    print("Game Over")
