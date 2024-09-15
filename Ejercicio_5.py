
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

def suma_filas (matriz): #funcion para la suma de filas
    fila = int (input("¿Que fila de la matriz desea sumar? TENGA EN CUENTA QUE LA COLUNMA EMPIEZA DESDE 0: ")) 
    if (fila<= len(matriz)): # Se verifica que la fila cumpla con el rango de filas que contiene la matriz
        suma = 0
        for j in range (len (matriz[0])): #Se recorre la colunma de la fila seleccionada
            suma += matriz [fila][j] #Suma cada elemento de la fila
        print (f"La suma de la columa {fila} es {suma}")
    if (fila > len(matriz) or fila < len(matriz) ):
        print ("El numero de columna ingresado es invalido")

#Funcion principal
if __name__ == "__main__":
    matriz = llenar_matriz()
    suma_filas(matriz)