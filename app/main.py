from datetime import datetime

menu = """
O que deseja fazer?
Digite o número correspondente à escolha.

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar cliente
[5] Criar conta
[6] Listar contas
[7] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []
contas = []



# Use Cases
def criar_cliente():
    global clientes
    
    cpf = input("Digite o CPF(apenas números): ")
    #pesquisa o cpf digitado já existe na base
    pesquisa_cliente = list(filter(lambda cliente: cliente['cpf'] == cpf, clientes))

    if pesquisa_cliente:
        return "[ERRO] Este CPF já foi cadastrado!"
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereco: ")
    telefone = int(input("Digite o telefone: "))

    clientes.append(
        {
            'nome': nome,
            'cpf': cpf,
            'endereco': endereco,
            'data_nascimento': data_nascimento,
            'telefone': telefone
        } 
    )

    return("Cliente cadastrado com sucesso!")

def criar_conta():
    global contas
    global clientes

    cpf = input("Informe o CPF do usuário(apenas números): ")
    pesquisa_cliente = list(filter(lambda cliente: cliente['cpf'] == cpf, clientes))

    if pesquisa_cliente:
        agencia = "0001"
        numero_conta = int(input("Digite o numero da conta: "))
        
        contas.append(
            {
                'conta': numero_conta,
                'agencia': agencia,
                'cpf_cliente': cpf
            }
        )
        print("Deu append!")
        return (f"""
        
        \nUsuário cadastrado com sucesso!

        Conta: {numero_conta}
        Agencia: {agencia}
        Usuário: {pesquisa_cliente[0]['nome']}

        """)
    else:
        return "[ERRO] Não foi encontrado um cliente com este CPF!"
         
def listar_contas():
    global contas
    texto_retorno = "Contas encontradas:"

    cpf = input("Informe o CPF do usuário(apenas números): ")
    pesquisa_contas = list(filter(lambda conta: conta['cpf_cliente'] == cpf, contas))

    if pesquisa_contas:
        for conta in pesquisa_contas:
            texto_retorno += f"""\n

            Conta: {conta['conta']}
            Agencia: {conta['agencia']}
            CPF: {conta['cpf_cliente']}

            """
        return texto_retorno
    else:
        return "[ERRO] Não foi encontrada uma conta com este CPF!"

def depositar ():
        global saldo
        global extrato
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            datahora = datetime.today().strftime("%d/%m/%Y %H:%M")
            extrato += f"{datahora}  Depósito: R$ {valor:.2f}\n"
            return (f"Operação realizada com sucesso! Saldo atual: {saldo:.2f}")

        else:
            return("[ERRO] Operação falhou! O valor informado é inválido.")

def sacar ():
        global saldo
        global extrato
        global numero_saques
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            return ("[ERRO] Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            return ("[ERRO] Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            return ("[ERRO] Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            datahora = datetime.today().strftime("%d/%m/%Y %H:%M")
            extrato += f"{datahora}  Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            return (f"Operação realizada com sucesso! Saldo atual: {saldo:.2f}")

        else:
            return("[ERRO] Operação falhou! O valor informado é inválido.")

def exibir_extrato():
         # Se houver valor em extrato -> mostra | se não -> mensagem alternativa
        return  (f"""
                 \n================ EXTRATO ================
                \n{extrato if extrato else "Não foram realizadas movimentações."}
                \nSaldo: R$ {saldo:.2f}
                \n==========================================""")



# Controlador
def switch_case(value):
    opcoes = {
        '1': depositar,
        '2': sacar,
        '3': exibir_extrato,
        '4': criar_cliente,
        '5': criar_conta,
        '6': listar_contas
    }
    
    # Retorna a função correspondente ou uma função padrão para valores não definidos
    return opcoes.get(value, lambda: "[ERRO] Operação inválida, por favor selecione novamente a operação desejada.")()

while True:
    valor_escolha = input(menu)
    if(valor_escolha == '7'): break
    mensagem = switch_case(valor_escolha)
    print(mensagem)
