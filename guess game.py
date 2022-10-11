# this is a guess game created using randint in random function of python
d = '~'*30
name = str(input("kindly input your username: "))
opt = str(input(f"Hello {name} Are you interested in playing a guess game,kindly specify Yes or No: "))
yes = ('Y','y','yes','Yes','YES')
no = ('n','N','no','No','NO')

interested = True

while interested:
    if opt in yes:
        from random import randint
        import math

        print(f"\n{d}GUESS GAME{d}")

        print(f"Hey {name} you have choose to play this guess game.\nthere are a few rules that guides this game and they are listed below.")
        print("kindly read and understand them before playing this guess game")
        print("1.You are to guess a number")
        print("2.Your input should be only number")
        print("3.You would continue to guess till you pass")
        print("4.We are with you so dont feel lonely.")
        print("Now you know the rules you are fit to play this game!!!\n")
        lower = int(input("\tkindly specify the lower bond:- "))
        upper = int(input("\tkindly specify the upper bond:- "))
        randomguess = randint(lower,upper)
        #print(randomguess)
        print(f'{d}GAME STARTS{d}')
        chance = round(math.log(upper - lower + 1,2))
        print("\n\tYou've only %d chances to make the right guess" % chance)
        guess = None
        numoftime = 0
        while numoftime <= chance:
            numoftime += 1
            remains = chance - numoftime
            guess = int(input("\tGuess a number between your range: "))
            if guess > randomguess and not guess < lower:
                print(f"\tyou guessed too high {numoftime} chance is used {remains} is remaining")
                continue
            if guess < randomguess and not guess < lower:
                print("\tyou guessed too low %d chance is used %d is remaining" % (numoftime, remains))
                continue
            if guess == randomguess:
                print("\tYou did it, you guessed right")
                break
            if numoftime > chance:
                print("\n\tThe number is %d" % randomguess)
            else:
                print('invalid input')
        break

    elif opt in no:
        print(f"{name} you choosed not to play this game! see you next time")
        break

    else:
        print("\nInvalid input")
        opt = input("\n\twould you like to try again[yes / no]: ")
        if opt in yes:
            continue

        elif opt in no:
            print(f"{name} you choosed not to play this game! see you next time")
            break