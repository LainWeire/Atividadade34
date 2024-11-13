# Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

n = [int(input("Número inteiro:   ")) for item in range(5)]
for i, uff in enumerate(n):
    print(i + 1,"°", '=>', uff)
