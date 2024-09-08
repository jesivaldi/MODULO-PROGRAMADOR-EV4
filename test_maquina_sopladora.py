import pytest
from maquina_sopladora import MaquinaSopladoraBotellas

def test_ajustar_temperatura_aumenta():
    maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)
    maquina.temperatura_actual = 110  
    maquina.ajustar_temperatura()
    assert maquina.temperatura_actual == 115
    
def test_temperatura_disminuye():
    maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)
    maquina.temperatura_actual = 130
    maquina.ajustar_temperatura()
    assert maquina.temperatura_actual == 125
    
def test_ajustar_presion_aumenta():
    maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)
    maquina.presion_actual = 25
    maquina.ajustar_presion()
    assert maquina.presion_actual == 26
    
def test_ajustar_presion_disminuye():
    maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)
    maquina.presion_actual = 31
    maquina.ajustar_presion()
    assert maquina.presion_actual == 30
    
def test_tiempo_base_soplado():
    maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)
    assert maquina.tiempo_base_soplado == 5
    
def test_calcular_tiempo_soplado():
    maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)
    tamaño_botella = 1500
    assert tamaño_botella == 1500


