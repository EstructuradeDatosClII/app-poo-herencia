from model.Vehiculo import Vehiculo
class Miniband(Vehiculo):
    
    def __init__(self, marca, modelo, anio, cant_pasajeros):
        super().__init__(marca, modelo, anio)
        self.cant_pasajeros = cant_pasajeros
    
    def descripcion(self):
        return f"{super().descripcion()}, Pasajeros: {self.cant_pasajeros}"