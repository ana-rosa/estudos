"""
Calculadora básica
==================

- Soma
- Subtração
- Divisão
- Multiplicação
- Calculadora barata de 1 operação com memória -> Recebe operação como texto e retorna valor
    - Soma
    - Subtração
    - Multiplicação
    - Divisão
- Suporte a float
- Interface -> texto? CLI?
    $ python calculadora.py
    Digite a expressão:  # saída
    1 + 5                # entrada
    = 6.0                  # saída
    $ python calculadora.py
    Digite a expressão:
    2 * -5
    = -10.0
- Interação/iteração
    $ python calculadora.py
    Digite a expressão:
    1 + 5
    = 6.0
    4 - 2
    = 2.0
    3 * 10
    = 30.0
    fim
- Interromper programa com ctrl+d ou digitando 'exit'
    - exit
    - ctrl+d
- Fazer expressões funcionarem sem espaço:
    1+ 5
    = 6.0
    1-10
    = -9.0
    1+-5
    = -4.0

- Tratar erros
- Memória -> pensar sobre
- Fazer resultado retornar inteiro se a entrada for inteira, por ex:
    1 + 5
    = 6
    e não 6.0
"""


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def divisao(a, b):
    return a / b


def multiplicacao(a, b):
    return a * b


def processa_expressao(expressao):
    for caracter in expressao:
        # if caracter == "+" or caracter == "-" or caracter == "*" or caracter == "/":
        if caracter in "+-*/":
            operacao = caracter
            break

    a, b = expressao.split(operacao)
    return float(a), float(b), operacao


def calculadora(expressao):
    a, b, operacao = processa_expressao(expressao)
    if operacao == "-":
        resultado = subtracao(a,b)
    elif operacao == "+":
        resultado = soma(a,b)
    elif operacao == "*":
        resultado = multiplicacao(a,b)
    elif operacao == "/":
        resultado = divisao(a,b)
    return resultado


def principal():
    print('Digite a expressão:')
    while True:
        try:
            expressao = input()
        except EOFError:
            break

        if expressao in ("fim", "exit"):
        # if expressao == "fim" or expressao == "exit":
            break
        resultado = calculadora(expressao)
        print('=', resultado)


if __name__ == '__main__':
    # chamado ao rodar python calculadora.py
    # e NUNCA chamado ao rodar import calculadora
    principal()
