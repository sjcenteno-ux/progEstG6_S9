cola_pendientes = []
pila_historial = []
siguiente_id = 1


def mostrar_estado():
    print("\nPendientes:", cola_pendientes)
    print("Historial:", pila_historial)

def registrar_solicitud(cliente, asunto):
    global siguiente_id
    if not cliente.strip() or not asunto.strip():
        return None

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente"
    }
    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud


#registrar_solicitud("Ana", "No conecta a Wi-Fi")
#registrar_solicitud("Luis", "Impresora sin papel")
#registrar_solicitud("Sofía", "Equipo lento")

def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud

def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud

def consultar_siguiente():
    if not cola_pendientes:
        return None

    return cola_pendientes[0]

def buscar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            return solicitud, "pendiente"

    for solicitud in pila_historial:
        if solicitud["id"] == id_solicitud:
            return solicitud, "historial"

    return None

def cancelar_pendiente(id_solicitud):

    for i in range(len(cola_pendientes)):

        if cola_pendientes[i]["id"] == id_solicitud:
            return cola_pendientes.pop(i)

    return None

def deshacer_varias(cantidad):

    if cantidad <= 0:
        return "La cantidad debe ser un entero positivo."

    recuperadas = 0

    for i in range(cantidad):
        resultado = deshacer_ultima_atencion()

        if resultado is None:
            break

        recuperadas += 1

    return f"Se recuperaron {recuperadas} solicitudes."

def ejecutar_menu():
    while True:
     try:
         print("\n1. Registrar solicitud")
         print("2. Atender siguiente")
         print("3. Deshacer última atención")
         print("4. Mostrar estado")
         print("5. Consultar siguiente")
         print("6. Buscar solicitud por ID")
         print("7. Cancelar solicitud pendiente")
         print("8.Eliminar varias atenciones.")
         print("9.Salir")
         opcion = int(input("Opción: "))

         if opcion == 1:
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            resultado = registrar_solicitud(cliente, asunto)
            print("Registrada:", resultado if resultado else "Datos inválidos")
         elif opcion == 2:
            print("Atendida:", atender_siguiente())
         elif opcion == 3:
             print("Restaurada:", deshacer_ultima_atencion())
         elif opcion == 4:
            mostrar_estado()
         elif opcion == 5:
            print("Siguiente:", consultar_siguiente())
         elif opcion == 6:
             id_solicitud= int(input("Ingrese el ID de la solictud:"))

             resultado= buscar_solicitud(id_solicitud)

             if resultado:
                 solicitud, ubicacion = resultado
                 print("solicitud encontrada:", solicitud)
                 print("Ubicacion:", ubicacion)
             else:
                 print("solicitud no encontrada.")
         elif opcion == 7:
             id_solicitud = int(input("Ingrese el ID de la solicitud a cancelar:"))
             resultado = cancelar_pendiente(id_solicitud)

             if resultado:
                 print("Solicitud cancelada:", resultado)
             else:
                 print("Solicitud no encontrada entre las pendientes.")

         elif opcion == 8:
              cantidad = int(input("¿Cuantas atenciones desea deshacer?: "))
              print(deshacer_varias(cantidad))
             
         elif opcion == 9:
             break
         else:
            print("Opción inválida")
     except ValueError:
         print("Error, debe ser un numero. ")
         
if __name__ == "__main__":
    ejecutar_menu()