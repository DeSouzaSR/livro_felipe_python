# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 17:13:04 2025

@author: srsouza

Calculadora para o cálculo do imposto de renda
"""

imposto = 27.
salario = int(input('Salário? '))


def salario_descontado(salario, imposto = 27.):
    return salario - (salario * imposto * 0.01)


while imposto > 0.:
    imposto = input('Imposto ou (s) para sair: ')
    if not imposto:
        imposto = 27.
    elif imposto == 's' or imposto == 'S':
        break
    else:
        imposto = float(imposto)
    novo_salario = salario_descontado(salario, imposto)
    print(f'Com imposto de {imposto}% o valor real: {novo_salario}')


