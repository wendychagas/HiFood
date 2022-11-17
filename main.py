import PySimpleGUI as sg


# Criar as janelas;
def janela_login():
    layout = [
        [sg.Text('Nome', size=(20, 0))],
        [sg.Input(size=(20, 0))],
        [sg.Button('Continuar', size=(20, 0))]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_pedido():
    layout = [
        [sg.Text('Fazer Pedido', size=(10, 0))],
        [sg.Text('Entradas', size=(10, 0))],
        [sg.Checkbox('Yakisoba', key='prato1'), sg.Checkbox('Sushi', key='prato2'), sg.Checkbox('Sunomono', key='prato3')],
        [sg.Text('Bebidas', size=(10, 0))],
        [sg.Checkbox('Refrigerante', key='prato4'), sg.Checkbox('Suco Natural', key='prato5')],
        [sg.Button('Voltar', size=(10, 0)), sg.Button('Fazer Pedido', size=(10, 0))]
    ]
    return sg.Window('Pedido', layout=layout, finalize=True)


# Criar as janelas inicias;
janela1, janela2 = janela_login(), None

# Leitura;
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada;
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para próxima janela;
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Fazer Pedido':
        if values['prato1'] == True and values['prato2'] == True and values['prato3'] == True and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Sunomono\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == True and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Sunomono\n1x Refrigerante')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == True and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Sunomono\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == True and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Sunomono')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == False and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == False and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Refrigerante')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == False and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Sushi\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == True and values['prato3'] == False and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Sushi')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == True and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Sunomono\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == True and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Sunomono\n1x Refrigerante')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == True and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Sunomono\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == True and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Sunomono')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == False and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == False and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Yakisoba\n1x Refrigerante')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == False and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Yakisoba\n1x Suco Natural')
        elif values['prato1'] == True and values['prato2'] == False and values['prato3'] == False and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Yakisoba')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == True and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Sushi\n1x Sunomono\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == True and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Sushi\n1x Sunomono\n1x Refrigerante\n')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == True and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Sushi\n1x Sunomono\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == True and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Sushi\n1x Sunomono\n')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == False and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Sushi\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == False and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Sushi\n1x Refrigerante\n')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == False and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Sushi\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == True and values['prato3'] == False and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Sushi\n')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == True and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Sunomono\n1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == True and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Sunomono\n1x Refrigerante\n')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == True and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Sunomono\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == True and values['prato4'] == False and values['prato5'] == False:
            sg.popup('1x Sunomono\n')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == False and values['prato4'] == True and values['prato5'] == True:
            sg.popup('1x Refrigerante\n1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == False and values['prato4'] == True and values['prato5'] == False:
            sg.popup('1x Refrigerante\n')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == False and values['prato4'] == False and values['prato5'] == True:
            sg.popup('1x Suco Natural')
        elif values['prato1'] == False and values['prato2'] == False and values['prato3'] == False and values['prato4'] == False and values['prato5'] == False:
            sg.popup('É necessário escolher ao menos um item.')
