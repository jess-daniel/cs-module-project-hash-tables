# Your code here
cache = {}

chars_to_ignore = "\" : ; , . - + = / \ | [ ] { } ( ) * ^ &"


def hist(filename):
    with open(filename) as file:
        data = file.read()

        words = data.lower().split()

        new_words = [word.strip(chars_to_ignore) for word in words]

        for word in new_words:
            if word not in cache:
                cache[word] = 1
            cache[word] += 1
        sorted_cache = sorted(cache.items(), key=lambda x: x[1], reverse=True)
        for word in dict(sorted_cache).items():
            print(f"{word[0]}  {(word[1] * '#').rjust(20)}")


print(hist("robin.txt"))
