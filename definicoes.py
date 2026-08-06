from equipamentos import Arma, Armadura
from habilidades import Habilidade, Magia
from inimigos import Inimigo
from personagem import Guerreiro, Mago

def criar_skills():

    #Habilidades:
    def efeito_golpe_forte(lancador, alvo):
         alvo.receber_dano(18)

    def efeito_golpe_cruzado(lancador, alvo):
         alvo.receber_dano(40)

    def efeito_escudo_protetor(lancador, alvo):
        lancador.escudo = True
        lancador.escudo_turnos = 2
        print(f'{lancador.nome} sofre -50% de dano por 2 turnos.')
    
    golpe_forte = Habilidade('Golpe Forte', 5, efeito_golpe_forte, 'Energia -5\tDano = 18')
    golpe_cruzado = Habilidade('Golpe Cruzado', 15, efeito_golpe_cruzado, 'Energia -15\tDano = 40')
    escudo_protetor = Habilidade('Escudo Protetor', 15, efeito_escudo_protetor, 'Energia -15\tDano sofrido -50%\tTurnos 2')

    #Magias:
    def efeito_fireball(lancador, alvo):
        alvo.receber_dano(40)

    def efeito_gelo(lancador, alvo):
        alvo.receber_dano(25)

    def efeito_cura(lancador, alvo):
        lancador.hp += 25

    fireball = Magia('Bola de Fogo', 12, efeito_fireball, 'Mana -12\tDano = 40')
    gelo = Magia('Gelo', 8, efeito_gelo, 'Mana -8\tDano = 25')
    cura = Magia('Cura', 10, efeito_cura, 'Mana -10\tHp +25')

    return [golpe_forte, golpe_cruzado, escudo_protetor], [fireball, gelo, cura]

def criar_armas():
    espada = Arma('Espada Longa', 'corpo', bonus_forca=10)
    cajado = Arma('Cajado', 'magico', bonus_inte=5, bonus_mana=5)
    return [espada, cajado]

def criar_armaduras():
    armadura_ferro = Armadura('Armadura de Ferro', bonus_defe=10)
    tunica = Armadura('Túnica', bonus_defe=5, bonus_inte=5)
    return [armadura_ferro, tunica]

def criar_inimigos():
    golpe_forte = Habilidade('Golpe Forte', 5, lambda lancador, alvo: alvo.receber_dano(15), '')
    lobo = Inimigo('Lobo', 50, 10, 12, 8, 5, 0, 15)
    lobo.add_habilidade(golpe_forte)

    esqueleto = Inimigo('Esqueleto', 40, 15, 15, 5, 3, 0, 15)
    esqueleto.add_habilidade(golpe_forte)

    baforada = Magia('Baforada', 50, lambda lancador, alvo: alvo.receber_dano(150), '')
    garra = Habilidade('Garras', 25, lambda lancador, alvo: alvo.receber_dano(65), '')
    dragao = Inimigo('Dragão', 328, 58, 38, 48, 60, 120, 100)
    dragao.add_habilidade(baforada)
    dragao.add_habilidade(garra)

    return [lobo, esqueleto], [dragao]

def criar_personagem():
        guerreiro = Guerreiro('', 'Guerreiro', 120, 15, 10, 10, 5, 25)
        mago = Mago('', 'Mago', 80, 5, 10, 10, 15, 45)
        return [guerreiro, mago]