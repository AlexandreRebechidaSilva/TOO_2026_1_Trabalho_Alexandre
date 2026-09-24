from model.personagem import Personagem
from model.enums import ClasseHeroi

class Heroi(Personagem):    
    def __init__(self, nome, classe, vida, vida_maxima, ataque, defesa): 
        super().__init__(nome, vida, vida_maxima, ataque, defesa)
        if not isinstance(classe, ClasseHeroi):
            raise TypeError("Classe precisa ser da ClasseHeroi")
        self.__classe = classe

    @property
    def classe(self):
        return self.__classe
    

    def exibir_dados(self):
        msg = f'''
Dados do Heroi:
{super().exibir_dados()}
Tipo: {self.classe.value}
'''
        return msg

    def __str__(self):
        return f"\nHeroi: {self.__dict__}" 
        