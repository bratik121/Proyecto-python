import pandas as pd




def total_participants(data):
    """Imprime la cantidad de participantes

    Args:
        data (list): lista de los participantes
    """
    print(f"Total de participantes: {len(data)-1}") #resto 1 por la cabecera

def list_participants(data):
    """Imprime la lista de participantes
    Args:
        data (list): lista de los participantes
    """
    print(data.to_string())
