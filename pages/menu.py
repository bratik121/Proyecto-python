import os
from controllers import data_acquisition
from controllers import data_processing



def start():
    option1 = 0
    data = None
    while(option1 != 3):
        print("Bienvenido a la competicion!")
        print("1. Archivo")
        print("2. Acciones")
        print("3. Salir")
        option1 = int(input())

        if(option1 == 1):
            option2 = 0
            while(option2 != 2):
                print("1. Cargar archivo")
                print("2. Salir")
                option2 = int(input())
                if(option2 == 1):
                    filename=""
                    while(os.path.isfile("data/"+filename) == False):
                        print("Ingrese el nombre de un archivo valido: ")
                        filename = input()
                    data = data_acquisition.read_file(filename)

        elif(option1 == 2):
            option2 = 0
            while(option2 != 2):
                print("1. Cantidad total de participantes")
                print("2. Lista con la totalidad de los participantes")
                print("3. Cantidad de participantes por grupo etario")
                print("4. Cantidad de participantes por sexo")
                print("5. Ganadores por grupo etario")
                print("5. Ganadores por sexo")
                print("6. Ganadores por Grupo Etario y sexo")
                print("7. Ganador General")
                print("8. Historigrama de Participantes por grupo Etario")
                print("9. Promedio de Tiempo por grupo Etario y Sexo")
                print("10. Volver")
                print("11. Salir")

                option2 = int(input())
                if(option2 == 1):
                    data_processing.total_participants(data)
                elif(option2 == 2):
                    data_processing.list_participants(data)