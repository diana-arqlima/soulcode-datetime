# Módulo Datetime ⏰

## O que é o módulo datetime ?

O módulo **datetime** fornece classes para manipulação de datas e horas

## Objetos conscientes e ingênuos
Objetos de data e hora podem ser categorizados como “cientes” ou “ingênuos”, dependendo se incluem ou não informações de fuso horário.

Objetos do tipo ```date``` são sempre ingênuos.

Um objeto do tipo ```time``` ou ```datetime``` pode ser consciente ou ingênuo.

A distinção entre ciente e ingênuo não se aplica a objetos ```timedelta```.

## *class* datetime.date 📅
Uma data do tipo ingênua baseada no calendário gregoriano atual.

Utilizamos a classe ```date``` quando iremos trabalhar somente com datas.

**Atributos:**
- year
- month
- day
```python
>>> from datetime import date

>>> year, month, day = 2021, 11, 19
>>> date_ = date(year, month, day)
>>> print (date_)
```
### *classmethod* date.today()
Retorna a data local atual.
```python
>>> today = date.today()
>>> print (today)
```
### *classmethod* date.fromisocalendar (year, week, day)
Retorna um objeto ```date``` correspondente à data especificada por ano, semana e dia.
```python
>>> date_ = date.fromisocalendar(2021,2,1)
>>> print (date_)
```
### *classmethod* date.isocalendar( )
Retorna uma tupla chamando objeto com três componentes: **year**, **week** e **weekday**.
```python
>>> date_ = date(2021,11,19).isocalendar()
>>> print (date_)
```
## *class* datetime.time ⏳ *class* datime.datetime 📅⏳
Os dois possuem métodos iguais da classe ```date```.

Utilizamos a classe ```time``` quando iremos trabalhar somente com horas e minutos.

Utilizamos a classe ```datetime``` quando iremos trabalhar com data, horas e minutos.


[*Documentação original*](https://docs.python.org/3/library/datetime.html)