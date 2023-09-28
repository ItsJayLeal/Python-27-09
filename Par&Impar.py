numero_base = int(input('Digite um valor : '))
valor_resultado = numero_base % 2

if valor_resultado % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")