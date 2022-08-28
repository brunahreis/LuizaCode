# Types
idade = 27
ano = 1995

print(type(idade))
print(type(ano))

altura = 1.75
peso = 60.0

print(type(altura))
print(type(peso))

semana = False
feriado = True

print(type(semana))
print(type(feriado))

nome = 'Marcia'
profissao = 'Desenvolvedora'

print(type(nome))
print(type(profissao))


# Variaveis
velocidade_do_carro = 200
print(velocidade_do_carro)

frase_boas_vindas = 'Sejam bem vindas ao LuizaCode'
print(frase_boas_vindas)

# Operadores
quatro = 4
dois = 2

soma = quatro + dois
print(soma)

subtracao = quatro - dois
print(subtracao)

multiplicacao = quatro * dois
print(multiplicacao)

divisao = quatro / dois
print(divisao)

divisao_inteira = quatro // dois
print(divisao_inteira)

modulo = quatro % dois
print(modulo)

exponenciacao = quatro ** dois
print(exponenciacao)


# Operadores comparativos

variavel = 5

if variavel == 5:
    print('Os valores são iguais')
    
if variavel != 7:
    print('O valor da variável não é igual a 7')

if variavel > 2:
    print('O valor da variável é maior que dois')
    
if variavel >= 5:
    print('O valor da variável é maior ou igual a 5')

if variavel < 7:
    print('O valor da variável é menor que 7')

if variavel <= 5:
    print('O valor da variável é menor ou igual a 5')
    
# Operadores de atribuição
numero = 5

numero += 7
print(numero)

numero = 5 
numero -= 3
print(numero)

numero = 5 
numero *= 2
print(numero)

numero = 5 
numero /= 4
print(numero)

numero = 5 
numero %= 2
print(numero)

# Operadores lógicos

num1 = 7
num2 = 4

#exemplo operador and
if num1 > 3 and num2 < 8:
    print('As duas condições são verdadeiras')

#exemplo operador or
if num1 > 4 or num2 <= 8:
    print('Uma ou duas das condições são verdadeiras')
    
# exemplo operador not
if not (num1 > 30 and num2 > 8):
    print('Inverte o resultado da condição entre os parâmetros')
    
lista = ['a', 'b', 'c', 'd'] 
if 'c' not in lista: 
    print('não tem o c na lista') 
else: 
    print('tem o c na lista')