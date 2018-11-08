# -*- coding: utf-8 -*-
# Programa de Análise de Log.

from analiselog_db import artigo_maisacessado, autores_maispopulares
from analiselog_db import erro_requisicao

titulo = artigo_maisacessado()
artigo = autores_maispopulares()
error = erro_requisicao()

print("Quais são os três artigos mais populares de todos os tempos?\n")
for i in range(0, len(titulo)):
    print (titulo[i][0], " - ", titulo[i][1])
print("\n")
print("Quem são os autores de artigos mais populares de todos os tempos?\n")
for i in range(0, len(artigo)):
    print (artigo[i][0], " - ", artigo[i][1])
print("\n")
print("Em quais dias mais de 1% das requisições resultaram em erros?\n")
for i in range(0, len(error)):
    print (error[i][0], " - ", error[i][1])
print("\n")
