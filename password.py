from english_words import get_english_words_set
import random
import math

# Get the set of English words
english_words = get_english_words_set(['web2'])

# Convert the set to a list to enable indexing
english_words_list = list(english_words)

# Pick four random words
wordList = random.sample(english_words_list, 4)

# get the number of chars for each word
wordListCt = sum(len(word) for word in wordList)

while wordListCt > 17:
    wordList = random.sample(english_words_list, 4)
    # print(wordList)
    wordListCt = sum(len(word) for word in wordList)


# print(wordList)
formattedWord = []

# swap chars with their similar symbosl randomly
charToSymbol = {
    "o": '0',
    'O': '0',
    "s": "$",
    'a': "@",
    'B': '8',
    'l': '1',
    'L': '1',
    'T': '7',
    'S': "$5",
    'A': '4'
}

# these are random symbols
randomChars = "-/:;()$&@.,?!"

# iterate through each word

for word in wordList:
    newWord = ""
    for char in word:
        currentChar = ""
        coinFlip = random.randint(0, 1)

        # flip to lower case
        if coinFlip == 0:
            currentChar = char.lower()

            if currentChar in charToSymbol:
                # second coinflip: pick between symbol and char
                coinFlip = random.randint(0, 1)

                if coinFlip == 0:
                    currentChar = random.choice(charToSymbol[currentChar])

        # flip to uppercase
        else:
            currentChar = char.upper()
        
            if currentChar in charToSymbol:
                # second coinflip: pick between symbol and a random char equivalent char
                coinFlip = random.randint(0, 1)

                if coinFlip == 0:
                    currentChar = random.choice(charToSymbol[currentChar])



        
        newWord += currentChar
    
    formattedWord.append(newWord)

randomSymbols = "-/:;()&.,?!"

print('-'.join(formattedWord))

