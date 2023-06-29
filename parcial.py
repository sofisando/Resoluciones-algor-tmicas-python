#funciones
def signo_numero(num):
    if num == 0:
        print('El número es igual a 0')
    elif num <0:
        print('El número es negativo')
    else:
        print('El número es positivo') #funiona

def suma(*args):
    suma = 0
    for arg in args:
        suma += int(arg)
    return suma 

def promedio(*args):
    suma = 0
    longitud = len(args)
    if longitud <= 0:  # evitar división entre 0
        return 0
    for arg in args:
        suma += int(arg)
    return suma / longitud

while True:
    opcion = int(input('Elija una opción del siguiente menú\n1- Cuántas veces una letra\n2- Conocer si el numero ingresado es negativo, positivo o igual a 0\n3- Ingresar numeros, sumatoria y promedio\n4- Calcular la suma de los dígitos de un número\n5- Salir: '))

    if opcion == 1:
        frase = input('Ingrese una frase: ')
        letras = *frase, #Es una tupla
        print(letras)
        diccionario = {}

        for letra in letras:
            cant= frase.count(letra) #Cuantas veces se repite la letra en la frase
            diccionario[letra]=cant
            
        print('Éstas son las letras y las veces que se repite: \n')
        for claves, valor in diccionario.items():
            print(f'{claves} : {valor}')
        # print(diccionario.items())

    elif opcion == 2:
        while True:
            num = input('Ingrese un número entero, si quiere salir ingrese "*": ')
            if num == '*':
                break
            else:
                signo_numero(int(num))
    
    elif opcion == 3:
        #Ingresar numeros, sumatoria y promedio
        lista = []
        while True:
            num = int(input('Ingrese números enteros, si desea salir ingrese 0: '))
            if num == 0:
                break
            else:
                lista.append(num) #funciona
        print(f'La suma de los números ingresados es {suma(*lista)} y el promedio de los mismos es {promedio(*lista)}')

    elif opcion == 4:
        numero = int(input('Ingrese un número: '))
        numero_str = str(numero)
        digitos =  *numero_str,
        
        print(f'Los dígitos del número ingresado son {digitos} y la sumatoria es: {suma(*digitos)}')

    elif opcion == 5:
        #opcion para salir
        print('¡Espero tengas buen día, adios!')
        break
    else:
        print('Por favor ingrese una opción del menú')

    print ('------------------------------------------------')
