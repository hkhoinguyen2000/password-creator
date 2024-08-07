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
    "o": 0,
    "s": "$",
    'a': "@"

}

# iterate through each word


