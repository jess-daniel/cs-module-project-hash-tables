def no_dups(s):
    cache = {}

    word_lst = s.split()

    no_dup_lst = []

    for word in word_lst:
        if word not in cache:
            cache[word] = True
            no_dup_lst.append(word)
    results = " ".join(no_dup_lst)

    return results


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
