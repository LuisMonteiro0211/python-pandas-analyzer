import re
from os import getenv
from pathlib import Path
from typing import List, Union

import pandas as pd

from src.models.export import Export
from src.models.filtro import Filtro


def get_dataframe(path: Union[str, Path]) -> pd.DataFrame:
    """
    Lê um arquivo Excel e retorna um DataFrame.

    Args:
        path: Caminho do arquivo Excel.

    Returns:
        DataFrame com os dados da planilha.

    Raises:
        FileNotFoundError: Se o arquivo não existir.
        ValueError: Se houver erro na leitura do arquivo.
    """
    if not Path(path).is_file():
        raise FileNotFoundError(f"Arquivo {path} não encontrado")

    try:
        return pd.read_excel(path)
    except Exception as e:
        raise ValueError(f"Erro ao ler o arquivo {path}: {e}") from e


def get_colunas(dataframe: pd.DataFrame) -> List[str]:
    """Retorna a lista de colunas do DataFrame."""
    return dataframe.columns.tolist()


def check_colunas(colunas: List[str], coluna: str) -> None:
    """
    Verifica se uma coluna existe na lista fornecida.

    Raises:
        ValueError: Se a coluna não for encontrada.
    """
    if coluna not in colunas:
        raise ValueError(f"Coluna '{coluna}' não encontrada no dataframe")


def get_valores_unicos(dataframe: pd.DataFrame, coluna: str) -> List[str]:
    """
    Retorna os valores únicos de uma coluna do DataFrame.

    Args:
        dataframe: DataFrame de origem.
        coluna: Nome da coluna.

    Returns:
        Lista com os valores únicos.
    """
    return dataframe[coluna].unique().tolist()


def applying_filters(filtro: Filtro) -> pd.DataFrame:
    """
    Aplica um filtro ao DataFrame e retorna o resultado.

    Args:
        filtro: Objeto Filtro com coluna, dataframe e valor.

    Returns:
        DataFrame filtrado.
    """
    return filtro.dataframe[filtro.dataframe[filtro.coluna] == filtro.valor]


def export_to_excel(export: Export) -> None:
    """
    Exporta um DataFrame para um arquivo Excel.

    Args:
        export: Objeto Export com dataframe, diretório, nome do arquivo e nome da aba.

    Raises:
        OSError: Se houver erro ao salvar o arquivo.
    """
    caminho_completo = export.diretorio / export.nome_arquivo
    try:
        export.dataframe.to_excel(
            caminho_completo,
            index=False,
            sheet_name=export.nome_aba,
        )
    except Exception as e:
        raise OSError(
            f"Erro ao exportar arquivo {caminho_completo}: {e}"
        ) from e


def check_environment_variables(variables: List[str]) -> None:
    """
    Verifica se todas as variáveis de ambiente da lista estão definidas.

    Args:
        variables: Lista com os nomes das variáveis.

    Raises:
        ValueError: Se alguma variável não estiver definida.
    """
    missing = [var for var in variables if not getenv(var)]

    if missing:
        raise ValueError(
            f"Variáveis de ambiente não encontradas: {', '.join(missing)}"
        )


def safe_name(text: str) -> str:
    """Remove caracteres inválidos para nomes de arquivo."""
    return re.sub(r'[<>:"/\\|?*]', "_", str(text)).strip()
