#replay
def replay(score):
    print("Next Session")
    min=int(input("Enter the Minimum Number of the range(integer only):"))
    max=int(input("Enter the Maximum Number of the range(integer only):"))
    randomnumber=ranger(min, max)
    print("The random number has been selected")
    print("You have 3 guesses")
    count=0
    sc=0
    newscore=game(randomnumber,sc,count)
    newscore=int(newscore)
    hscore=score+newscore
    return(hscore)
#range giver
def ranger(min,max):
    import random as r
    num=r.randint(min,max)
    return(num)
#game
def game(num,score,count):
    guess=int(input("Your Guess(Input the integer number):"))
    while (count<4):
        if(guess==num):
            print("Congrats Your Guess was right")
            score=score+1
            print("You got 1 Score!!")
            return(ece(score))
            break
        elif(guess>num):
            print("Your Guess is bigger , Have one more try")
            count=count+1
            break
        elif(guess<num):
            print("Your Guess is smaller , Have one more try")
            count=count+1
            break
    if count == 3:
        print("You lost, the number was", num)
        return (ece(score))
    else:
        return(game(num, score, count))
#exit or contine
def ece(score):
    eorc = input("To exit input(E) or To continue input(C):")
    if eorc == "e" or eorc == "E":
        return(score)
    elif eorc == "c" or eorc == "C":
        return(replay(score))
    else:
        print("Invalid reply either enter E or C")
        return(ece(score))

#body
print("Hello People!")
print("Welcome to the Guessing Game!")
input("Press ENTER to continue....")
print("Rules For the Game are:")
print("1.The player has to give a maximum number and a minimum number for the range(integers only)")
print("2.The player has to guess which number the computer is holding between the given range")
print("3.The player has 3 chances to guess the number")
print("4.If the player Guesses the number correctly ,the player will be rewarded with one point each")
input("If you have finished reading the rules press ENTER.....")
print("Lets Begin!")
print("Enter the Range:")
min=int(input("Enter the Minimum Number of the range(integer only):"))
max=int(input("Enter the Maximum Number of the range(integer only):"))
randomnumber=ranger(min,max)
print("The random number has been selected")
print("You have 3 guesses")
sc=0
count=0
score=game(randomnumber,sc,count)
print("Your Total Score is",score)
print("Thank you for playing the Guessing Game")
