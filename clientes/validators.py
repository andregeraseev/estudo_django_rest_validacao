import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    """Verifica se o campo CPF eh valido'"""
    cpf = CPF()
    return cpf.validate(numero_do_cpf)


def nome_valido(nome):
    """Verifica se o campo nome tem apenas letras"""
    return nome.isalpha()


def rg_valido(numero_rg):
    """Verifica se o campo nome tem 9 digitos"""
    return len(numero_rg) == 9


def celular_valido(numero_celular):
    """Verifica se o celular e valido (11 98129-8667)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
