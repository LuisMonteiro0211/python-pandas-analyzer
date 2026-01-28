import pandas as pd
from typing import List
from src.models.filtro import Filtro

dataframe = pd.read_excel('./dados_ficticios_2025.xlsx')

def get_dataframe(path: str) -> pd.DataFrame:
    dataframe = pd.read_excel(path)
    return dataframe

def get_colunas(dataframe: pd.DataFrame) -> List[str]:
    colunas: List[str] = dataframe.columns.tolist()
    return colunas

def check_colunas(colunas: List[str], coluna: str) -> None:
    if coluna not in colunas:
        raise ValueError(f"Coluna '{coluna}' não encontrada no dataframe")

def get_setores(dataframe: pd.DataFrame) -> List[str]:
    setores: List[str] = dataframe['Setor'].unique().tolist()
    return setores

def get_turnos(dataframe: pd.DataFrame) -> List[str]:
    turnos: List[str] = dataframe['Turno'].unique().tolist()
    return turnos

def applying_filters(filtro: Filtro) -> pd.DataFrame:
    return filtro.dataframe[filtro.dataframe[filtro.coluna] == filtro.valor]

if __name__ == "__main__":
    print(applying_filters(dataframe, 'Produção'))
    df_producao = applying_filters(dataframe, 'Produção')
    print(df_producao.shape)