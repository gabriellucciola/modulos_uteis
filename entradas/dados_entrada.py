def receber_int(mensagem, error=False):
    """Recebe um valor e verifica se é um inteiro
    Se o valor não for inteiro solicita novamente
    :param: mensagem = mostra uma mensagem para o usuário orientando o que deve digitar
    :param: error = (opcional) mostra uma mensagem de entrada incorreta para o usuário
    antes de solicitar para digitar novamente um valor válido
    :return: o valor digitado como um número inteiro"""
    while True:
        valor = input(f'{mensagem}').strip()
        if valor.isdigit():
            return int(valor)
        if error:
            print(f"\033[91mERRO! Digite um número inteiro válido.\033[m")


def receber_float(mensagem, error=False):
    """Recebe um valor e verifica se é um float
    Se o valor não for float solicita novamente
    :param: mensagem = mostra uma mensagem para o usuário orientando o que deve digitar
    :param: error = (opcional) mostra uma mensagem de entrada incorreta para o usuário
    antes de solicitar para digitar novamente um valor válido
    :return: o valor digitado como um número float"""
    while True:
        valor = input(f'{mensagem}').strip().replace(",", ".")
        if valor.replace(".", "", 1).isdigit():
            return float(valor)
        if error:
            print(f"\033[91mERRO! Digite um número float válido\033[m")


def receber_str(mensagem):
    """Recebe um valor e retorna uma string
    :param: mensagem = mostra uma mensagem para o usuário orientando o que deve digitar
    :return: o valor digitado como uma string"""
    msg = input(f'{mensagem}')
    return msg


def receber_bool(mensagem):
    """Recebe um valor e verifica se é um booleano
    Se o valor não for booleano solicita novamente
    :param: mensagem = mostra uma mensagem para o usuário orientando o que deve digitar
    :param: error = (opcional) mostra uma mensagem de entrada incorreta para o usuário
    antes de solicitar para digitar novamente um valor válido
    :return: o valor digitado como um booleano"""
    while True:
        valor = input(f'{mensagem}')
        if valor == "True" or valor == False:
            return bool(valor)
        else:
            print(f"\033[91mERRO! Esta entrada deve ser \"True\" ou \"False\"!\033[m")

