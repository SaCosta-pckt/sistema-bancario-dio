from datetime import datetime

menu = """
O que deseja fazer?
Digite o número correspondente à escolha.

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



# Use Cases
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
            return("Operação falhou! O valor informado é inválido.")

def sacar ():
        global saldo
        global extrato
        global numero_saques
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            return ("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            return ("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            return ("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            datahora = datetime.today().strftime("%d/%m/%Y %H:%M")
            extrato += f"{datahora}  Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            return (f"Operação realizada com sucesso! Saldo atual: {saldo:.2f}")

        else:
            return("Operação falhou! O valor informado é inválido.")

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
        '3': exibir_extrato
    }
    
    # Retorna a função correspondente ou uma função padrão para valores não definidos
    return opcoes.get(value, lambda: "Operação inválida, por favor selecione novamente a operação desejada.")()

while True:
    valor_escolha = input(menu)
    if(valor_escolha == '4'): break
    mensagem = switch_case(valor_escolha)
    print(mensagem)
