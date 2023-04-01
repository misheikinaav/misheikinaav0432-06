string = input("Введите текст: ")

words = string.split()

longest_word = max(words, key=len)

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)

print("Самое длинное слово:", longest_word)
print("Наиболее часто встречающееся слово:", most_common_word)