import random as rd

def choose():
    print("welcome to the game ")
    number=rd.randint(1,100)
    attempt=0

    while True:
        user=int(input("enter number between (1-100) "))
        attempt+=1

        if user < number:
            print("too small number guess again")
        elif user > number:
            print("too large number try again")
        else:
            print(f"you guess the write number in {attempt} tries")
            break

while True:
    choose()
    play_again=input("do u want to play again (yes / no)")
    if play_again!="yes":
        print("tnq for playing with me ")
        break
