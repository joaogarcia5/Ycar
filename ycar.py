#Import
import webbrowser
opera = 'C:/Users/azule/AppData/Local/Programs/Opera GX/opera.exe %s'
import pandas as pd
from datetime import datetime
from math import sqrt
import time
import random
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'oculto'
import pygame
import colorama
from colorama import Fore, Style
colorama.init()
pygame.init()
dataday = time.strftime('%d/%m/%Y')

#Definições
#Easter Egg Lore def
def lorena_easter_egg():
    #EasterEgg Lore
    #PyGame DBGT
    mscfundo = pygame.mixer.music.stop()
    dbgt = pygame.mixer.music.load('mscs/lzul.mp3')
    dbgt = pygame.mixer.music.play(start=2.5)
    dbgt = pygame.mixer.music.set_volume(0.1)

    lp()
    print('E{}u{} te amo Lore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu {}t{}e amo Lore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu t{}e{} amo Lore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te {}a{}mo Lore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te a{}m{}o Lore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te am{}o{} Lore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo {}L{}ore <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo L{}o{}re <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo Lo{}r{}e <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo Lor{}e{} <333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo Lore {}<{}333'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo Lore <{}3{}33'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo Lore <3{}3{}3'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print('Eu te amo Lore <33{}3{}'.format('\033[0;31m', '\033[m'))
    time.sleep(0.2)
    lp()
    print(Fore.RED+'Eu te amo {}Lore{} <333 \n(♥ω♥ )'.format('\033[4m', '\033[0;31m')+Fore.RESET)
    print()
    input('Pressione ENTER para continuar.')

#Processamento_OP1
def Processamento_op1():
    lp()
    if es == '1' and c == '1':
        print('{}SOMA{}'.format('\033[4m', '\033[m'))
        print(n2, '+', n3, '= {:2}'.format(n2+n3))
    elif c == '2' and es == '1':
        print('{}SUBTRAÇÃO{}'.format('\033[4m', '\033[m'))
        print(n2, '-', n3, '= {:2}'.format(n2-n3))
    elif c == '3' and es == '1':
        print('{}MULTIPLICAÇÃO{}'.format('\033[4m', '\033[m'))
        print(n2, 'x', n3, '= {:2}'.format(n2*n3))
    else:
        print('{}DIVISÃO{}'.format('\033[4m', '\033[m'))
        print(n2, '/', n3, '= {:.2f}'.format(n2/n3))

#Processamento_OP2
def Processamento_op2():
    lp()
    print('{}SOMA{}'.format('\033[4m', '\033[m'))
    print(n1, '+ 1 = {:2}'.format(n1+1), '|', n1, '+ 2 = {:2}'.format(n1+2))
    print(n1, '+ 3 = {:2}'.format(n1+3), '|', n1, '+ 4 = {:2}'.format(n1+4))
    print(n1, '+ 5 = {:2}'.format(n1+5), '|', n1, '+ 6 = {:2}'.format(n1+6))
    print(n1, '+ 7 = {:2}'.format(n1+7), '|', n1, '+ 8 = {:2}'.format(n1+8))
    print(n1, '+ 9 = {:2}'.format(n1+9), '|', n1, '+ 10 = {:2}'.format(n1+10))

    print('{}SUBTRAÇÃO{}'.format('\033[4m', '\033[m'))  
    print(n1, '- 1 = {:2}'.format(n1-1), '|', n1, '- 2 = {:2}'.format(n1-2))
    print(n1, '- 3 = {:2}'.format(n1-3), '|', n1, '- 4 = {:2}'.format(n1-4))
    print(n1, '- 5 = {:2}'.format(n1-5), '|', n1, '- 6 = {:2}'.format(n1-6))
    print(n1, '- 7 = {:2}'.format(n1-7), '|', n1, '- 8 = {:2}'.format(n1-8))
    print(n1, '- 9 = {:2}'.format(n1-9), '|', n1, '- 10 = {:2}'.format(n1-10))

    print('{}MULTIPLICAÇÃO{}'.format('\033[4m', '\033[m'))
    print(n1, 'x 1 = {:2}'.format(n1*1), '|', n1, 'x 2 = {:2}'.format(n1*2))
    print(n1, 'x 3 = {:2}'.format(n1*3), '|', n1, 'x 4 = {:2}'.format(n1*4))
    print(n1, 'x 5 = {:2}'.format(n1*5), '|', n1, 'x 6 = {:2}'.format(n1*6))
    print(n1, 'x 7 = {:2}'.format(n1*7), '|', n1, 'x 8 = {:2}'.format(n1*8))
    print(n1, 'x 9 = {:2}'.format(n1*9), '|', n1, 'x 10 = {:2}'.format(n1*10))

    print('{}DIVISÃO{}'.format('\033[4m', '\033[m'))
    print(n1, '/ 1 = {:.2f}'.format(n1/1), '|', n1, '/ 2 = {:.2f}'.format(n1/2))
    print(n1, '/ 3 = {:.2f}'.format(n1/3), '|', n1, '/ 4 = {:.2f}'.format(n1/4))
    print(n1, '/ 5 = {:.2f}'.format(n1/5), '|', n1, '/ 6 = {:.2f}'.format(n1/6))
    print(n1, '/ 7 = {:.2f}'.format(n1/7), '|', n1, '/ 8 = {:.2f}'.format(n1/8))
    print(n1, '/ 9 = {:.2f}'.format(n1/9), '|', n1, '/ 10 = {:.2f}'.format(n1/10))

#Processamento_OP2.1
def Processamento_op2p1():
    lp()
    if c == '1':
        print('{}SOMA{}'.format('\033[4m', '\033[m'))
        print(n1, '+ 1 = {:2}'.format(n1+1), '|', n1, '+ 2 = {:2}'.format(n1+2))
        print(n1, '+ 3 = {:2}'.format(n1+3), '|', n1, '+ 4 = {:2}'.format(n1+4))
        print(n1, '+ 5 = {:2}'.format(n1+5), '|', n1, '+ 6 = {:2}'.format(n1+6))
        print(n1, '+ 7 = {:2}'.format(n1+7), '|', n1, '+ 8 = {:2}'.format(n1+8))
        print(n1, '+ 9 = {:2}'.format(n1+9), '|', n1, '+ 10 = {:2}'.format(n1+10))
    elif c == '2':
        print('{}SUBTRAÇÃO{}'.format('\033[4m', '\033[m'))  
        print(n1, '- 1 = {:2}'.format(n1-1), '|', n1, '- 2 = {:2}'.format(n1-2))
        print(n1, '- 3 = {:2}'.format(n1-3), '|', n1, '- 4 = {:2}'.format(n1-4))
        print(n1, '- 5 = {:2}'.format(n1-5), '|', n1, '- 6 = {:2}'.format(n1-6))
        print(n1, '- 7 = {:2}'.format(n1-7), '|', n1, '- 8 = {:2}'.format(n1-8))
        print(n1, '- 9 = {:2}'.format(n1-9), '|', n1, '- 10 = {:2}'.format(n1-10))
    elif c == '3':
        print('{}MULTIPLICAÇÃO{}'.format('\033[4m', '\033[m'))
        print(n1, 'x 1 = {:2}'.format(n1*1), '|', n1, 'x 2 = {:2}'.format(n1*2))
        print(n1, 'x 3 = {:2}'.format(n1*3), '|', n1, 'x 4 = {:2}'.format(n1*4))
        print(n1, 'x 5 = {:2}'.format(n1*5), '|', n1, 'x 6 = {:2}'.format(n1*6))
        print(n1, 'x 7 = {:2}'.format(n1*7), '|', n1, 'x 8 = {:2}'.format(n1*8))
        print(n1, 'x 9 = {:2}'.format(n1*9), '|', n1, 'x 10 = {:2}'.format(n1*10))
    else:
        print('{}DIVISÃO{}'.format('\033[4m', '\033[m'))
        print(n1, '/ 1 = {:.2f}'.format(n1/1), '|', n1, '/ 2 = {:.2f}'.format(n1/2))
        print(n1, '/ 3 = {:.2f}'.format(n1/3), '|', n1, '/ 4 = {:.2f}'.format(n1/4))
        print(n1, '/ 5 = {:.2f}'.format(n1/5), '|', n1, '/ 6 = {:.2f}'.format(n1/6))
        print(n1, '/ 7 = {:.2f}'.format(n1/7), '|', n1, '/ 8 = {:.2f}'.format(n1/8))
        print(n1, '/ 9 = {:.2f}'.format(n1/9), '|', n1, '/ 10 = {:.2f}'.format(n1/10))

#Clear
def lp():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

#Boas-vindas #Versão
print('-'*37)
print(Fore.CYAN+'Olá, seja bem-vindo(a) ao '+Fore.BLUE+'Ycar a1.7')
print(Fore.CYAN+'Data atual: {}'.format(dataday)+Fore.RESET)
print('-'*37)
print()
colorama.deinit()

#Escolha de função
while True:
    while True:
        while True:
            print('{}MENU{}'.format('\033[4m', '\033[m'))
            print('Qual serviço deseja usar?')
            print()
            print('Opção 1 - Calculadora')
            print('Opção 2 - Gerador de senha')
            print('Opção 3 - Consultar cotação de moedas')
            print('Opção 4 - Músicas')
            print('Opção 5 - Informações')
            print('Opção 6 - GANHE 1 MILHÃO DE REAIS')
            print()
            serv = str(input('Digite o número da opção desejada: ')).strip()
            lp()
            if serv in ['1', '2', '3', '4', '5', '6']:
                break
            print(Fore.RED+'ERRO'+Fore.RESET)
            print('Não foi possível entender o seu comando. Por favor, digite apenas 1, 2, 3 ou 4! Tente novamente.')
            print()
        if serv in ['1', '2', '3', '4', '6']:
            break

        #Função 5
        #Escolha de música
        if serv == '5':
            while True:
                while True:
                    print('{}SELETOR DE MÚSICAS{}'.format('\033[4m', '\033[m'))
                    print('(Digite o número que está entre parênteses para testar antes de selecionar.)')
                    print()
                    print('Opção 00 - Parar música')
                    print('Opção 0 - Cancelar' )
                    print('Opção 1 (10) - LO-FI')
                    print('Opção 2 (20) - Sorvete de Ovomaltine')
                    print('Opção 3 (30) - Chala Head Chala')
                    print('Opção 4 (40) - Rap do Minecraft')
                    print('Opção 5 (50) - Numb')
                    print('Opção 6 (60) - Wii Theme')
                    print()
                    emsc = input(str('Digite o número de opção desejada: ')).strip()
                    lp()
                    if emsc in ['00', '0', '1', '2', '3', '4', '5', '6', '10', '20', '30', '40', '50', '60']:
                        break
                    else:
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas uma das opções disponíveis! Tente novamente.')
                        print()

                #Teste de música
                if emsc == '10':
                    mscfundo = pygame.mixer.music.load('mscs/lofi.mp3')
                    pygame.mixer.music.play(start=15.35)
                    pygame.mixer.music.set_volume(0.1)
                    print('Você está ouvindo "LO-FI".')
                    input('Pressione ENTER para voltar.')
                    lp()
                    pygame.mixer.music.stop()
                elif emsc == '20':
                    mscfundo = pygame.mixer.music.load('mscs/sorvo.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.1)
                    print('Você está ouvindo "Sorvete de Ovo Maltine".')
                    input('Pressione ENTER para voltar.')
                    lp()
                    pygame.mixer.music.stop()
                elif emsc == '30':
                    mscfundo = pygame.mixer.music.load('mscs/chala.mp3')
                    pygame.mixer.music.play(start=2)
                    pygame.mixer.music.set_volume(0.1)
                    print('Você está ouvindo "Chala Head Chala".')
                    input('Pressione ENTER para voltar.')
                    lp()
                    pygame.mixer.music.stop()
                elif emsc == '40':
                    mscfundo = pygame.mixer.music.load('mscs/minerap.mp3')
                    pygame.mixer.music.play(start=5)
                    pygame.mixer.music.set_volume(0.1)
                    print('Você está ouvindo "Rap do Minecraft".')
                    input('Pressione ENTER para voltar.')
                    lp()
                    pygame.mixer.music.stop()
                elif emsc == '50':
                    mscfundo = pygame.mixer.music.load('mscs/numb.mp3')
                    pygame.mixer.music.play(start=3.5)
                    pygame.mixer.music.set_volume(0.1)
                    print('Você está ouvindo "Numb".')
                    input('Pressione ENTER para voltar.')
                    lp()
                    pygame.mixer.music.stop()
                elif emsc == '60':
                    mscfundo = pygame.mixer.music.load('mscs/wii.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.1)
                    print('Você está ouvindo "Wii Theme".')
                    input('Pressione ENTER para voltar.')
                    lp()
                    pygame.mixer.music.stop()
                else:
                    break

            #Play músicas
            if emsc == '1':
                mscfundo = pygame.mixer.music.load('mscs/lofi.mp3')
                pygame.mixer.music.play(start=5)
                pygame.mixer.music.set_volume(15.35)
            elif emsc == '2':
                mscfundo = pygame.mixer.music.load('mscs/sorvo.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.1)
            elif emsc == '3':
                mscfundo = pygame.mixer.music.load('mscs/chala.mp3')
                pygame.mixer.music.play(start=5)
                pygame.mixer.music.set_volume(0.1)
            elif emsc == '4':
                mscfundo = pygame.mixer.music.load('mscs/minerap.mp3')
                pygame.mixer.music.play(start=5)
                pygame.mixer.music.set_volume(0.1)
            elif emsc == '5':
                mscfundo = pygame.mixer.music.load('mscs/numb.mp3')
                pygame.mixer.music.play(start=3.5)
                pygame.mixer.music.set_volume(0.1)
            elif emsc == '6':
                mscfundo = pygame.mixer.music.load('mscs/wii.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.1)
            elif emsc == '00':
                pygame.mixer.music.stop()
            else:
                lp()

        #Função 6
        #Informações
        elif serv == '6':
            print('{}INFORMAÇÕES{}'.format('\033[4m', '\033[m'))
            print()
            print('Este é um programa desenvolvido por pura diversão como principal finalidade o aprimoramento de técnicas.')
            print('O programa atualmente conta com três principais funções em seu menu principal:')
            print('A opção número 1 se trata de uma calculadora capaz de gerar cálculos rápidos de baixa complexidade.')
            print('Já a opção número 2 é um gerador de senha aleatória capaz de gerar infinitas possibilidades de senhas.')
            print('Por fim, a opção de número 3 traz de forma atualizada a cotação de 3 das principais moedas do mundo.')
            print()
            #Versão
            print('Ycar a1.7, Feito por: João Pedro Garcia')
            print()
            input('Pressione ENTER para voltar.')
            lp()

    #Função 1
    #Início - Entrada de dados
    while True:
        if serv == '1':
            while True:
                print('Opção 1 - Fazer o cálculo de 2 números.')
                print('Opção 2 - Tabuada do 1 ao 10.')
                print('Opção 3 - Cálculo rápido de vários números.')
                print('Opção 4 - Descobrir raiz quadrada.')
                print()
                es = str(input('Digite o número da opção desejada: ')).strip()
                if es in ['1', '2', '3', '4']:
                    break
                lp()
                print(Fore.RED+'ERRO'+Fore.RESET)
                print('Não foi possível entender o seu comando. Por favor, digite apenas 1, 2 ou 3! Tente novamente.')
                print()

            #Entrada de dados avançado:
            #Entrada da opção 1
            if es == '1':
                lp()
                while True:
                    try:
                        n2 = int(input('Digite o primeiro número: '))
                        break
                    except ValueError:
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                        print()
                while True:
                    try:
                        n3 = int(input('Digite o segundo número: '))
                        break
                    except ValueError:
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                        print()
                        print('Digite o primeiro número:', n2)

                #EasterEgg Lore
                if n2 == 1 and n3 == 8:
                    lorena_easter_egg()

                while True:
                    print()
                    print('Opção 1 - Somar')
                    print('Opção 2 - Subtrair')
                    print('Opção 3 - Multiplicar')
                    print('Opção 4 - Dividir')
                    print()
                    c = str(input('Digite o número da opção desejada: ')).strip()
                    if c in ['1', '2', '3', '4']:
                        break
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Por favor, digite uma das 4 opções! Tente novamente.')
                    print()
                    print('Digite o primeiro número:', n2)
                    print('Digite o segundo número:', n3)

                #Processamento OP1
                Processamento_op1()

            #Entrada da opção 2
            elif es == '2':
                lp()
                while True:
                    try:
                        n1 = int(input('Digite um número qualquer para a tabuada de 1 ao 10: '))
                        break
                    except ValueError:
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                        print()
                lp()
                while True:
                    es2 = str(input('Deseja 4 tabuadas? Subtrair, somar, dividir e multiplicar? \nS para Sim \nN para Não \n \nDigite: ')).strip()
                    print()
                    if es2 in ['s', 'S', 'n', 'N']:
                        break
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                    print()
                if es2 == 'n' or es2 == 'N':
                    lp()
                    while True:
                        print('Opção 1 - Somar')
                        print('Opção 2 - Subtrair')
                        print('Opção 3 - Multiplicar')
                        print('Opção 4 - Dividir')
                        print()
                        c = str(input('Digite o número da opção desejada: '))
                        if c in ['1', '2', '3', '4']:
                            break
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, escolha uma das 4 opções! Tente novamente.')
                        print()

                #Processamento OP2
                if es2 == 's' or es2 == 'S':
                    Processamento_op2()

                #Processamento OP2.1
                else:
                    Processamento_op2p1()
            
            #Entrada da opção 3
            elif es == '3':
                lp()
                while True:
                    print('Opção 1 - Somar')
                    print('Opção 2 - Subtrair')
                    print('Opção 3 - Multiplicar')
                    print('Opção 4 - Dividir')
                    print()
                    c = str(input('Digite o número da opção desejada: '))
                    if c in ['1', '2', '3', '4']:
                        break
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Por favor, escolha uma das 4 opções! Tente novamente.')          
                    print()

                #Processamento OP3
                if c == '1':
                    lp()
                    def sn_soma():
                        soma = 0
                        while True:
                            try:
                                print('Digite a sequência de número que deseja calcular.')
                                print('Caso não hajá mais número, basta enviar o número 0')
                                print()
                                numero = float(input('Digite um número: '))
                                lp()
                                if numero == 0:
                                    break
                                soma += numero
                            except ValueError:
                                lp()
                                print(Fore.RED+'ERRO'+Fore.RESET)
                                print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                                print()
                        return soma

                    resultado = sn_soma()
                    print('A soma dos números digitados é:', resultado)
                
                elif c == '2':
                    lp()
                    def sn_sub():
                        sub = float(input('Digite o número inicial: '))
                        lp()
                        while True:
                            try:
                                print('Digite a sequência de número que deseja calcular.')
                                print('Caso não hajá mais número, basta enviar o número 0')
                                print()
                                numero = float(input('Digite outro número: '))
                                lp()
                                if numero == 0:
                                    break
                                sub -= numero
                            except ValueError:
                                lp()
                                print(Fore.RED+'ERRO'+Fore.RESET)
                                print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                                print()
                        return sub

                    resultado = sn_sub()
                    print('A subtração dos números digitados é:', resultado)

                elif c == '3':
                    lp()
                    def sn_mult():
                        mult = 1
                        while True:
                            try:
                                print('Digite a sequência de número que deseja calcular.')
                                print('Caso não hajá mais número, basta enviar o número 0')
                                print()
                                numero = float(input('Digite um número: '))
                                lp()
                                if numero == 0:
                                    break
                                mult *= numero
                            except ValueError:
                                lp()
                                print(Fore.RED+'ERRO'+Fore.RESET)
                                print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                                print()
                        return mult

                    resultado = sn_mult()
                    print('A multiplicação dos números digitados é:', resultado)

                else:
                    lp()
                    def sn_div():
                        print('Digite a sequência de números pelos quais deseja dividir.')
                        print('Caso não haja mais números, basta enviar o número 0')
                        print()
                        div = float(input('Digite o número inicial: '))
                        lp()
                        while True:
                            try:
                                print('Digite a sequência de números pelos quais deseja dividir.')
                                print('Caso não haja mais números, basta enviar o número 0')
                                print()
                                numero = float(input('Digite outro número: '))
                                lp()
                                if div == 0 and numero == 0:
                                    print('Não é possível dividir zero por ele mesmo.')
                                    break
                                if numero == 0:
                                    break
                                div /= numero
                            except ValueError:
                                print(Fore.RED+'ERRO'+Fore.RESET)
                                print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                                print()
                        return div

                    resultado = sn_div()
                    if resultado > 0:
                        print('A divisão dos números digitados é:', resultado)


            #Entrada da opção 4
            else:
                lp()
                while True:
                    while True:
                        try:
                            rz2 = float(input('Digite um número: '))
                            break
                        except ValueError:
                            lp()
                            print(Fore.RED+'ERRO'+Fore.RESET)
                            print('Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.')
                            print()
                    if rz2 > -1:
                        break
                    else:
                        print()
                        print('Impossível calcular a raiz de um número menor que zero! Tente novamente.')
                        print()

                #Processamento OP4
                if rz2 > -1:
                    raiz = sqrt(rz2)
                    print()
                    print('A raiz quadrada de {} é {:.2f}'.format(rz2, raiz))

            #Repetição opcional
            while True:
                while True:
                    print()
                    print('Gostaria de voltar ao começo da calculadora?\n\nS para Sim\nN para Não')
                    print()
                    bfim = str(input('Digite: ')).upper().strip()
                    if bfim in ['S', 'N']:
                        lp()
                        break
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                if bfim in ['s', 'S']:
                    lp()
                    break
                else:
                    while True:
                        print('Gostaria de retornar ao seletor de funções?\n\nS para Sim\nN para Não (encerrar o programa)')
                        print()
                        cfim = str(input('Digite: ')).strip()
                        if cfim in ['s', 'S', 'n', 'N']:
                            lp()
                            break
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                        print()
                    break
            if bfim in ['n', 'N'] and cfim in ['n', 'N']:
                lp()
                print('Obrigado por testar o script ;)')
                print()
                input('Pressione ENTER para fechar.')
                exit()
            elif bfim in ['n', 'N'] and cfim in ['s', 'S']:
                break
            else:
                continue


        #Função 2
        #Pre-salvamento caracteres
        elif serv == '2':
            min = 'abcdefghijklmnopqrstuvwxyz'
            mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            num = '0123456789'
            sib = '[]{}()*#;/,-_%'

            #Ínicio gerador
            while True:
                while True:
                    try:
                        quant = int(input('Digite a quantidade de caracteres (max: 100): '))
                        break
                    except ValueError:
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Digite apenas números! Tente novamente.')
                        print()
                if quant <=100 and quant > 0:
                    break
                elif quant > 100:
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Número max: 100! Tente novamente.')
                    print()
                else:
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Digite um número maior que 0! Tente novamente.')
                    print()

            length = quant

            #Opções
            lp()
            while True:
                print('Qual das opções se adapta melhor a sua necessidade?:')
                print()
                print('Opção 1 - Apenas letras')
                print('Opção 2 - Apenas números')
                print('Opção 3 - Letras e números')
                print('Opção 4 - Letras, números e símbolos (*#;/,-_%)')
                print()
                nc = str(input('Digite a opção desejada: ')).strip()

                #EasterEgg Lore 2
                if nc in ['1/8', '01/8', '1/08', '01/08']:
                    lorena_easter_egg()
                    print()

                elif nc in ['1', '2', '3', '4']:
                    break
                else:
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Digite apenas uma das opções! Tente novamente.')
                    print()

            def gs(comp, carc):
                senha = ''
                for _ in range(comp):
                    senha += random.choice(carc)
                return senha

            #Loading
            lp()
            print('Gerando senha, por favor aguarde')
            time.sleep(0.5)
            lp()
            print('Gerando senha, por favor aguarde.')
            time.sleep(0.5)
            lp()
            print('Gerando senha, por favor aguarde..')
            time.sleep(0.5)
            lp()
            print('Gerando senha, por favor aguarde...')
            time.sleep(0.5)
            lp()
            print('Obrigado por usar o gerador! :)\nAqui está a sua senha:')
            print()

            #Op 1 Usando apenas letras
            if nc == '1':
                psle = gs(length, min+mai)
                print(psle)

            #Op 2 Usando apenas números
            elif nc == '2':
                psnu = gs(length, num)
                print(psnu)

            #Op 3 Usando letras e números
            elif nc == '3':
                psln = gs(length, min+mai+num)
                print(psln)

            #Op 4 Usando todos
            else:
                pstd = gs(length, min+mai+num+sib)
                print(pstd)

            #Repetição opcional 2
            while True:
                while True:
                    print()
                    print('Gostaria de voltar ao começo do gerador?\n\nS para Sim\nN para Não')
                    print()
                    bfim = str(input('Digite: ')).strip()
                    if bfim in ['s', 'S', 'n', 'N']:
                        lp()
                        break
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                if bfim in ['s', 'S']:
                    lp()
                    break
                else:
                    while True:
                        print('Gostaria de retornar ao seletor de funções?\n\nS para Sim\nN para Não (encerrar o programa)')
                        print()
                        cfim = str(input('Digite: ')).strip()
                        if cfim in ['s', 'S', 'n', 'N']:
                            lp()
                            break
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                        print()
                    break
            if bfim in ['n', 'N'] and cfim in ['n', 'N']:
                lp()
                print('Obrigado por testar o script ;)')
                print()
                input('Pressione ENTER para fechar.')
                exit()
            elif bfim in ['n', 'N'] and cfim in ['s', 'S']:
                break
            else:
                continue     

        #Jogos
        #Função 4
        elif serv in ['4']:
            print('Opção 1 - Pedra')
            print('Opção 2 - Papel')
            print('Opção 3 - Tesoura')
            play = str(input('Escolha: ')).strip().upper()
            lp()

            def gs(comp, carc):
                joken = ''
                for _ in range(comp):
                    joken += random.choice(carc)
                return joken
            num = '123'
            esc = gs(1, num)

            print('PEEDRA')
            time.sleep(0.4)
            print('PAPEEL')
            time.sleep(0.4)
            print('TESOOURA!')
            time.sleep(0.5)
            print()

            if play == '1' and esc == '1':
                print(Fore.YELLOW+'PEDRA'+Fore.RESET, 'X', Fore.YELLOW+'PEDRA'+Fore.RESET)
                print('EMPATE!')
            elif play == '1' and esc == '2':
                print(Fore.RED+'PEDRA'+Fore.RESET, 'X', Fore.GREEN+'PAPEL'+Fore.RESET)
                print('EU GANHEI! ')
            elif play == '1' and esc == '3':
                print(Fore.GREEN+'PEDRA'+Fore.RESET, 'X', Fore.RED+'TESOURA'+Fore.RESET)
                print('VOCÊ GANHOU!')

            elif play == '2' and esc == '1':
                print(Fore.GREEN+'PAPEL'+Fore.RESET, 'X', Fore.RED+'PEDRA'+Fore.RESET)
                print('VOCÊ GANHOU!')
            elif play == '2' and esc == '2':
                print(Fore.YELLOW+'PAPEL'+Fore.RESET, 'X', Fore.YELLOW+'PAPEL'+Fore.RESET)
                print('EMPATE!')
            elif play == '2' and esc == '3':
                print(Fore.RED+'PAPEL'+Fore.RESET, 'X', Fore.GREEN+'TESOURA'+Fore.RESET)
                print('EU GANHEI!')

            elif play == '3' and esc == '1':
                print(Fore.RED+'TESOURA'+Fore.RESET, 'X', Fore.GREEN+'PEDRA'+Fore.RESET)
                print('EU GANHEI!')
            elif play == '3' and esc == '2':
                print(Fore.GREEN+'TESOURA'+Fore.RESET, 'X', Fore.RED+'PAPEL'+Fore.RESET)
                print('VOCÊ GANHOU!')
            elif play == '3' and esc == '3':
                print(Fore.YELLOW+'TESOURA'+Fore.RESET, 'X', Fore.YELLOW+'TESOURA'+Fore.RESET)
                print('EMPATE!')

            #Repetição opcional 4
            while True:
                while True:
                    print()
                    print('Gostaria de jogar novamente?\n\nS para Sim\nN para Não')
                    print()
                    bfim = str(input('Digite: ')).upper().strip()
                    if bfim in ['S', 'N']:
                        lp()
                        break
                    lp()
                    print(Fore.RED+'ERRO'+Fore.RESET)
                    print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                if bfim in ['S']:
                    lp()
                    break
                else:
                    while True:
                        print('Gostaria de retornar ao seletor de funções?\n\nS para Sim\nN para Não (encerrar o programa)')
                        print()
                        cfim = str(input('Digite: ')).strip()
                        if cfim in ['s', 'S', 'n', 'N']:
                            lp()
                            break
                        lp()
                        print(Fore.RED+'ERRO'+Fore.RESET)
                        print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                        print()
                    break
            if bfim in ['n', 'N'] and cfim in ['n', 'N']:
                lp()
                print('Obrigado por testar o script ;)')
                print()
                input('Pressione ENTER para fechar.')
                exit()
            elif bfim in ['n', 'N'] and cfim in ['s', 'S']:
                break
            else:
                continue

        else:
            webbrowser.get(opera).open_new_tab('https://www.youtube.com/watch?v=6QlQ7CRGTe4')

        #Repetição opcional 4
        while True:
            while True:
                print('Gostaria de retornar ao seletor de funções?\n\nS para Sim\nN para Não (encerrar o programa)')
                print()
                cfim = str(input('Digite: ')).strip()
                if cfim in ['s', 'S', 'n', 'N']:
                    lp()
                    break
                lp()
                print(Fore.RED+'ERRO'+Fore.RESET)
                print('Não foi possível entender o seu comando. Por favor, digite apenas "S" ou "N"! Tente novamente.')
                print()
            break
        if cfim in ['n', 'N']:
            lp()
            print('Obrigado por testar o script ;)')
            print()
            input('Pressione ENTER para fechar.')
            exit()
        elif cfim in ['s', 'S']:
            break
        else:
            continue