# coding=utf-8
__author__ = 'guillermo'
"""5. Implemente una calculadora simple, en donde se ingrese (por entrada estándar) dos
operandos y el operador (+,-,*, /) e imprima el valor de la operación resultante (por el
momento no tenga en cuenta errores de tipos, ej: que el operando no sea número o que
el operador no sea los enumerados)."""

ope1 = raw_input('ingrese el operando 1: ')
operador = raw_input('ingrese el operador: ')
ope2 = raw_input('ingrese el operador 2: ')

print eval(ope1 + operador + ope2)

