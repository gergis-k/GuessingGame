"""

"""

import pickle as pk
import random as rd

# Th list of words
WORDS = pk.load(open("data/words.dat", "rb"))

# Flag indicating whether the game is over or not
GAME_OVER = False

# The number of available tries
TRIES = int()

# A variable to hold a random index [0, n - 1]
INDEX = int()

# A variable to hold a random word
WORD = str()

# A variable to hold an unknown random word version
UNKNOWN = str()

# Utilities
correct = [
    "Well done",
    "Bravo",
    "Nice, that's right",
    "Correct letter",
    "Cheers",
    "It's works"
    ]
incorrect = [
    "What a pity!",
    "Bad luck",
    "Wrong letter",
    "Try again"
    ]

#
# Generate a random word and return its unknown version
#
def generate():
    global INDEX
    global WORD
    global UNKNOWN
    global TRIES
    global GAME_OVER
    
    
    GAME_OVER = False
    
    INDEX = rd.randint(0, len(WORDS) - 1)
    WORD = WORDS[INDEX]
    UNKNOWN = '_' * len(WORD)
    
    temp = set(WORD)
    TRIES = len(temp)
    
    if TRIES < 6: 
        TRIES = 6
    
def get_unknown():
    global UNKNOWN
    
    unknown_var = ""
    for c in UNKNOWN:
        unknown_var += ' ' + c + ' '
    return unknown_var

def get_word():
    global WORD
    
    word_var = ""
    for c in WORD:
        word_var += ' ' + c + ' '
    return word_var

def get_correct_msg():
    return correct[rd.randint(0, len(correct) - 1)]

def get_incorrect_msg():
    return incorrect[rd.randint(0, len(incorrect) - 1)]