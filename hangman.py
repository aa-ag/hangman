import random_word
from random_word import RandomWords
r = RandomWords()
rand_word = r.get_random_word()
print(rand_word)

def display_hangman(guess):
    drawings = [  # other leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # the other arm
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # rope
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # pole
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """

    ]
    return drawings[guess]

def round():
   word = rand_word
   return word.upper()

def play():
   # round rules
   tries = 8
   survived = False
   length_hint = "_" * len(word)
   attempted_letters = []
   attempted_words = []

   # user instructions
   print(f"Let's play! \nYou have {tries} tries left.")
   print(display_hangman(guess))
   print(length_hint + "\n")

   while not survived and tries > 0:
      guess = input("Guess a letter or, if you're feeling like taking a risk, the entire word.").upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in attempted_letters:
            tries -= 1
            print(f'Oops! You have wasted a try... "{guess}" was already attempted. You have {tries} tries left...')
         elif guess not in word:
            print(f'PSYCH... not even close, brah.')
            attempted_letters.append(guess)
            tries -= 1
         else:
            print(f'That\'s how it\'s done! "{guess}" is in da word.')
            attempted_letters.append(guess)
            length_hint_list = list(length_hint)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               length_hint_list[index] = guess
            length_hint = "".join(length_hint_list)
            if "_" not in length_hint:
               survived = True
      elif len(guess) == len(word) and guess.isalpha():
         if guess in attempted_words:
            tries -= 1
            print(f'Oops! You have wasted a try... "{guess}" was already attempted. You have {tries} tries left...')
         elif guess != word:
            tries -= 1
            print(f'{guess} is not the word... you have {tries} tries left...')
         else:
            guessed = True
            length_hint = word
      else:
         print("This is not a valid guess. ")
      
      print(display_hangman(tries))
      print(f'{length_hint} \n')
   if guessed:
      print("Congrats you have guessed the word! You win!")
   else:
      print(f'You have run out of words.  The word was {word}')
      





# Instructions
# Enter 'start' to get started, or 'help' if you need the instructions."
# MAKE

