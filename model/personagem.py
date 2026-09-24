class Personagem: 
    def __init__(self, nome, vida, vida_maxima, ataque, defesa): 
            self.__nome = nome
            self.__vida = vida
            self.__vida_maxima = vida_maxima
            self.__ataque = ataque
            self.__defesa = defesa
            self.__nivel = 1
            self.__xp = 0

    @property
    def nivel(self): 
        return self.__nivel
    
    @property
    def xp(self): 
        return self.__xp 

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @property
    def ataque(self):
        return self.__ataque

    @property
    def defesa(self):
        return self.__defesa

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        elif valor > self.__vida_maxima:
            self.__vida = self.__vida_maxima
        else:
            self.__vida = valor

    @ataque.setter
    def ataque(self, valor):
        if valor < 0:
            self.__ataque = 0
        else:
            self.__ataque = valor

    @defesa.setter
    def defesa(self, valor):
        if valor < 0:
            self.__defesa = 0
        else:
            self.__defesa = valor

    def ganhar_experiencia(self, quantidade):
        if quantidade <= 0:
            return
        self.__xp += quantidade
        while self.__xp >= self.__nivel * 100:
            self.__xp -= self.__nivel * 100
            self.__nivel += 1
            self._aumentar_atributos()
            print(f'{self.nome} subiu para o nível {self.nivel}!')

    def _aumentar_atributos(self):
        self.__vida_maxima += 10          
        self.ataque = self.ataque + 2     
        self.defesa = self.defesa + 1
        self.vida = self.vida_maxima     

    def esta_vivo(self):
        return self.__vida > 0

    def _receber_dano(self, valor):
        self.__vida = self.__vida - valor
        if self.__vida < 0: 
                    self.__vida = 0

    def atacar(self, alvo):
        dano = self.calcular_dano_contra(alvo)
        alvo._receber_dano(dano)
        print(f'{self.__nome} atacou {alvo.nome} causando {dano} de dano')

    def calcular_dano_contra(self, alvo):
        dano =  self.__ataque - alvo.defesa
        if dano > 0:
            return dano
        else:
            return 1   

    def exibir_dados(self):
        msg = f'''
Nome: {self.nome}
Vida: {self.vida}
Ataque: {self.ataque}
Defesa: {self.defesa}
Nível: {self.nivel}
XP: {self.xp}'''
        return msg