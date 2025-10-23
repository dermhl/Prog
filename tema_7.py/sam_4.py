import re

file = 'input.txt'
sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!"
with open(file, 'r', encoding='utf-8') as f:
    bad_words = f.read().split()
bad_words = [word.lower() for word in bad_words]

pattern = re.compile('|'.join([re.escape(word) for word in bad_words]), re.IGNORECASE)
def replace_bad_words(text):
    def replacer(match):
        word = match.group()
        if word.lower() in bad_words:
            return '*' * len(word)
        return word
    return pattern.sub(replacer, text)

result = replace_bad_words(sentence)
print(result)