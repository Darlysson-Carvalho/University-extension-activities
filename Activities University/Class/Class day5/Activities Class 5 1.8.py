#Algoritmo para verificar numero positivo e mostrar raiz
a=int(input("Digite um número: "))

if a>=0:
    b=(a**0.5)
    print("A raiz quadrada do numero é", b)
else:
    print("Numero invalido")
