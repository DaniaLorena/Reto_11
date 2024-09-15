#Funcion para llenar la matriz
def llenar_matriz ():
    num_fila = int (input ("Ingrese el numero de filas:"))
    num_colum = int (input("Ingrese el numero de columnas: "))
    matriz = []
    for i in range (num_fila):
        fila = []
        for j in range (num_colum):
            elemento = int (input(f"Elemento {[i]}{[j]}: "))
            fila.append(elemento)
        matriz.append(fila)
    print ("Matriz Original:") #Se muestra la matriz original
    for i in range (len(matriz)):
        print (matriz[i])
    return num_fila, num_colum, matriz

#funcion para mostrar la transpuesta
def transpuesta ():
    num_fila, num_colum, matriz = llenar_matriz () #Se utiliza la funcion dentro de otra funcion
    fila_trans = num_colum #El numero de filas pasa a ser el numero de columnas de la nueva matriz
    colum_trans = num_fila #El numero de columnas pasa a ser el numero de filas  de la nueva matriz
    matriz_transpuesta = [[0]*colum_trans for _ in range(fila_trans)] #Se crea una matriz con una determinada dimension
    for i in range (len(matriz_transpuesta)): #recorre las filas de la ultima matriz creada
        for j in range (len (matriz_transpuesta[i])):
            matriz_transpuesta [i][j] = matriz [j][i] #EL elemento cambia de posicion
    print ("Matriz transpuesta") #Se muestra la matriz transpuesta
    for i in range (len(matriz_transpuesta)):
        print (matriz_transpuesta[i])



if __name__ == "__main__":
    transpuesta ()