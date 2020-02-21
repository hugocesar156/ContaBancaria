import os
import control
import menuPrincipal

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('LOGIN DE ACESSO\n')
    print('1 - Acessar uma conta')
    print('2 - Criar uma conta')
    print('3 - Finalizar programa')

    while True:
         x = int(input(': '))
           
         if (x == 1 or x == 2 or x == 3):
              break
               
         else:
             input('Opção inválida.\n:')
    clr()

    if (x == 1):
        conta = control.Conta()
        conta.numero = int(input('Número da conta: '))

        try:
            if (control.checaNumero(conta) == True):
                
                control.pegaRegistro(conta)
                menuPrincipal.menu(conta)
            else:
                 print('Número de conta não encontrado.\n')
                            
        except:
               print('Algo deu errado\n')
            
    elif (x == 2):
        print('CONTA BANCÁRIA\n')
        print('Tipo de conta:')
        print('1 - Conta Corrente')
        print('2 - Conta Poupança')

        while True:
            x = int(input(': '))
            if (x == 1 or x == 2):
                break
            else:
                input('Opção inválida.\n:')
                
        clr()

        conta = control.Conta()
        conta.numero = int(input('Número da conta: '))
        conta.tipo = int(x)
        conta.dono = input('Nome: ')

        try:
            if (control.checaNumero(conta) == False):
                
                control.criarConta(conta)
                input('\nConta criada com sucesso!\n')

            else:
                input('\nNumero de conta já registrado.\nFalha ao cadastrar\n')
                             
        except:
            input('\nAlgo deu errado.\n')

    else:
        input('\nFim da execução do programa\n')
        break

    clr()
