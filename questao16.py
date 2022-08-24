string = "Faltam 3 meses 2 semanas e 9 dias para o fim do semestre"
result = ''.join(filter(lambda aux: aux if aux.isdigit() else None, string))
print(result)