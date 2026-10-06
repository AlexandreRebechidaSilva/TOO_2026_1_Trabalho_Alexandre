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
        if self.status != 'CONCLUÍDA':
          return 0
        return self.recompensa

    def concluir_missao(self, heroi):
        self.status = 'CONCLUÍDA'
        heroi.ganhar_experiencia(self.calcular_recompensa())
        ...
        
class Mis_combate(Missao):
        def __init__(self, nome, descricao, recompensa, inimigo,qtd_inimigos, xp_por_inimigo):
            super().__init__(nome, descricao, recompensa)
            self.__inimigo = inimigo
            self.__qtd_inimigos = qtd_inimigos
            self.__xp_por_inimigo = xp_por_inimigo

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

# setter para que a quantidade de xp por inimigo não seja negativa
        @xp_por_inimigo.setter
        def xp_por_inimigo(self, valor):
            if valor < 0:
                raise ValueError("A quantidade de XP por inimigo não pode ser negativa.")
            self.__xp_por_inimigo = valor

        def calcular_recompensa(self):
            if self.status == 'CONCLUÍDA':
                recompensa=self.recompensa +(self.qtd_inimigos*self.xp_por_inimigo)
                return recompensa
            else:
                return 0

           
class Mis_coleta(Missao):
        def __init__(self, nome, descricao, recompensa, item, qtd_item, xp_por_item):
            super().__init__(nome, descricao, recompensa)
            self.__item = item
            self.__qtd_item = qtd_item
            self.__xp_por_item = xp_por_item

        @property
        def item(self):
            return self.__item

        @property
        def qtd_item(self):
            return self.__qtd_item

        @property
        def xp_por_item(self):
            return self.__xp_por_item
        
# setter para que a quantidade de xp por item não seja negativa
        @xp_por_item.setter
        def xp_por_item(self, valor):
            if valor < 0:
                raise ValueError("A quantidade de XP por item não pode ser negativa.")
            self.__xp_por_item = valor

        def calcular_recompensa(self):
            if self.status == 'CONCLUÍDA':
                recompensa=self.recompensa +(self.qtd_item*self.xp_por_item)
                return recompensa
            else: 
                return 0

class Mis_transporte(Missao):
        def __init__(self, nome, descricao, recompensa, carga, qtd_item, xp, distancia):
            super().__init__(nome, descricao, recompensa)
            self.__carga = carga
            self.__qtd_item = qtd_item
            self.__xp = xp
            self.__distancia = distancia

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

# setter para que a distância não seja negativa
        @distancia.setter
        def distancia(self, valor):
            if valor < 0:
                raise ValueError("A distância não pode ser negativa.")
            self.__distancia = valor
            
# setter para que a quantidade de xp não seja negativa
        @xp.setter
        def xp(self, valor):
            if valor < 0:
                raise ValueError("A quantidade de XP não pode ser negativa.")
            self.__xp = valor

        def calcular_recompensa(self):
            if self.status == 'CONCLUÍDA':
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


        