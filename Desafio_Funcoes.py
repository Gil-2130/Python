def welcome(saudacao, nome):  # 1-- Desafio da função de saudação
    print(f'{saudacao} {nome}')

welcome('Olá Devs', 'Boa noite')
welcome('Ainda tô dando meus baby-steps', ',mas chego lá!!!')
welcome('Um dia chego no nível de vocês', ',me aguardem')



def soma(n1, n2, n3):   # 2-- Desafio da função de somar valores com parãmetros definidos
    print(n1 + n2 + n3)
soma(55, 55, 15)
soma(25, 30, 40)
soma(52, 90, 8)



def percentual(valor, porcentagem):  #3-- Desafio de função para percentual de números
    return valor+(valor*porcentagem/100)

pct = percentual(100, 50)
print(pct)
pct = percentual(25, 50)
print(pct)
pct = percentual(80, 10)
print(pct)
pct = percentual(15, 100)
print(pct)


def fb(n):  # 4--Desafio 'FIZZ' "BUZZ'
    if n % 3 == 0 and n % 5 == 0:
        return f'FIZZBUZZ, {n} é divisivel por 3 e 5'
    if n % 5 == 0:
        return f'BUZZ, {n} é divisivel por 5'
    if n % 3 == 0:
        return f'BUZZ, {n} é divisivel por 3'
    return f'{n} ,número não divisivel pelos parâmetros padrões!!!'
# from random import randint
# for i in range(100):
#     aleatorio = randint(0, 100)
print(fb(25))
print(fb(33))
print(fb(24))
print(fb(28))


