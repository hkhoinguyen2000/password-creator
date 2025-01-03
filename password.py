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



def passwordCreator(word_count, password_len):

    if word_count >= password_len:
        print("It is not possible to have more words than the length of the password")
        return
        
    # Pick a specified amount of words
    random_word_list = random.sample(english_words_list, word_count)

    # get the number of chars for each word
    random_word_list_ct = sum(len(word) for word in random_word_list)

    # password should be up to password_len
    # with word_count - 1 separators

    print("The program is now creating a password of length", password_len, "composed of", word_count, "words.")
    while random_word_list_ct > (password_len - word_count - 1):
        random_word_list = random.sample(english_words_list, word_count)
        random_word_list_ct = sum(len(word) for word in random_word_list)

    print("The program has now found a random_word_list of length", word_count, "that sums to", password_len, "chars.")

    formatted_password = []


    # iterate through each word
    for word in random_word_list:
        new_word = ""
        for char in word:
            current_char = ""
            coinFlip = random.randint(0, 1)

            # flip to lower case
            if not coinFlip:
                current_char = char.lower()

                if current_char in charToSymbol:
                    # second coinflip: pick between symbol and a random char equivalent
                    coinFlip = random.randint(0, 1)
                    
                    if not coinFlip:
                        current_char = random.choice(charToSymbol[current_char])

            # flip to uppercase
            else:
                current_char = char.upper()
            
                if current_char in charToSymbol:
                    # second coinflip: pick between symbol and a random char equivalent
                    coinFlip = random.randint(0, 1)

                    if not coinFlip:
                        current_char = random.choice(charToSymbol[current_char])

            new_word += current_char
        
        formatted_password.append(new_word)

    return('-'.join(formatted_password))

numWords = input("Enter the number of words you want in your password: ")
password_len = input("Enter the desired length of your password: ")
print(passwordCreator(int(numWords), int(password_len)))