import re
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
num_lines = len(lines)
text = ''.join(lines)
words = re.findall(r'\b\w+\b', text)
num_words = len(words)


letters = re.findall(r'[A-Za-z]', text)
num_letters = len(letters)
print(f"Input file contains:\n{num_letters} letters\n{num_words} words\n{num_lines} lines")