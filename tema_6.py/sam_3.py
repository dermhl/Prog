from collections import Counter

def three(s):
    counts = Counter(int(digit) for digit in s)
    most_common = counts.most_common(3)
    top = sorted([item[0] for item in most_common])
    return top

input_str = "583902748193475"
result = three(input_str)
print("Три самых часто встречающихся числа:", result)