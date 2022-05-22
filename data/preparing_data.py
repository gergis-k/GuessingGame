"""

# Open the data file 'english-words-medium.txt'.

# Prepare the data and clean it.

# Create a list of prepared and cleaned words.

# Serialize the list of words usnig pickle module
  ---- The pickle module implements binary protocols for serializing
  ---- and de-serializing a Python object structure.

# https://docs.python.org/3.12/library/pickle.html

"""

# Pickle — Python object serialization
import pickle as pk

# Open the '.txt' data file 
file = open("english-words-medium.txt", "r")

# Create list of words
LIST = [ (line.strip()).split()[0].lower() for line in file ]

# Save the list of words as a '.dat' file using binary file protocol
pk.dump(LIST, open("words.dat", "wb"))

