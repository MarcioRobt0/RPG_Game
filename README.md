# 🎮 RPG Game

Um jogo RPG baseado em turnos desenvolvido em Python, com sistema de combate dinâmico, personagens com classes distintas e progressão por batalhas.

## 📋 Descrição

RPG Game é um projeto pessoal que implementa um sistema de RPG completo com:
- **2 Classes de Personagens**: Guerreiro e Mago
- **Sistema de Combate em Turnos**: Batalhas interativas baseadas em turnos
- **Equipamentos**: Armas e armaduras que modificam atributos
- **Habilidades Especiais**: Cada classe possui habilidades únicas com custos de recursos
- **Inimigos**: Adversários com níveis de dificuldade variados, do Lobo ao temido Dragão

## 🚀 Como Jogar

### Requisitos
- Python 3.6+

### Executar o Jogo

```bash
python main.py
```

### Fluxo do Jogo

1. **Menu Principal**: Escolha entre Jogar ou Sair
2. **Criação do Personagem**:
   - Insira seu nome
   - Escolha sua classe (Guerreiro ou Mago)
   - Selecione 2 habilidades/magias
   - Equipar uma arma
   - Equipar uma armadura

3. **Combate**: Enfrente 3 rodadas de batalhas:
   - 2 inimigos normais (Lobo, Esqueleto)
   - 1 chefe final (Dragão)

4. **Sistema de Turnos**:
   - Escolha atacar ou usar uma habilidade/magia
   - Inimigos atacam automaticamente
   - A velocidade (DEX) determina quem ataca primeiro
   - Derrotar o dragão significa vitória!

## 🎭 Classes de Personagens

### Guerreiro ⚔️
- **HP**: 120
- **Força**: 15
- **Defesa**: 10
- **Energia**: 25 (recurso para habilidades)
- **Habilidades Disponíveis**:
  - **Golpe Forte**: Causa 18 de dano (Custo: 5 energia)
  - **Golpe Cruzado**: Causa 40 de dano (Custo: 15 energia)
  - **Escudo Protetor**: Reduz dano em 50% por 2 turnos (Custo: 15 energia)

### Mago 🔮
- **HP**: 80
- **Inteligência**: 15
- **Mana**: 45 (recurso para magias)
- **Magias Disponíveis**:
  - **Bola de Fogo**: Causa 40 de dano (Custo: 12 mana)
  - **Gelo**: Causa 25 de dano (Custo: 8 mana)
  - **Cura**: Recupera 25 HP (Custo: 10 mana)

## 👹 Inimigos

| Nome | HP | Força | Defesa | Dificuldade |
|------|-------|-------|--------|-------------|
| Lobo | 50 | 12 | 5 | ⭐ Fácil |
| Esqueleto | 40 | 15 | 3 | ⭐ Fácil |
| Dragão | 328 | 38 | 60 | ⭐⭐⭐⭐⭐ Lendário |

## 📊 Atributos do Personagem

- **HP (Health Points)**: Pontos de vida
- **Força**: Dano físico aumentado
- **Destreza (DEX)**: Velocidade e chance de atacar primeiro
- **Defesa (DEF)**: Reduz dano recebido
- **Inteligência (INT)**: Aumenta dano mágico
- **Energia/Mana**: Recurso para usar habilidades/magias

## 📂 Estrutura do Projeto

```
RPG_Game/
├── main.py                 # Ponto de entrada do jogo
├── executar.py             # Lógica principal do jogo
├── batalha.py              # Sistema de combate em turnos
├── personagem.py           # Classes de personagens
├── habilidades.py          # Sistema de habilidades e magias
├── equipamentos.py         # Classes de armas e armaduras
├── inimigos.py             # Definição dos inimigos
├── definicoes.py           # Criação de recursos (skills, armas, inimigos)
└── README.md               # Este arquivo
```

### 📝 Descrição dos Arquivos

**main.py**
- Ponto de entrada simples que chama a função `jogo()`

**executar.py**
- Contém a lógica principal do jogo
- `jogo()`: Loop principal do menu
- `criar_Player()`: Sistema de criação de personagem
- `batalhas()`: Orquestra as 3 rodadas de combate

**batalha.py**
- `iniciar_batalha()`: Gerencia a lógica de combate completo
- `turno_personagem()`: Permite o jogador escolher ações
- `turno_inimigo()`: Lógica de IA dos inimigos
- `calcular_dano()`: Sistema de cálculo de dano
- Funções utilitárias: `limpar_tela()`, `tecla()`

**personagem.py**
- `Personagem`: Classe base com atributos e métodos comuns
- `Guerreiro`: Classe especializada com Energia
- `Mago`: Classe especializada com Mana

**habilidades.py**
- `Skill_Interface`: Interface abstrata para habilidades
- `Habilidade`: Habilidades que usam Energia
- `Magia`: Magias que usam Mana

**equipamentos.py**
- `Equipamento`: Classe base com bônus de atributos
- `Arma`: Equipamento com tipo (corpo, magia)
- `Armadura`: Equipamento defensivo

**inimigos.py**
- `Inimigo`: Classe que define adversários com suas próprias habilidades

**definicoes.py**
- `criar_skills()`: Define todas as habilidades e magias
- `criar_armas()`: Define as armas disponíveis
- `criar_armaduras()`: Define as armaduras disponíveis
- `criar_inimigos()`: Define os inimigos normais e chefe
- `criar_personagem()`: Define os personagens jogáveis

## 🎮 Mecânicas Principais

### Sistema de Combate
- Turnos alternados baseados em Destreza
- Dano = Atributo do Atacante - Defesa do Defensor
- Mínimo de 1 ponto de dano
- Escudo especial do Guerreiro reduz dano em 50%

### Equipamento
- Equipar itens fornece bônus de atributos
- Trocar equipamento remove bônus anterior e aplica novo
- Sistema de inventário com limite de slots

### Recursos
- **Guerreiro**: Usa Energia para habilidades
- **Mago**: Usa Mana para magias
- Ambas regeneram 2-3 pontos por turno

## 🔧 Desenvolvimento Futuro

Possíveis melhorias:
- [ ] Sistema de experiência e níveis
- [ ] Mais classes de personagens
- [ ] Mais variedade de inimigos
- [ ] Sistema de itens no chão
- [ ] Efeitos visuais/animações
- [ ] Salvamento de progresso
- [ ] Dificuldade configurável

## 📄 Licença

Este é um projeto pessoal sem licença específica.

## 👨‍💻 Autor

**MarcioRobt0** - Desenvolvedor

---
