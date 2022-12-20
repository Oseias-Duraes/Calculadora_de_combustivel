class Menu:

    def __init__ (self):
        self.menu_inicial = int(input(
        ''' Selecione o tipo de combustível
           [1] Gasolina
           [2] Etanol
           [3] Diesel
           [4] Flex '''))
        if self.menu_inicial >= 5:
            print ('Opção inválida')
            exit()


