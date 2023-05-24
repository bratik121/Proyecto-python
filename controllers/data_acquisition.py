import pandas as pd
from models import participants

def read_file(filename):
    try:
        df = pd.read_csv("data/"+filename, header=None)
        df.columns = participants.columns
        return df
    except:
        print("Error al leer el archivo")
        print("Verifique que el archivo exista y que se encuentre en la carpeta data")
        return None