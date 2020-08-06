cache = {}

chars_to_ignore = ":;,.-+=/'"


def word_count(s):
    # Your code here
    # returns a words with their counts
    words = s.split()
    print(words)
    for character in chars_to_ignore:
        # error: list has no object replace
        new_words = words.replace(character, "")
        return new_words
    print(new_words)


word_count("Hello, my cat. And my cat doesn't say hello back.")

# if __name__ == "__main__":
#     print(word_count(""))
#     print(word_count("Hello"))
#     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(word_count(
#         'This is a test of the emergency broadcast network. This is only a test.'))
