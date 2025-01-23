import random

#generate a random number (the given end range like 4 will not be generated)
# l= random.randrange(1,4)
# print(l)

end_range =  input("Type whatever number comes in your mind: ")
if end_range.isdigit():
    end_range = int(end_range)
    if end_range <= 0:
        print("Please enter a number greater than zero")
        quit()
else:
    print("Please enter only a number.")

#this will also print the given end range like 0,100 or whatever the range is 
guess = random.randint(0,end_range)
# print(guess)
count =0


while True:
    count+=1
    #asking input from user for the number to guess
    user_guess =input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)    
    else:
        print("Enter a number next time :) ")
        continue

    if user_guess == guess:
        print("Yes you're correct")
        break
    else:
        if user_guess > guess:
            print("The number is greater than guess")
        else:
            print("The number is lower than guess")
        
print(f"You guess the number in {count} times. ")

    
