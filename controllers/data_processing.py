from tabulate import tabulate
import pandas as pd


def total_participants(data):
    """Imprime la cantidad de participantes

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print()
    # resto 1 por la cabecera e imprimo
    print(f"Total de participantes: {len(data)-1}")
    print("Presione enter para continuar...")
    input()
    print()


def list_participants(data):
    """Imprime la lista de participantes
    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print()
    print("Lista de participantes:")
    print(tabulate(data, headers='keys', tablefmt='psql', showindex=False))
    print()
    print("Presione enter para continuar...")
    input()
    print()


def etatian_groups(data):
    """Imprime la cantidad de participantes por grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print()
    print("Cantidad de participantes por grupo etario")

    # Cuenta la cantidad de participantes por grupo etario
    juniors = list(data[data["Edad"] <= 25].to_string()).count("\n")
    seniors = list(data[(data["Edad"] > 25) & (
        data["Edad"] <= 40)].to_string()).count("\n")
    masters = list(data[data["Edad"] > 40].to_string()).count("\n")

    # Imprime la tabla
    print(f"+{'-'*12}+{'-'*12}+")
    print(f"| {'Categoría':<10} | {'Cantidad':<10} |")
    print(f"|{'-'*12}|{'-'*12}|")
    print(f"| {'Juniors':<10} | {juniors:<10} |")
    print(f"| {'Seniors':<10} | {seniors:<10} |")
    print(f"| {'Masters':<10} | {masters:<10} |")
    print(f"+{'-'*12}+{'-'*12}+")

    print("Presione enter para continuar...")
    input()
    print()


def gender_groups(data):
    """Imprime la cantidad de participantes por sexo

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Cantidad de participantes por sexo")

    # Cuenta la cantidad de participantes por sexo
    masculine_count = list(data[data["Sexo"] == "M"].to_string()).count("\n")
    femenine_count = list(data[data["Sexo"] == "F"].to_string()).count("\n")

    # Imprime la tabla
    print(f"+{'-'*12}+{'-'*12}+")
    print(f"| {'Sexo':<10} | {'Cantidad':<10} |")
    print(f"|{'-'*12}|{'-'*12}|")
    print(f"| {'Masculino':<10} | {masculine_count:<10} |")
    print(f"| {'Femenino':<10} | {femenine_count:<10} |")
    print(f"+{'-'*12}+{'-'*12}+")

    print()
    print("Presione enter para continuar...")
    input()
    print()


def winners_by_eterian_group(data):
    """Imprime los ganadores por grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Ganadores por grupo etario")

    # Filtrar los datos por cada categoría y obtener el ganador
    junior_winner = data[data["Edad"] <= 25].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)
    senior_winner = data[(data["Edad"] > 25) & (data["Edad"] <= 40)].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)
    master_winner = data[data["Edad"] > 40].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)

    # Crear una nueva columna con la etiqueta correspondiente para cada ganador
    junior_winner["Grupo Etario"] = "Junior"
    senior_winner["Grupo Etario"] = "Senior"
    master_winner["Grupo Etario"] = "Master"

    # Concatenar los datos de los ganadores en un único DataFrame
    winners = pd.concat([junior_winner, senior_winner, master_winner])

    # Seleccionar las columnas en el orden deseado
    winners = winners[["Grupo Etario", "CI", "1er Apellido", "2do Apellido",
                       "Nombre", "Edad", "Sexo", "Horas", "Minutos", "Segundos"]]

    # Imprimir la tabla
    print(tabulate(winners, headers='keys', tablefmt='psql', showindex=False))
    print()
    print("Presione enter para continuar...")
    input()
    print()


def winners_by_gender(data):
    """Imprime los ganadores por sexo

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Ganadores por sexo")

    # Filtrar los datos por cada sexo y obtener el ganador
    masculine_winner = data[data["Sexo"] == "M"].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)
    femenine_winner = data[data["Sexo"] == "F"].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)

    # Crear una nueva columna con la etiqueta correspondiente para cada ganador
    masculine_winner["Genero"] = "Masculino"
    femenine_winner["Genero"] = "Femenino"

    # Concatenar los datos de los ganadores en un único DataFrame
    winners = pd.concat([masculine_winner, femenine_winner])

    # Seleccionar las columnas en el orden deseado
    winners = winners[["Genero", "CI", "1er Apellido", "2do Apellido",
                       "Nombre", "Edad", "Sexo", "Horas", "Minutos", "Segundos"]]

    # Imprimir la tabla

    print(tabulate(winners, headers='keys', tablefmt='psql', showindex=False))
    print()
    print("Presione enter para continuar...")
    input()
    print()


def winner_by_gender_and_etarian_group(data):
    """
    imprime los gandores por sexo y grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """

    print("Ganadores por sexo y grupo etario")

    masculine_junior_winner = data[(data["Edad"] <= 25) & (data["Sexo"] == "M")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)

    masculine_senior_winner = data[(data["Edad"] > 25) & (data["Edad"] <= 40) & (
        data["Sexo"] == "M")].sort_values(by=["Horas", "Minutos", "Segundos"]).head(1)

    masculine_master_winner = data[(data["Edad"] > 40) & (data["Sexo"] == "M")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)

    femenine_junior_winner = data[(data["Edad"] <= 25) & (data["Sexo"] == "F")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)

    femenine_senior_winner = data[(data["Edad"] > 25) & (data["Edad"] <= 40) & (
        data["Sexo"] == "F")].sort_values(by=["Horas", "Minutos", "Segundos"]).head(1)

    femenine_master_winner = data[(data["Edad"] > 40) & (data["Sexo"] == "F")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)

    # Crear una nueva columna con la etiqueta correspondiente para cada ganador
    masculine_junior_winner["Grupo Etario"] = "Junior"
    masculine_junior_winner["Genero"] = "Masculino"
    masculine_senior_winner["Grupo Etario"] = "Senior"
    masculine_senior_winner["Genero"] = "Masculino"
    masculine_master_winner["Grupo Etario"] = "Master"
    masculine_master_winner["Genero"] = "Masculino"
    femenine_junior_winner["Grupo Etario"] = "Junior"
    femenine_junior_winner["Genero"] = "Femenino"
    femenine_senior_winner["Grupo Etario"] = "Senior"
    femenine_senior_winner["Genero"] = "Femenino"
    femenine_master_winner["Grupo Etario"] = "Master"
    femenine_master_winner["Genero"] = "Femenino"

    # Concatenar los datos de los ganadores en un único DataFrame
    winners = pd.concat([masculine_junior_winner, masculine_senior_winner, masculine_master_winner,
                        femenine_junior_winner, femenine_senior_winner, femenine_master_winner])

    # Seleccionar las columnas en el orden deseado
    winners = winners[["Grupo Etario", "Genero", "CI", "1er Apellido",
                       "2do Apellido", "Nombre", "Edad", "Sexo", "Horas", "Minutos", "Segundos"]]

    # Imprimir la tabla

    print(tabulate(winners, headers='keys', tablefmt='psql', showindex=False))

    print()
    print("Presione enter para continuar...")
    input()
    print()


def general_winner(data):
    """
    Imprime el ganador general

    Args:
        data (data frame): data frame de pandas que tiene los participantes

    """

    print("Ganador General:")
   # Obtener el ganador general
    general_winner = data.sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1)
    winner_dict = general_winner.to_dict('records')[0]
    print(f"{winner_dict['1er Apellido']} {winner_dict['2do Apellido']} {winner_dict['Nombre']} ({winner_dict['Edad']}, {winner_dict['Sexo']}) - tiempo de culminacion: {winner_dict['Horas']}:{winner_dict['Minutos']}:{winner_dict['Segundos']}")
    print()
    print("Presione enter para continuar...")
    input()
    print()


def generate_histomgram(data):
    """
    Genera un histograma por cada grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """

    print("Histograma de grupos etarios:")
    print()
    juniors = list(data[data["Edad"] <= 25].to_string()).count("\n")
    print(f"Junior ({juniors}):\t|{'*'*juniors} ")  # f string

    seniors = list(data[(data["Edad"] > 25) & (
        data["Edad"] <= 40)].to_string()).count("\n")
    print(f"Senior ({seniors}):\t|{'*'*seniors} ")

    masters = list(data[data["Edad"] > 40].to_string()).count("\n")
    print(f"Master ({masters}):\t|{'*'*masters} ")
    print()
    print("Presione enter para continuar...")
    input()
    print()
