def permutation(word, k=0):
    if (k == len(word)):
        print word
    else:
        for index in range(k, len(word)):
            word[k], word[index] = word[index], word[k]
            permutation(word, k + 1)
            word[k], word[index] = word[index], word[k]

permutation(list("abc"))

