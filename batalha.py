import random
import os
import platform

def tecla():
    input('pressione ENTER para continuar.')

def limpar_tela():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def calcular_dano(atacante, defensor):
    return max(1, atacante.tipo_dano() - defensor.defe)

def iniciar_batalha(personagem, inimigo):
    print(f'Iniciando batalha entre {personagem.nome} e {inimigo.nome}')
    if inimigo.dex > personagem.dex:
        while personagem.hp > 0 and inimigo.hp > 0:
            turno_inimigo(inimigo, personagem)
            tecla()
            limpar_tela()

            if personagem.hp > 0:
                turno_personagem(personagem, inimigo)
                tecla()
                limpar_tela()
            
    else:
        while personagem.hp > 0 and inimigo.hp > 0:
            turno_personagem(personagem, inimigo)
            tecla()
            limpar_tela()

            if inimigo.hp > 0:
                turno_inimigo(inimigo, personagem)
                tecla()
                limpar_tela()

    if personagem.hp > 0:
        print(f'{personagem.nome} venceu a batalha')
    else:
        print(f'{inimigo.nome} venceu a batalha')
    tecla()
    limpar_tela()

def turno_personagem(personagem, inimigo):
    print(f'\nSeu turno')

    while True:
        print('Esclha uma ação:')
        print('1- Atacar\n2- Usar habilidade')
        op = input('> ')

        if op == '1':
            dano = calcular_dano(personagem, inimigo)
            inimigo.receber_dano(dano)
            print(f'{personagem.nome} atacou {inimigo.nome} causando {dano} de dano.')
            personagem.recarrega_elemento(3)
            break 
        elif op == '2':
            if personagem.skills:
                exibir_skills(personagem)
                try:
                    op_skill = int(input('Escolha uma habilidade: '))
                    limpar_tela()
                    if 0 < op_skill <= len(personagem.skills):
                        skill = personagem.skills[op_skill-1]
                        print(skill.nome)
                        if skill.usar(personagem, inimigo):
                            break
                        else:
                            print('ihh')
                            continue
                    else:
                        print('Habilidade inválida!')
                except ValueError:
                    print('Escolha uma habilidade válida.')
            else:
                print(f'{personagem.nome} não tem skills.')
        else:
            print('Ação inválida!')

def turno_inimigo(inimigo, personagem):
    print(f'\nTurno de {inimigo.nome}')

    if inimigo.habilidades and random.choice([True, False]):
        skill = random.choice(inimigo.habilidades)
        if not skill.usar(inimigo, personagem):
            dano = calcular_dano(inimigo, personagem)
            personagem.receber_dano(dano)
            print(f'{inimigo.nome} atacou {personagem.nome} causando {dano} de dano.')
            inimigo.recarrega_elemento(2)
    else: 
        dano = calcular_dano(inimigo, personagem)
        personagem.receber_dano(dano)
        print(f'{inimigo.nome} atacou {personagem.nome} causando {dano} de dano.')
        inimigo.recarrega_elemento(2)

def exibir_skills(personagem):
    print('Skills disponíveis:')
    for i, habilidade in enumerate(personagem.skills):
        print(f'{i+1}. {habilidade.nome} (Custo: {habilidade.custo}) (Descrição: {habilidade.descricao})')