import random

# Understand:

# Plan:
# Read input.txt and spit into words
# Analyze the text, building up the dataset
# choose a random "start word" to begin
# start word starts with " or first or second starts with capital letter
# Make a list of start words
# loop through, choose a random following word
# stop at a stop word
# word ends with a . ? ! ... or second to last character

# why a hashtable? Good way to relate info, associate key/value pair
# frequent lookups, key: word, value: list of words that can follow that word

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words) -> prints whole text
    # split into words
split_words = words.split()


# TODO: analyze which words can follow other words
# Your code here
dataset = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    # if word is not in the dataset, add it in
    if word not in dataset:
        dataset[word] = [next_word]
    # word is in dataset, so add to the list
    else:
        dataset[word].append(next_word)

# Make a list of start words
start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)


# TODO: construct 5 random sentences
# Your code here
# TODO: wrap around another loop to get 5 random sentences

stopped = False
stop_signs = "?.!"
count = 0

while count < 5:
    count += 1
    stopped = False
    print(count)
    while not stopped:
        print(word, end=" ")
        # if stop word, stop
        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True
        # choose a randon following word
        following_words = dataset[word]
        word = random.choice(following_words)
