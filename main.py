from model.Deportivo import Deportivo
from model.Furgoneta import Furgoneta
from model.Miniband import Miniband
from model.Futbolista import Futbolista

#Creando el objeto a partir de la instancia 
objFutbolista = Futbolista(1, "Paolo", "Guerrero", 40, 99, "Delantero")
print(objFutbolista.partidoFutbol())



objDeportivo = Deportivo("Ferrari", "550", 
                         "2020", 320)

print(objDeportivo.descripcion())
objDeportivo.marca = "Moustage"
objDeportivo.modelo = "F850"
print(objDeportivo.descripcion())
print(objDeportivo.abastecerGasolina())

objFurgoneta = Furgoneta("Changan", "x89", "2022", 20000)
print(objFurgoneta.descripcion())

objMiniband = Miniband("Toyota", "Cross", "2024", 15)
print(objMiniband.descripcion())