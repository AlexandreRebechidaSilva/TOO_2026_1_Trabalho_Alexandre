class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = 'PENDENTE'

    def iniciar_missao(self):
        if self.__status == 'PENDENTE':
            self.__status = "EM ANDAMENTO"
            return f"A missão {self.nome} começou! O objetivo é {self.descricao}."
        else:
            return f'A missão {self.nome} já foi iniciada!!!'


    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def recompensa(self):
        return self.__recompensa
    @property
    def status(self):
        return self.__status

#setter criado para permitir a alteração do status da missão, mas apenas para os valores válidos: 'PENDENTE', 'EM ANDAMENTO' ou 'CONCLUÍDA'.
    @status.setter
    def status(self, valor):
        if valor in ['PENDENTE', 'EM ANDAMENTO', 'CONCLUÍDA']:
            self.__status = valor
        else:
            raise ValueError("Status inválido. Use 'PENDENTE', 'EM ANDAMENTO' ou 'CONCLUÍDA'.")
   
    def calcular_recompensa(self):
        if self.status is not 'CONCLUIDA':
          return 0
        return self.recompensa

    def concluir_missao(self, heroi):
        ...
        
class Mis_combate(Missao):
        def __init__(self, nome, descricao, recompensa, inimigo):
            super().__init__(nome, descricao, recompensa)
            self.__inimigo = inimigo
            self.__qtd_inimigos = 0
            self.__xp_por_inimigo = 0

        @property
        def inimigo(self):
            return self.__inimigo
        @property
        def qtd_inimigos(self):
            return self.__qtd_inimigos
# setter  para que sempre aja inimigos na missão
        @qtd_inimigos.setter
        def qtd_inimigos(self, valor):
            if valor < 0:
                raise ValueError("A quantidade de inimigos não pode ser negativa.")
            self.__qtd_inimigos = valor 

        @property
        def xp_por_inimigo(self):
            return self.__xp_por_inimigo

        def calcular_recompensa(self):
            if self.status is 'CONCLUIDA':
                recompensa=self.recompensa +(self.qtd_inimigos*self.xp_por_inimigo)
                return recompensa
            else:
                return 0

           
class Mis_coleta(Missao):
        def __init__(self, nome, descricao, recompensa, item, qtd_item):
            super().__init__(nome, descricao, recompensa)
            self.__item = item
            self.__qtd_item = qtd_item
            self.__xp_por_item = 0

        @property
        def item(self):
            return self.__item

        @property
        def qtd_item(self):
            return self.__qtd_item
        @property
        def xp_por_item(self):
            return self.__xp_por_item

        def calcular_recompensa(self):
            if self.status is 'CONCLUIDA':
                recompensa=self.recompensa +(self.qtd_item*self.xp_por_item)
                return recompensa
            else: 
                return 0

class Mis_transporte(Missao):
        def __init__(self, nome, descricao, recompensa, carga, qtd_item):
            super().__init__(nome, descricao, recompensa)
            self.__carga = carga
            self.__qtd_item = qtd_item
            self.__xp = 0
            self.__distancia = 0

        @property
        def carga(self):
            return self.__carga

        @property
        def qtd_item(self):
            return self.__qtd_item
        @property
        def xp(self):
            return self.__xp
        @property
        def distancia(self):
            return self.__distancia

        def calcular_recompensa(self):
            if self.status is 'CONCLUIDA':
                recompensa=self.recompensa +(self.distancia*self.xp)
                return recompensa
            else: 
                return 0
     

def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status}
'''

        return msg

def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status}'


        