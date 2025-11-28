############################################################################
#                SISTEMA GESTION DE TICKETS                                #
#                                                                          #
############################################################################

####################### MOSTRAR MENU PRINCIPAL #############################
def mostrar_menu():
    print()
    print('*************************************')
    print('Hola Bienvenido a Sistema de Tickets\n')
    print('*************************************')
    print('1 - Generar un Ticket\n')
    print('2 - Leer un Ticket\n')
    print('3 - Salir\n')
    #
    opcion = input('Ingrese una opción (1/2/3): ')
    return(opcion)

####################### SUBMENU para CARGAR TICKET ########################
def desplegar_opcion_1(opcion_elegida,archivo):
  
    if opcion_elegida == '1': # Genera Ticket
        print(' ')
        print('Ingrese datos para generar el nuevo Ticket\n')
        nombre = input('Ingrese Nombre: ')
        sector = input('Ingrese Sector: ')
        asunto = input('Ingrese Asunto: ')
        mensaje = input('Ingrese Mensaje: ')
        print(' ')
        print("============================================\n")
        print('=      Se generó el siguiente Ticket       =\n')
        print("============================================\n")      
        print (f'Su nombre: {nombre}\t')   
        print (f'Su TICKET: \n')
        print (f'Sector: {sector}')
        print (f'Asunto: {asunto}')
        print (f'Mensaje: {mensaje}/n')
        nro_ticket = random.randrange(1000, 9999)
        print ("==========================================\n") 
        print (f'Por favor recordar su Nro Ticket: {nro_ticket}')
        print ("==========================================\n") 
   
        # Creamos el diccionario con los datos
        ticket = {"nombre": nombre,
                  "sector": sector,
                  "asunto": asunto,
                  "mensaje": mensaje,
                  "nro_ticket": nro_ticket
                 }

        tickets = cargar_tickets(archivo, ticket)
       
        input ('Presione una techa para continuar: ')
        os.system('cls')

    if opcion_elegida == 2: #Lee Ticket
        nro_ticke = input('Ingrese nro ticket a leer: ')


    if opcion_elegida == 3: #Sale de Aplicación
        salir = input('Desea Salir de la aplicación (S/N)?')
        return(3)

###################      Cargar nuevo ticket al File #######################
def cargar_tickets(archivo,ticket):
    
    # Si el archivo existe y tiene contenido válido, lo cargamos
    tickets = []
    if os.path.isfile(archivo) and os.path.getsize(archivo) > 0:
        with open(archivo, "r", encoding="utf-8") as f:
            tickets = json.load(f)
 
    # Agregar el nuevo ticket
    tickets.append(ticket)

    # Guardar la lista actualizada
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=4)

    print("*** Ticket agregado correctamente.***")

    return()

####################### Leer un Ticket ya cargado ##########################
def obtener_ticket(archivo: str, nro_ticket: str):
    # Si no existe o está vacío, no hay nada que buscar
    if not os.path.isfile(archivo) or os.path.getsize(archivo) == 0:
        return()

    with open(archivo, "r", encoding="utf-8") as f:
        tickets = json.load(f)  # debe ser una lista de dicts

    # Busca por NRO_TICKET (también acepta "nro_ticket")
    for t in tickets:
        if str(t.get("NRO_TICKET", t.get("nro_ticket"))) == str(nro_ticket):
            return t

    return()  # si no se encontró


#############################################################################
#                            PRINCIPAL- MAIN                                #
#############################################################################
import json, sys, os, random

 # Nombre del archivo donde se guardarán los datos
archivo = "C:\\A_PYTHON\TP\\ticket.json"

opcion = '1'
while opcion  in ('1','2','3'):
    opcion = mostrar_menu()
    if opcion != '1' and opcion != '2' and opcion != '3': 
         print('Seleccionó una opcion incorrecta')
  
    if opcion == '1': ####### CREA TICKET ########
        respuesta = 'S'
        while respuesta == 'S':
            desplegar_opcion_1(opcion,archivo)
            respuesta = input('¿Desea crear otro ticket? (S/N):')
            if respuesta == 'N':
                break
    elif opcion == '2': ######## LEE TICKET ########
        respuesta = 'S'
        while respuesta == 'S':
            nro_ticket_consulta = input('Ingrese el nro ticket a consultar: ')
            t = obtener_ticket(archivo, nro_ticket_consulta)
            # Mostrar desglosado
            if t:
                print("")
                print("Información del ticket:")
                for clave, valor in t.items():
                    print(f"- {clave}: {valor}")
            else:
                print("No se encontró el ticket.")
            print("")
            respuesta = input('¿Desea leer otro ticket? (S/N):')
            if respuesta == 'N':
                break
      
    elif opcion == '3': ##### CONFIRMA SI SALE DE APLICACION #####
        while opcion != 'N' or opcion != 'S':
            respuesta = input('¿Seguro desea salir de la aplicación? (S/N) ')
            if respuesta == 'S':
                opcion = 'X'
                break
            elif respuesta != 'N':
                print('Opción incorrecta')
            elif respuesta == 'N':
                break 