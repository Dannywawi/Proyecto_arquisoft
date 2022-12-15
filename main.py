from cliente.reg import Register #port: 5002
from cliente.log import Login #port: 5001

from cliente.cliAsignarMesa import asignarMesa #port: 5004
from cliente.cliLiberarMesa import liberarMesa  #port: 5005
from cliente.cliAgregarSucursal import agregarSucursal  #port: 5007
from cliente.cliEliminarSucursal import eliminarSucursal #port: 5008
from cliente.cliValidarReserva import validarReserva #port: 5010
from cliente.cliConfirmarReserva import confirmarReserva #port: 5011
from cliente.cliVerComentarios import verComentarios #port: 5009
from cliente.cliAsignarMenu import asignarMenu #port: 5006
from cliente.cliAgregarHorario import agregarHorario #port: 5003

from cliente.res import reservar #port: 6000
from cliente.his import mostrarhistorial #port: 6001
from cliente.canReserva import cancelar #port: 6002
from cliente.writecom import WriteCom #port: 25000
from cliente.cliVerMenu import VerMenu #port: 25009

from os import system


isAdmin = 0
correo = ""

def main():
    global isAdmin, correo
    system("clear")
    while True:
        #system("cls")
        if isAdmin == 0:

            #MENU PRINCIPAL

            print("Que desea hacer?")
            print("1. Crear una nueva cuenta")
            print("2. Ingresar a una cuenta existente")
            print("3. Salir")

            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    print("Creando nueva cuenta")
                    x = Register()
                    print("Registro exitoso")
                    system('clear')
                elif opcion == 2:
                    print("Ingresando a una cuenta existente")
                    x, y = Login()
                    correo = y
                    isAdmin = int(x)
                    system('clear')
                elif opcion == 3:
                    print("Saliendo")
                    system('clear')
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")

        elif isAdmin == 1:

            #VISTA ADMIN

            print("Que desea hacer?")
            print("1. Asignar mesa")
            print("2. Liberar mesa")
            print("3. Agregar sucursal")
            print("4. Eliminar sucursal")
            print("5. Validar reserva")
            print("6. Confirmar uso de reserva")
            print("7. Revisar comentarios")
            print("8. Asignar menu")
            print("9. Agregar horario")
            print("10. Salir")

            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    #Funcion asignar mesa
                    print("Asignando mesa ...")
                    x = asignarMesa()
                    #print("Asignacion exitosa")
                    system('clear')
                elif opcion == 2:
                    #Funcion liberar mesa
                    print("Liberando mesa ...")
                    x = liberarMesa()
                    #print("Liberacion exitosa")
                    system('clear')
                elif opcion == 3:
                    #Funcion Agregar sucursal
                    print("Creando una nueva sucursal")
                    x = agregarSucursal()
                    #print("Creacion exitosa")
                    system('clear')
                elif opcion == 4:
                    #Funcion Eliminar sucursal
                    print("Eliminando sucursal")
                    x = eliminarSucursal()
                    #print("Eliminacion exitosa")
                    system('clear')
                elif opcion == 5:
                    #Funcion Validar reserva
                    print("Validando reserva ...")
                    x = validarReserva()
                    system('clear')
                elif opcion == 6:
                    #Funcion Confirmar uso de reserva
                    print("Confirmando reserva ...")
                    x = confirmarReserva()
                    system('clear')
                elif opcion == 7:
                    #Funcion Revisar comentarios
                    print("Buscando comentarios ...")
                    x = verComentarios()
                    system('clear')
                elif opcion == 8:
                    #Funcion Asignar menu
                    print("Creando menu ...")
                    x = asignarMenu()
                    system('clear')
                elif opcion == 9:
                    #Funcion Asignar horario
                    print("Creando horas")
                    agregarHorario()
                    #print("Creacion exitosa")
                    system('clear')
                elif opcion == 10: 
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")

        elif isAdmin == 2:

            #VISTA CLIENTE

            print(correo)
            print("Que desea hacer?")
            print("1. Reservar mesa")
            print("2. Historial de reservas")
            print("3. Cancelar Reservas")
            print("4. Escribir comentarios")
            print("5. Revisar menu")
            print("6. Salir")

            try:
                opcion = int(input("Ingrese una opcion: ").strip())

                if opcion == 1:
                    print("reserva de mesa")
                    reservar(correo)
                    system('clear')
                elif opcion == 2:
                    print("Historial")
                    mostrarhistorial(correo)
                    system('clear')
                elif opcion == 3:
                    #Funcion Cancelar Reservas
                    print("cancelar reserva")
                    cancelar(correo)
                    system('clear')
                elif opcion == 4:
                    #Funcion Escribir comentarios
                    WriteCom(isAdmin, correo)
                    system('clear')
                elif opcion == 5:
                    #Funcion Revisar menu
                    VerMenu()
                    system('clear')
                elif opcion == 6:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")

main()
