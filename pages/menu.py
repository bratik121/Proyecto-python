import os
from controllers import data_acquisition
from controllers import data_processing


def start():
    option1 = 0
    data = None
    # Menu principal
    while (option1 != 3):
        print("Bienvenido a la competicion!")
        print("1. Archivo")
        print("2. Acciones")
        print("3. Salir")
        try:
            option1 = int(input())
        except ValueError:
            print("****Debe introducir un numero****")
            print()
            continue
        # Menu de archivos
        if (option1 == 1):
            option2 = 0
            while (option2 != 10):
                print("1. Cargar archivo")
                print("2. Volver")
                print("3. Salir")
                try:
                    option2 = int(input())
                except ValueError:
                    print("****Debe introducir un numero****")
                    print()
                    continue
                if (option2 == 1):
                    filename = ""
                    while (os.path.isfile("data/"+filename) == False):
                        print("Ingrese el nombre de un archivo valido: ")
                        filename = input()
                    data = data_acquisition.read_file(filename)
                elif (option2 == 2):
                    print("Volviendo al menu principal")
                    print()
                elif (option2 == 3):
                    print("Gracias por usar el programa!")
                    option1 = 3
                    option2 = 10
                else:
                    print("Ingrese una opcion valida")
        elif (option1 == 2):
            option2 = 0
            while (option2 != 10):
                print("1. Cantidad total de participantes")
                print("2. Lista con la totalidad de los participantes")
                print("3. Cantidad de participantes por grupo etario")
                print("4. Cantidad de participantes por sexo")
                print("5. Ganadores por grupo etario")
                print("6. Ganadores por sexo")
                print("7. Ganadores por Grupo Etario y sexo")
                print("8. Ganador General")
                print("9. Historigrama de Participantes por grupo Etario")
                print("10. Volver")
                print("11. Salir")
                try:
                    option2 = int(input())
                except ValueError:
                    print("****Debe introducir un numero****")
                    print()
                    continue
                if (option2 == 1):
                    data_processing.total_participants(data)
                elif (option2 == 2):
                    data_processing.list_participants(data)
                elif (option2 == 3):
                    data_processing.etatian_groups(data)
                elif (option2 == 4):
                    data_processing.gender_groups(data)
                elif (option2 == 5):
                    data_processing.winners_by_eterian_group(data)
                elif (option2 == 6):
                    data_processing.winners_by_gender(data)
                elif (option2 == 7):
                    data_processing.winner_by_gender_and_etarian_group(data)
                elif (option2 == 8):
                    data_processing.general_winner(data)
                elif (option2 == 9):
                    data_processing.generate_histomgram(data)
                elif (option2 == 10):
                    print("Volviendo al menu principal")
                    print()
                elif (option2 == 11):
                    print("Gracias por usar el programa!")
                    option1 = 3
                    option2 = 10
                else:
                    print("Ingrese una opcion valida")
        elif (option1 == 3):
            print("Gracias por usar el programa!")
