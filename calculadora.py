class Calculadora:
    km: float
    total_gasolina: float
    total_etanol: float
    total_diesel: float

    def calcular_total_gasolina (self,km, preco_gasolina):
        self.total_gasolina = km * preco_gasolina
        ## return self.total_gasolina -- não necessário pois o print está no main.py


    def calcular_total_etanol(self,km, preco_etanol):
        self.total_etanol = km * preco_etanol
        ## return self.total_etanol -- não necessário pois o print está no main.py


    def calcular_total_diesel(self,km, preco_diesel):
        self.total_diesel = km * preco_diesel
        ## return self.total_diesel -- não necessário pois o print está no main.py
