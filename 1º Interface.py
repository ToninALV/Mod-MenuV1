import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown1')
        #layout
        layout = [
           [sg.Text('Nome',size=(10,0)),sg.Input(size=(35,0),key='nome')],
            [sg.Text('Sobrenome', size=(10,0)),sg.Input(size=(35,0),key='sobrenome')],
            [sg.Text('Idade', size=(10,0)),sg.Input(size=(35,0),key='idade')],
            [sg.Text('Data de Nascimento', size=(10,0)),sg.Input(size=(35,0),key='data_de_nascimento')],
            [sg.Checkbox('Gmail',key='Gmail'), sg.Checkbox('Outlook',key='Outlook'), sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Slider(range=(0, 100), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Concluir Cadastro', size=(10,0))],
            [sg.Output(size=(100,20))],
        ]
        #janela
        self.janela = sg.Window('Cadastro de Usuário').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            sobrenome = self.values['sobrenome']
            idade = self.values['idade']
            data_de_nascimento = self.values['data_de_nascimento']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            velocidade_script = self.values['sliderVelocidade']
            print('-=-'*15)
            print('Primeiro Nome: {}'.format(nome))
            print('Ultimo Nome: {}'.format(sobrenome))
            print('Idade: {}'.format(idade))
            print('Data de Nascimento: {}'.format(data_de_nascimento))
            print('Aceita Gmail: {}'.format(aceita_gmail))
            print('Aceita Outlook: {}'.format(aceita_outlook))
            print('Aceita Yahoo: {}'.format(aceita_yahoo))
            print('Velocidade Script: {:.0f}'.format(velocidade_script))
            print('-=-' * 15)
            print(' ')



tela = TelaPython()
tela.Iniciar()

