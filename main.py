import random
import re
import os

def __formata_CPF(cpf):
    return re.sub(
        r'[^0-9]', '', cpf
    )
    
def __verifica_cpf(cpf_formatado, digito_1, digito_2):
    if cpf_formatado[-1] == digito_2 and cpf_formatado[-2] == digito_1:
        return True
    return False

def __verifica_entrada_repetida(cpf):
    repetido = cpf[0] * len(cpf)
    return True if repetido == cpf else False

def __soma_digitos(digitos, contador_regressivo):
    soma = 0
    for digito in digitos:
        soma += int(digito) * contador_regressivo
        contador_regressivo -= 1

    resultado = (soma * 10) % 11
    return resultado if resultado <= 9 else 0

while True:
    digitos = ''
    digito_1 = ''
    digito_2 = ''
    option = input('O que deseja fazer?\n'
                   '[1] Gerar CPF válido\n'
                   '[2] Verificar se CPF é valido\n'
                   ':'
                   )
    
    os.system('clear')
    match option:
        case '1':
            for _ in range(9):
                digitos += str(random.randint(0, 9))

            digito_1 = __soma_digitos(digitos, len(digitos)+1)

            digitos += str(digito_1)
            digito_2 = __soma_digitos(digitos, len(digitos)+1)

            cpf_gerado = digitos + str(digito_2)

            print(cpf_gerado)
        
        case '2':
            cpf = input('Digite o CPF [xxx.xxx.xxx-xx]: ')
            repetido = __verifica_entrada_repetida(cpf)

            if repetido:
                print('CPF inválido por números repetidos')

            cpf_formatado = __formata_CPF(cpf)
            digitos = cpf_formatado[:9]

            digito_1 = __soma_digitos(digitos, len(digitos)+1)

            digitos += str(digito_1)
            digito_2 = __soma_digitos(digitos, len(digitos)+1)

            cpf_valido = __verifica_cpf(cpf_formatado, str(digito_1), str(digito_2))
            resposta = 'CPF válido' if cpf_valido == True else 'CPF Invalido'
            print(resposta)
        
        case _:
            print('Selecione uma opção válida')
            continue
    input('Aperte enter para continuar')
    os.system('clear')