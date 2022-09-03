


print("Hello , Lets put your knowledge to the test to the test!")
name = input("Enter your name:")
print("what a nice name " + name + "!")

score = 0

option = input("Do you want to play the quiz? (Respond with Y for YES or N or NO) :")
if option != "Y":
        quit()


answer1 = input("What was the First war of independence in India? (answer in lowercase)")
if answer1 != "ans1":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1
#replace questions and answers with yours

answer1 = input("q2 (answer in SMALL letters)")
if answer1 != "abcde":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


answer1 = input("q3 (fill the blank and answer in lowercase)")
if answer1.lower() != "abcde":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


answer1 = input("Who was our first president? hint: Dr ________ Prasad (fill in the blank and answer in lowercase):")
if answer1 != "rajendra":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


answer1 = input("my name is _____ (fill in the blank and answer in lowercase):")
if answer1 != "jai": # really
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


print("this is the end of the quiz")
print("your score is " + str(score))
