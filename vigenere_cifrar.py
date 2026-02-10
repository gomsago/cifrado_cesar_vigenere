#Este apartado solo puede cifrar y descifrar la clave CON CLAVE, no hay opción para descrifrar sin clave

abc = 'abcdefghijklmnopqrstuvwxyz'

def cifrar(c, clave):
    text_cifrar = ''
    i = 0
    for letra in c:
        suma = abc.find(letra) + abc.find(clave[i % len(clave)])
        modulo = suma % len(abc)
        text_cifrar += abc[modulo]
        i += 1
    return text_cifrar


def descifrar(c, clave):
    text_descifrar = ''
    i = 0
    for letra in c:
        resta = abc.find(letra) - abc.find(clave[i % len(clave)])
        modulo = resta % len(abc)
        text_descifrar += abc[modulo]
        i += 1
    return text_descifrar


def main():
    while True:
        print('\n--- MENÚ ---')
        print('1. Cifrar')
        print('2. Descifrar')
        print('3. Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            c = input('Cadena a cifrar: ').lower()
            clave = input('Clave: ').lower()
            print('Resultado:', cifrar(c, clave))

        elif opcion == '2':
            c = input('Cadena a descifrar: ').lower()
            clave = input('Clave: ').lower()
            print('Resultado:', descifrar(c, clave))

        elif opcion == '3':
            print('Programa finalizado')
            break

        else:
            print('Opción inválida, intenta de nuevo')

main()