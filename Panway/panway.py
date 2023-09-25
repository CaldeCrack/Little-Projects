#Andrés Calderón Guardia
import estructura
from ingredientes import *
from lista import *

# --------------------- Sándwiches --------------------- #

#sandwich: pan(lista(ingrediente)), queso(lista(ingrediente)), proteina(lista(ingrediente)),
#          verdura(lista(ingrediente)), salsa(lista(ingrediente))
estructura.crear("sandwich", "pan queso proteina verdura salsa")

# --------------------- Recetas --------------------- #

#Baratísimo
R1 = sandwich(lista(B2, listaVacia), lista(C2, listaVacia), lista(P1, listaVacia), lista(V3, listaVacia), listaVacia)
gramosR1 = lista(40, lista(50, lista(30, lista(100, listaVacia))))

#Texano
R2 = sandwich(lista(B6, listaVacia), lista(C1, listaVacia), lista(P3, listaVacia), lista(V3, listaVacia), lista(S4, listaVacia))
gramosR2 = lista(30, lista(20, lista(50, lista(60, lista(100, listaVacia)))))

#Gourmet
R3 = sandwich(lista(B5, listaVacia), lista(C4, listaVacia), lista(P2, listaVacia), lista(V1, listaVacia), lista(S2, listaVacia))
gramosR3 = lista(50, lista(30, lista(50, lista(40, lista(150, listaVacia)))))

#Especial Vegetariano
R4 = sandwich(lista(B1, listaVacia), lista(C3, listaVacia), lista(P6, listaVacia), lista(V4, lista(V6, lista(V2, listaVacia))), listaVacia)
gramosR4 = lista(30, lista(50, lista(60, lista(40, lista(20, lista(75, listaVacia))))))

#Lista de sándwiches predefinidos
listaSandwiches = lista(R1, lista(R2, lista(R3, lista(R4, listaVacia))))
gramosR1R2 = lista(40, lista(50, lista(30, lista(100, gramosR2))))

# ---------------------- Funciones ---------------------- #
#(Todas las funciones asumen que recibirán los parámetros adecuados del programa
#interactivo para evitar el tener que ponerse en más casos de los necesarios)

#esSandwich: lista(ingrediente) -> bool
#recibe un sándwich y devuelve True si es un sándwich válido y False en caso contrario
#ejemplo: esSandwich(R1) == True
def esSandwich(s):
    return type(s) == sandwich and esLista(s.pan) and esLista(s.queso) and esLista(s.proteina) and esLista(s.verdura) and esLista(s.salsa)

assert esSandwich(R1)

#invertirLista: lista(any) -> lista(any)
#recibe una lista y la devuelve dada vuelta
#ejemplo: invertirLista(B) retorna lista(B1, lista(B2, lista(B3, lista(B4, lista(B5, lista(B6, listaVacia))))))
def invertirLista(l, nuevaLista = listaVacia):
    assert esLista(l)
    if l == listaVacia: return nuevaLista
    return invertirLista(cola(l), crearLista(cabeza(l), nuevaLista))

assert invertirLista(B) == lista(B1, lista(B2, lista(B3, lista(B4, lista(B5, lista(B6, listaVacia))))))

#precioIngrediente: ingrediente int -> int
#recibe un ingrediente y los gramos pedidos para devolver el precio respectivo
#ejemplo: precioIngrediente(B1, 200) devuelve 4000
def precioIngrediente(i, gramos):
    assert esIngrediente(i) and type(gramos) == int
    return i.precio * gramos // 100

assert precioIngrediente(B1, 200) == 4000

#precioLista: lista(ingrediente) lista(int) -> int
#recibe una lista de ingredientes y los gramos respectivos para devolver el precio del total
#ejemplo: precioLista(B, gramosPan) retorna 10625
def precioLista(l, listaGramos, precio = 0):
    assert esLista(l) and esLista(listaGramos)
    if l == listaVacia: return 0
    precio = precioIngrediente(cabeza(l), cabeza(listaGramos))
    return precio + precioLista(cola(l), cola(listaGramos), precio)

gramosPan = lista(50, lista(100, lista(100, lista(100, lista(100, lista(100, listaVacia))))))
assert precioLista(B, gramosPan) == 10625

#gramosSobrantes: lista(ingrediente) lista(int) -> lista(int)
#recibe una lista de ingredientes y una lista con gramos para devolver la lista de gramos sobrantes
#ejemplo: gramosSobrantes(B, gramosExtra) retorna lista(100, listaVacia)
def gramosSobrantes(l, listaGramos):
    assert esLista(l) and esLista(listaGramos)
    if l == listaVacia: return listaGramos
    return gramosSobrantes(cola(l), cola(listaGramos))

gramosExtra = lista(100, lista(100, lista(100, lista(100, lista(100, lista(100, lista(50, listaVacia)))))))
assert gramosSobrantes(B, gramosExtra) == lista(50, listaVacia)

#gramosSobrantesSandwich: sandwich lista(int) -> lista(int)
#recibe un sándwich y devuelve la lista de gramos sobrantes
#ejemplo: gramosSobrantesSandwich(R1, gramosR2) retorna lista(100, listaVacia)
def gramosSobrantesSandwich(sandw, l):
    assert esSandwich(sandw) and esLista(l)
    l = gramosSobrantes(sandw.salsa, l)
    l = gramosSobrantes(sandw.verdura, l)
    l = gramosSobrantes(sandw.proteina, l)
    l = gramosSobrantes(sandw.queso, l)
    l = gramosSobrantes(sandw.pan, l)
    return l

assert gramosSobrantesSandwich(R1, gramosR2) == lista(100, listaVacia)

#precioSandwich: sandwich lista(int) -> int
#recibe un sándwich y una lista con los gramos pedidos de cada ingrediente para devolver el precio respectivo
#ejemplo: precioSandwich(R1, gramosR1) retorna 1480
def precioSandwich(sandw, listaGramos):
    assert esSandwich(sandw) and esLista(listaGramos)
    precio = 0
    listaInvertida = invertirLista(listaGramos)
    precio += precioLista(invertirLista(sandw.pan), listaInvertida)
    listaInvertida = gramosSobrantes(sandw.pan, listaInvertida)
    precio += precioLista(invertirLista(sandw.queso), listaInvertida)
    listaInvertida = gramosSobrantes(sandw.queso, listaInvertida)
    precio += precioLista(invertirLista(sandw.proteina), listaInvertida)
    listaInvertida = gramosSobrantes(sandw.proteina, listaInvertida)
    precio += precioLista(invertirLista(sandw.verdura), listaInvertida)
    listaInvertida = gramosSobrantes(sandw.verdura, listaInvertida)
    precio += precioLista(invertirLista(sandw.salsa), listaInvertida)
    return precio

assert precioSandwich(R1, gramosR1) == 1480

#sandwichBuscado: int -> sandwich
#recibe un número y devuelve el sándwich predefinido que representa
#ejemplo: sandwichBuscado(1) retorna R1
def sandwichBuscado(i):
    assert type(i) == int
    if i == 1: return R1
    elif i == 2: return R2
    elif i == 3: return R3
    elif i == 4: return R4

assert sandwichBuscado(1) == R1

#gramosBuscados: sandwich -> lista(int)
#recibe un sándwich predefinido y devuelve su lista de gramos
#ejemplo: gramosBuscados(R1) retorna gramosR1
def gramosBuscados(sandw):
    assert esSandwich(sandw)
    if sandw == R1: return gramosR1
    elif sandw == R2: return gramosR2
    elif sandw == R3: return gramosR3
    elif sandw == R4: return gramosR4

assert gramosBuscados(R1) == gramosR1

#imprimirPrecioIngredientes: lista(ingrediente) lista(int) -> None
#recibe una lista de ingredientes y una lista con los respectivos gramos para imprimir la información relevante en un formato agradable
def imprimirPrecioIngredientes(l, i):
    assert esLista(l) and esLista(i)
    if l == listaVacia: return
    print(cabeza(l).nombre + " (" + str(cabeza(i)) + "gr) - $" + str(precioIngrediente(cabeza(l), cabeza(i))))
    imprimirPrecioIngredientes(cola(l), cola(i))

#imprimirSandwich: sandwich lista(int) -> None
#recibe un sándwich y una lista con sus respectivos gramos e imprime la información relevante del mismo en un formato agradable
def imprimirSandwich(sandw, l):
    assert esSandwich(sandw) and esLista(l)
    print("\nSu sándwich personalizado tiene un precio de: $" + str(precioSandwich(sandw, invertirLista(l))))
    #Pan
    panInvertido = invertirLista(sandw.pan)
    imprimirPrecioIngredientes(panInvertido, l)
    nuevosGramos = gramosSobrantes(sandw.pan, l)

    #Queso
    quesoInvertido = invertirLista(sandw.queso)
    imprimirPrecioIngredientes(quesoInvertido, nuevosGramos)
    nuevosGramos = gramosSobrantes(sandw.queso, nuevosGramos)

    #Proteína
    proteinaInvertido = invertirLista(sandw.proteina)
    imprimirPrecioIngredientes(proteinaInvertido, nuevosGramos)
    nuevosGramos = gramosSobrantes(sandw.proteina, nuevosGramos)

    #Verdura
    verduraInvertido = invertirLista(sandw.verdura)
    imprimirPrecioIngredientes(verduraInvertido, nuevosGramos)
    nuevosGramos = gramosSobrantes(sandw.verdura, nuevosGramos)

    #Salsa
    salsaInvertido = invertirLista(sandw.salsa)
    imprimirPrecioIngredientes(salsaInvertido, nuevosGramos)
    nuevosGramos = gramosSobrantes(sandw.salsa, nuevosGramos)

#imprimirSandwiches: lista(sandwich) lista(int) -> None
#recibe una lista de sándwiches y una lista con sus respectivos precios e imprime la información relevante del mismo en un formato agradable
def imprimirSandwiches(l, listaPrecios, i = 1):
    assert esLista(l) and esLista(listaPrecios)
    if l == listaVacia: return
    print("Sándwich número " + str(i) + ": $" + str(cabeza(listaPrecios)))
    return imprimirSandwiches(cola(l), cola(listaPrecios), i + 1)