import pytest
from maquina_grabado import MaquinaGrabadoCuero

def test_instancias_maquina():
    maquina1 = MaquinaGrabadoCuero("LaserPro", "LP1000", 60, (40, 40))
    maquina2 = MaquinaGrabadoCuero("CutMaster", "CM500", 40, (30, 30))
    maquina3 = MaquinaGrabadoCuero("EngraveX", "EX300", 30, (25, 25))
    
    # Verificamos los atributos 
    assert maquina1.marca == "LaserPro"
    assert maquina2.modelo == "CM500"
    assert maquina3.potencia == 30
    assert maquina1.area_grabado == (40, 40)


# Test para encender la máquina 
def test_encender_apagar_maquina():
    maquina = MaquinaGrabadoCuero("LaserPro", "LP1000", 60, (40, 40))
    assert not maquina.encendida
    maquina.encender()
    assert maquina.encendida
    maquina.apagar()
    assert not maquina.encendida

# Test para iniciar grabado
def test_iniciar_grabado():
    maquina = MaquinaGrabadoCuero("CutMaster", "CM500", 40, (30, 30))
    maquina.iniciar_grabado("cuero")
    assert maquina.material_actual == ""  
    maquina.encender()
    maquina.iniciar_grabado("cuero")
    assert maquina.material_actual == "cuero" 
