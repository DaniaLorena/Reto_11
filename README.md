# Reto 11

Aprendiendo sobre Matrices :)

> #### Ejercicio 1
> Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

Condiciones  |
------------- |
- La condición que deben cumplir las matrices para que que se puedan sumar (o restar) es que sean de las misma dimensión, esto es, que tengan el mismo número de filas y el mismo número de columnas|

```pyhton
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
```
> #### Ejercicio 2
> Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

Condiciones  |
------------- |
- la primera debe tener el mismo número de columnas que filas la segunda.
- La matriz resultante del producto quedará con el mismo número de filas de la primera y con el mismo número de columnas de la segunda. |

```pyhton

#Funcion para llenamr la matriz
def llenar_matriz ():
    matriz : list = [] #Se crean e inicializan variables a utilizar
    num_fila = int (input ("Ingrese el numero de filas: "))
    num_colum = int (input ("Ingrese el numero de columnas: "))
    for i in range (num_fila):
        fila :list = [] # Se crea una variable fila que contendra las fila de la matriz
        for j in range (num_colum):
            elemento = float (input (f"Ingrese el elemento en la posicicon {[i]}{[j]}: ")) #Ingreso de los elementos de la matriz por teclado
            fila.append (elemento) #Se agrega el elemento en la fila
        matriz.append(fila) #Se agrega la fila a la amtriz
    return num_fila, num_colum, matriz #Retorna valores que se utilizaran después

#funcipn para multiplicar por un escalar
def multiplicar_esclar (matriz_base):
    filas = len(matriz_base)
    columnas = len(matriz_base[0])
    matriz_operacion = [[0] * columnas for _ in range(filas)] #Se crea una matriz con el mismo numero de filas y columnas de la matriz inicial
    escalar = int (input("Numero esclarar por el cual desea multiplicar la matriz: ")) #Se pide ingresar elo numero por el cual se va a multiplicar la matriz
    for i in range (len (matriz_base)): #Se recorre las filas de la matriz
        for j in range (len(matriz_base [0])): #Se recorre cada elemento de la fila (COLUMNA)
            matriz_operacion[i][j] = escalar * matriz_base [i][j] #Se multiplica cada elemento por el escalar y pasa a llenar la matriz creada para la operacion
    print ("Resultado")
    for i in range (len(matriz_operacion)): #Muestra la nueva matriz en forma de la misma
        print (matriz_operacion[i])

#Funcion para multiplicar dos matrices
def multiplicar_matriz (num_fila_base, num_colum_2, matriz_base, matriz_2): #Argumentos que la funcion utilizara
    filas = num_fila_base #El numero de filas de la primera matriz pasa a ser el numero de filas de la matriz que va a almacenar la operacion
    columnas = num_colum_2 #El numero de columnas de la segunda matriz pasa a ser el numero de columnasde la matriz que va a almacenar la operacion
    matriz_operacion = [[0] * columnas for _ in range(filas)] 
    for i in range(len(matriz_base)): #Recorre las filas de la matriz base
        for j in range(len(matriz_2[0])): #Recorre las columnas de la segunda matriz
            for k in range(len(matriz_2)): #Recorre las filas de la segunda matriz
                matriz_operacion[i][j] += matriz_base[i][k] * matriz_2[k][j] #Multiplica los elemento de las matrices
    print ("\nResultado de multiplicar ambas matrices es: ")
    for i in range (len(matriz_operacion)):
        print (matriz_operacion[i])

#Funcion para comprobar los criterios para multiplicar dos matrices
def condicion (num_colum_base, num_fila_2):
    if num_colum_base == num_fila_2:
        print ("La condicion de que el numero de columnas de la primera matriz sea igual al numero de columnas de la segunda matriz se cumple, puede continuar")
        return True
    else: 
        print ("La condicion para multiplicar las matrices no se cumple")
        return False

#funcion principal
if __name__ == "__main__":
    num_fila_base, num_colum_base, matriz_base = llenar_matriz() #Se llena la primera matriz
    for i in range (len(matriz_base)):#Muestra la matriz como tal
        print (matriz_base[i])
    operacion = int (input (f"Desea multiplicar la matriz por \n 1.Escalar \n 2.Matriz \n ")) #Se pregunta que operacion se desea reaizar
    if operacion == 1: # Si es uno se opera por el escalar
        multiplicar_esclar (matriz_base)
    elif operacion == 2: #Se opera por la matria
        num_fila_2, num_colum_2, matriz_2 = llenar_matriz() #Se llena la matriz dos
        condicion (num_colum_base, num_fila_2) #Se verifica la condicion
        multiplicar_matriz (num_fila_base, num_colum_2, matriz_base, matriz_2) #se operan las matrices


```
> #### Ejercicio 3
> Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

Condiciones  |
------------- |
La traspuesta de una matriz A consiste en intercambiar las filas por las columnas (o las columnas porlas filas) y se denota por: A^T|

```pyhton
Funcion para llenar la matriz
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

```
> #### Ejercicio 4
> Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```pyhton

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
```
> #### Ejercicio 5
> Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```pyhton

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
    if (fila > len(matriz) or fila < len(matriz)):
        print ("El numero de fila ingresado es invalido")

#Funcion principal
if __name__ == "__main__":
    matriz = llenar_matriz()
    suma_filas(matriz)

```
