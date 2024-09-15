
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
