import string
letters = list(string.ascii_lowercase)

def cesar(message, passcode):
    result = ""
    for i in message:
        if i in letters:
            index = (letters.index(i) + passcode) % 26
            result += letters[index]
        else:
            result += i
    return result


def cesarCipher():
    message = input("Ingrese el mensaje que quiere cifrar: ").lower()
    passcode = int(input("Ingrese la clave numérica para el cifrado: "))

    encrypted = cesar(message, passcode)
    print(f"Frase encriptada: {encrypted}")


def cesarDecryption():
    message = input("Ingrese el mensaje cifrado que quiere descifrar: ").lower()
    print()
    askPasscode = input("¿Conoce la clave? (si/no): ").lower()

    match askPasscode:
        case 'si':
            passcode = int(input("Ingrese la clave: "))
            decrypted = cesar(message, -passcode)
            print(f"El mensaje descifrado es: {decrypted}")

        case 'no':
            print("\nIniciando fuerza bruta:\n")
            for passcode in range(1, 26):
                decrypted = cesar(message, -passcode)
                print(f"Clave {passcode}: {decrypted}")

        case _:
            print("Opción inválida")
            cesarDecryption()


while True:

    print('''
    
Menú cifrado césar: 
    1. Cifrar un mensaje
    2. Descifrar un mensaje
    3. Salir
    ''')

    option = int(input("Ingrese la opción que desee: "))

    match option:
        case 1:
            cesarCipher()
        case 2:
            cesarDecryption()
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Ingrese un número válido")