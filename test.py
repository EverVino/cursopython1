from hw1 import suma3
from hw2 import contar_letras 
from hw3 import lejano_n
from hw4 import convertir_grados

def testhw1():
    assert suma3(1, 2, 3) == 6 , "Resultado incorrecto en la suma para 1, 2, 3"
    assert suma3(2, 4, 5) == 11, "Resuldado incorrecto para suma3(2, 4, 5)"
    assert suma3(0, 0, 0) == 0, "Resultado incorrecto para suma3(0, 0, 0)"
    print("hw1 Correcto! :)")

def testhw2():
    assert contar_letras("hola") == 4, "Resultados incorrecto para contar_letras('hola')"
    assert contar_letras("") == 0, "Resultado incorrecto para contar_letras('')"
    assert contar_letras("123LITROS") == 9, "Resultado incorrecto para contar_letras('123LITROS')"
    print("hw2 Correcto! :)")

def testhw3():
    assert lejano_n(1) =="Los laboratorios se encuentran en un lugar muy lejano.", ":( No funciona con 1)"
    assert lejano_n(3) == "Los laboratorios se encuentran en un lugar muy, muy, muy lejano.", ":( No funciona con 3"
    assert lejano_n(0) == "Los laboratorios se encuentran en un lugar lejano.", ":( No funciona con 0"
    print("hw3 Correcto! :)")

def testhw4():
    assert convertir_grados(100) == 212, "No convierte correctamente 100"
    assert convertir_grados(0) == 32, "No convierte correctamente 0 "
    assert convertir_grados(25) == 77, "No convierte correctamente 25"
    print("hw4 Correcto! :)")

testhw1()
testhw2()
testhw3()
testhw4()