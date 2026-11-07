# importações

from VulcanOS import *

from rich import print
from rich.panel import Panel
from time import sleep

#começo do código
def main():
    # funções
    def separador():
        print("=" * 30)
    print(f'Carregando Projeto...\n')
    sleep(1)


    print(Panel('  Bem-Vindo ao [red]VulcanOS[/] :volcano:  ', width=35, border_style='red'))




 # starting
    Vulcoes = []

    while True:

        print(f'\nEscolha uma das opcões listadas: ')
        print(f"""
        [1] - Cadastrar um vulcão novo
        [2] - Consultar vulcões registrados
        [3] - Analisar nível de risco
        [4] - Simulador de erupções
        [0] - Encerrar sistema
        """)
        try:
            opcao = int(input("Escolha uma opção: "))

            match opcao:
                case 1:
                     nome = input("Digite o nome do seu vulcão: ").strip()
                     while True:
                        try:
                            temperatura = int(input('Digite a temperatura do seu vulcão [700 - 1200]: '))
                            break
                        except ValueError:
                            print(f'[red]Apenas numeros![/]')
                     Vulcao = Vulcao_POO(nome, temperatura)
                     Vulcoes.append(Vulcao)
                     print(f'\n[green]Vulcão salvo![/]')
                case 2:
                    if not Vulcoes:
                        print('\n[yellow]Lista de vulcões vazia[/]')

                    for num, info in enumerate(Vulcoes):
                        print(Panel(f'''[yellow]Vucão {1+num}º[/]\n[blue]Informações:[/] {info}''', width=50, border_style='red'))
                        sleep(0.4)

                case 3:
                    if not Vulcoes:
                        print(f'\n[yellow]Lista de vulcão vazia![/]')
                    else:
                        while True:
                            for num, info in enumerate(Vulcoes):
                                print(Panel(f'''[yellow]Vucão {1 + num}º[/]\n[blue]Informações:[/] {info}''',
                                            width=50, border_style='red'))
                                sleep(0.4)
                            try:
                                escolha_vulcão = int(input(f'Digite o número do vulcão para verificar o nível de risco: '))
                                if 1 <= escolha_vulcão <= len(Vulcoes):
                                    escolha_vulcão = Vulcoes[escolha_vulcão - 1]
                                    print(f'[green]Nome: {escolha_vulcão.nome}[/]')
                                    print(f'[red]Temperatura: {escolha_vulcão._temperatura}[/]')
                                    if escolha_vulcão._temperatura <= 850:
                                        print(f'Seu vulcão vai congelar em breve amigo :crying_face:')
                                        break
                                    elif escolha_vulcão._temperatura <= 1000:
                                        print(f'Seu Vulcão ta SAFE irmão :grinning:')
                                        break
                                    elif escolha_vulcão._temperatura >= 1051:
                                        print(f'Seu vulcão ta quase entrando em erupção :flushed:')
                                        break
                                else:
                                    print('\n[blue]Digite apenas os numeros dos vulcões listados[/]')

                            except ValueError:
                                print(f'\n[blue]Digite apenas os números dos vulcões listados![/]')
                case 4:
                    if not Vulcoes:
                        print(f'\n[yellow]Lista de vulcão vazia![/]')
                    else:
                        while True:
                            for num, info in enumerate(Vulcoes):
                                print(Panel(f'''[yellow]Vucão {1 + num}º[/]\n[blue]Informações:[/] {info}''',
                                            width=50, border_style='red'))
                                sleep(0.4)
                            try:
                                erupcao = int(input('Escolha um vulcão para iniciar a simulação: '))
                                if 1 <= erupcao <= len(Vulcoes):
                                    num_vulcão = erupcao - 1
                                    erupcao = Vulcoes[erupcao - 1]
                                    print(f'\nIniciado protocolo erupção do vulcão: {erupcao.nome}... ')
                                    if erupcao._temperatura >= 1000:
                                        print(f'\nEle tem a temperatura ideal para o protocolo que é no minimo: "1000º"')
                                        sleep(1)
                                        print(f'3...')
                                        sleep(1.5)
                                        print(f'2...')
                                        sleep(1.5)
                                        print(f'1...')
                                        sleep(2)
                                        print(f'[red]\nSeu vulcão entrou em erupcão... E acabou com tudo[/] :volcano:')
                                        print(f'\n[purple]Vulcão "{erupcao.nome}" eliminado da lista[/]')
                                        Vulcoes.pop(num_vulcão)
                                        break
                                    else:
                                        sleep(0.6)
                                        print(f'[blue]\nSeu vulcão é muito fraco ainda[/] :joy:')
                                        sleep(0.7)
                                        print(f'\nEle tem a temperatura muito baixo para o protocolo que é no minimo: "1000º"')
                                        break
                                else:
                                    print('\n[blue]Digite apenas os numeros dos vulcões listados[/]')
                            except ValueError:
                                print(f'\n[blue]Digite apenas os números dos vulcões listados![/]')

                case 0:
                    print(f'\nObrigado por usar o [red]VulcanOS[/]!')
                    break
                case _:
                    print(f'  [blue]Escolha um número válido[/]')
        except ValueError:
            print(f'  [blue]Digite apenas números.[/]')





if __name__ == "__main__":
    main()


