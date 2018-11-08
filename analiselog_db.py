# -*- coding: utf-8 -*-
# Conecta no Banco de dados 'News' e retorna os valores.

import psycopg2

def artigo_maisacessado():
    """Função que retorna todos os artigos"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select a.title, count(l.path) || ' views' as view from articles as a join \
    log as l on substring(path from 10)=a.slug group by a.title \
    order by count(a.title) desc limit 3")
    return c.fetchall()
    db.close()
