from random import choice

with open("english_words.txt", "r") as f:
    words = f.read()
words = words.split("\n")

# Getting the configuration
with open("config.txt", "r") as f:
    config = f.read()
config = config.split("\n")

NUMBER_OF_WORDS = int(config[0])
SEPARATOR = config[1]
DO_CAPITALIZE = bool(int(config[2]))
ADD_NUMBER = bool(int(config[3]))

l = list(choice(words) for i in range(NUMBER_OF_WORDS)) #Randomly chooses NUMBER_OF_WORDS words from a list of all english words
if DO_CAPITALIZE:
    for i in range(len(l)):
        l[i] = l[i].capitalize()

message = l[0]
for i in range(1, NUMBER_OF_WORDS):
    message = message + SEPARATOR + l[i]
if ADD_NUMBER:
    message = message + SEPARATOR + choice("0123456789")
print(message)
