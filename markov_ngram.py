import sys
from random import choice

input_path = sys.argv[1]
ngram_num = int(raw_input('Please choose a n-gram number.'))

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_text = open(file_path).read()

    # print file_text

    return file_text


def make_chains(text_string, num):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    # instantiating the chains dictionary as an empty dictionary
    chains = {}
 
    # splitting all words from file as separate strings in text list
    text = text_string.split()

    # interating over the text list (on index) for range of the length of the list - num (ngram)
    for i in range(len(text) - num):
        # creating tuple word which includes n number of strings
        # we need another for loop?
        for tuple_index in range(num):
            word 


        word = text[i], text[i + 1]
        # checking for if key word exists in chain dictionary
        # if it does not, default add empty dictionary
        # add to value of key word the next string in text list
        chains[word] = chains.get(word, [])
        chains[word].append(text[i + 2])
        # print chains
    # print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    #randomly choosing a key from chains dictionary and storing in random_key
    #random_key is returned one tuple
    random_key = choice(chains.keys())
    # print random_key
    
    #unpacking string values from a tuple
    # key_word_1, key_word_2 = random_key[0], random_key[1]
    key_word_1, key_word_2 = random_key
    # text += str(random_key[0]) + ' ' + str(random_key[1])
    #concatenating unpacked string values to text variable, which is an empty string
    text += key_word_1 + ' ' + key_word_2 + ' '
    # print text


    # random_key_values = chains[random_key[0]] #accessing the chains dictionary to find the corresponding value which is a list
    # random_value = random.choice(random_key_values)
    
    # while the key is a memeber of the chains dictionary...
    while random_key in chains:
        # choosing a random item from the value list
        random_value = choice(chains[random_key])

        # adding the random string item to text plus space
        text += random_value + ' '
        
        # creating new tuple with second word from the first key and the random word from the value list
        random_key = (random_key[1], random_value)
        # if while loop continues, from the new tuple, grab the values from chains dictionary
        # and randomly choosing an item from the value list. Rinse and repeat.
    
    return text


# input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text