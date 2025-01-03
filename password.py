from english_words import get_english_words_set
import random

# Get the set of English words
english_words = get_english_words_set(['web2'])

# Convert the set to a list to enable indexing
english_words_list = list(english_words)


# swap chars with their similar symbols randomly
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

# random chars
randomChars = "-/:;()$&@.,?!"
random_separators = "_-"


def passwordCreator(wordCt, passwordLen, randomSep):

    if wordCt >= passwordLen:
        print("It is not possible to have more words than the length of the password")
        return
        
    # Pick a specified amount of words
    wordList = random.sample(english_words_list, wordCt)

    # get the number of chars for each word
    wordListCt = sum(len(word) for word in wordList)

    # password should be up to passwordLen
    # with wordCt - 1 separators

    print("The program is now creating a password of length", passwordLen, "composed of", wordCt, "words.")
    while wordListCt > (passwordLen - wordCt - 1):
        wordList = random.sample(english_words_list, 4)
        # print(wordList)

        wordListCt = sum(len(word) for word in wordList)

    print("The program has now found a wordlist of length", wordCt, "that sums to", passwordLen, "chars.")

    formattedWord = []




    # iterate through each word
    for word in wordList:
        newWord = ""
        for char in word:
            currentChar = ""
            coinFlip = random.randint(0, 1)

            # flip to lower case
            if not coinFlip:
                currentChar = char.lower()

                if currentChar in charToSymbol:
                    # second coinflip: pick between symbol and char
                    coinFlip = random.randint(0, 1)
                    
                    if not coinFlip:
                        currentChar = random.choice(charToSymbol[currentChar])

            # flip to uppercase
            else:
                currentChar = char.upper()
            
                if currentChar in charToSymbol:
                    # second coinflip: pick between symbol and a random char equivalent char
                    coinFlip = random.randint(0, 1)

                    if not coinFlip:
                        currentChar = random.choice(charToSymbol[currentChar])

            newWord += currentChar
        
        formattedWord.append(newWord)

    if randomSep:
        randomSeparatorChar = random.choice(random_separators)
        return(randomSeparatorChar.join(formattedWord))

    else:
        return('-'.join(formattedWord))

numWords = input("Enter the number of words you want in your password: ")
passwordLen = input("Enter the desired length of your password: ")
print(passwordCreator(int(numWords), int(passwordLen), False))