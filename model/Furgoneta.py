from model.Vehiculo import Vehiculo
class Furgoneta(Vehiculo):
    
    def __init__(self, marca, modelo, anio, capacidad_max):
        super().__init__(marca, modelo, anio)
        self.capacidad_max = capacidad_max
    
    def descripcion(self):
        return f"{super().descripcion()}, Cap. Max. = {self.capacidad_max}"
    
    