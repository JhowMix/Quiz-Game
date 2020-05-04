import random
from bin import data_output

def choose_question(list1, list2, list3, c, answers):
    compare = ['A', 'B', 'C', 'D']
    number = random.randint(0,len(list1)-1)
    question = list1[number].split('@')
    alternatives = list2[number].split('@')
    templet = list3[number]
    question[0] = str(c)+'. '+question[0]
    for i in question:
        print(i)
    for i in alternatives:
        print(i)
    #print(templet)
    get_answer(templet, compare, answers)
    return number

def delete_question(number, list1, list2, list3,):
    del(list1[number])
    del (list2[number])
    del (list3[number])

def players():
    aux = ''
    while True:
        data_output.print_back()
        number_players = input(aux + 'Digite quantos irão jogar: ')
        if number_players in ['1','2','3','4','5']:
            return number_players
        else:
            aux = 'Erro! Comando Inválido!\n'

def get_answer(list, compare, answers):
    while True:
        cmd = str(input('Resposta: ')).upper()
        if cmd in compare:
            if cmd == list:
                answers.append(True)
                break
            else:
                answers.append(False)
                break
        else:
            print('Erro! Comando Inválido!')

def line_players(number):
    line = list(range(number))
    if number > 1:
        for i in line:
            line[i]= str(input("Digite o nome do player[%i]: "%(i+1)))
    else:
        line[0] = str(input("Digite seu nome: "))
    return line

def out_result(list, line):
    if len(line) == 1:
        x = 0
        for i in list:
            if i == True:
                x += 1
        result = (x * 100) / 15
        return result
    elif len(line) == 2:
        p = [0,0]
        cal(list, p, len(list), len(line))
        result = [int((p[0] * 100) / 7), int((p[1] * 100) / 7)]
        return result
    elif len(line) == 3:
        p = [0, 0, 0]
        cal(list, p, len(list), len(line))
        result = [int((p[0] * 100) / 5), int((p[1] * 100) / 5),int((p[2] * 100) / 5)]
        return result
    elif len(line) == 4:
        p = [0, 0, 0, 0]
        cal(list, p, len(list), len(line))
        result = [int((p[0] * 100) / 3), int((p[1] * 100) / 3), int((p[2] * 100) / 3), int((p[3] * 100) / 3)]
        return result
    elif len(line) == 5:
        p = [0, 0, 0, 0, 0]
        cal(list, p, len(list), len(line))
        result = [int((p[0] * 100) / 3), int((p[1] * 100) / 3), int((p[2] * 100) / 3), int((p[3] * 100) / 3), int((p[4] * 100) / 3)]
        return result

def cal(list, p, end, players):
    for i in range(players):
        if i == 0:
            for j in range(0, end, players):
                if list[i] == True:
                    p[i] += 1
        else:
            for j in range(i, end+1, players):
                if list[i] == True:
                    p[i] +=  1

def stack_player(line):
    aux = line[0]
    del(line[0])
    line.append(aux)
    return line[0]

def main(line, questions, alternatives, template, answers):
    for i in range((15//len(line))*len(line)):
        print("Rodada: ", stack_player(line))
        delete_question(choose_question(questions, alternatives, template,i+1,answers), questions, alternatives, template)