import os
import control

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(obj):
    while True:
        print('MENU PRINCIPAL\n')
        print('1 - Abrir conta')
        print('2 - Informações de conta bancária')
        print('3 - Realizar depósito')
        print('4 - Realizar saque')
        print('5 - Pagar mensalidade')
        print('6 - Fechar conta')
        print('7 - Sair')

        op = int(input(': '))
        clr()

        if (op == 1):
            print('ABRIR CONTA BANCÁRIA:\n')

            if (obj.tipo == 1):
                print('Valor de inicialização de Conta Corrente: R$ 50.00\n')
            else:
                print('Valor de inicialização de Conta Poupança: R$ 150.00\n')

            x = int(input('Continuar? [1 - Sim, 2 - Não]\n: '))

            if (x == 1):
                try:
                    if (control.abrirConta(obj) == True):
                         print('Conta bancária aberta.\n')    
                    else:
                      print('A conta já está aberta.\n')
                 
                except:
                    print('Algo deu errado')
            else:
                print('Operação cancelado pelo usuário\n')
                
        elif (op == 2):
            print('INFORMAÇÕES DE CONTA BANCÁRIA:\n')
            print('Número de conta:',obj.numero)
            print('Proprietário:', obj.dono)

            if (obj.tipo == 1):
                tipo = 'Conta Corrente'
            else:
                tipo = 'Conta Popupança'
            print('Tipo de conta:',tipo)

            print('Saldo atual: R$',obj.saldo)

            if (obj.status == True):
                status = 'Aberta'
            else:
                status = 'Fechada'

            print('Status:',status)

        elif (op == 3):
            print('REALIZAR DEPÓSITO:\n')

            if (obj.status == True):
                valor = float(input('Valor do depósito: R$ '))

                try:
                     if (control.depositar(obj, valor) == True):
                          print('Depósito realizado com sucesso.\n' + 
                          'Saldo atual: R$',obj.saldo)           
                     else:
                          print('Valor inválido.\n')
                except:
                     print('Algo deu errado.')                  
            else:
                print('Não é possível realizar depósito.\nConta fechada.\n')

        elif (op == 4):
             print('REALIZAR SAQUE:\n')

             if (obj.status == True):
                 valor = float(input('Valor do saque: R$ '))

                 try:
                      if (control.sacar(obj, valor) == True):
                           print('Saque realizado com sucesso.\n' + 
                                  'Saldo atual: R$',obj.saldo)    
                      else:
                           print('Valor excedente ao saldo atual ou inválido.\n')

                 except:
                      print('Algo deu errado')
             else:
                  print('Não é possível realizar saque.\nConta fechada.\n')

        elif (op == 5):
            print('PAGAR MENSALIDADE:\n')

            try:
                control.pagarMensal(obj)
                print('Mensalidade paga.\n')
            except:
                print('Algo deu errado')
            
        elif (op == 6):
            print('FECHAR CONTA:\n')
            x = int(input('Tem certeza que deseja continuar? [1 - Sim, 2 - Não]\n: '))

            if (x == 1):
                try:
                    if (control.fecharConta(obj) == True):
                        print('Conta fechada.\n')
                    else:
                        print('A conta deve possuir saldo zerado para realizar ação.\n')

                except:
                    print('Algo deu errado')
                       
        elif (op == 7):
            break
            
        input('Pressione qualquer tecla para voltar ao Menu Principal\n: ')
        clr()
