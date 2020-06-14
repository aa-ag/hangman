# import random_word
# from random_word import RandomWords
# r = RandomWords()
# rand_word = r.get_random_word()

import random 
from words import word_list

def round():
   word = random.choice(word_list)
   return word.upper()

def play(word):
   # round rules
   tries = 7
   survived = False
   length_hint = "_" * len(word)
   attempted_letters = []
   attempted_words = []

   # user instructions
   print("\n* Let's play!\n")
   print(display_hangman(tries))
   print(length_hint + "\n")

   while not survived and tries > 0:

      guess = input("\n* Guess a letter or, if you're feeling like taking a risk, the entire word: \n").upper()
      
      if len(guess) == 1 and guess.isalpha():
         if guess in attempted_letters:
            print("\n* Oops! That letter was already attempted.\n")
         elif guess not in word:
            print("\n* PSYCH... not even close, brah.\n")
            attempted_letters.append(guess)
            tries -= 1
         else:
            print("\n* Totally in da word!\n")
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
            print("\n* Oops! That word was already attempted.\n")
         elif guess != word:
            tries -= 1
            print("\n* Not the word...\n")
         else:
            survived = True
            length_hint = word
      else:
         print("\n* Not a valid guess :s\n")
      
      print(display_hangman(tries))
      print(length_hint)
   
   if survived:
      print("\n* Congrats you have guessed the word! You win!\n")
   else:
      print("\n* You have run out of tries.  The word was " + word + ".\n")

def display_hangman(tries):
    drawings = [  # other leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
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
    ]
    return drawings[tries]
      
def main():
   word = round()
   play(word)
   while input('* Enter "again" to play again or "quit" to exit: ').lower() == "again":
      word = round()
      play(word)      
      

if __name__ == "__main__":
   main()
