# Hangman-game-
Here's a game "Hangman" created using python.


        

        if guess not in word:
          turn= turn-1
          print(turn," turns left")
        
        if turn == 0:
          print("-------")
          print("   o_|  ")
          print("  /|\   ")
          print("  / \    ")
          print("Sorry you loose")
          break


Start your own game using python!!

name = input('Enter your name: ')
print('Hello!', name)
print('GUESS THE WORD IN 10 ATTEMPTS')
hangman()
