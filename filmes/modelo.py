class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __str__(self):
        return "{} - {} - {}".format(self._nome, self.ano, self._likes)


class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.__duracao = duracao

    def __str__(self):
        return "{} - {} - {} - {}".format(self._nome, self.ano, self.__duracao, self._likes)


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome,ano)
        self.__temporada = temporada

    def __str__(self):
        return "{} - {} - {} - {}".format(self._nome, self.ano, self.__temporada, self._likes)

class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    # @property
    # def listatem(self):
    #     return self._programas
    #
    # @property
    # def tamanho(self):
    #     return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_likes()

riverdale = Serie("riverdale - chicago", 2018, 5)
riverdale.dar_likes()

lista = [vingadores,riverdale]

playlist = Playlist("fim_de_semana", lista)

for programa in playlist:
    print(programa)

print("O tamanho da lista é: {}".format(len(playlist)))