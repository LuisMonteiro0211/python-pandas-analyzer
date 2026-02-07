import pandas as pd
from typing import List
from src.models.filtro import Filtro
from src.models.export import Export
from pathlib import Path
from os import getenv

def get_dataframe(path: str) -> pd.DataFrame:
    """
    Função para obter o dataframe a partir do caminho da planilha

    Args:
        path: Caminho da planilha
    Returns:
        pd.DataFrame: DataFrame com os dados da planilha
    """
    if not Path(path).is_file():
        raise FileNotFoundError(f"Arquivo {path} não encontrado")
    
    try:
        df = pd.read_excel(path)
        return df
    except Exception as e:
        raise ValueError(f"Erro ao ler o arquivo {path}: {e}")

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

def export_to_excel(object_to_export: Export) -> None:
    """
    Função para exportar o dataframe para um arquivo Excel
    Args:
        object_to_export: Objeto Export com o dataframe, diretório, nome do arquivo e nome da pasta
    Returns:
        None
    """
    ##Cria a pasta de exportação se não existir
    if not object_to_export.diretorio.exists():
        object_to_export.diretorio.mkdir(parents=True, exist_ok=True)

    diretorio: Path = object_to_export.diretorio
    object_to_export.dataframe.to_excel(diretorio / object_to_export.nome_arquivo, index=False, sheet_name=object_to_export.nome_pasta)

def check_environment_variables(environment_variable: str) -> None:
    """
    Função para verificar se a variável de ambiente existe
    Args:
        environment_variable: Variável de ambiente a ser verificada
    Returns:
        None (Se a variável de ambiente não existir, uma exceção é lançada)
    """

    if not getenv(environment_variable):
        raise ValueError(f"Variável de ambiente {environment_variable} não encontrada")
    return getenv(environment_variable)

if __name__ == "__main__":

    dataframe = pd.read_excel('./dados_ficticios_2025.xlsx')
    print(applying_filters(dataframe, 'Produção'))
    df_producao = applying_filters(dataframe, 'Produção')
    print(df_producao.shape)