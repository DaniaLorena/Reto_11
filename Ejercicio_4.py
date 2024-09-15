
#Se crea una funcion para llenar la matriz
def llenar_matriz ():
    num_filas = int (input("Ingrese el numero de las filas: ")) #Se pide ingresar numero de filas
    num_colum = int (input("Ingrese el numero de las columas: "))#Se pide ingresar numero de columnas que tenga cada matriz
    matriz : list = [] # Se crea una lista o matriz vacia
    for i in range (num_filas): #Recorrer numero de filas
        fila: list =[] #Se crea una lista vacia que almacenara las filas
        for j in range (num_colum):
            elemento = int (input (f"Elemento {[i]}{[j]}: ")) #Se ingresa el elemto
            fila.append(elemento) #Se agrega el elemento a la fila
        matriz.append(fila) #Se agrega la fila a la matriz
    for i in range (len(matriz)): #Imprime la matriz en forma de la misma
        print (matriz[i])
    return matriz #Retorna la matriz

def suma_columnas (matriz): #Funcion para la suma de columnas
    columna = int (input("¿Que columna de la matriz desea sumar? TENGA EN CUENTA QUE LA COLUNMA EMPIEZA DESDE 0: "))
    if (columna <= len(matriz[0])): # Se verifica   que el ingreso de la columna a sumar este dentro del rango de las columnas que conforman la matriz
        suma = 0
        for i in range (len(matriz)):#Recorre las filas de la matriz
            suma += matriz [i][columna] #Suma el elemento de la columna seleccionada
        print (f"La suma de la columa {columna} es {suma}") 
    if (columna > len(matriz[0]) or columna < len(matriz[0])): # Si el numero de la columna ingresa es mayor al rango se retorna un mensaje de columna invalida
        print ("El numero de columna ingresado es invalido")


if __name__ == "__main__": #Funcion principal
    matriz = llenar_matriz() #Se hacen uso de las funciones
    suma_columnas(matriz)