#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Conecta no Banco de dados 'News' e retorna os valores.

import psycopg2


def artigo_maisacessado():
    """Função que retorna todos os artigos"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select a.title, count(l.path) || ' views' as view from articles\
    as a join log as l on substring(path from 10)=a.slug group by a.title \
    order by count(a.title) desc limit 3")
    return c.fetchall()
    db.close()
    
    
def autores_maispopulares():
    """Função que retorna os autores de artigos mais populares de todos os
    tempos"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select at.name, count(l.path) as view from articles as a join \
    log as l on substring(path from 10)=a.slug join authors as at \
    on at.id=a.author group by at.name order by count(at.name) desc")
    return c.fetchall()
    db.close()
    
    
def erro_requisicao():
    """Função que retorna em quais dias ocorerram mais de 1% de requisições com
    erro"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select to_char(cast(time as date), 'FMMonth DD, YYYY'), \
    round(cast(count(path) / cast(total.Total as numeric(10,2)) * 100 as \
    numeric(10,2)), 2) || '% error' as percentual from log, \
    (select cast(time as date) as Totalerror, count(path) as Total from \
    log group by cast(time as date) order by cast(time as date) asc) as \
    total where substring(status, 1, 1)='4' and \
    total.Totalerror=cast(time as date) group by cast(time as date), \
    total.Total order by cast(count(path) / \
    cast(total.Total as numeric(10,2)) \
    * 100 as numeric(10,2)) desc limit 1")
    return c.fetchall()
    db.close()
