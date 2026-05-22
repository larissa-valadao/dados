class Avaliacao:
    def __init__(self, cliente = '', nota = float):
        self._cliente = cliente
        
        if ((nota < 0) or (nota > 5)):
            raise ValueError("Valor não permitido. Insira valores entre 0 e 5!")       
        self._nota = round(nota,1)      
