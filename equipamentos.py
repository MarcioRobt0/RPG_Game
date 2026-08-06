class Equipamento:

    def __init__(self, nome, bonus_hp, bonus_forca, bonus_dex, bonus_defe, bonus_inte, bonus_mana, bonus_energia) -> None:
        self._nome = nome 
        self._bonus_hp = bonus_hp
        self._bonus_forca = bonus_forca
        self._bonus_dex = bonus_dex
        self._bonus_defe = bonus_defe
        self._bonus_inte = bonus_inte
        self._bonus_mana = bonus_mana
        self._bonus_energia = bonus_energia

    @property
    def nome(self):
        return self._nome
    
    @property
    def bonus_hp(self):
        return self._bonus_hp
    
    @property
    def bonus_forca(self):
        return self._bonus_forca
    
    @property
    def bonus_dex(self):
        return self._bonus_dex
    
    @property
    def bonus_defe(self):
        return self._bonus_defe
    
    @property
    def bonus_inte(self):
        return self._bonus_inte
    
    @property
    def bonus_mana(self):
        return self._bonus_mana
    
    @property
    def bonus_energia(self):
        return self._bonus_energia
    
    def info_equipamento(self):
        atributos = {
            'bonus_hp': self._bonus_hp,
            'bonus_forca': self._bonus_forca,
            'bonus_dex': self._bonus_dex,
            'bonus_defe': self._bonus_defe,
            'bonus_inte': self._bonus_inte,
            'bonus_mana': self._bonus_mana,
            'bonus_energia': self._bonus_energia
        }
        for atributo, valor in atributos.items():
            if valor != 0:
                print(f'{atributo}: {valor}')


class Arma(Equipamento):
    
    def __init__(self, nome, tipo, bonus_hp=0, bonus_forca=0, bonus_dex=0, bonus_defe=0, bonus_inte=0, bonus_mana=0, bonus_energia=0) -> None:
        super().__init__(nome, bonus_hp, bonus_forca, bonus_dex, bonus_defe, bonus_inte, bonus_mana, bonus_energia)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo
    
    def info_equipamento(self):
        print('Nome: ',self.nome)
        print('Tipo: ',self.tipo)
        return super().info_equipamento()


class Armadura(Equipamento):

    def __init__(self, nome, bonus_hp=0, bonus_forca=0, bonus_dex=0, bonus_defe=0, bonus_inte=0, bonus_mana=0, bonus_energia=0) -> None:
        super().__init__(nome, bonus_hp, bonus_forca, bonus_dex, bonus_defe, bonus_inte, bonus_mana, bonus_energia)

    def info_equipamento(self):
        print('Nome: ',self.nome)
        return super().info_equipamento()