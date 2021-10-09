import random
def hangman():

    word= random.choice(["ironman","vision","thanos","blackwidow","scarlet"])
    print("____________")
    print('hint- "Marvel"')
    valid= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turn= 10
    guesscorr= ''


    while len(word) >0:
        main=""
        for i in word:
            if i in guesscorr:
              main= main+ i
            else:
              main= main+ "_"

        if main == word:
            print(main)
            print("YOU WIN!!!!")
            break

        print("Your guess : ", main)
        guess= input()


        if guess in valid:
          guesscorr= guesscorr+ guess

        else:
          print("enter valid character ")
          guess= input()

        if guess not in word:
          turn= turn-1
          print(turn," turns left")
        if turn==9:
          print("-------")
        if turn == 8:
          print("-------")
          print("   o    ")
        if turn == 7:
          print("-------")
          print("   o    ")
          print("   |    ")
        if turn == 6:
          print("-------")
          print("   o    ")
          print("  \|    ")
        if turn == 5:
          print("-------")
          print("   o    ")
          print("  \|/   ")
        if turn == 4:
          print("-------")
          print("   o    ")
          print("  \|/   ")
          print("  /     ")
        if turn == 3:
          print("-------")
          print("   o    ")
          print("  \|/   ")
          print("  / \    ")
        if turn == 2:
          print("-------")
          print("   o _   ")
          print("  \|/   ")
          print("  / \    ")
        if turn == 1:
          print("-------")
          print("   o _|  ")
          print("  \|/   ")
          print("  / \    ")
        if turn == 0:
          print("-------")
          print("   o_|  ")
          print("  /|\   ")
          print("  / \    ")
          print("Sorry you loose")
          break

name = input('Enter your name: ')
print('Hello!', name)
print('GUESS THE WORD IN 10 ATTEMPTS')
hangman()