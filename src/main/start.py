import os
from pathlib import Path
from src.services.service import process_spreadsheet
from dotenv import load_dotenv
from src.helpers.helper import check_environment_variables
from src.helpers.log import setup_logging
import logging as lg

def validate_paths(path_planilha: Path, path_export: Path, path_log: Path) -> None:
    if not path_planilha.is_file():
        raise FileNotFoundError(f"Caminho informado {path_planilha} não é um arquivo válido")
    
    if not path_export.is_dir():
        raise NotADirectoryError(f"Caminho informado {path_export} não é um diretório válido")
        
    if not os.access(path_export, os.W_OK):
        raise PermissionError(f"Permissão negada para acessar o diretório {path_export}")

    if not path_log.is_dir():
        raise NotADirectoryError(f"Caminho informado {path_log} não é um diretório válido")

    if not os.access(path_log, os.W_OK):
        raise PermissionError(f"Permissão negada para acessar o diretório {path_log}")


def start():
    load_dotenv() ##Carrega as variáveis de ambiente do arquivo .env
    setup_logging()
    logger = lg.getLogger(__name__)

    list_of_variables = [
        'DIRETORIO_PLANILHA', 
        'DIRETORIO_EXPORT',
        'DIRETORIO_LOG'
        ]
    
    try:
        check_environment_variables(list_of_variables)
    except ValueError as e:
        logger.error(f"{e}")
        return

    path_planilha = Path(os.getenv('DIRETORIO_PLANILHA'))
    path_export = Path(os.getenv('DIRETORIO_EXPORT'))
    path_log = Path(os.getenv('DIRETORIO_LOG'))

    try:
        validate_paths(path_planilha, path_export, path_log)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        logger.error(f"Erro ao validar o caminho: {e}")
        return

    process_spreadsheet(path_planilha)
    

if __name__ == "__main__":
    start()