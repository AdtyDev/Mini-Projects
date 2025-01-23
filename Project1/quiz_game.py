print("Welcome to the Quiz")

Confirm = input("Do you want to play? ")
print(Confirm)

if Confirm.lower() != "yes":
    quit()

print("Good, Let's Play :) ")

score = 0

question1 = input("What does CPU stands for? ")
if question1.lower() == "central processing unit":
    print("Correct Answer")
    score+=1
else:
    print("wrong answer")

question = int(input("What is 3*3 ?"))
if question == 3*3:
    print("Correct Answer")
    score+=1
else:
    print("wrong answer")

question1 = input("What does RAM stands for? ")
if question1.lower() == "random access memory":
    print("Correct Answer")
    score +=1
else:
    print("wrong answer")

question = int(input("What is 20*3 ?"))
if question == 20*3:
    print("Correct Answer")
    score+=1
else:
    print("wrong answer")

print("You got",score,"question correct")
print("You got",(score/4)*100,"%")