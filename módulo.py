def leitaint(str=':',lim=0):
    """validação numérica simples, tal qual um 'int(input())'
com a diferença fundamental de que rejeita o parâmetro caso o mesmo não seja numérico
(não é nescessário utilizar entrada do tipo 'int'). Parâmetro 'lim' define que caso """
    while True:
        i = input(str)
        if i.isnumeric() == True:
            return int(i)
        else:
            print('digite um número válido',end='')
            return False

#cria n pontos em um tempo t
def pontinhos(n = 3,t = 0.33,end=''):
    """cria n pontos em um tempo t espaçados por end"""
    from time import sleep
    for l in range(0,n):
        sleep(t)
        print('.',end=end)
    sleep(t)