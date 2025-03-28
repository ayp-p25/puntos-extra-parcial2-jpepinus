def contar_digitos_divisores(numero):
    original = numero
    contador = 0
    
    if original == 0:
        return 0
    
    numero = abs(numero)
    
    while numero > 0:
        digito = numero % 10
        if digito != 0 and original % digito == 0:
            contador += 1
        numero = numero // 10
    
    return contador

def main():
    try:
        entrada = input("Introduzca un número: ")
        numero = int(entrada)
        resultado = contar_digitos_divisores(numero)
        print(f"Dígitos divisores: {resultado}")
    except ValueError:
        print("Error: Por favor introduzca un número entero válido.")

if __name__ == "__main__":
    main()