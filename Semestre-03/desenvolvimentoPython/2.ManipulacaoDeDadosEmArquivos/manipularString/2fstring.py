# fstring é uma forma de formatar strings de maneira mais simples e legível, introduzida no Python 3.6.
# Ela permite incorporar expressões dentro de strings, prefixando a string com a letra 'f' ou 'F'.

nome = "Alice"
idade = 30
peso = 65.5

#usando .format()
print("Meu nome é {} e eu tenho {} anos. Tenho {}".format(nome, idade, peso))

#usando f-string
print(f"Meu nome é {nome} e eu tenho {idade} anos. Tenho {peso:.0f}kg")

#mais exemplos
from datetime import datetime

hoje = datetime.now()
dataFormatada = hoje.strftime("%d/%m/%Y") #formata a data como dia/mês/ano com metrodo 'format()'
print(dataFormatada)

dataFormatadaFstring = f"{hoje:%d/%m/%Y}" #formata a data como dia/mês/ano com f-string
print(dataFormatadaFstring)