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
                   |     / \\
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