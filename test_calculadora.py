import io
from unittest import mock

import pytest

from calculadora import (
    calculadora, divisao, multiplicacao, principal,
    processa_expressao, soma, subtracao,
)


@pytest.fixture
def digita(monkeypatch):
    """
    Recebe uma lista de strings que serão consideradas como entrada do usuário
    na stdin
    """

    def digita(entrada):
        output = "\n".join(entrada)
        monkeypatch.setattr('sys.stdin', io.StringIO(output))

    return digita


@pytest.fixture
def checa_saida(capsys):
    """
    Captura toda saída do programa (stdout e stderr) e compara com o esperado
    pelo argumento saída
    """

    def checa_saida(saida_esperada):
        saida_real = capsys.readouterr()
        saida_real = saida_real.out.split('\n')[:-1]
        assert saida_real == saida_esperada

    return checa_saida


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


def test_processa_expressao_sem_espaco():
    assert processa_expressao("1+-5") == (1, -5, '+')
    assert processa_expressao("1/5") == (1, 5, '/')
    assert processa_expressao("100/    124") == (100, 124, '/')


def test_calculadora_soma():
    assert calculadora("1 + 5") == 6
    assert calculadora("5 + 3") == 8


def test_calculadora_subtracao():
    assert calculadora("3 - 2") == 1
    assert calculadora("1 - 4") == -3


def test_calculadora_multiplicacao():
    assert calculadora("4 * 5") == 20
    assert calculadora("100 * 6") == 600


def test_calculadora_divisao():
    assert calculadora("4 / 2") == 2


def test_calculadora_float():
    assert calculadora("3 / 2") == 1.5
    assert calculadora("1.5 + 1") == 2.5 


def test_principal_soma(digita, checa_saida):
    digita(["1 + 5", "fim"])

    principal()

    checa_saida(["Digite a expressão:", "= 6.0"])


def test_principal_soma_subtracao(digita, checa_saida):
    digita(["3 + 6", "7 - 4", "fim"])

    principal()

    checa_saida(["Digite a expressão:", "= 9.0", "= 3.0"])


def test_fecha_programa_exit(digita, checa_saida):
    digita(["exit"])

    principal()

    checa_saida(["Digite a expressão:"])


def test_fecha_programa_ctrld(digita, checa_saida):
    with mock.patch("calculadora.input") as input_mock:
        input_mock.side_effect = EOFError
        principal()

    checa_saida(["Digite a expressão:"])

