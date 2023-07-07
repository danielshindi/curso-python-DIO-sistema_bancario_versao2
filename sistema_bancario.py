depositos = 0
saques = 0
QUANTIDADE_SAQUE_DIARIO = 3
VALOR_SAQUE_MAX = 500
quantidade_saques = 0
saldo = 0
extrato = ''

menu = '''------------------- Selecione uma opção: ----------------------

    d - Depositar
    s - Sacar
    e - Extrato
    q - Sair

----------------------------------------------------------------
'''

def validaFloat(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor = float(valor)
            if valor > 0:
                break
            else:
                print('Digite valores acima de zero.')
                continue
        except ValueError:
            print('Valor inválido.')
            continue
    return valor    

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += f'+ R${valor:.2f}\n'

def sacar(valor):
    global saldo, extrato
    saldo -= valor
    extrato += f'- R${valor:.2f}\n'


while True:
    opcao = input(menu)
    if opcao in 'Dd':
        valor = validaFloat('Digite o valor do depósito: ')
        depositar(valor)

    elif opcao in 'Ss':
        if quantidade_saques >= QUANTIDADE_SAQUE_DIARIO:
            print(f'\nLimite de {QUANTIDADE_SAQUE_DIARIO} saques diários atingido.\n')
        else:
            valor = validaFloat('Digite o valor do saque: ')
            if valor <= VALOR_SAQUE_MAX:
                if valor <= saldo:
                    sacar(valor)
                    quantidade_saques += 1
                else:
                    print('\nSaldo insuficiente.\n')
            else:
                print(f'\nValor máximo para saque é de R${VALOR_SAQUE_MAX:.2f}.\n')

    elif opcao in 'Ee':
        print('==========================Extrato: ============================')
        print(extrato if extrato != '' else 'Nenhuma movimentação realizada', f'\nSaldo: R${saldo:.2f}')
        print('===============================================================')
    
    elif opcao in 'Qq':
        break

    else:
        print('Opção inválida.')

            
            
                

