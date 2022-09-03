


print("Hello , Lets put your knowledge about India to the test to the test!")
name = input("Enter your name:")
print("what a nice name " + name + "!")

score = 0

option = input("Do you want to play the quiz on India's freedom? (Respond with Y for YES or N or NO) :")
if option != "Y":
        quit()


answer1 = input("What was the First war of independence in India? (answer in lowercase)")
if answer1 != "revolt of 1857":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


answer1 = input("how long has india remained independant? (answer in SMALL letters)")
if answer1 != "75":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


answer1 = input("In which year did we get independence? (fill the blank and answer in lowercase)")
if answer1.lower() != "1947":
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


answer1 = input("Who started the revolt of 1857? __________ Pandey (fill in the blank and answer in lowercase):")
if answer1 != "mangal":
    print("you got the answer wrong!")
else:
    print("you got the answer correct")
    score += 1


print("this is the end of the quiz")
print("your score is " + str(score))