from datetime import date # Importando a class date do modulo datetime.

#exemplo simples de utilização da class date importada do modulo datetime.

variavel_ano= int(input("Ano de nascimento"))

idade = int(date.today().year) - variavel_ano

print(idade)
