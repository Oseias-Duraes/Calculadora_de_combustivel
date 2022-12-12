from preco import Preco
from calculadora import Calculadora


calc = Calculadora()

preco: float= (Preco(
    float(input ('Qual o preço da gasolina: ')),
    float(input ('Qual o preço do etanol: ')),
    float(input ('Qual o preço da diesel: '))
))

calc.km:float = float (input(
    'Informe o KM rodado: '
))

calc.calcular_total_gasolina(calc.km,preco.preco_gasolina)
calc.calcular_total_diesel(calc.km,preco.preco_diesel)
calc.calcular_total_etanol(calc.km,preco.preco_etanol)

print ('O preço total da gasolina é: R$', calc.total_gasolina)
print ('O preço total do etanol é: R$', calc.total_etanol)
print ('O preço total do diesel é: R$', calc.total_diesel)