print("Digite a quantidade de palavras da sua list")
list = []
word_number = int(input())

counter = 0
while counter < word_number:
    list.append(input("Insira a palavra:"))
    counter = counter + 1

print("Sua lista é: ", list)

word4 = list[4]

del list[4]
list.insert(1, word4)
list.append(word4)

print("\nSua nova lista é: ", list)