# -*- coding: utf-8 -*-
# Programa de Análise de Log.

from analiselog_db import artigo_maisacessado, autores_maispopulares
from analiselog_db import erro_requisicao

titulo = artigo_maisacessado()
artigo = autores_maispopulares()
error = erro_requisicao()
