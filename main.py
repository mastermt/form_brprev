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


class Jogador:
    def __init__(self, comportamento):
        self.comportamento = comportamento
        self.saldo = SALDO_INICIAL 
        self.propriedades = []
        self.vitorias = 0


class Jogo:
    def __init__(self, num_simulations):
        self.num_simulations = num_simulations
        self.jogadores = []

    def add_jogador(self, jogador):
        self.jogadores.append(jogador)
