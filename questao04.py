print("Escreva alguma coisa: ")
register = input()
print("Você escreveu isso: " + str(register))
id1 = [char for char in register if char.islower()]
id2 = [char for char in register if char.isupper()]
output = ''.join(id1 + id2)
print( "Essa é a sua palavra exibindo as letras minúsculas primeiro: " + output)