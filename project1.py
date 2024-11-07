#hangman game
import random
from collections import Counter

words = '''apple banana berry cherry mango orange 
pineapple watermelon coconut '''

words = words.split(" ")

word = random.choice(words)

if __name__ == "__main__":
    print("guess the word! HINT: the word is a name of a fruit")

    for i in word:
        print("_", end=" ")

    print()

    playing = True

    letterGuesses = ""
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:

        while(chances != 0) and flag == 0:
  

            print()
            chances -= 1

            try:
               guess = str(input("Enter a letter: "))
            except:
               print("Enter only a letter")
               continue

            if not guess.isalpha():
                print("Enter only a LETTER")
                continue

            elif len(guess) > 1:
                print("Enter only A SINGLE LETTER")
                continue
            elif guess in letterGuesses:
                print("you have already guessed that letter")
                continue

            if guess in word:

                k = word.count(guess)

                for _ in range(k):
                   letterGuesses += guess

            for char in word:
                if char in letterGuesses and (Counter(letterGuesses))!= Counter(word):
            

                  print(char, end =" ")
                  correct += 1

                elif (Counter(letterGuesses)== Counter(word)):
             
                  print("the word is: ", end=" ")
                  print(word)
                  flag = 1

                  print("Congratulations, you won!")
                  break
                  break
                else:
                  print("_", end =" " )

        if chances <= 0 and (Counter(letterGuesses)!= Counter(word)):
                 print()
                 print("Sorry you lose! Try again..")
                 print(f"The word was: {word}")
    except KeyboardInterrupt:
        print()
        print("TRY AGAIN..")
        exit()