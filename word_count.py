text = input("Enter text: ")
words = text.lower().split()
word_freq = {word: words.count(word) for word in set(words)}
print("Word frequency:", word_freq)
unique_words = sorted(set(words))
print("Unique words:", unique_words)