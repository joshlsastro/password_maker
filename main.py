NUMBER_OF_WORDS = 4
SEPARATOR = '-' # This separates words from numbers and each other
DO_CAPITALIZE = True # This is True if each word is capitalized
ADD_NUMBER = True # This is True if a number will be appended to the end
###################################################################
from random import choice

with open("english_words.txt", "r") as f:
    words = f.read()
words = words.split("\n")

l = list(choice(words) for i in range(NUMBER_OF_WORDS)) #Randomly chooses 4 words from a list of all english words
if DO_CAPITALIZE:
    for i in range(len(l)):
        l[i] = l[i].capitalize()
message = l[0]
for i in range(1, NUMBER_OF_WORDS):
    message = message + SEPARATOR + l[i]
if ADD_NUMBER:
    message = message + SEPARATOR + choice("0123456789")
print(message)
