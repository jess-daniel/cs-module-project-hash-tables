cache = {}

chars_to_ignore = " \" : ; , . - + = / \ | [ ] { } ( ) * ^ &"


def word_count(s):
    # Your code here
    # returns a words with their counts
    words = s.lower().split()
    # print(words)

    # strips the chars out while making a new array
    new_words = [word.strip(chars_to_ignore) for word in words]

    for word in new_words:
        cache[word] = new_words.count(word)
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
