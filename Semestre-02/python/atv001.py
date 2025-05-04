numInt = int(input('Digite um número inteiro: '))
numFlo = float(input('Digite um número de ponto flutuante: '))
valBol = input('Digite um valor booleano (True ou False): ')

valBol = valBol.lower()
valBol = valBol == 'true'

print(f'''
- Número inteiro: {numInt} (tipo: {type(numInt)})
- Número de ponto flutuante:{numFlo} (tipo: {type(numFlo)})
- Valor booleano: {valBol} (tipo: {type(valBol)})
''')