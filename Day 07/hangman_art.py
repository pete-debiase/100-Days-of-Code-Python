#!/usr/bin/python
"""Art resources for hangman game"""

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
'''

lives_6 = '''  +---+
  |   |
      |
      |
      |
      |
========='''

lives_5 = '''  +---+
  |   |
  O   |
      |
      |
      |
========='''

lives_4 = '''  +---+
  |   |
  O   |
  |   |
      |
      |
========='''

lives_3 = '''  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''

lives_2 = '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

lives_1 = '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

lives_0 = '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

lives_art_dict = {0: lives_0,
                  1: lives_1,
                  2: lives_2,
                  3: lives_3,
                  4: lives_4,
                  5: lives_5,
                  6: lives_6}

