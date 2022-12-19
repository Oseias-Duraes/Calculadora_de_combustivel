from preco import Preco
from calculadora import Calculadora

preco = Preco()
tp_combustivel = bool

calc = Calculadora()

tp_combustivel = input('O veículo é a diesel? ')

calc.km:float = float (input(
    'Informe o KM rodado: '
))

if tp_combustivel == 'S':
    preco.preco_diesel = float(input('Qual o preço do diesel? '  ))
    calc.calcular_total_diesel(calc.km, preco.preco_diesel)
    print('O preço total do diesel é: R$', calc.total_diesel)
else:
    preco.preco_etanol = float(input('Qual o preço do etanol? '))
    preco.preco_gasolina = float(input('Qual o preço da gasolina? '))
    calc.calcular_total_gasolina(calc.km, preco.preco_gasolina)
    calc.calcular_total_etanol(calc.km, preco.preco_etanol)
    print('O preço total da gasolina é: R$', calc.total_gasolina)
    print('O preço total do etanol é: R$', calc.total_etanol)










