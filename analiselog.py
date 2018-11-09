#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Programa de Análise de Log.

from analiselog_db import artigo_maisacessado, autores_maispopulares
from analiselog_db import erro_requisicao

titulo = artigo_maisacessado()
artigo = autores_maispopulares()
error = erro_requisicao()

print("Quais são os três artigos mais populares de todos os tempos?\n")
for row in titulo:
    print('"{}" -- {} views'.format(row[0], row[1]))
print("\n")
print("Quem são os autores de artigos mais populares de todos os tempos?\n")
for row in artigo:
    print('"{}" -- {} views'.format(row[0], row[1]))
print("\n")
print("Em quais dias mais de 1% das requisições resultaram em erros?\n")
print("Em qual dia teve a maior porcentagem de erros?\n")
print('Day: "{}" -- {}'.format(error[0][0], error[0][1]))
print("\n")
