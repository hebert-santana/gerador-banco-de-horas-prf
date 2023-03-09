import datetime as dt
# pacote para calcular dias úteis
import workdays as wd

print('===================== BANCO DE HORAS PRF =====================\n')
ano = 2023
dia_inicial = 1
mes = int(input('Informe o número do mês de referência: '))
dia_final = int(input('Informe qual o último dia do mês de referência (28 ou 30 ou 31): '))
feriados = int(input('Informe quantos feriados (em dias da semana) há no mês de referência: '))

data_inicial = dt.date(ano, mes, dia_inicial)
data_final = dt.date(ano, mes, dia_final)

dias_uteis = wd.networkdays(data_inicial, data_final) - feriados

# 8 horas a cada dia útil
horas_a_trabalhar = 8 * dias_uteis

# cada plantão acumula 25,5h
plantoes_no_mes = int(input('Informe a quantidade de plantões que está escalado no mês: '))
horas_trabalhadas = 25.5 * plantoes_no_mes

saldo_horas = horas_trabalhadas - horas_a_trabalhar

dias_uteis = print(f'\nNúmero de dias úteis: {dias_uteis}\nHoras a trabalhar: {horas_a_trabalhar}\nHoras escalado: {horas_trabalhadas}\nSaldo de horas: {saldo_horas}\n' )
print('===================== ================== =====================')

