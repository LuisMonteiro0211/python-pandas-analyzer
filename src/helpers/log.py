import logging as lg
from os import getenv
from pathlib import Path

def setup_logging():
    """
    Configura o logging para o arquivo de log
    """
    DIRETORIO_LOG = Path(getenv('DIRETORIO_LOG'))
    lg.basicConfig(
        level=lg.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=DIRETORIO_LOG / 'app.log',
        filemode='a',
        encoding='utf-8',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    