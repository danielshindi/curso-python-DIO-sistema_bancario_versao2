depositos = 0
saques = 0
QUANTIDADE_SAQUE_DIARIO = 3
VALOR_SAQUE_MAX = 500
AGENCIA = '0001'
quantidade_saques = 0
saldo = 0
extrato = ''
usuarios = []
contas = []
numero_conta = 1

menu = '''------------------- Selecione uma opção: ----------------------

    d - Depositar
    s - Sacar
    e - Extrato
    u - Cadastrar usuário
    c - Cadastrar conta corrente
    l - Listar contas
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

def depositar(valor, saldo, extrato):
    saldo += valor
    extrato += f'+ R${valor:.2f}\n'
    return saldo, extrato

def sacar(*, valor, saldo, extrato):
    saldo -= valor
    extrato += f'- R${valor:.2f}\n'
    return saldo, extrato

def emitir_extrato(saldo, *, extrato):
    print('==========================Extrato: ============================')
    print(extrato if extrato != '' else 'Nenhuma movimentação realizada', f'\nSaldo: R${saldo:.2f}')
    print('===============================================================')

def busca_cpf(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def cadastrar_usuario():
    cpf = input('Digite seu CPF (apenas números): ')
    if busca_cpf(cpf):
        print('Usuário já cadastrado!')
    else:
        nome = input('Digite seu nome completo: ')
        nascimento = input('Digite sua data de nascimento: ')
        print('Digite seu endereço:')
        logradouro = input('Logradouro: ')
        numero_endereco = input('Número: ')
        bairro = input('Bairro: ')
        cidade_estado = input('Cidade/Estado: ')

        usuario = {"cpf": cpf,
                "nome": nome,
                "nascimento": nascimento,
                "endereco": {"logradouro": logradouro,
                            "número": numero_endereco, 
                            "bairro": bairro, 
                            "cidade/estado": cidade_estado
                            }
                    }
        usuarios.append(usuario)
    
def criar_conta(contas):
    cpf = input('Digite o CPF do usuário: ')
    usuario = busca_cpf(cpf)
    if not usuario:
        print('Usuário não cadastrado!')
        return None
    else:
        conta = {'agencia': AGENCIA,
                'numero_conta': numero_conta,
                'usuario': usuario}
        print('Conta criada com sucesso!')
        return conta

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


#---------------------------------------------- Main ----------------------------------------------------
while True:
    opcao = input(menu)
    if opcao in 'Dd':
        valor = validaFloat('Digite o valor do depósito: ')
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao in 'Ss':
        if quantidade_saques >= QUANTIDADE_SAQUE_DIARIO:
            print(f'\nLimite de {QUANTIDADE_SAQUE_DIARIO} saques diários atingido.\n')
        else:
            valor = validaFloat('Digite o valor do saque: ')
            if valor <= VALOR_SAQUE_MAX:
                if valor <= saldo:
                    saldo, extrato = sacar(valor=valor, saldo=saldo, extrato=extrato)
                    quantidade_saques += 1
                else:
                    print('\nSaldo insuficiente.\n')
            else:
                print(f'\nValor máximo para saque é de R${VALOR_SAQUE_MAX:.2f}.\n')

    elif opcao in 'Ee':
        emitir_extrato(saldo, extrato=extrato)
    
    elif opcao in 'Qq':
        break
    elif opcao in 'Uu':
        cadastrar_usuario()
    elif opcao in 'Cc':
        conta = criar_conta(contas)
        if conta:
            contas.append(conta)
            numero_conta += 1    
    elif opcao in 'Ll':
        listar_contas(contas)
    else:
        print('Opção inválida.')
