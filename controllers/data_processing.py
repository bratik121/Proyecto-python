import pandas as pd


def total_participants(data):
    """Imprime la cantidad de participantes

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print(f"Total de participantes: {len(data)-1}")  # resto 1 por la cabecera


def list_participants(data):
    """Imprime la lista de participantes
    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print(data.to_string())


def etatian_groups(data):
    """Imprime la cantidad de participantes por grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Cantidad de participantes por grupo etario")
    print("Juniors: ", end="")
    print(list(data[data["Edad"] <= 25].to_string()).count("\n"))
    print("Seniors: ", end="")
    print(list(data[(data["Edad"] > 25) & (
        data["Edad"] <= 40)].to_string()).count("\n"))
    print("Masters: ", end="")
    print(list(data[data["Edad"] > 40].to_string()).count("\n"))


def gender_groups(data):
    """Imprime la cantidad de participantes por sexo

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Cantidad de participantes por sexo")
    print("Masculino: ", end="")
    print(list(data[data["Sexo"] == "M"].to_string()).count("\n"))
    print("Femenino: ", end="")
    print(list(data[data["Sexo"] == "F"].to_string()).count("\n"))


def winners_by_eterian_group(data):
    """Imprime los ganadores por grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Ganadores por grupo etario")
    print("Juniors: ")
    print(data[data["Edad"] <= 25].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()
    print("Seniors: ")
    print(data[(data["Edad"] > 25) & (
        data["Edad"] <= 40)].sort_values(by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()
    print("Masters: ")
    print(data[data["Edad"] > 40].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())


def winners_by_gender(data):
    """Imprime los ganadores por sexo

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """
    print("Ganadores por sexo")
    print("Masculino: ")
    print(data[data["Sexo"] == "M"].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()
    print("Femenino: ")
    print(data[data["Sexo"] == "F"].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())


def winner_by_gender_and_etarian_group(data):
    """
    imprime los gandores por sexo y grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """

    print("Ganador Masculino Junior")
    print(data[(data["Edad"] <= 25) & (data["Sexo"] == "M")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()

    print("Ganador Masculino Senior")
    print(data[(data["Edad"] > 25) & (data["Edad"] <= 40) & (
        data["Sexo"] == "M")].sort_values(by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()

    print("Ganador Masculino Master")
    print(data[(data["Edad"] > 40) & (data["Sexo"] == "M")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()

    print("Ganador Femenino Junior")
    print(data[(data["Edad"] <= 25) & (data["Sexo"] == "F")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()

    print("Ganador Femenino Senior")
    print(data[(data["Edad"] > 25) & (data["Edad"] <= 40) & (
        data["Sexo"] == "F")].sort_values(by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()

    print("Ganador Femenino Master")
    print(data[(data["Edad"] > 40) & (data["Sexo"] == "F")].sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()


def general_winner(data):
    """
    Imprime el ganador general

    Args:
        data (data frame): data frame de pandas que tiene los participantes

    """

    print("Ganador General")
    print(data.sort_values(
        by=["Horas", "Minutos", "Segundos"]).head(1).to_string())
    print()


def generate_histomgram(data):
    """
    Genera un histograma por cada grupo etario

    Args:
        data (data frame): data frame de pandas que tiene los participantes
    """

    print("Histograma de grupos etarios")
    print()
    juniors = list(data[data["Edad"] <= 25].to_string()).count("\n")
    print(f"Junior ({juniors}):\t|{'*'*juniors} ")  # f string

    seniors = list(data[(data["Edad"] > 25) & (
        data["Edad"] <= 40)].to_string()).count("\n")
    print(f"Senior ({seniors}):\t|{'*'*seniors} ")

    masters = list(data[data["Edad"] > 40].to_string()).count("\n")
    print(f"Master ({masters}):\t|{'*'*masters} ")
    print()
