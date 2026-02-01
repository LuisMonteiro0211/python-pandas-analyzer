import pandas as pd
from dataclasses import dataclass
from pathlib import Path
@dataclass
class Export:
    dataframe: pd.DataFrame
    diretorio: Path
    nome_arquivo: str
    nome_pasta: str
