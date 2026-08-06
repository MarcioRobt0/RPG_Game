from definicoes import criar_skills, criar_armas, criar_armaduras, criar_inimigos, criar_personagem
from batalha import iniciar_batalha, limpar_tela, tecla
import random

def jogo():
    while True:
        print('The End:\n1- Jogar\n2- Sair')
        op = input('> ')

        if op == '1':
            limpar_tela()
            criar_Player()
        elif op == '2':
            print('\nSaindo do Jogo...')
            break
        else:
            print('Escolha inválida!')

def criar_Player():
    habilidades, magias = criar_skills()
    armas = criar_armas()
    armaduras = criar_armaduras()
    inimigos, morte = criar_inimigos()
    players = criar_personagem()

    #----------------------------criar player
    nome = input('Olá aventureiro. Qual o seu nome? ')
    limpar_tela()
    print('Escolha seu personagem:\n')
    for i, player in enumerate(players):
        print(f'{i+1}- '), player.info()
        print()

    try:
        op_pers = int(input('> '))
        player = players[op_pers-1]
    except (ValueError, IndexError):
        print('Escolha inválida!')
        tecla()
        limpar_tela()
        return
    
    player.nome = nome
    limpar_tela()

    print('Você escolheu:')
    print(player.classe)
    print()

    #-------------------------------add skills:
    if player.classe == 'Guerreiro':
        skills_ = habilidades
    elif player.classe == 'Mago':
        skills_ = magias
    else:
        print('Erro!')
        return
    
    print('Escolha duas Skills:\n')
    for i, skill in enumerate(skills_):
        print(f'{i+1}- {skill.nome}\nDescrição: {skill.descricao}')
        print()

    while len(player.skills) < 2:
        try:
            op_skill = int(input('> '))
            if 0 < op_skill <= len(skills_):
                skill = skills_[op_skill-1]
                if skill not in player.skills:
                    player.skills.append(skill)
                else:
                    print('Skill já escolhida.')
            else: 
                print('Skill inválida.')
        except ValueError:
            print('Escolha inválida.')
    
    limpar_tela()
    print('Você selecionou as seguintes skills:')
    for skill in player.skills:
        print(f'{skill.nome}\nDescrição: {skill.descricao}')
        print()
    
    tecla()
    limpar_tela()

    #----------------------------add arma:
    while not player.equipamentos["arma"]:
        print('Escolha uma arma:\n')
        for i, arma in enumerate(armas):
            print(f'{i+1}- {arma.nome}\nAtributos:')
            arma.info_equipamento()
            print()

        try:
            op_arma = int(input('> '))
            if 0 < op_arma <= len(armas):
                player.equipamentos["arma"] = armas[op_arma-1]
            else:
                print('Arma inválida.')
        except ValueError:
            print('Escolha inválida.')
    
    limpar_tela()

    print(f'Você selecionou a arma: {player.equipamentos["arma"].nome}')

    tecla()
    limpar_tela()

    #--------------------------add armadura:
    while not player.equipamentos["armadura"]:
        print('Escolha uma armadura:\n')
        for i, armadura in enumerate(armaduras):
            print(f'{i+1}- {armadura.nome}\nAtributos:')
            armadura.info_equipamento()
            print()

        try:
            op_armadura = int(input('> '))
            if 0 < op_armadura <= len(armaduras):
                player.equipamentos["armadura"] = armaduras[op_armadura-1]
            else:
                print('Armadura inválida.')
        except ValueError:
            print('Escolha inválida.')

    limpar_tela()

    print(f'Você selecionou a armadura: {player.equipamentos["armadura"].nome}')

    tecla()
    limpar_tela()

    #-----------------------------batalhas:
    batalhas(player, inimigos, morte)


def batalhas(player, inimigos, morte):
    rodadas = 3

    for i in range(rodadas-1):
        inimigo = random.choice(inimigos)
        print(f'Rodada {i+1}: {player.nome} vs {inimigo.nome}')
        iniciar_batalha(player, inimigo)
        if player.hp <= 0:
            print('GAME OVER!')
            break 
        print(player.hp)
        player.hp = player.hp_Max
        print(player.hp)
    
    print(f'Rodada {rodadas}: {player.nome} vs {morte.nome}')
    iniciar_batalha(player, morte)
    if player.hp > 0:
        print('Será que milagres acontecem?')
    else:
        print('GAME OVER!')