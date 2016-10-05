from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_text = open(file_path).read()

    # print file_text

    return file_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    text = text_string.split()

    for i in range(len(text) - 2):
        word = text[i], text[i + 1]
        # print word
        chains[word] = chains.get(word, [])
        chains[word].append(text[i + 2])
        # print chains
    # print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    import random 
    #randomly choosing a key from chains dictionary and storing in random_key
    #random_key is returned one tuple
    random_key = random.choice(chains.keys())
    print random_key
    
    #unpacking string values from a tuple
    # key_word_1, key_word_2 = random_key[0], random_key[1]
    key_word_1, key_word_2 = random_key
    # text += str(random_key[0][0]) + ' ' + str(random_key[0][1])
    #concatenating unpacked string values to text variable, which is an empty string
    text += key_word_1 + ' ' + key_word_2 + ' '
    print text


    # random_key_unlisted = random_key[0] #since the tuple is in a string, need to unpack in order to use as a key for dictionary
    # random_key_values = chains[random_key[0]] #accessing the chains dictionary to find the corresponding value which is a list
    # random_value = random.choice(random_key_values)
    # choosing a random item from the value list

    while random_key in chains:

        random_value = random.choice(chains[random_key])
        print random_value

        # adding the random string item to text
        text += random_value
        print text + ' ' ########WHY NOT ADDING SPACE AFTER 3RD WORD???????????#######
        
        # creating new tuple with second word from the first key and the random word from the value list
        random_key = (random_key[1], random_value)
        print random_key
        # print chains[new_key]
        # from the new tuple, grabbing the values from chains dictionary and randomly choosing an item from the value list
        # new_random_value = random.choice(chains[new_key])
        # print new_random_value
        # second_new_key = (random_value, new_random_value)
    print text


    # return random_key 

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
# random_text = make_text(chains)

# print random_text

open_and_read_file(input_path)
make_text(chains)