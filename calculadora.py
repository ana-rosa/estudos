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
    Digite a expressão:
    1 + 4
    = 5
    - 2
    = 3
"""


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def divisao(a, b):
    return a / b


def multiplicacao(a, b):
    return a * b


# def calculadora(expressao):
#     # expressao = "100 + 1"
#     a = float(expressao[0])
#     b = float(expressao[4])
#     operacao = expressao[2]
#
#     if operacao == "+":
#         return soma(a, b)


def processa_expressao(expressao):
    a, operacao, b = expressao.split()
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


def test_soma():
    assert soma(2, 2) == 4
    assert soma(-3, 5) == 2


def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(3, 3) == 0


def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(6, -3) == -2


def test_multiplicacao():
    assert multiplicacao(6, 2) == 12
    assert multiplicacao(3, 3) == 9


def test_processa_expressao():
    assert processa_expressao("1 + 5") == (1, 5, '+')
    assert processa_expressao("100 + 1") == (100, 1, '+')
    assert processa_expressao("100 - 1") == (100, 1, '-')
    assert processa_expressao("100 * 1") == (100, 1, '*')
    assert processa_expressao("100 / 1") == (100, 1, '/')


def test_calculadora_soma():
    assert calculadora("1 + 5") == 6
    assert calculadora("5 + 3") == 8

def test_calculadora_subtracao():
    assert calculadora ("3 - 2") == 1
    assert calculadora ("1 - 4") == -3

def test_calculadora_multiplicacao():
    assert calculadora ("4 * 5") == 20
    assert calculadora ("100 * 6") == 600

def test_calculadora_divisao():
    assert calculadora ("4 / 2") == 2

def test_calculadora_float():
    assert calculadora ("3 / 2") == 1.5
    assert calculadora ("1.5 + 1") == 2.5 

