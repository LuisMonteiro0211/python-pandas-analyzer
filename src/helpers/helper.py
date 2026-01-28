import pandas as pd
from typing import List
from src.models.filtro import Filtro

dataframe = pd.read_excel('./dados_ficticios_2025.xlsx')

def get_dataframe(path: str) -> pd.DataFrame:
    """
    Função para obter o dataframe a partir do caminho da planilha

    Args:
        path: Caminho da planilha
    Returns:
        pd.DataFrame: DataFrame com os dados da planilha
    """
    dataframe = pd.read_excel(path)
    return dataframe

def get_colunas(dataframe: pd.DataFrame) -> List[str]:
    """
    Função para obter as colunas do dataframe

    Args:
        dataframe: DataFrame com os dados
    Returns:
        List[str]: Lista com as colunas do dataframe
    """
    colunas: List[str] = dataframe.columns.tolist()
    return colunas

def check_colunas(colunas: List[str], coluna: str) -> None:
    """
    Função para verificar se a coluna existe no dataframe

    Args:
        colunas: Lista com as colunas do dataframe
        coluna: Coluna a ser verificada
    Returns:
        None (Se a coluna não existir, uma exceção é lançada)
    """
    if coluna not in colunas:
        raise ValueError(f"Coluna '{coluna}' não encontrada no dataframe")

def get_setores(dataframe: pd.DataFrame) -> List[str]:
    """
    Função para obter os setores do dataframe
    
    Args:
        dataframe: DataFrame com os dados
    Returns:
        List[str]: Lista com os setores do dataframe
    """
    setores: List[str] = dataframe['Setor'].unique().tolist()
    return setores

def get_turnos(dataframe: pd.DataFrame) -> List[str]:
    """
    Função para obter os turnos do dataframe
    Args:
        dataframe: DataFrame com os dados
    Returns:
        List[str]: Lista com os turnos do dataframe
    """
    turnos: List[str] = dataframe['Turno'].unique().tolist()
    return turnos

def applying_filters(filtro: Filtro) -> pd.DataFrame:
    """
    Função para aplicar os filtros ao dataframe

    Args:
        filtro: Filtro a ser aplicado (Objeto Filtro - coluna, dataframe, valor)
    Returns:
        pd.DataFrame: DataFrame com os dados filtrados
    """
    return filtro.dataframe[filtro.dataframe[filtro.coluna] == filtro.valor]

if __name__ == "__main__":
    print(applying_filters(dataframe, 'Produção'))
    df_producao = applying_filters(dataframe, 'Produção')
    print(df_producao.shape)