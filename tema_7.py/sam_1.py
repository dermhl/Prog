import re
from collections import Counter

f = 'input.txt'
with open(f, 'r', encoding='utf-8') as file:
    text = file.read()

# Очистка текста от пунктуации и разбивка на слова
words = re.findall(r'\b\w+\b', text.lower())
total_words = len(words)
counter = Counter(words)
most_common_word, frequency = counter.most_common(1)[0]

print(f"Общее количество слов: {total_words}")
print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {frequency} раз)")