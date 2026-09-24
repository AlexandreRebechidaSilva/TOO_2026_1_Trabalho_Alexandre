from model.personagem import Personagem
from model.enums import TipoInimigo

class Inimigo(Personagem):
    def __init__(self, nome, tipo, vida, vida_maxima, ataque, defesa): 
        super().__init__(nome, vida, vida_maxima, ataque, defesa)
        if not isinstance(tipo, TipoInimigo):
            raise TypeError('Tipo precisa ser um TipoInimigo')
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    def exibir_dados(self):
        msg = f'''
Dados do Inimigo:
{super().exibir_dados()}
Tipo: {self.tipo.value}

'''
        return msg

    def __str__(self): 
        return f"\nInimigo: {self.__dict__}" 