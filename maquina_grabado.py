class MaquinaGrabadoCuero:
    def __init__(self, marca, modelo, potencia, area_grabado):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.area_grabado = area_grabado
        self.encendida = False
        self.material_actual = ""  # Atributo tipo str

    def encender(self):
        self.encendida = True if not self.encendida else print("La máquina ya está encendida.")
    
    def apagar(self):
        self.encendida = False if self.encendida else print("La máquina ya está apagada.")
    
    def iniciar_grabado(self, material):
        if self.encendida:
            self.material_actual = material
            print(f"Grabando sobre {self.material_actual}.")
        else:
            print("La máquina debe estar encendida para grabar.")


# Instancias de ejemplo
maquina1 = MaquinaGrabadoCuero("LaserPro", "LP1000", 60, (40, 40))
maquina2 = MaquinaGrabadoCuero("CutMaster", "CM500", 40, (30, 30))
maquina3 = MaquinaGrabadoCuero("EngraveX", "EX300", 30, (25, 25))
