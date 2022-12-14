from cliente.log import Login
from cliente.reg import Register
from cliente.res import reservar
from cliente.writecom import WriteCom ##Escribir cometario
from cliente.his import mostrarhistorial
from os import system


isAdmin = 0
correo = ""

def main():
    global isAdmin, correo
    system("clear")
    while True:
        #system("cls")
        if isAdmin == 0:

            #MENU PRINCIPAL ->Terminado

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
            print("9. Salir")

            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    #Funcion asignar mesa
                    system('clear')
                elif opcion == 2:
                    #Funcion liberar mesa
                    system('clear')
                elif opcion == 3:
                    #Funcion Agregar sucursal
                    system('clear')
                elif opcion == 4:
                    #Funcion Eliminar sucursal
                    system('clear')
                elif opcion == 5:
                    #Funcion Validar reserva
                    system('clear')
                elif opcion == 6:
                    #Funcion Confirmar uso de reserva
                    system('clear')
                elif opcion == 7:
                    #Funcion Revisar comentarios
                    system('clear')
                elif opcion == 8:
                    #Funcion Asignar menu
                    system('clear')
                elif opcion == 9:
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
                    system('clear')
                elif opcion == 4:
                    #Funcion Escribir comentarios
                    WriteCom(isAdmin, correo)
                    system('clear')
                elif opcion == 5:
                    #Funcion Revisar menu
                    system('clear')
                elif opcion == 6:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")

main()
