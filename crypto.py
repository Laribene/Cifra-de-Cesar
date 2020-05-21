#import string
import requests


codificado = []
str = ""
mensagem = input("Escreva a mensagem para criptografa-la: ")

mensagem= mensagem.lower()

chave = 11 

for letra in mensagem:
	passou = ord(letra)
	if passou >=123 and passou <=127:
		letra1 = chr(passou)
		codificado.append(letra1)
		print("Passou aqui")
	elif passou >= 32 and passou <=64:
		letra1 = chr(passou)
		codificado.append(letra1)
	elif (passou + chave) > 122 :
		certo=((passou + chave) - 26)
		letra1 = chr(certo)
		codificado.append(letra1)
	else :
		letra1 = chr(passou+ chave)
		codificado.append(letra1)

print(str.join(codificado))