class Pessoa:

    __slots__ = ['_nome', '_cpf', '_endereco', '_nascimento']

    def __init__(self, nome, cpf, endereco, nascimento):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def cpf(self):
        return self._cpf


    @property
    def nascimento(self):
        return self._nascimento