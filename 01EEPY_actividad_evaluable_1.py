

PROFESSOR's comments to redo the whole thing:

Only 1 and 3 are correct! I got 5/10


# # Ejercicio 1. (1 punto) Resolver los apartados 1.1 y 1.2:

# # 1.1. Crear una lista ordenada que contenga los números del 1 al 20 (ambos inclusive).
# # 1.2. Usando la lista creada en el apartado 1.1, mostrar por pantalla otra lista que contenga sólo los números múltiplos de 5, es decir: [5, 10, 15, 20].
# En ambos apartados, no está permitido usar condiciones (por ejemplo, x % 5 == 0), 
# ni sentencias condicionales (if), ni bucles (while o for). 
# Además, tampoco se pueden usar las expresiones literales de las listas (u otros tipos de datos compuestos) para escribir de manera literal las listas que se piden.
Mario says: OK

numeros_lista = list(range(1, 20+1))
print(numeros_lista[4::5])


# Ejercicio 2. (1 punto) Crear una función que reciba un parámetro como entrada. 
# Este parámetro debe ser una lista que puede contener objetos de diferentes tipos. 
# Por simplificar, para este problema se consideran únicamente números enteros, 
# números decimales y strings. La función debe devolver como salida 
# (es decir, el resultado de la función debe ser) la suma de los números (enteros y decimales) 
# e ignorar los strings. Ejemplo: el resultado para la lista ['b', 'c', 1, 3.4, 'a', 2] sería 6.4.

MARIO says:
2.

- No necesitas la lista "lista_sumar". Lo correcto es usar una variable que referencie a un objeto de tipo "int". 
Esta variable la puedes usar para ir acumulando el resultado (la suma) en cada iteración del bucle.

- Las funciones, lo convencional, es que devuelvan su resultado por medio de un "return", 
no que muestren información con "print".

- Contestando a tu comentario al principio del ejercicio, no se necesita usar lambdas en este caso.

1/1 # Me da resultado (NONE), no sé cómo utilizar lambada en este caso

def funcion(lista1): 
    for i in lista1:
        lista_sumar = []
        if type(i) == 'float' or type(i) == 'int':
            total = lista_sumar.append(i)
            print(total)
            
lista2 = ['b', 'c', 1, 3.4, 'a', 2]
print(funcion(lista2))

# **Ejercicio 3.** (2 puntos) Escribir un programa (sin funciones) 
# que compare dos diccionarios cualquiera y muestre *True* por pantalla si tienen algún elemento en común y *False* 
# en caso contrario. Tener un elemento en común significa que existe un elemento (clave-valor) 
# que está presente en ambos diccionarios. Por ejemplo, el programa mostrará *True* para 
# los diccionarios a = {'a': 3, 'b': 4} y b = {'c': 1, 'a': 3} 
# dado que ambos incluyen el elemento 'a': 3.

Mario says: OK

dic1 = {'a': 3, 'b': 4}
dic2 = {'c': 1, 'a': 3} 

if dic1.items() & dic2.items():
    print(True)
    print("Los elementos (clave-valor) son:", dic1.items() & dic2.items())
else:
    print(False)


# **Ejercicio 4.** (2 puntos) Escribe una función que reciba como parámetros dos strings y 
# compruebe si estos strings cumplen las siguientes propiedades: 
# (1) ambos strings tienen los mismos caracteres y, además, 
# (2) estos caracteres aparecen el mismo número de veces 
# en ambos strings (es decir, si el primer string tiene 3 'a', por ejemplo, el segundo string también tendrá 3 'a', 
# aunque éstas pueden aparecer en posiciones diferentes). 
# Para resolver el problema, **no** puedes importar ningún módulo de Python (como, por ejemplo, *collections*) 
# ni usar funciones de ordenación (como *sort*).

#    * Ejemplos para los que la función devolverá *False*:
#        * 'hola' y 'adios'.
#        * 'java' y 'javascript'.
#        * 'maria' y 'mariam'.
#        * 'aab' y 'abb'.


#    * Ejemplos para los que la función devolverá *True*:
#        * 'python' y 'python'
#        * 'listen' y 'silent'
#        * 'aabbcc' y 'abcabc'

Mario says:
- En este ejercicio, sería más natural que la función devolviera True o False.

- El segundo bucle nunca se ejecuta. 
Fíjate que siempre terminas la función en la primera iteración del primer bucle.

- En este ejercicio, debes calcular las frecuencias de aparición de cada caracter en cada string y luego compararlas. 
Es importante tener en cuenta que sólo se puede terminar la función antes de tiempo 
(con return False) si se determina que los strings no satisfacen las propiedades que se especifica. Sólo se debe hacer "return True" al final, en este ejercicio.


def match(string_1, string_2):
    for character in string_1:
        if character in string_2 and len(string_1) == len(string_2):
            return f"Los dos strings {string_1} y {string_2} tienen los mismos caracteres"
        else:
            return f"Los dos strings {string_1} y {string_2} NO tienen los mismos caracteres"
# 1/2-----El siguiente loop no tiene output!!!!
    for character in string_1:
        stringChar_1 = string_1[character]
        stringChar_2 = string_1[character]
        if string_1.count(stringChar_1) == string_2.count(stringChar_2):
# 2/2 -----This is an extra: How can I get the actual letters that are repeated, as in the following line?
            # print(f"Ambos tienen las mismas repeticiones de la/s misma/a letras {stringChar_1}")
            return "Ambos tienen las mismas repeticiones de la/s misma/a letras."
        else:
            return "Ambos NO tienen las mismas repeticiones de la/s misma/a letras."
# REPETIDO--------This is an extra: How can I get the actual letters that are repeated, as in the following line?
            # print(f"Ambos NO tienen las mismas repeticiones de la/s misma/a letras {stringChar_2}")
print(match("python", "python"))
print(match("listen", "slient"))
print(match("aabbcc", "abcabc"))
print(match("hola", "adios"))
print(match("java", "javsascript"))
print(match("maria", "mariam"))



# **Ejercicio 5.** (2 puntos) En "*./actividades/res/ciudades.csv*" tenéis un fichero CSV con información acerca de un conjunto de ciudades: 
# nombre de la ciudad, país al que pertenece y número de habitantes. Escribir un programa que acceda al fichero y obtenga:

# * Una *lista* con los nombres de las ciudades españolas que tienen más de 300.000 habitantes.
# * El *número total* de ciudades francesas.

# El programa debe mostrar la lista y el número por pantalla.

Mario says:
- Tienes especificado de manera incorrecta el delimitador. El del fichero es "|", 
por lo que tu código no parte bien las líneas del fichero.

- Te falta un cero en "30000".

- Usas "total_ciudades_francesas" de manera incorrecta para guardar el resultado de "csv.reader(...)"

- No es necesario almacenar las ciudades francesas en una lista. Se puede usar un contador.

1/2# He cambiado '|' a ',' en el fichero 'ciudades.csv' y siempre me sale el error 'list index out of range'.


import csv

with open("ciudades.csv") as fichero:    
    lista_ciudades = []
    lista_ciudades = csv.reader(fichero, delimiter=',')
    for linea in lista_ciudades:
        if linea[1] == "Espanya" and int(linea[2]) > 30000:
            lista_ciudades_filtrados = linea[0]
            print(linea)
2/2# Una observación: no sabía cómo poner esta la linea siguiente antes del print la lista (lista_ciudades_filtrados)
    print("Arriba es una lista con los nombres de las ciudades españolas que tienen más de 300.000 habitante" ) 
        
with open("ciudades.csv") as fichero:
    total_ciudades_francesas = []
    total_ciudades_francesas = csv.reader(fichero, delimiter=',')
    for linea in total_ciudades_francesas:
        if linea[1] == "Francia":
            total_ciudades_francesas.append(linea[1])
            print("El número total de ciudades francesas",len(total_ciudades_francesas))


# **Ejercicio 6.** (2 puntos) Escribe una *list comprehension* que obtenga una lista que contenga 
# todos los números impares del 1 al 30 (ambos inclusive). Aquellos que sean múltiplos de 5, serán marcados con una 'x'. Es decir, 
# el resultado debe ser: [1, 3, '5x', 7, 9, 11, 13, '15x', 17, 19, 21, 23, '25x', 27, 29]

# Me da el error (int' object has no attribute 'insert')

Mario says:
- Este problema se puede resolver por medio de una sola list comprehension. 
Seguramente te lo facilitaría el hecho de que puedes usar un tercer parámetro en la función "range" 
para especificar el "paso", al igual que se hace en el slicing. 
Esto te evita tener que usar el filtro "if numb % 2 != 0"


impares = [numb for numb in range(1, 30+1) if numb % 2 != 0]
multiplos5 = [mul_5 for mul_5 in impares if mul_5%5 ==0]
for multiplos5 in impares:
    multiplos5.insert('x')
    print(impares)