from datetime import date # Importado a class date do modulo datetime (manipulação de datas).

#          (ano, mes, dia) Padrão gregoriano.
data = date(2021, 2, 2) 

print(data) # -> 2021-02-02 configurada 

print('Data Atual: {}'.format(date.today()))

print('Dia: {}'.format(data.day))

print('Mês: {}'.format(data.month))

print('Ano: {}'.format(data.year))

