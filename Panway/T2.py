#Andrés Calderón Guardia
from ingredientes import *
from panway import *
from lista import *

# --------------------------- Funciones auxiliares --------------------------- #
#(Todas las funciones asumen que recibirán los parámetros adecuados del programa
#interactivo para evitar el tener que ponerse en más casos de los necesarios)

#infoPredefinido: sandwich  int -> None
#recibe un sándwich predefinido para imprimir en pantalla la información necesaria
def infoPredefinido(sandw, precio):
    assert esSandwich(sandw) and type(precio) == int
    if sandw == R1: print("\n¡Baratísimo agregado a su orden!\nLleva " + str(precio + 1480) + "$ en su orden.")
    elif sandw == R2: print("\n¡Texano agregado a su orden!\nLleva " + str(precio + 2994) + "$ en su orden.")
    elif sandw == R3: print("\n¡Gourmet agregado a su orden!\nLleva " + str(precio + 4900) + "$ en su orden.")
    elif sandw == R4: print("\n¡Especial Vegetariano agregado a su orden!\nLleva " + str(precio + 2575) + "$ en su orden.")

#parametroPorOmision: int lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> lista(ingrediente)
#recibe una categoría y listas de ingredientes para devolver la lista correcta de la función tienda
#ejemplo (solo sirve antes de ejecutar la función tienda pues al iniciarse este valor irá variando): parametroPorOmision(1) retorna B
def parametroPorOmision(categoria, l1, l2, l3, l4, l5):
    assert type(categoria) == int and esLista(l1) and esLista(l2) and esLista(l3) and esLista(l4) and esLista(l5)
    if categoria == 1: return l1
    elif categoria == 2: return l2
    elif categoria == 3: return l3
    elif categoria == 4: return l4
    elif categoria == 5: return l5

#parametroLista: str int lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> None
#recibe un estado, una categoría y listas de ingredientes para reasignar la
#nueva al parámetro adecuado de la función tienda y mantener el resto igual
def parametroLista(estado, categoria, nuevaLista, l1, l2, l3, l4, l5):
    assert type(estado) == str and type(categoria) == int and esLista(nuevaLista) and\
           esLista(l1) and esLista(l2) and esLista(l3) and esLista(l4) and esLista(l5) 
    if categoria == 1: tienda(estado, panes = nuevaLista, quesos = l2, proteinas = l3, verduras = l4, salsas = l5)
    elif categoria == 2: tienda(estado, panes = l1, quesos = nuevaLista, proteinas = l3, verduras = l4, salsas = l5)
    elif categoria == 3: tienda(estado, panes = l1, quesos = l2, proteinas = nuevaLista, verduras = l4, salsas = l5)
    elif categoria == 4: tienda(estado, panes = l1, quesos = l2, proteinas = l3, verduras = nuevaLista, salsas = l5)
    elif categoria == 5: tienda(estado, panes = l1, quesos = l2, proteinas = l3, verduras = l4, salsas = nuevaLista)

#esEntero: str -> bool
#recibe un string y devuelve True si al pasarlo a número es un entero
#ejemplo: esEntero("2") retorna True
def esEntero(text):
    assert type(text) == str
    #se que no hemos visto esto en clases pero no tenía mejor forma de verificar si un texto puede pasarse a int con lo enseñado
    #además de que solo sirve para casos de escribir mal un input lo cual no se pide en la tarea técnicamente pero asumo de
    #todas formas lo que pueda implicar usar esta función
    if text.isdigit(): return True
    return False

assert esEntero("2")
assert not esEntero("-3.4")

#errorInicio: str -> str
#recibe un texto que indica el tipo de sándwich y verifica que sea correcto para devolverlo y sino volver a ejecutarse hasta que sea válido
#ejemplo: errorTipoSandwich("predefinido") retorna "predefinido"
def errorInicio(tipo):
    assert type(tipo) == str
    if tipo == "agregar" or tipo == "quitar" or tipo == "fin": return tipo
    nuevoTipo = input("\nTexto ingresado no válido (ingrese solamente 'agregar', 'quitar' o 'fin')\n- ")
    return errorInicio(nuevoTipo)

assert errorInicio("agregar") == "agregar"

#errorEntre: str int -> int
#recibe un entero y verifica que esté entre 1 y el máximo para devolverlo y sino volver a ejecutarse hasta que sea válido
#ejemplo: errorEntre("5", 6) retorna 5
def errorEntre(i, maximo):
    assert type(i) == str and type(maximo) == int
    if not esEntero(i):
        nuevoI = input("\nValor ingresado no válido (ingrese solamente números enteros entre 1 y " + str(maximo) + ")\n- ")
        return errorEntre(nuevoI, maximo)
    elif int(i) < 1 or int(i) > maximo:
        nuevoI = input("\nValor ingresado no válido (ingrese solamente números enteros entre 1 y " + str(maximo) + ")\n- ")
        return errorEntre(nuevoI, maximo)
    return int(i)

assert errorEntre("5", 6) == 5

#errorCantidad: str int -> int
#recibe una cantidad y un mínimo para verificar que la misma sea válida y así devolverla, y sino volver a ejecutarse hasta que cumpla
#ejemplo: errorCantidad("3", 1) retorna 3
def errorCantidad(cantidad, minimo):
    assert type(cantidad) == str and type(minimo) == int
    if not esEntero(cantidad):
        nuevaCantidad = input("\nValor ingresado no válido (ingrese solamente números enteros mayores a " + str(minimo) + ")\n- ")
        return errorCantidad(nuevaCantidad, minimo)
    elif int(cantidad) < minimo:
        nuevaCantidad = input("\nValor ingresado no válido (ingrese solamente números enteros mayores a " + str(minimo) + ")\n- ")
        return errorCantidad(nuevaCantidad, minimo)
    return int(cantidad)

assert errorCantidad("3", 1) == 3

#errorTipoSandwich: str -> str
#recibe un texto que indica el tipo de sándwich y verifica que sea correcto para devolverlo y sino volver a ejecutarse hasta que sea válido
#ejemplo: errorTipoSandwich("predefinido") retorna "predefinido"
def errorTipoSandwich(tipo):
    assert type(tipo) == str
    if tipo == "predefinido" or tipo == "personalizado": return tipo
    nuevoTipo = input("\nOpción no válida (ingrese solamente 'predefinido' o 'personalizado')\n- ")
    return errorTipoSandwich(nuevoTipo)

assert errorTipoSandwich("predefinido") == "predefinido"

#errorInput: str int -> str or int
#recibe un entero y el string de un input para verificar que sea correcto y devolverlo sino volver a ejecutarse hasta que sea válido
#ejemplo: errorInput("fin") retorna "fin"
def errorInput(tipo, i):
    assert type(tipo) == str and type(i) == int
    if tipo == "fin": return tipo
    elif esEntero(tipo) and i + 1 > int(tipo) > 0: return int(tipo)
    nuevoTipo = input("\nOpción no válida (ingrese solamente 'fin' o un número entero entre 1 y " + str(i) + ")\n- ")
    return errorInput(nuevoTipo, i)

assert errorInput("fin", 4) == "fin"
assert errorInput("1", 5) == 1

#existeR1: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> bool
#verifica que existan los ingredientes para pedir el sándwich R1
#ejemplo: existeR1(B, C, P, V, S) retorna True
def existeR1(listaB, listaC, listaP, listaV, listaS):
    assert esLista(listaB) and esLista(listaC) and esLista(listaP) and esLista(listaV) and esLista(listaS)
    return buscarIngrediente(listaB, B2) and buscarIngrediente(listaC, C2) and buscarIngrediente(listaP, P1) and buscarIngrediente(listaV, V3)

assert existeR1(B, C, P, V, S)

#existeR2: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> bool
#verifica que existan los ingredientes para pedir el sándwich R2
#ejemplo: existeR2(B, C, P, V, S) retorna True
def existeR2(listaB, listaC, listaP, listaV, listaS):
    assert esLista(listaB) and esLista(listaC) and esLista(listaP) and esLista(listaV) and esLista(listaS)
    return buscarIngrediente(listaB, B6) and buscarIngrediente(listaC, C1) and buscarIngrediente(listaP, P3) and\
        buscarIngrediente(listaV, V3) and buscarIngrediente(listaS, S4)

assert existeR2(B, C, P, V, S)

#existeR3: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> bool
#verifica que existan los ingredientes para pedir el sándwich R3
#ejemplo: existeR3(B, C, P, V, S) retorna True
def existeR3(listaB, listaC, listaP, listaV, listaS):
    assert esLista(listaB) and esLista(listaC) and esLista(listaP) and esLista(listaV) and esLista(listaS)
    return buscarIngrediente(listaB, B5) and buscarIngrediente(listaC, C4) and buscarIngrediente(listaP, P2) and\
        buscarIngrediente(listaV, V1) and buscarIngrediente(listaS, S2)

assert existeR3(B, C, P, V, S)

#existeR4: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> bool
#verifica que existan los ingredientes para pedir el sándwich R4
#ejemplo: existeR4(B, C, P, V, S) retorna True
def existeR4(listaB, listaC, listaP, listaV, listaS):
    assert esLista(listaB) and esLista(listaC) and esLista(listaP) and esLista(listaV) and esLista(listaS)
    return buscarIngrediente(listaB, B1) and buscarIngrediente(listaC, C3) and buscarIngrediente(listaP, P6) and\
        buscarIngrediente(listaV, V4) and buscarIngrediente(listaV, V6) and buscarIngrediente(listaV, V2)

assert existeR4(B, C, P, V, S)

#existenPredefinidos: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> bool
#verifica que existan ingredientes disponibles para pedir un sándwich predifinido
#ejemplo: existenPredefinidos(B, C, P, V, S) retorna True
def existenPredefinidos(listaB, listaC, listaP, listaV, listaS):
    assert esLista(listaB) and esLista(listaC) and esLista(listaP) and esLista(listaV) and esLista(listaS)
    return existeR1(listaB, listaC, listaP, listaV, listaS) or existeR2(listaB, listaC, listaP, listaV, listaS)\
        or existeR3(listaB, listaC, listaP, listaV, listaS) or existeR4(listaB, listaC, listaP, listaV, listaS)

assert existenPredefinidos(B, C, P, V, S)

#errorPredefinido: int lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) -> int
#recibe un entero y listas de ingredientes para verificar que puede pedir el sándwich
#predefinido deseado y sino volver a ejecutarse hasta que sea válido y devolverlo
#ejemplo: errorPredefinido(1, B, C, P, V, S) retorna 1
def errorPredefinido(i, listaB, listaC, listaP, listaV, listaS):
    assert type(i) == int and esLista(listaB) and esLista(listaC) and esLista(listaP) and esLista(listaV) and esLista(listaS)
    if i == 1 and not existeR1(listaB, listaC, listaP, listaV, listaS):
        nuevoI = errorEntre(input("\nLo sentimos, no disponemos de los ingredientes necesarios para preparar el sándwich Baratísimo, por favor elija otro\n- "), 4)
        return errorPredefinido(nuevoI, listaB, listaC, listaP, listaV, listaS)
    if i == 2 and not existeR2(listaB, listaC, listaP, listaV, listaS):
        nuevoI = errorEntre(input("\nLo sentimos, no disponemos de los ingredientes necesarios para preparar el sándwich Texano, por favor elija otro\n- "), 4)
        return errorPredefinido(nuevoI, listaB, listaC, listaP, listaV, listaS)
    if i == 3 and not existeR3(listaB, listaC, listaP, listaV, listaS):
        nuevoI = errorEntre(input("\nLo sentimos, no disponemos de los ingredientes necesarios para preparar el sándwich Gourmet, por favor elija otro\n- "), 4)
        return errorPredefinido(nuevoI, listaB, listaC, listaP, listaV, listaS)
    if i == 4 and not existeR4(listaB, listaC, listaP, listaV, listaS):
        nuevoI = errorEntre(input("\nLo sentimos, no disponemos de los ingredientes necesarios para preparar el sándwich Especial Vegetariano, por favor elija otro\n- "), 4)
        return errorPredefinido(nuevoI, listaB, listaC, listaP, listaV, listaS)
    return i

assert errorPredefinido(1, B, C, P, V, S)

# ---------------------------- Programa Interactivo ---------------------------- #

editar = errorInicio(input("\n# ---------------- Bienvenido a PanWay ---------------- #\n(Todos los precios de los ingredientes están ajustados a 100gr)\n\n¿Desea editar los ingredientes del menú? ('agregar' - 'quitar' - 'fin' para pasar)\n- "))

#tienda: str (lista(ingrediente)) (lista(ingrediente)) (lista(ingrediente)) (lista(ingrediente)) (lista(ingrediente)) -> None
#primera función principal que maneja la edición de la lista de ingredientes del programa interactivo de la tienda
def tienda(estado, panes = B, quesos = C, proteinas = P, verduras = V, salsas = S):
    assert type(estado) == str

    #agregar ingredientes
    if estado == "agregar":
        nombre = input("\n¿Qué ingrediente desea agregar?\n- ")
        categoria = errorEntre(input("\n¿En qué categoría? (ingrese el número)\n1- Tipos de pan\n2- Tipos de queso\n3- Tipos de proteína\n4- Tipos de verdura\n5- Tipos de salsa\n- "), 5)
        precio = errorCantidad(input("\n¿Cuál es el precio por 100 gramos?\n- "), 100)
        nuevaLista = agregarIngrediente(parametroPorOmision(categoria, panes, quesos, proteinas, verduras, salsas),\
                     categoriaBuscada(categoria), nombre, precio)
        nuevoEstado = errorInicio(input("\n¡Listo! ¿Desea seguir editando los ingredientes? ('agregar' - 'quitar' - 'fin' para pasar)\n- "))
        parametroLista(nuevoEstado, categoria, nuevaLista, panes, quesos, proteinas, verduras, salsas)

    #quitar ingredientes
    elif estado == "quitar":
        categoria = errorEntre(input("\n¿En qué categoría? (ingrese el número)\n1- Tipos de pan\n2- Tipos de queso\n3- Tipos de proteína\n4- Tipos de verdura\n5- Tipos de salsa\n- "), 5)
        print()
        if categoria == 1:
            if largo(panes) == 1:
                print("No puedes quitar todos los ingredientes de una lista")
                tienda("quitar", panes, quesos, proteinas, verduras, salsas)
                return
            imprimirListaIngredientes(invertirLista(panes))
        elif categoria == 2 and largo(quesos) != 0:
            if largo(quesos) == 1:
                print("No puedes quitar todos los ingredientes de una lista")
                tienda("quitar", panes, quesos, proteinas, verduras, salsas)
                return
            imprimirListaIngredientes(invertirLista(quesos))
        elif categoria == 3 and largo(proteinas) != 0:
            if largo(proteinas) == 1:
                print("No puedes quitar todos los ingredientes de una lista")
                tienda("quitar", panes, quesos, proteinas, verduras, salsas)
                return
            imprimirListaIngredientes(invertirLista(proteinas))
        elif categoria == 4 and largo(verduras) != 0:
            if largo(verduras) == 1:
                print("No puedes quitar todos los ingredientes de una lista")
                tienda("quitar", panes, quesos, proteinas, verduras, salsas)
                return
            imprimirListaIngredientes(invertirLista(verduras))
        elif categoria == 5 and largo(salsas) != 0:
            if largo(salsas) == 1:
                print("No puedes quitar todos los ingredientes de una lista")
                tienda("quitar", panes, quesos, proteinas, verduras, salsas)
                return
            imprimirListaIngredientes(invertirLista(salsas))
        largoParametro = largo(parametroPorOmision(categoria, panes, quesos, proteinas, verduras, salsas))
        index = errorEntre(input("\n¿Qué ingrediente desea quitar? (ingrese el número)\n- "), largoParametro)
        i = buscarIndex(parametroPorOmision(categoria, panes, quesos, proteinas, verduras, salsas), index)
        nuevaLista = reindexarLista(quitarIngrediente(parametroPorOmision(categoria, panes, quesos, proteinas, verduras, salsas), i),\
                     str(categoria))
        nuevoEstado = errorInicio(input("\nListo! ¿Desea seguir editando los ingredientes? ('agregar' - 'quitar' - 'fin' para pasar)\n- "))
        parametroLista(nuevoEstado, categoria, nuevaLista, panes, quesos, proteinas, verduras, salsas)
    
    #empezar con el pedido de los sándwiches
    elif estado == "fin":
        cantidad = errorCantidad(input("\n¿Cuántos sándwiches desea en su orden?\n- "), 1)
        programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, tipo = "pregunta", cantidad = cantidad)

#programaListaSandwiches: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente)
#                         (str) (int) (int) (lista(sandwich)) (lista(int)) -> None
#segunda función principal del programa interactivo que controla el pedido de los sándwiches
def programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, tipo = "", cantidad = 0, precio = 0, listaSandwichesPedidos = listaVacia, listaPrecios = listaVacia):
    #final del pedido
    if cantidad == largo(listaSandwichesPedidos):
                    print()
                    imprimirSandwiches(invertirLista(listaSandwichesPedidos), invertirLista(listaPrecios))
                    print("\nSu orden tiene un precio final de: $" + str(precio) + "\n")
                    return
    #preguntar en cada iteración si quiere un sándwich predefinido o personalizado
    if tipo == "pregunta":
        tipo = errorTipoSandwich(input("\n¿Desea que su sándwich número " + str(largo(listaSandwichesPedidos) + 1) + " sea predefinido o personalizado?\n- "))
    
    #pedido de sándwich predefinido
    if tipo == "predefinido" and existenPredefinidos(panes, quesos, proteinas, verduras, salsas):
        numeroSandwich = errorPredefinido(errorEntre(input("\n¿Qué sándwich predefinido desea? (ingrese el número)" + \
                                        "\n1- Baratísimo (Precio: 1480$)\n" + \
                                        "100gr de pan Croissant, 30gr de queso Gauda, 50gr de Mortadela y 40gr de cebolla.\n" + \
                                        "\n2- Texano (Precio: 2994$)\n" + \
                                        "100gr de pan de completo, 60gr de queso Cheddar, 50gr de pollo apanado, 20gr de cebolla y 30gr de salsa Chipotle.\n" + \
                                        "\n3- Gourmet (Precio: 4900$)\n" + \
                                        "150gr de pan Baguette, 40gr de queso azul, 50gr de jamón serrano, 30gr de pimentón y 50gr de mayonesa.\n" + \
                                        "\n4- Especial Vegetariano (Precio: 2575$)\n" + \
                                        "75gr de pan de molde, 20gr de queso mantecoso, 40gr de tofu, 60gr de tomate, 50gr de lechuga y 30gr de palta.\n- "), 4),\
                                            panes, quesos, proteinas, verduras, salsas)
        sandwichPredefinido = sandwichBuscado(numeroSandwich)
        infoPredefinido(sandwichPredefinido, precio)
        nuevoPrecio = precioSandwich(sandwichPredefinido, gramosBuscados(sandwichPredefinido))
        programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, "pregunta", cantidad, precio + nuevoPrecio,\
                                crearLista(sandwichPredefinido, listaSandwichesPedidos), crearLista(nuevoPrecio, listaPrecios))

    #alternativa de predefinido cuando no existen los ingredientes disponibles para crear alguno
    if tipo == "predefinido" and not existenPredefinidos(panes, quesos, proteinas, verduras, salsas,):
        print("\nLo sentimos no disponemos de los ingredientes necesarios para hacer sándwiches predefinidos, por favor elija uno personalizado")
        programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, "pregunta", cantidad, precio, listaSandwichesPedidos, listaPrecios)

    #pedido de sándwich personalizado
    if tipo == "personalizado":
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, estado = "inicio", largoI = largo(panes))

#armarSandwich: lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) lista(ingrediente) int lista(int) int
#               lista(sandwiches) (str) (int) (int) (lista(ingrediente)) (lista(ingrediente)) (lista(ingrediente)) (lista(ingrediente))
#               (lista(ingrediente)) (sandwich) (lista(int)) (int) -> None
#tercera función principal del,programa que se encarga de la interfaz y gestión en la creación de un sándwich personalizado
def armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos,\
                  estado = "fin", precioSandw = 0, largoI = 1, listaPan = listaVacia, listaQueso = listaVacia,\
                  listaProteina = listaVacia, listaVerdura = listaVacia, listaSalsa = listaVacia,\
                  sandwFinal = sandwich(listaVacia, listaVacia, listaVacia, listaVacia, listaVacia), listaFinal = listaVacia, gramosSalsaFinal = 0):
    listaFinalGramos = listaFinal

    #realizar nuevo input solamente después del input que se realiza antes de entrar a esta función
    if estado != "inicio" and estado != "final": nuevoInput = errorInput(input("- "), largoI)

    #manejar si seguir en pan o avanzar
    if estado == "fin1" and nuevoInput == "fin": estado = "fin1rep"
    elif estado == "fin1" and type(nuevoInput) == int: estado = "fin"

    #manejar si seguir en queso o avanzar
    if estado == "fin2" and nuevoInput == "fin": estado = "fin2rep"
    elif estado == "fin2" and type(nuevoInput) == int: estado = "fin1"

    #manejar si seguir en proteína o avanzar
    if estado == "fin3" and nuevoInput == "fin": estado = "fin3rep"
    elif estado == "fin3" and type(nuevoInput) == int: estado = "fin2"

    #manejar si seguir en verdura o avanzar
    if estado == "fin4" and nuevoInput == "fin": estado = "fin4rep"
    elif estado == "fin4" and type(nuevoInput) == int: estado = "fin3"

    #manejar si seguir en salsa o avanzar
    if estado == "fin5" and nuevoInput == "fin": estado = "fin5rep"
    elif estado == "fin5" and type(nuevoInput) == int: estado = "fin4"

    #manejar caso especial del fin de salsa
    if estado == "fin6" and nuevoInput == "fin":
        listaFinal = crearLista(gramosSalsaFinal, listaFinal)
        imprimirSandwich(sandwFinal, invertirLista(listaFinal))
        nuevoPrecio = precioSandwich(sandwFinal, listaFinal)
        listaSandwichesPedidos = crearLista(sandwFinal, listaSandwichesPedidos)
        listaPrecios = crearLista(nuevoPrecio, listaPrecios)
        #final del pedido
        if cantidad == largo(listaSandwichesPedidos):
            print()
            imprimirSandwiches(invertirLista(listaSandwichesPedidos), invertirLista(listaPrecios))
            print("\nSu orden tiene un precio final de: $" + str(precio + nuevoPrecio) + "\n")
            return
        return programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, "pregunta",\
                                       cantidad, precio + nuevoPrecio, listaSandwichesPedidos, listaPrecios)
    elif estado == "fin6" and type(nuevoInput) == int: estado = "fin4"

    #Panes
    if estado == "inicio" or (estado != "fin1" and estado != "fin2" and estado != "fin3" and estado != "fin4" and estado != "fin5" and\
        estado != "fin1rep" and estado != "fin2rep" and estado != "fin3rep" and estado != "fin4rep" and estado != "fin5rep" and estado != "final"):
        if estado == "inicio":
            print("\n¿Qué pan desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
            imprimirListaIngredientes(invertirLista(panes))
            nuevoInput = errorInput(input("- "), largo(panes))
            if nuevoInput == "fin":
                print("\n¿Qué queso desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
                imprimirListaIngredientes(invertirLista(quesos))
                sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
                armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos,\
                              "fin2", precioSandw, largo(quesos), listaPan = listaPan, listaFinal = listaFinalGramos)
        if type(nuevoInput) == str: return
        nuevoPan = buscarIndex(panes, nuevoInput)
        listaPan = crearLista(nuevoPan, listaPan)
        gramosPan = errorCantidad(input("\nIngrese la cantidad de gramos deseados:\n- "), 10)
        precioSandw += precioIngrediente(nuevoPan, gramosPan)
        print("\n" + str(gramosPan) + "gr de " + nuevoPan.nombre + " ($" + str(precioIngrediente(nuevoPan, gramosPan)) +\
            ") fue añadido a su sándwich personalizado\nSu precio del sándwich es: $" + str(precioSandw))
        listaFinalGramos = crearLista(gramosPan, listaFinalGramos)
        print("\n¿Qué pan desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
        imprimirListaIngredientes(invertirLista(panes))
        sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin1",\
                      precioSandw, largo(panes), listaPan = listaPan, sandwFinal = sandwFinal, listaFinal = listaFinalGramos)
        return

    #Quesos
    if estado != "inicio" and estado != "fin2" and estado != "fin3" and estado != "fin4" and estado != "fin5" and estado != "fin" and\
        estado != "fin2rep" and estado != "fin3rep" and estado != "fin4rep" and estado != "fin5rep" and estado != "final":
        if estado == "fin1rep":
            print("\n¿Qué queso desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
            imprimirListaIngredientes(invertirLista(quesos))
            nuevoInput = errorInput(input("- "), largo(quesos))
            if nuevoInput == "fin":
                print("\n¿Qué proteína desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
                imprimirListaIngredientes(invertirLista(proteinas))
                sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
                armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin3", precioSandw, largo(proteinas), listaPan = listaPan, listaQueso = listaQueso,\
                              sandwFinal = sandwFinal, listaFinal = listaFinalGramos)
        if type(nuevoInput) == str: return
        nuevoQueso = buscarIndex(quesos, nuevoInput)
        listaQueso = crearLista(nuevoQueso, listaQueso)
        gramosQueso = errorCantidad(input("\nIngrese la cantidad de gramos deseados:\n- "), 10)
        precioSandw += precioIngrediente(nuevoQueso, gramosQueso)
        print("\n" + str(gramosQueso) + "gr de " + nuevoQueso.nombre + " ($" + str(precioIngrediente(nuevoQueso, gramosQueso)) +\
            ") fue añadido a su sándwich personalizado\nSu precio del sándwich es: $" + str(precioSandw))
        listaFinalGramos = crearLista(gramosQueso, listaFinalGramos)
        print("\n¿Qué queso desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
        imprimirListaIngredientes(invertirLista(quesos))
        sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin2", precioSandw, largo(quesos), listaPan = listaPan, listaQueso = listaQueso, sandwFinal = sandwFinal,\
            listaFinal = listaFinalGramos)
        return

    #Proteinas
    if estado != "inicio" and estado != "fin3" and estado != "fin4" and estado != "fin5" and estado != "fin" and estado != "fin1rep" and\
        estado != "fin3rep" and estado != "fin4rep" and estado != "fin5rep" and estado != "final":
        if estado == "fin2rep":
            print("\n¿Qué proteína desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
            imprimirListaIngredientes(invertirLista(proteinas))
            nuevoInput = errorInput(input("- "), largo(proteinas))
            if nuevoInput == "fin":
                print("\n¿Qué verdura desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
                imprimirListaIngredientes(invertirLista(verduras))
                sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
                armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin4", precioSandw, largo(verduras), listaPan = listaPan, listaQueso = listaQueso,\
                              listaProteina = listaProteina, sandwFinal = sandwFinal, listaFinal = listaFinalGramos)
        if type(nuevoInput) == str: return
        nuevaProteina = buscarIndex(proteinas, nuevoInput)
        listaProteina = crearLista(nuevaProteina, listaProteina)
        gramosProteina = errorCantidad(input("\nIngrese la cantidad de gramos deseados:\n- "), 10)
        precioSandw += precioIngrediente(nuevaProteina, gramosProteina)
        print("\n" + str(gramosProteina) + "gr de " + nuevaProteina.nombre + " ($" + str(precioIngrediente(nuevaProteina, gramosProteina)) +\
            ") fue añadido a su sándwich personalizado\nSu precio del sándwich es: $" + str(precioSandw))
        listaFinalGramos = crearLista(gramosProteina, listaFinalGramos)
        print("\n¿Qué proteína desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
        imprimirListaIngredientes(invertirLista(proteinas))
        sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin3", precioSandw, largo(proteinas), listaPan = listaPan, listaQueso = listaQueso,\
            listaProteina = listaProteina, sandwFinal = sandwFinal, listaFinal = listaFinalGramos)
        return

    #Verduras
    if estado != "inicio" and estado != "fin4" and estado != "fin5" and estado != "fin" and estado != "fin1rep" and\
        estado != "fin2rep" and estado != "fin4rep" and estado != "fin5rep" and estado != "final":
        if estado == "fin3rep":
            print("\n¿Qué verdura desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
            imprimirListaIngredientes(invertirLista(verduras))
            nuevoInput = errorInput(input("- "), largo(verduras))
            if nuevoInput == "fin":
                print("\n¿Qué salsa desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
                imprimirListaIngredientes(invertirLista(salsas))
                sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
                armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos,\
                              "fin5", precioSandw, largo(salsas), listaPan = listaPan, listaQueso = listaQueso, listaProteina = listaProteina,\
                              listaVerdura = listaVerdura, sandwFinal = sandwFinal, listaFinal = listaFinalGramos)
        if type(nuevoInput) == str: return
        nuevaVerdura = buscarIndex(verduras, nuevoInput)
        listaVerdura = crearLista(nuevaVerdura, listaVerdura)
        gramosVerdura = errorCantidad(input("\nIngrese la cantidad de gramos deseados:\n- "), 10)
        precioSandw += precioIngrediente(nuevaVerdura, gramosVerdura)
        print("\n" + str(gramosVerdura) + "gr de " + nuevaVerdura.nombre + " ($" + str(precioIngrediente(nuevaVerdura, gramosVerdura)) +\
            ") fue añadido a su sándwich personalizado\nSu precio del sándwich es: $" + str(precioSandw))
        listaFinalGramos = crearLista(gramosVerdura, listaFinalGramos)
        print("\n¿Qué verdura desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
        imprimirListaIngredientes(invertirLista(verduras))
        sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin4",\
                      precioSandw, largo(verduras), listaPan = listaPan, listaQueso = listaQueso, listaProteina = listaProteina,\
                      listaVerdura = listaVerdura, sandwFinal = sandwFinal, listaFinal = listaFinalGramos)
        return

    #Salsas
    if estado != "inicio" and estado != "fin5" and estado != "fin" and estado != "fin1rep" and estado != "fin2rep" and\
        estado != "fin3rep" and estado != "fin5rep" and estado != "final":
        if estado == "fin4rep":
            print("\n¿Qué salsa desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
            imprimirListaIngredientes(invertirLista(salsas))
            nuevoInput = errorInput(input("- "), largo(salsas))
            if nuevoInput == "fin":
                #esto se ejecuta si es que no se pide ningún ingrediente durante la creación del sándwich
                if largo(listaPan) + largo(listaQueso) + largo(listaProteina) + largo(listaVerdura) + largo(listaSalsa) == 0:
                    print("\nDebe pedir al menos un ingrediente en su sandwich")
                    return armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio,\
                                         listaSandwichesPedidos, "inicio", precioSandw, largo(panes), listaPan = listaPan,\
                                         listaQueso = listaQueso, listaProteina = listaProteina, listaVerdura = listaVerdura,\
                                         sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa),\
                                         listaFinal = listaFinalGramos)
                sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
                armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos,\
                              "final", precioSandw, largo(verduras), listaPan = listaPan, listaQueso = listaQueso,\
                              listaProteina = listaProteina, listaVerdura = listaVerdura,\
                              sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa), listaFinal = listaFinalGramos)
                imprimirSandwich(sandwFinal, invertirLista(listaFinal))
                nuevoPrecio = precioSandwich(sandwFinal, listaFinal)
                listaSandwichesPedidos = crearLista(sandwFinal, listaSandwichesPedidos)
                listaPrecios = crearLista(nuevoPrecio, listaPrecios)
                #final del pedido
                if cantidad == largo(listaSandwichesPedidos):
                    print()
                    imprimirSandwiches(invertirLista(listaSandwichesPedidos), invertirLista(listaPrecios))
                    print("\nSu orden tiene un precio final de: $" + str(precio + nuevoPrecio) + "\n")
                    return
                return programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, "pregunta", cantidad,\
                                               precio + nuevoPrecio, listaSandwichesPedidos, listaPrecios)
        nuevaSalsa = buscarIndex(salsas, nuevoInput)
        listaSalsa = crearLista(nuevaSalsa, listaSalsa)
        gramosSalsa = errorCantidad(input("\nIngrese la cantidad de gramos deseados:\n- "), 10)
        gramosSalsaFinal = gramosSalsa
        precioSandw += precioIngrediente(nuevaSalsa, gramosSalsa)
        print("\n" + str(gramosSalsa) + "gr de " + nuevaSalsa.nombre + " ($" + str(precioIngrediente(nuevaSalsa, gramosSalsa)) +\
            ") fue añadido a su sándwich personalizado\nSu precio del sándwich es: $" + str(precioSandw))
        listaFinalGramos = crearLista(gramosSalsa, listaFinalGramos)
        print("\n¿Qué salsa desea? (ingrese un número), o 'fin' para pasar a la siguiente categoría")
        imprimirListaIngredientes(invertirLista(salsas))
        sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos, "fin6",\
                      precioSandw, largo(salsas), listaPan = listaPan, listaQueso = listaQueso, listaProteina = listaProteina,\
                      listaVerdura = listaVerdura, listaSalsa = listaSalsa, sandwFinal = sandwFinal, listaFinal = listaFinalGramos)

    #Caso particular de salsas
    if estado == "fin5rep":
        sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa)
        armarSandwich(panes, quesos, proteinas, verduras, salsas, cantidad, listaPrecios, precio, listaSandwichesPedidos,\
                      "final", precioSandw, largo(verduras), listaPan = listaPan, listaQueso = listaQueso,\
                      listaProteina = listaProteina, listaVerdura = listaVerdura,\
                      sandwFinal = sandwich(listaPan, listaQueso, listaProteina, listaVerdura, listaSalsa), listaFinal = listaFinalGramos)
        imprimirSandwich(sandwFinal, invertirLista(listaFinal))
        nuevoPrecio = precioSandwich(sandwFinal, listaFinal)
        listaSandwichesPedidos = crearLista(sandwFinal, listaSandwichesPedidos)
        listaPrecios = crearLista(nuevoPrecio, listaPrecios)
        #final del pedido
        if cantidad == largo(listaSandwichesPedidos):
            print()
            imprimirSandwiches(invertirLista(listaSandwichesPedidos), invertirLista(listaPrecios))
            print("\nSu orden tiene un precio final de: $" + str(precio + nuevoPrecio) + "\n")
            return
        return programaListaSandwiches(panes, quesos, proteinas, verduras, salsas, "pregunta", cantidad,\
                                       precio + nuevoPrecio, listaSandwichesPedidos, listaPrecios)

tienda(editar)