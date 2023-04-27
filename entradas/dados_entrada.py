def receber_int(mensagem, error=False):
    while True:
        valor = input(f'{mensagem}').strip()
        if valor.isdigit():
            return int(valor)
        if error:
            print(f"\033[91mERRO! Digite um número inteiro válido.\033[m")


def receber_float(mensagem, error=False):
    while True:
        valor = input(f'{mensagem}').strip().replace(",", ".")
        if valor.replace(".", "", 1).isdigit():
            return float(valor)
        if error:
            print(f"\033[91mERRO! Digite um número float válido\033[m")


def receber_str(mensagem):
    msg = input(f'{mensagem}')
    return msg


def receber_bool(mensagem):
    while True:
        valor = input(f'{mensagem}')
        if valor == "True" or valor == False:
            return bool(valor)
        else:
            print(f"\033[91mERRO! Esta entrada deve ser \"True\" ou \"False\"!\033[m")





inteiro = receber_int("Digite um inteiro: ", True)
real = receber_float("Digite um número real: ", True)
strin = receber_str("Digite o que quiser: ")
booleano = receber_bool("Digite True ou False: ")
