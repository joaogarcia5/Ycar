import random

print('Opção 1 - Pedra')
print('Opção 2 - Tesoura')
print('Opção 3 - Papel')
play = str(input('Digite: '))

def gs(comp, carc):
    joken = ''
    for _ in range(comp):
        joken += random.choice(carc)
    return joken
num = '123'
esc = gs(1, num)

if play == '1' and esc == '1':
    print('EMPATE')
elif play == '1' and esc == '2':
    print('VOCÊ GANHOU')
elif play == '1' and esc == '3':
    print('EU GANHEI')

elif play == '2' and esc == '1':
    print('EU GANHEI')
elif play == '2' and esc == '2':
    print('EMPATE')
elif play == '2' and esc == '3':
    print('VOCÊ GANHOU')

elif play == '3' and esc == '1':
    print('VOCÊ GANHOU')
elif play == '3' and esc == '2':
    print('EU GANHEI')
elif play == '3' and esc == '3':
    print('EMPATE')