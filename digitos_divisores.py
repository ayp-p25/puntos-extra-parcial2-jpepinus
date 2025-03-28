# Codifica aquí tu programa
"""
digitos_divisores.py

Este programa cuenta cuántos dígitos de un número entero dado son divisores exactos de ese número.
Cada ocurrencia de un dígito divisor se cuenta por separado, incluso si el dígito se repite.

Ejemplos:
>>> Introduzca un número: 111
Dígitos divisores: 3

>>> Introduzca un número: 12
Dígitos divisores: 2

>>> Introduzca un número: 1012
Dígitos divisores: 3
"""

def contar_digitos_divisores(numero):
    """
    Cuenta cuántos dígitos del número dado son divisores exactos del mismo.
    
    Args:
        numero (int): El número entero a analizar.
        
    Returns:
        int: Cantidad de dígitos que son divisores del número.
    """
    original = numero
    contador = 0
    
    # Manejo del caso especial cuando el número es 0
    if original == 0:
        return 0
    
    # Convertir el número a positivo para simplificar
    numero = abs(numero)
    
    while numero > 0:
        digito = numero % 10
        # Evitar división por cero
        if digito != 0 and original % digito == 0:
            contador += 1
        numero = numero // 10
    
    return contador

def main():
    """Función principal que maneja la entrada/salida del programa."""
    try:
        entrada = input("Introduzca un número: ")
        numero = int(entrada)
        resultado = contar_digitos_divisores(numero)
        print(f"Dígitos divisores: {resultado}")
    except ValueError:
        print("Error: Por favor introduzca un número entero válido.")

if __name__ == "__main__":
    main()