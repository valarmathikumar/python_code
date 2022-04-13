"""QUESTION: Longest word from the given text"""

sentence = input("Enter the sentence:\n")
words = sentence.split()

# consider first word as longest word. if any other word greater than this replace it to largest_word
word_length = len(words[0])
largest_word = words[0]
for i in words:
    length = len(i)
    if length > word_length:
        word_length = length
        largest_word = i
print("longest word:", largest_word)
