from model.SeleccionFutbol import SeleccionFutbol

class Futbolista(SeleccionFutbol):
    
    def __init__(self, id, nombre, apellidos, edad,iddorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.iddorsal = iddorsal
        self.demarcacion = demarcacion
    
    #Método de la clase futbolista
    def entrevista(self):
        return "Entrevista al futbolista"
    
    #Aplicando Polimorfismo
    def partidoFutbol(self):
        return "Estadio Monumental, juega de volante"
    
    def entrenamiento(self):
        return "Entrenamiento en campomar."
        
        

    
 