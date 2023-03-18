import random
import PySimpleGUI as sg

dvd = 'oifofo'
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.resposta = 's'
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        
        while True:
            # criar uma janela
            
            # ler os valores
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == sg.WIN_CLOSED:
                break
            try:
                if self.eventos == 'Sim' or self.eventos == "S":
                    self.GerarValorDoDado()
                elif self.eventos == 'Não' or self.eventos == "N":
                    print('tudo bem ;-;')
                    break
                else:
                    print('Digite Sim ou Não')
            except:
                print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
