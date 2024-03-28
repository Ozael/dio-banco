import os, platform

MENU = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

LIMITE_SAQUES_DIARIOS = 3
LIMITE_POR_SAQUE = 500

saldo = 0
saques_realizados = 0


def limpar_console():
    if platform.system() == "Windows":
        clear = lambda: os.system('cls')
        clear()
    else:
        os.system('clear')

def extrato(saldo, saques):
    print(f"""
    Saldo:          ${saldo}
    Total de Saques: {saques}
""")

def deposito(valor_deposito):
    global saldo 
    saldo += valor_deposito

def saque(valor_saque, limite_valor, limite_saques_diarios):
    global saldo
    global saques_realizados
    if saques_realizados < limite_saques_diarios:
        if valor_saque <= limite_valor:
            if saldo >= valor_saque:
                saldo -= valor_saque
                saques_realizados += 1
        else:
            print("Limite acima do permitido")
            print(f"Limite permitido ${limite_valor}")
    else:
        print("Limite Atingido de saques")

while True:
    limpar_console()
    print(MENU)
    opcao = int(input())
    match opcao:
        case 1:
            deposito(valor_deposito=float(input("Digite o valor a ser depositado: $")))
            continue
        case 2:
            saque(valor_saque=float(
                input("Quanto deseja sacar? $ ")), 
                limite_valor = LIMITE_POR_SAQUE, 
                limite_saques_diarios = LIMITE_SAQUES_DIARIOS)
            continue
        case 3:
            extrato(saldo, saques_realizados)
        case 4:
            print("Obrigado por utilizar nosso banco")
            print("Volte sempre :)")
            break
    input("Aperte qualquer tecla para continuar")