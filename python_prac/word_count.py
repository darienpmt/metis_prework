n, words = 4, ['bcdef', 'abcdefg', 'bcde', 'bcdef']

word_dict = {}

for word in words:
    word_dict.setdefault(word, 0)
    word_dict[word] += 1

print(len(word_dict))
print(*word_dict.values())
