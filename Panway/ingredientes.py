#Andrés Calderón Guardia
import estructura
from lista import *

# --------------------- Ingredientes --------------------- #

#ingrediente: categoria(str), index(int), nombre(str), precio(int)
estructura.crear("ingrediente", "categoria index nombre precio")

# ---------------- Tipos de Pan ---------------- #
B1 = ingrediente("B", 1, "Pan de molde", 2000)
B2 = ingrediente("B", 2, "Croissant", 1000)
B3 = ingrediente("B", 3, "Marraqueta", 1500)
B4 = ingrediente("B", 4, "Hallulla", 3000)
B5 = ingrediente("B", 5, "Baguette", 2250)
B6 = ingrediente("B", 6, "Pan de completo", 1750)

#Lista de los tipos de panes
B = lista(B6, lista(B5, lista(B4, lista(B3, lista(B2, lista(B1, listaVacia))))))

# ---------------- Quesos ---------------- #
C1 = ingrediente("C", 1, "Cheddar", 1250)
C2 = ingrediente("C", 2, "Gauda", 400)
C3 = ingrediente("C", 3, "Mantecoso", 600)
C4 = ingrediente("C", 4, "Azul", 1000)
C5 = ingrediente("C", 5, "Mozzarella", 350)
C6 = ingrediente("C", 6, "Ahumado", 800)
#Lista de los tipos de quesos
C = lista(C6, lista(C5, lista(C4, lista(C3, lista(C2, lista(C1, listaVacia))))))

# ---------------- Proteínas ---------------- #
P1 = ingrediente("P", 1, "Mortadela", 400)
P2 = ingrediente("P", 2, "Jamón serrano", 1000)
P3 = ingrediente("P", 3, "Pollo apanado", 450)
P4 = ingrediente("P", 4, "Atún", 300)
P5 = ingrediente("P", 5, "Carne de soya", 250)
P6 = ingrediente("P", 6, "Tofu", 800)

#Lista de los tipos de proteínas
P = lista(P6, lista(P5, lista(P4, lista(P3, lista(P2, lista(P1, listaVacia))))))

# ---------------- Verduras ---------------- #
V1 = ingrediente("V", 1, "Pimentón", 750)
V2 = ingrediente("V", 2, "Tomate", 450)
V3 = ingrediente("V", 3, "Cebolla", 400)
V4 = ingrediente("V", 4, "Palta", 800)
V5 = ingrediente("V", 5, "Aceitunas", 300)
V6 = ingrediente("V", 6, "Lechuga", 250)

#Lista de los tipos de verduras
V = lista(V6, lista(V5, lista(V4, lista(V3, lista(V2, lista(V1, listaVacia))))))

# ---------------- Salsas ---------------- #
S1 = ingrediente("S", 1, "Ketchup", 1000)
S2 = ingrediente("S", 2, "Mayonesa", 800)
S3 = ingrediente("S", 3, "Mostaza", 700)
S4 = ingrediente("S", 4, "Chipotle", 630)
S5 = ingrediente("S", 5, "Cebolla dulce", 520)

#Lista de los tipos de salsas
S = lista(S5, lista(S4, lista(S3, lista(S2, lista(S1, listaVacia)))))

# ---------------------- Funciones ---------------------- #
#(Todas las funciones asumen que recibirán los parámetros adecuados del programa
#interactivo para evitar el tener que ponerse en más casos de los necesarios)

#esIngrediente: ingrediente -> bool
#recibe un ingrediente y devuelve True si es un ingrediente válido y False en caso contrario
#ejemplo: esIngrediente(B1) retorna True
def esIngrediente(i):
    return type(i) == ingrediente and type(i.categoria) == str and type(i.index) == int and type(i.nombre) == str and type(i.precio) == int

assert esIngrediente(B1)

#esta función la creé porque lo pide la tarea pero no necesité usarla
#precioId: int lista(ingrediente) -> int
#recibe un índex y una lista de ingredientes y devuelve el precio del ingrediente correspondiente de la lista
#ejemplo: precioId(1, B) retorna 2000
def precioId(index, l):
    assert type(index) == int and esLista(l)
    if cabeza(l).index == index: return cabeza(l).precio
    return precioId(index, cola(l))

assert precioId(1, B) == 2000

#categoriaBuscada: int -> str
#recibe un número y devuelve la letra de la categoría que representa
#ejemplo: categoriaBuscada(1) retorna "B"
def categoriaBuscada(categoria):
    assert type(categoria) == int
    if categoria == 1: return "B"
    elif categoria == 2: return "C"
    elif categoria == 3: return "P"
    elif categoria == 4: return "V"
    elif categoria == 5: return "S"
    return listaVacia

assert categoriaBuscada(1) == "B"

#agregarIngrediente: lista(ingrediente) str str int -> lista(ingrediente)
#recibe una lista de ingredientes y le añade un nuevo ingrediente con los demás parámetros recibidos
#ejemplo: agregarIngrediente(B, "B", "Pan de ajo", 1500) retorna
#lista(ingrediente("B", 7, "Pan de ajo", 1500)), lista(B6, lista(B5, lista(B4, lista(B3, lista(B2, lista(B1, listaVacia))))))
def agregarIngrediente(l, categoria, nombre, precio):
    assert esLista(l) and type(categoria) == str and type(nombre) == str and type(precio) == int
    i = ingrediente(categoria, largo(l) + 1, nombre, precio)
    return crearLista(i, l)

assert agregarIngrediente(B, "B", "Pan de ajo", 1500) ==\
    lista(ingrediente("B", 7, "Pan de ajo", 1500), lista(B6, lista(B5, lista(B4, lista(B3, lista(B2, lista(B1, listaVacia)))))))

#buscarIndex: lista(ingrediente) int -> ingrediente
#recibe una lista de ingredientes y un entero para devolver el ingrediente con el mismo índex
#ejemplo: buscarIndex(B, 1) retorna B1
def buscarIndex(l, i):
    assert esLista(l) and type(i) == int
    if i == cabeza(l).index: return cabeza(l)
    return buscarIndex(cola(l), i)

assert buscarIndex(B, 1) == B1

#buscarIngrediente: lista(ingrediente) ingrediente -> bool
#recibe una lista de ingredientes y un ingrediente para devolver True si es que está y False en caso contrario
#ejemplo: buscarIngrediente(B, B1) retorna True
def buscarIngrediente(l, i):
    assert esLista(l) and esIngrediente(i)
    if l == listaVacia: return False
    if i.nombre == cabeza(l).nombre and i.categoria == cabeza(l).categoria: return True
    return buscarIngrediente(cola(l), i)

#print(buscarIngrediente(B, ingrediente("B", 7, "Pan de molde", 2000)))
assert buscarIngrediente(B, B1)
assert not buscarIngrediente(B, C1)

#reindexarLista: lista(ingrediente) str -> lista(ingrediente)
#recibe una lista de ingredientes y su categoría para reindexarla de modo que siempre tenga las ids más bajas posibles
#ejemplo: reindexarLista(lista(S5, lista(S3, lista(S2, lista(S1, listaVacia)))), "S") retorna
#lista(S4, lista(S3, lista(S2, lista(S1, listaVacia))))
def reindexarLista(l, categoria):
    assert esLista(l) and type(categoria) == str
    if l == listaVacia: return listaVacia
    elif cabeza(l).index == largo(l): return l
    nuevaCabeza = ingrediente(categoriaBuscada(int(categoria)), largo(l), cabeza(l).nombre, cabeza(l).precio)
    return crearLista(nuevaCabeza, reindexarLista(cola(l), categoria))

assert reindexarLista(lista(S5, lista(S3, lista(S2, lista(S1, listaVacia)))), "5") == \
    lista(ingrediente("S", 4, "Cebolla dulce", 520), lista(S3, lista(S2, lista(S1, listaVacia))))

#quitarIngrediente: lista(ingrediente) ingrediente -> lista(ingrediente)
#recibe una lista y le quita el ingrediente ingresado
#ejemplo: quitarIngrediente(C, C1) retorna lista(C6, lista(C5, lista(C4, lista(C3, lista(C2, listaVacia)))))
def quitarIngrediente(l, i):
    assert esLista(l) and esIngrediente(i)
    if l == listaVacia: return listaVacia
    elif cabeza(l) != i: return crearLista(cabeza(l), quitarIngrediente(cola(l), i))
    return quitarIngrediente(cola(l), i)

assert quitarIngrediente(C, C1) == lista(C6, lista(C5, lista(C4, lista(C3, lista(C2, listaVacia)))))

#textoIngrediente: ingrediente -> str
#recibe un ingrediente y devuelve un string con la información esencial del ingrediente dispuesto en un formato agradable
#ejemplo: textoIngrediente(B1) retorna "Pan de molde (Precio: 2000)"
def textoIngrediente(i):
    assert esIngrediente(i)
    return i.nombre + " (Precio: " + str(i.precio) + "$)"

assert textoIngrediente(B1) == "Pan de molde (Precio: 2000$)"

#imprimirListaIngredientes: lista(ingrediente) -> None
#recibe una lista de ingredientes y los imprime en pantalla en un formato agradable
def imprimirListaIngredientes(l, i = 1):
    assert esLista(l)
    if l == listaVacia: return
    print(str(i) + "-" , textoIngrediente(cabeza(l)))
    return imprimirListaIngredientes(cola(l), i + 1)