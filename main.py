from preco import Preco
from calculadora import Calculadora
from menu import Menu
preco = Preco()
menu_inicial: float

calc = Calculadora()
menu = Menu()


calc.km:float = float (input(
    'Informe o KM rodado: '
))

if menu.menu_inicial == 3:
    preco.preco_diesel = float(input('Qual o preço do diesel? '  ))
    calc.calcular_total_diesel(calc.km, preco.preco_diesel)
    print('O preço total do diesel é: R$', calc.total_diesel)
elif menu.menu_inicial == 2:
    preco.preco_etanol = float(input('Qual o preço do etanol? '))
    calc.calcular_total_etanol(calc.km, preco.preco_etanol)
    print('O preço total do etanol é: R$', calc.total_etanol)

elif menu.menu_inicial == 1:
    preco.preco_gasolina = float(input('Qual o preço da gasolina? '))
    calc.calcular_total_gasolina(calc.km, preco.preco_gasolina)
    print('O preço total da gasolina é: R$', calc.total_gasolina)
    calc.calcular_percentual(preco.preco_gasolina)

elif menu.menu_inicial == 4:
    preco.preco_etanol = float(input('Qual o preço do etanol? '))
    calc.calcular_total_etanol(calc.km, preco.preco_etanol)
    preco.preco_gasolina = float(input('Qual o preço da gasolina? '))
    calc.calcular_total_gasolina(calc.km, preco.preco_gasolina)
    print('O preço total do etanol é: R$', calc.total_etanol)
    print('O preço total da gasolina é: R$', calc.total_gasolina)
    calc.calcular_percentual(preco.preco_gasolina)
    print('O preço ideal do etanol deve estar abaixo de: ', calc.preco_ideal_etanol)










