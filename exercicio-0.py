#0) Faça um programa que tenha uma função que calcule a soma de dois números.#

def soma(x, y):
    return x+y

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))

    resultado = soma(x=num1, y=num2)
    print(f'{num1} + {num2} = {resultado}') 