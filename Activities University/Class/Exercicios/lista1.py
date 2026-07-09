def exercicio1():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    print("Boa tarde, ", nome, sobrenome)


def exercicio2():
    numero = int(input("Digite um número para realizar a multiplicação: "))
    multiplicação = int(input("Digite quantas vezes deseja multiplicar: "))
    print("O resultado da multiplicação é: ", numero * multiplicação)

def exercicio3():
    lista = []
    for i in range (4):
        numero = int(input("Digite um número: "))
        lista.append(numero)
        soma = sum(lista)
    print("A soma dos números é: ", soma)

def exercicio4():
    lista = []
    for i in range(3):
        numero = float(input("Digite um número: "))
        lista.append(numero)
        media = sum(lista) / len(lista)
    print("A média dos números é: ", media)

def exercicio5():
    valor = float(input("Digite o valor do produto: "))
    quantidade = float(input("Digite a quantidade de produtos: "))
    desconto = float(input("Digite o valor do desconto: "))
    valortotal = valor * quantidade
    valordesconto = valortotal * (desconto/100)
    print("O valor total do produto é:", valortotal, "O desconto foi de: ", desconto, "% O valor final ficou", valortotal - valordesconto)

exercicio5()

 