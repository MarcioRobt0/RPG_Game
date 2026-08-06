import abc 

class Skill_Interface(abc.ABC):

    def __init__(self, nome, custo, efeito, descricao) -> None:
        self._nome = nome
        self._custo = custo
        self._efeito = efeito
        self._descricao = descricao
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def custo(self):
        return self._custo
    
    @custo.setter
    def custo(self, valor):
        self._custo = valor

    @property
    def efeito(self):
        return self._efeito
    
    @efeito.setter
    def efeito(self, valor):
        self._efeito = valor

    @property
    def descricao(self):
        return self._descricao

    @abc.abstractmethod
    def usar(self, lancador, alvo):
        pass


class Habilidade(Skill_Interface):
    
    def __init__(self, nome, custo, efeito, descricao) -> None:
        super().__init__(nome, custo, efeito, descricao)


    #mudar verificação de alvo para lançador e reduzir a energia quando usada
    def usar(self,lancador, alvo):
        if callable(self.efeito):
            if lancador.energia >= self.custo:
                lancador.energia -= self.custo
                print(f'{lancador.nome} utilizou {self.nome}. Efeito: ')
                self.efeito(lancador, alvo)
                return True
            else:
                print('Não há energia suficiente para usar essa habilidade!')
                return False

class Magia(Skill_Interface):

    def __init__(self, nome, custo, efeito, descricao) -> None:
        super().__init__(nome, custo, efeito, descricao)

    def usar(self,lancador, alvo):
        if callable(self.efeito):
            if lancador.mana >= self.custo:
                lancador.mana -= self.custo
                self.efeito(lancador, alvo)
                return True
            else:
                print('Não há mana suficiente para usar essa magia!')
                return False