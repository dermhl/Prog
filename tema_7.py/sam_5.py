import re
with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
words = re.findall(r'\b\w+\b', content)
print(f"В файле содержится {len(words)} слов.")