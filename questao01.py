print("Escreva uma palavra:")
word = input()
print("Essa é a sua palavra:", word)
word_size = len(word)
half_the_word = (word_size//2)
new_word = word[0] + word[half_the_word] + word[-1]
print("\nEssas são a primeria letra, a letra do meio e a letra final da sua palavra:", new_word)