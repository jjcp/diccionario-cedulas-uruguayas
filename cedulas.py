def digitoVerificador (numero):
    suma = 0
    for x in range(0, 7):
        suma += int(numero[x])
    return suma % 10

def crearDiccionarioCedulas (nombre):
    try:
        cedulas = open(nombre, 'x')
    except FileExistsError:
        print('Error: el archivo %s ya existe' % nombre)

    for x in range(6000000, -1, -1):
        num = str(x).zfill(7)
        print(num + str(digitoVerificador(num)), file=cedulas)

    cedulas.close()

crearDiccionarioCedulas('cedulas.txt')
