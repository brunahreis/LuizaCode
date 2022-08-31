numero_escolhido = int(input('Digite um numero inteiro positivo: '))

fatorial = numero_escolhido

while numero_escolhido > 1:
  numero_escolhido = numero_escolhido - 1
  fatorial = fatorial * numero_escolhido

print (fatorial)