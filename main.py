class MaquinaTuring:
    def __init__(self, cinta, estadoI, estadosF):
        self.cinta = list(cinta)
        self.cabezal = 0
        self.estado = estadoI
        self.estadosF = estadosF