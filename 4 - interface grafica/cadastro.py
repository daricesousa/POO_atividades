class Cadastro:
   
    __slots__ = ['_lista_Pessoas']

    def __init__(self):
       self._lista_Pessoas = []


    def cadastrar(self, pessoa):
        existe = self.buscar(pessoa.cpf)
        if(existe == None):
            self._lista_Pessoas.append(pessoa)
            return True
        else:
            return False


    def buscar(self, cpf):
        for pessoa in self._lista_Pessoas:
            if pessoa.cpf == cpf:
                return pessoa
            else:
                return None