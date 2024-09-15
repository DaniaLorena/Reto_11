# Funcion para llenar la matriz
def llenar_matriz(matriz):
    matriz =[]
    num_fila : int = int (input (f"Ingrese el numero de filas de la matriz {matriz}: "))
    num_colum : int = int (input (f"Ingrese el numero de columnas de la matriz {matriz}: "))
    for i in range (num_fila):
        fila : list = []
        for j in range (num_colum):
            elemento = int (input(f"Ingrese el elemento de la fila {[i]}{[j]}:"))
            fila.append (elemento)
        matriz.append (fila)
    return num_fila, num_colum, matriz

#funcion para comprobar la condicion necesaria para poder sumar dos matrices
def verificar_criterio(num_fila_1, num_colum_1, num_fila_2, num_colum_2):
    if num_fila_1 == num_fila_2 and num_colum_1 == num_colum_2:
        return True
    else:
        return False

#Funcion de sumar o restar matrices
def suma_resta (operacion, matriz_1, matriz_2, num_fila_1, num_colum_1):
    #Se incializan variables a utilicar
    filas = len(matriz_1) 
    columnas = len(matriz_1[0])
    matriz_operacion = [[0] * columnas for _ in range(filas)] #Se crea una matriz con el mismo numero de filas y columnas que las matrices
    if operacion == 1:
        lista_operacion = [] #Se crea una lista que almacenara la suma de los elemento de las matrices
        for i in range(num_fila_1): # Recorre filas
            for j in range(num_colum_1): # Recorre cada elemento columnas
                matriz_operacion [i][j] = matriz_1 [i][j]+ matriz_2 [i][j] # Se operan dos elementos de dos matrices que tengan la miwsma posicion
        print ("Resultado de la suma es:")
        for i in range(len(matriz_operacion)): #Se imprime la matriz
            print(matriz_operacion[i])
    if operacion == 2:
        lista_operacion = []
        for i in range(num_fila_1): # Recorre filas
            for j in range(num_colum_1): # Recorre cada elemento de la fila (Columna)
                matriz_operacion [i][j] = matriz_1 [i][j] - matriz_2 [i][j]
        print ("Resultado de la resta es:")
        for i in range(len(matriz_operacion)):
            print(matriz_operacion[i])



if __name__ == "__main__":
    #Se crean dos matrices vacias
    matriz_1 = []
    matriz_2 = []
    print ("Llenar Matriz 1")
    num_fila_1, num_colum_1, matriz_1 = llenar_matriz (matriz_1) #Se utiliza la funcion de llenar matriz
    for i in range(len(matriz_1)):
        print(matriz_1[i])
    print ("Llenar Matriz 2")
    num_fila_2, num_colum_2, matriz_2 = llenar_matriz (matriz_2)
    for i in range(len(matriz_2)):#Se imprime la matriz
        print(matriz_2[i])
    condicion = verificar_criterio (num_fila_1, num_colum_1, num_fila_2, num_colum_2) #Se verifica si se pueden sumar ambas amtrices
    if condicion == True: 
        print ("La condicion de operar dos matrices con igual numero de filas y numero de colunmas es verdadera, puede continuar")
        operacion = int (input ("¿Que operacion desea realizar? \n (1.) SUMA \n (2.) RESTA \n  ")) #Se pregunta que operacion desea realizar
        matriz_operacion = suma_resta (operacion, matriz_1, matriz_2, num_fila_1, num_colum_1) #Se operan las matrices
    else: #Si la condicion no se cumple muestra el caso del porque no se puede realizar 
        print ("No se cumple la condicion de tener el mismo numero de filas y columnas en ambas matrices ")
        if num_fila_1 == num_fila_2:
            print ("El numero de filas es diferentes")
        elif num_colum_1 == num_colum_1 :
            print ("El numero de filas es diferentes")
        else:
            print ("Numero numero de filas y columnas es distinto")


