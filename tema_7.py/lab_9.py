def longest_word(file):
    with open(file, encoding= 'utf-8') as f:
        word = f.read().split()
        max_length = len(max(word, key=len))
        for w in word:
            if len(w)==max_length:
                sought_word = w
        if len(sought_word)==1:
            return sought_word[0]
        return sought_word
print(longest_word('input.txt'))
