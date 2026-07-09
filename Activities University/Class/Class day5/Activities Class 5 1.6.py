#Algoritmo para ler dois números e verificar qual é o maior
a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))

if a==b:
    print("Os dois números são iguais")
elif a>b:
    print("O maior número é", a)
else:
    print("O maior número é", b)
