import os
import time
import math

def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2 if num2 != 0 else float("nan")

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            print('Calculadora')
            print('----------------------------------\n')

            num1 = float(input("Primeiro número: "))
            operador = input("Operador (+, -, *, / ou q para sair): ")

            if operador.lower() == 'q':
                break

            num2 = float(input("Segundo número: "))

            resultado = calculadora(num1, num2, operador)

            if math.isnan(resultado):
                print("\nOperação inválida!")
            else:
                print(f"\nResultado: {resultado}")

            input("\nEnter para continuar...")

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')