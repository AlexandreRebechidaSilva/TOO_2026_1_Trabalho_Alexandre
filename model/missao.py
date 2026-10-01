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


        