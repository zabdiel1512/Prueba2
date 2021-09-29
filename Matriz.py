matriz1=[]

matriz2=[]

matrizResultado=[]

 

print("Matriz 3*3")

for a in range(3):

    matriz1.append([])

    for b in range(3):

        matriz1[a].append(input("Ingresar valor de la primera matriz: "))

for c in range(3):

    matriz2.append([])

    for d in range(3):

        matriz2[c].append(input("Ingresar valor de la segunda matriz: "))

 

sumar= matriz1 + matriz2

matrizResultado=(sumar)

print(matrizResultado)