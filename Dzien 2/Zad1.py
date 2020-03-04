
word = input('podaj tekst > 7')
center = len(word)//2
word_new = word[center - 1] + word[center] + word[center + 1]

print(word_new)