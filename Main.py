from bin import data_output 
from bin import ingame
from bin import json_output

prompt = '\nComando: '
menu_init = '[1]Iniciar Jogo            [2]Instrucoes              [3]Sair\n{0} '
menu_guide = '[M]Modos de Jogo            [V]Voltar ao Menu Principal\n{0}'
menu_modes = '[{0}]Menu Principal\n{1}'
menu_rankig = '[M]Menu Principal'
final01 = ' '*19+'Sua pontuacao é de %i%%'
final02 = ' '*19+'%io Lugar: Player %i [%s] %i%%'
msg= ''

while True:
    questions = json_output.getData()['question']
    alternatives = json_output.getData()['choice']
    template = json_output.getData()['answer']
    answers = []

    cmd = data_output.scope_input('\n'+menu_init, prompt, ['1','2','3','4'])

    if cmd == '1':
        line = ingame.line_players(int(ingame.players()))
        ingame.main(line, questions, alternatives, template, answers)
        data_output.print_back()
        z = ingame.out_result(answers,line)

        if len(line) == 1:
            print(final01%z)
        elif len(line) > 1:
            print(z, line)
            for i in range(len(line)):
                for j in range(1,len(line)):
                    if (z[j] > z[i]):
                        aux, aux1 = z[i], line[i]
                        z[i],line[i] = z[j], line[j]
                        z[j],line[j] = aux, aux1

            if z[1] == 0:
                z[1] = z[len(z)-1]
                z[len(z)-1] = 0

            for i in range(len(line)):
                print(final02%(i+1, i+1,line[i],z[i]))
            print(msg)

        cmd = data_output.set_input(menu_rankig+prompt)
        if cmd == 'G':
            storage = (line[0], z[0])
            file = open('content/scores', 'r+')
            aux = file.readlines()
            aux.append(storage)
            file.write(aux[len(aux)-1])
    elif cmd == '2':
        while True:
            cmd = data_output.scope_input(data_output.output_txt('content/guide'), '\n'+ prompt,['V','M'])
            if cmd == 'M':
                cmd = data_output.scope_input(data_output.output_txt('content/mode'), '\n' + prompt,['V'])
            elif cmd == 'V':
                break
    elif cmd == '3':
        break