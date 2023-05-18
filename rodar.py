from main import Jogo, Jogador, Comportamento, SIMULACOES

print('teste')
print(Comportamento.ALEATORIO)

jogo = Jogo(num_simulations=SIMULACOES)
jogo.add_jogador(Jogador(comportamento=Comportamento.IMPULSIVO))
jogo.add_jogador(Jogador(comportamento=Comportamento.EXIGENTE))
jogo.add_jogador(Jogador(comportamento=Comportamento.CAUTELOSO))
jogo.add_jogador(Jogador(comportamento=Comportamento.ALEATORIO))
jogo.simulate()
