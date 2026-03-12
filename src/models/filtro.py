from dataclasses import dataclass

import pandas as pd


@dataclass
class Filtro:
    """
    Representa um filtro a ser aplicado em um DataFrame.

    Attributes:
        coluna: Nome da coluna a ser filtrada.
        dataframe: DataFrame de origem.
        valor: Valor usado como critério de filtragem.
    """

    coluna: str
    dataframe: pd.DataFrame
    valor: str
