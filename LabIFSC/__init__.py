#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .geral import TODAS_AS_UNIDADES, MAPA_DE_DIMENSOES, PREFIXOS_SI_LONGOS, PREFIXOS_SI_CURTOS, PREFIXOS_SI, analisa_numero, analisa_unidades, calcula_dimensao, parse_dimensions, acha_unidade, unidades_em_texto
from .medida import Medida, M
from .unidade import Unidade
from .lista_de_unidades import registra_unidades
from .matematica import cos, sin, tan, cot, sec, csc, arc_cos, arc_sin, arc_tan, log, log10, log2, ln, sqrt, cbrt
from .tabela import media, desvio_padrao, linearize, compare


__all__ = [
    "TODAS_AS_UNIDADES", "MAPA_DE_DIMENSOES", "PREFIXOS_SI_LONGOS", "PREFIXOS_SI_CURTOS", "PREFIXOS_SI", "analisa_numero", "analisa_unidades", "calcula_dimensao", "parse_dimensions", "acha_unidade", "unidades_em_texto",
    "Medida", "M",
    "Unidade",
    "registra_unidades",
    "cos", "sin", "tan", "cot", "sec", "csc", "arc_cos", "arc_sin", "arc_tan", "log", "log10", "log2", "ln", "sqrt", "cbrt",
    "media", "desvio_padrao", "linearize", "compare"
]

def init():
    global TODAS_AS_UNIDADES
    registra_unidades()

init()