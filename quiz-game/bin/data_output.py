import os

aux = ''

def get_txt(file):
    list = []
    with open(str(file), 'r+') as File:
        for i in File.readlines():
            list.append(i.strip("\n"))
    return list

def output_txt(file):
    text = ''
    list = get_txt(file)
    for i in list:
        text = text+'\n'+i
    return text

def set_input(text):
    global cmd
    cmd = str(input(text)).upper()
    

def print_back():
    os.system('cls')
    print('='*62)
    print(' '*24,'REDE QUIZ v.2')
    print('='*62)

def format_scope(scope, error):
    return (scope.format(error))

def scope_input(scope, error, comand):
    while True:
        print_back()
        global aux
        set_input(format_scope(scope, aux+error))
        if cmd in comand:
            aux= ''
            return cmd
        else:
            aux = '\nErro! Comando Invalido!'