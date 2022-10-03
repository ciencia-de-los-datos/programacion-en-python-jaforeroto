
from numpy import append
from pyparsing import line
from sqlalchemy import false


datos=[]
with open('data.csv','r') as file:
    for line in file:
        line=line.replace(chr(32),"")
        line=line.replace("\n","")
        tupla = tuple(list(line.split("\t")))
        datos.append(tupla)


def pregunta_01():

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    segunda_columna = [linea[1] for linea in datos[0:]]
    segunda_columna = [int(linea) for linea in segunda_columna]

    """
    lista1 = [int(elemento) for linea in datos for elemento in linea[1]]
    return sum(lista1)

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    lista2 = [linea[0] for linea in datos[0:]]
    lista2 = [
        
        ("A",lista2.count("A")),
        ("B",lista2.count("B")),
        ("C",lista2.count("C")),
        ("D",lista2.count("D")),
        ("E",lista2.count("E")),
    ]
    
    return lista2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    lista3 = [linea[0:2] for linea in datos]
    lista3 = [(linea[0], int(linea[1])) for linea in lista3]
    listaB = []
    for a in dict(lista3).keys():
        i = 0
        for (x,y) in lista3:
            if x == a:
                i += y # Es lo mismo que i = i + y
        listaB.append((a,i)) 
    listaB.sort(reverse = False)

    return listaB

    '''
    lista3 =[(k, sum([y for (x,y) in lista3 if x == k])) for k in dict(lista3).keys()]
    lista3.sort(reverse = False)
    '''


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista4 = [linea[2].split("-")[1] for linea in datos]
    lista4 = [(k,sum([1 for x in lista4 if x == k])) for k in list(dict.fromkeys(lista4))]
    lista4.sort(reverse = False)

    return lista4

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista5 = [linea[0:2] for linea in datos]
    lista5 = [(linea[0], int(linea[1])) for linea in lista5]
    lista5 = [(k, max(y for (x,y) in lista5 if x == k), min(y for (x,y) in lista5 if x == k)) for k in dict(lista5).keys()]
    lista5.sort()
    

    # for a in dict(lista5).keys(): 
    #     max = 0
    #     min = 0
    #     for (x,y) in lista5:
    #         if a == x:
    #             # min(lista5[1])
    #             if y > max:
    #                 max = y   
    #     listaC.append((a,max,min))


    return lista5


def pregunta_06():

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista6 = [linea[4] for linea in datos]
    lista6 = [linea.split(",") for linea in lista6]
    lista6 = [item for lista in lista6 for item in lista]
    lista6 = [linea.split(":") for linea in lista6]
    lista6 = [(linea[0], int(linea[1])) for linea in lista6]
    lista6 = [(k, min(y for (x,y) in lista6 if x == k), max(y for (x,y) in lista6 if x == k)) for k in dict(lista6).keys()]
    lista6.sort()

    return lista6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    
    """
    lista9 = [linea[4] for linea in datos]
    lista9 = [linea.split(",") for linea in lista9]
    lista9 = [item for lista in lista9 for item in lista]
    lista9 = [linea.split(":") for linea in lista9]
    lista9 = [linea[0] for linea in lista9]
    lista9 = [(k,sum([1 for x in lista9 if x == k])) for k in list(dict.fromkeys(lista9))]
    lista9.sort()
    lista9 = dict(lista9)
    
    return lista9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    

    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
