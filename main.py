import os
import time

saldo = 600
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
qt_saque = []


menu ="""
Escolha uma opção:
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair
\n
 """



def transacoes(opcao,saldo):


  if opcao == '1':
    if len(qt_saque) >= 3:
      print('Limite de saque diario atingido, saque nao liberado!')
      time.sleep(3)
      menu_p(menu,saldo)
    else:
      saque = int(input('Digite o valor do saque.\n'))
      if saldo < saque:
        print('Saldo insuficiente.\n')
      elif saque <= 0:
        print("Digite um valor valido!!")
      elif saque > 500:
        print('Valor de saque excedido!')
      else:
        print('Saque liberado.\n')
        qt_saque.append('sq')
        saldo = saldo - saque
        print(f'Imprimindo extrato...\nSaldo Disponivel: R${saldo:,.2f}\nSaque: R${saque:,.2f}')
  elif opcao == '2':
    deposito = float(input('Informe o valor do deposito.\n'))
    if deposito <=0:
      print('Informe um valor valido!\n')
    else:
      print('Deposito realizado com Sucesso!')
      saldo = saldo + deposito
      print(f'Saldo atualizado {saldo:,.2f}')
  elif opcao == '3':
    print(f'Imprimindo saldo...\nSaldo Atual R${saldo:,.2f}')
  else:
    print("Operação encerrada, Ate Breve!")

  time.sleep(2)
  menu_p(menu,saldo)



def menu_p(menu,saldo):
  os.system('cls')
  print(menu)
  opcao = input()
  transacoes(opcao,saldo)


menu_p(menu,saldo)