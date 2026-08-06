from equipamentos import Arma, Armadura

class Personagem:

    def __init__(self, nome, classe, hp, forca, dex, defe, inte, limite=10) -> None:
        self._nome = nome
        self._hp_Max = hp
        self._hp = hp
        self._forca = forca
        self._dex = dex
        self._defe = defe
        self._inte = inte
        self._inventario = []
        self._inventario_limite = limite
        self._equipamentos =  {"arma": None, "armadura": None}
        self._skills = []
        self._classe = classe

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @property
    def hp_Max(self):
        return self._hp_Max
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, valor):
        self._hp = valor
    
    @property
    def forca(self):
        return self._forca

    @forca.setter
    def forca(self, valor):
        self._forca = valor

    @property
    def dex(self):
        return self._dex

    @dex.setter
    def dex(self, valor):
        self._dex = valor

    @property
    def defe(self):
        return self._defe

    @defe.setter
    def defe(self, valor):
        self._defe = valor

    @property
    def inte(self):
        return self._inte

    @inte.setter
    def inte(self, valor):
        self._inte = valor

    @property
    def inventario(self):
        return self._inventario
    
    @property
    def inventario_limite(self):
        return self._inventario_limite

    @property
    def equipamentos(self):
        return self._equipamentos

    @property
    def skills(self):
        return self._skills
    
    @skills.setter
    def skills(self, valor):
        self._skills = valor

    @property
    def classe(self):
        return self._classe


    def add_item_inventario(self, item):
        if len(self._inventario) < self._inventario_limite:
            self._inventario.append(item)
            print(f'{item.nome} adicionado ao inventário.')
        else:
            print('Inventário cheio! Não é possível adicionar mais itens.')

    def remover_item_inventario(self, item):
        if item in self._inventario:
            self._inventario.remove(item)
            print(f'{item.nome} removido do inventario.')
            return True
        else:
            print('Item não está no inventario.')
            return False

    def somar_atributos(self, equipamento):
        self._hp += equipamento.bonus_hp
        self._forca += equipamento.bonus_forca
        self._dex += equipamento.bonus_dex
        self._defe += equipamento.bonus_defe
        self._inte += equipamento.bonus_inte

    def reduzir_atributos(self, equipamento):
        self._hp -= equipamento.bonus_hp
        self._forca -= equipamento.bonus_forca
        self._dex -= equipamento.bonus_dex
        self._defe -= equipamento.bonus_defe
        self._inte -= equipamento.bonus_inte
    
    def equipar_arma(self, arma):
        if isinstance(arma, Arma):
            if self.remover_item_inventario(arma):
                if self._equipamentos["arma"]:
                    self.reduzir_atributos(self._equipamentos["arma"])
                    self.add_item_inventario(self._equipamentos["arma"])
                self._equipamentos["arma"] = arma
                self.somar_atributos(arma)
                print(f'Arma {arma.nome} equipada.')
        else:
            print('Esse item não é uma arma.')

    def equipar_armadura(self, armadura):
        if isinstance(armadura, Armadura):
            if self.remover_item_inventario(armadura):
                if self._equipamentos["armadura"]:
                    self.reduzir_atributos(self._equipamentos["armadura"])
                    self.add_item_inventario(self._equipamentos["armadura"])
                self._equipamentos["armadura"] = armadura
                self.somar_atributos(armadura)
                print(f'Armadura {armadura.nome} equipada.')
        else:
            print('Esse item não é uma armadura.')

    def tipo_dano(self):
        arma = self._equipamentos["arma"]
        if arma:
            if arma.tipo == 'corpo':
                return self.forca
            if arma.tipo == 'distancia':
                return self.dex
            if arma.tipo == 'magica':
                return self.inte
        else:
            return self.forca
        
    def receber_dano(self, dano):
        self._hp -= dano
        print(f'{self.nome} sofreu {dano} de dano.')
        if self._hp <= 0:
            self._hp = 0
            print(f'{self._nome} foi derrotado!')


class Guerreiro(Personagem):

    def __init__(self, nome, classe, hp, forca, dex, defe, inte, energia) -> None:
        super().__init__(nome, classe, hp, forca, dex, defe, inte)
        self._energia_Max = energia
        self._energia = energia
        #para skills:
        self._escudo = False
        self._escudo_turnos = 0

    @property
    def energia_Max(self):
        return self._energia_Max

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        self._energia = valor

    @property
    def escudo(self):
        return self._escudo
    
    @escudo.setter
    def escudo(self, valor):
        self._escudo = valor

    @property
    def escudo_turnos(self):
        return self._escudo_turnos
    
    @escudo.setter
    def escudo_turnos(self, valor):
        self._escudo_turnos = valor
        
    def somar_atributos(self, equipamento):
        super().somar_atributos(equipamento)
        self._energia += equipamento.bonus_energia

    def reduzir_atributos(self, equipamento):
        super().reduzir_atributos(equipamento)
        self._energia -= equipamento.bonus_energia

    def receber_dano(self, dano):
        if self._escudo == True:
            dano = dano/2
            self._escudo_turnos -= 1
            if self._escudo_turnos <= 0:
                self._escudo = False
        return super().receber_dano(dano)
    
    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Classe: {self.classe}')
        print(f'HP: {self.hp}')
        print(f'Força: {self.forca}')
        print(f'Dex: {self.dex}')
        print(f'Defesa: {self.defe}')
        print(f'Inteligência: {self.inte}')
        print(f'Energia: {self.energia}')

    def recarrega_elemento(self, valor):
        if self._energia < self._energia_Max:
            self._energia += valor
            if self._energia > self._energia_Max:
                self._energia = self._energia_Max


class Mago(Personagem):

    def __init__(self, nome, classe, hp, forca, dex, defe, inte, mana) -> None:
        super().__init__(nome, classe, hp, forca, dex, defe, inte)
        self._mana_Max = mana
        self._mana = mana 

    @property
    def mana_Max(self):
        return self._mana_Max

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, valor):
        self._mana = valor

    def somar_atributos(self, equipamento):
        super().somar_atributos(equipamento)
        self._mana += equipamento.bonus_mana

    def reduzir_atributos(self, equipamento):
        super().reduzir_atributos(equipamento)
        self._mana -= equipamento.bonus_mana

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Classe: {self.classe}')
        print(f'HP: {self.hp}')
        print(f'Força: {self.forca}')
        print(f'Dex: {self.dex}')
        print(f'Defesa: {self.defe}')
        print(f'Inteligência: {self.inte}')
        print(f'Energia: {self.mana}')

    def recarrega_elemento(self, valor):
        if self.mana < self.mana_Max:
            self.mana += valor
            if self.mana > self.mana_Max:
                self.mana = self.mana_Max