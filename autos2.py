#Segunda parte del programa de autos. Que lo disfrutes ! saludos
def precioMarca(marca):
    if marca == 'ford':
        return 100000
    elif marca == 'chevrolet':
        return 120000
    elif marca == 'fiat':
        return  80000
def precioPuertas(puertas):
    if puertas == '2':
        return 50000
    elif puertas == '4':
        return 65000
    elif puertas == '5':
        return  78000
def precioColor(color):
    if color == 'blanco':
        return 10000
    elif color == 'azul':
        return 20000
    elif color == 'negro':
        return  30000
def precioFinal(precioDeColor, precioDeMarca, precioDePuertas):
    #Todo esto se podria poner de una mejor manera sin tantas cosas, pero ya venia modificando el programa anterior y me parecia
    #divertido trabajar sobre lo que ya tenia.
    precioTotal = precioDeMarca + precioDePuertas + precioDeColor
    return precioTotal
def descuento(cantClientes, precioTotal, comprasClientes):
    #calcula el descuento final en base a la cantidad de clientes dados. Dejo los numeros de pueba en vez de los del ejercicio.
    for i in range(len(comprasClientes)):
        if cantClientes >= 2 and cantClientes <= 3:
            comprasClientes[i]['precio'] = comprasClientes[i]['precio'] - ((10 * comprasClientes[i]['precio']) / 100)
        elif cantClientes >=4 and cantClientes <= 5:
            comprasClientes[i]['precio'] = comprasClientes[i]['precio'] - ((15 * comprasClientes[i]['precio']) / 100)
        elif cantClientes > 5:
            comprasClientes[i]['precio'] = comprasClientes[i]['precio'] - ((18 * comprasClientes[i]['precio']) / 100)
def impresionFinal():
    for i in range(len(comprasClientes)):
        print( 'Compra N°' + str(i + 1)
        + '\n' +
        'Nombre comprador: ' + str(comprasClientes[i]['nombre'])
        + '\n' + 
        'Marca: ' + str(comprasClientes[i]['marca'])
        + '\n' + 
        'Puertas: ' + str(comprasClientes[i]['puertas'])
        + '\n' +
        'Color: ' + str(comprasClientes[i]['color'])
        + '\n' +
        'Precio final: ' + str(comprasClientes[i]['precio'])
        + '\n')
        
marcasDeAutos = ['ford', 'chevrolet', 'fiat']
cantDePuertas = ['2', '4', '5']
coloresAutos = ['blanco', 'azul', 'negro'] 
#Se iniciliza la lista donde se van a guardar los diccionarios con las compras de los clientes
comprasClientes = []    
cantClientes = 0
while True:

#Pedir nombre y apellido del cliente
    nombreCliente = input('Ingrese su nombre y apellido: ')
#Consultar marca, puertas y color
    marca = input('Elija su marca: Ford, Chevrolet o Fiat. ').lower()
    while marca not in marcasDeAutos:
        marca = input('Ingresa nuevamente tu marca. ').lower()
    
    puertas = input('¿Cuantas puertas queres? 2, 4, o 5. ')
    while puertas not in cantDePuertas:
        puertas = input('Ingresa nuevamente tu cantidad de puertas. ')
    
    color = input('Por ultimo ¿que color te gustaria? Blanco, azul o negro. ').lower()
    while color not in coloresAutos:
        color = input('Ingresa nuevamente el color de tu auto. ')
    
    precioDeMarca = precioMarca(marca)
    precioDePuertas = precioPuertas(puertas)
    precioDeColor = precioColor(color)
    #calcula el precio final
    precioTotal = precioFinal(precioDeMarca, precioDePuertas, precioDeColor)
    #agrega un diccionario con los datos de la compra
    comprasClientes.append({'nombre' : nombreCliente, 'marca': marca, 'puertas': puertas, 'color': color, 'precio': precioTotal})

    cantClientes = cantClientes + 1
#pregunta si desea seguir cargando compras o cierra el programa
    if input('¿Desea agreagar otro cliente? ').lower().startswith('n'):
        break
#calcula el descuento final   
descuento(cantClientes, precioTotal, comprasClientes)
#imprime la lista con todas las compras y el descuento ya realizado.
impresionFinal()