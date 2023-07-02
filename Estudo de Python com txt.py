#se d = 3 a funcionalidade não está completa
from módulo import leitaint, pontinhos
from time import sleep

#verifica se Ex115 está vazio
Vazio = True
with open("Ex115.txt",'r') as ex115:
    if len(ex115.read()) > 0:
        Vazio = False

#mero contador, "d" = contador de loops geral, "t" = contador de tentativas de visualização do txt vazio
d = t = 0
while True:
    if t >= 2 and Vazio == True:
        d = leitaint('''
[2] - cadastrar nova pessoa
[4] - sair do sistema
''','24')
    else:
#d = decisão, com o leiaint() [help(leitaint)] guarda a escolha da opção aceitando apenas números de 1 a 4
        d = leitaint('''[1] - ver pessoas cadastradas
[2] - cadastrar nova pessoa
[3] - apagar cadastro já feito
[4] - sair do sistema
''','1234')
#como estabelecido pela função leiaint (help(leitaint) quando o texto não é validado um valor "False" é retornado
    if d == False:
        pontinhos(3,0.575)
        print('')

# se "d" = 1 abra arquivo de texto escolhido como "reader" e escreva oq está escrito
    if d == 1:
        if Vazio == False:
            with open("Ex115.txt","r") as ex115:
                for nome in ex115.readlines():
                    print(nome,end='')
            print('')
        else:
            t += 1
            print('"Ex115" está vazio, adicione novos nomes para vê-los',end='')
            pontinhos(3,0.575)
            print('')

#se "d" = 2 peça ao usuário escrever um nome e uma idade e guarde em um documento sob a forma:
#Forma: Exemplo-9;
    if d == 2:
        with open("Ex115.txt",'a') as ex115:
            ex115.write(input('Nome:'))
            ex115.write('-')
            ex115.write(str(leitaint('Idade:')))
            ex115.write('\n')


 #se "d" = 3 apague cadastros já feitos a escolha do usuário [WP n achei a função de apagar o bgl, mas ta selecionado bonitinho, uma hora eu ajeito, confia]
    if d == 3:
        if Vazio == False:
            print('veja as opções e decida qual apagar:')
            sleep(0.80/100)
            with open("Ex115.txt", "r") as ex115:
                for k in range(0, len(ex115.readlines())):
                    with open("Ex115.txt", "r") as ex115:
                            print(f"{k + 1}° {ex115.readlines()[k]}", end='')
            with open("Ex115.txt", "a") as ex115:
                b = int(input(':'))

        else:
            t += 1
            print('"Ex115" está vazio, adicione novos nomes para vê-los', end='')
            pontinhos(3, 0.575)
            print('')


#se "d" = 4 escreva "obrigado por usar e encerre o programa"
    if d == 4:
        print('obrigado por usar :)')
        exit()
