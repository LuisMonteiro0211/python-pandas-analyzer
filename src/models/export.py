from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class Export:
    """
    Representa os dados necessários para exportar um DataFrame para Excel.

    Attributes:
        dataframe: DataFrame a ser exportado.
        diretorio: Diretório de destino do arquivo.
        nome_arquivo: Nome do arquivo de saída (ex: 'relatorio.xlsx').
        nome_aba: Nome da aba (sheet) dentro do arquivo Excel.
    """

    dataframe: pd.DataFrame
    diretorio: Path
    nome_arquivo: str
    nome_aba: str
