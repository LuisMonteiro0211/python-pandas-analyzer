from dataclasses import dataclass
import pandas as pd
from typing import Optional
@dataclass
class Filtro:
    """
    Classe para representar um filtro
    Args:
        coluna: Coluna a ser filtrada
        dataframe: DataFrame a ser filtrado
        valor: Valor a ser filtrado
    """
    
    coluna: str
    dataframe: pd.DataFrame
    valor: str    