print("Welcome to the Quiz_game")

playing = input("Do you want to play?")

if playing != "yes":
    quit()

print("Okey! Let's play :) ")

playing = input("Are you a UCU Student?")

if playing !='yes':

    quit()

answer = input("what does u.c.u stand for?")

if answer == "uganda christian university":
    print("correct!")

else:
    print("incorrect!")


