# Projeto de sistema bancário

O objetivo é fazer uma segunda versão do Sistema Bancário (https://github.com/danielshindi/curso-python-DIO-sistema_bancario) e implementar as três operações essenciais: depósito, saque e extrato, em funções.

Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.



### Função de depósito

A função depósito deve receber os argumentos apenas por posição (positional only).

Sugestão de argumentos: saldo, valor, extrato.

Sugestão de retorno: saldo e extrato.

Deve ser possível depositar valores positivos para a conta bancária.



### Função de saque

A função saque deve receber os argumentos apenas por nome (keyword only).

Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.

Sugestão de retorno: saldo e extrato.

O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.

Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.



### Função de extrato

A função extrato deve receber os argumentos por posição e nome (positional e keyword).

Argumentos posicionais: saldo, argumentos nomeados: extrato.

Essa operação deve listar todos os depósitos e saques realizados na conta.

No fim da listagem deve ser exibido o saldo atual da conta.

Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações".

Os valores devem ser exibidos utilizando o formato R$xxx.xx, exemplo: 1500.45 = R$1500.45



### Novas funções

#### Criar usuário (cliente)

O programa deve armazenar os usuários em uma lista.

Um usuário é composto por: nome, data de nascimento, cpf e endereço.

O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado.

Deve ser armazenado somente os números do CPF (string).

Não podemos cadastrar 2 usuários com o mesmo CPF.



#### Cadastrar conta corrente

O programa deve armazenar contas em uma lista.

Uma conta é composta por: agência, número da conta e usuário.

O número da conta é sequencial, iniciando em 1.

O número da agência é fixo: '0001'.

O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.



##### Dica

- Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF para cada usuário da lista.





