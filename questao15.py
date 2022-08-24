print("Escreva uma frase com caracteres especiais: ")
string = input()

new_string = ''.join(filter(str.isalnum, string))
print(new_string)