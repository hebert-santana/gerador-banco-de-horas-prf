import datetime as dt
import workdays as wd
from prettytable import PrettyTable

meses_validos = [i for i in range(1, 13)]
ano_atual = dt.datetime.now().year
dia_inicial = 1


def ultimoDia(mes):
    # determina dia final do mês
    if mes == 2:
        dia = 28
    elif mes in [4, 6, 9, 11]:
        dia = 30
    else:
        dia = 31
    return dia


while True:
    print()
    print('\033[94m===================================\033[0m \033[1;33mBANCO DE HORAS PRF\033[0m \033[94m===================================\033[0m\n')
    mes = input('Número do Mês: ').strip()
    plantoes = int(input('Informe a quantidade de plantões que está escalado no mês: '))
    num_feriados = int(input('Informe quantos feriados (em dias da semana) há no mês de referência: '))
    if int(mes) in meses_validos:
        mes = int(mes)
        dia_final = ultimoDia(mes)

        data_inicial = dt.date(ano_atual, mes, dia_inicial)
        data_final = dt.date(ano_atual, mes, dia_final)
        dias_uteis = wd.networkdays(data_inicial, data_final) - int(num_feriados)

        # 8 horas a cada dia útil
        horas_a_trabalhar = 8 * dias_uteis
        # cada plantão o PRF acumula 25,5h
        horas_trabalhadas = 25.5 * plantoes
        banco_de_horas = horas_trabalhadas - horas_a_trabalhar

        # cor no saldo do banco de horas
        if banco_de_horas > 0:
            banco_de_horas_cor = f'\033[92m{banco_de_horas} horas\033[0m'
        else:
            banco_de_horas_cor = f'\033[91m{banco_de_horas} horas \033[0m'

        # Criando tabela com prettytable
        tabela = PrettyTable()
        tabela.field_names = ["Descrição", "Valor"]
        tabela.add_row(["Número de dias úteis", f"{dias_uteis} dias"])
        tabela.add_row(["Horas a trabalhar", f"{horas_a_trabalhar} horas"])
        tabela.add_row(["Horas escaladas", f"{horas_trabalhadas} horas"])
        tabela.add_row(["Saldo de horas", banco_de_horas_cor])

        # Imprimindo a tabela
        print(tabela)
        break
    else:
        print('Mês não válido!\nExemplo:\n1 = Janeiro\n11 - Novembro')

print('\033[94m=================================== ================== ===================================\033[0m')
