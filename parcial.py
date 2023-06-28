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
    opcion = int(input('Elija una opción del siguiente menú\n2- Conocer si el numero ingresado es negativo, positivo o igual a 0\n3- Ingresar numeros, sumatoria y promedio\n4- Salir: '))

    if opcion == 2:
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
        #opcion para salir
        print('¡Espero tengas buen día, adios!')
        break
    else:
        print('Por favor ingrese una opción del menú')

    print ('------------------------------------------------')
