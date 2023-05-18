import random
from enum import Enum

SIMULACOES = 300
RODADAS = 1000
SALDO_INICIAL = 300


class Comportamento(Enum):
    IMPULSIVO = 1
    EXIGENTE = 2
    CAUTELOSO = 3
    ALEATORIO = 4
