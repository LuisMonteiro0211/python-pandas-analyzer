from dataclasses import dataclass
import pandas as pd

@dataclass
class Filtro:
    coluna: str
    dataframe: pd.DataFrame
    valor: str