"""
    @reroes
    Counter
    Functional Python Programming - 2015

"""
from collections import Counter


cadena = """Ecuador es un país que se extiende por el ecuador en la costa oeste de Sudamérica. Sus diversos paisajes abarcan la selva del Amazonas, las zonas altas andinas y las islas Galápagos de abundante fauna. En las laderas de los Andes, a una elevación de 2,850 m, Quito, su capital, es famosa por su centro colonial español que se ha conservado intacto por mucho tiempo, con palacios decorados del siglo XVI y XVII y sitios religiosos, como la ornamentada Iglesia de la Compañía de Jesús."""

cadena = cadena.split(" ")
lista = Counter(cadena).most_common(2) 
print(lista)

