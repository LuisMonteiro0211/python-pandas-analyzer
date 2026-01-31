import pandas as pd
from dataclasses import dataclass

@dataclass
class Export:
    dataframe: pd.DataFrame
    diretorio: str
    nome_pasta: str
