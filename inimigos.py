class Inimigo:

    def __init__(self, nome, hp, forca, dex, defe, inte, mana, energia) -> None:
        
        self._nome = nome
        self._hp = hp
        self._forca = forca
        self._dex = dex
        self._defe = defe
        self._inte = inte
        self._mana_Max = mana
        self._mana = mana
        self._energia_Max = energia
        self._energia = energia
        self._habilidades = []

    @property
    def nome(self):
        return self._nome

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, valor):
        self._hp = valor

    @property
    def forca(self):
        return self._forca

    @property
    def dex(self):
        return self._dex

    @property
    def defe(self):
        return self._defe

    @property
    def inte(self):
        return self._inte
    
    @property
    def mana_Max(self):
        return self._mana_Max

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, valor):
        self._mana = valor

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
    def habilidades(self):
        return self._habilidades
    

    def receber_dano(self, dano):
        self._hp -= dano
        print(f'{self.nome} sofreu {dano} de dano.')
        if self._hp <= 0:
            self._hp = 0
            print(f'{self._nome} foi derrotado!')

    def tipo_dano(self):
        if self._forca > self._dex and self._forca > self._inte:
            return self.forca
        if self._dex > self._forca and self._dex > self._inte:
            return self.dex
        if self._inte > self._forca and self._inte > self._dex:
            return self.inte
        else: 
            return self.forca
        
    def add_habilidade(self, habilidade):
        self._habilidades.append(habilidade)

    def recarrega_elemento(self, valor):
        if self._energia < self._energia_Max:
            self._energia += valor
            if self._energia > self._energia_Max:
                self._energia = self._energia_Max
        if self.mana < self.mana_Max:
            self.mana += valor
            if self.mana > self.mana_Max:
                self.mana = self.mana_Max