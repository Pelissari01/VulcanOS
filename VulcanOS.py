from rich import print

class Vulcao_POO():

    def __init__(self,nome, temperatura):
        self.nome = nome
        self._temperatura = None
        self.valido = temperatura

    @property
    def valido(self):
        return self._temperatura

    @valido.setter
    def valido(self, valor):
        if valor < 700:
            print(f'\nAcho que seu vulcão é feito de gelo :joy:')
            print(f'Temperatura definida para 700')
            self._temperatura = 700
        elif valor > 1200:
            print(f'\nSeu vulcão é mais quente que o foguete do Elun Musk :joy:')
            print(f'Temperatura definida para 1200')
            self._temperatura = 1200
        else:
            self._temperatura = valor


    def __str__(self):
        return f'''\n   [green]Nome:[/] {self.nome}\n   [purple]Temperatura:[/] {self._temperatura}'''

