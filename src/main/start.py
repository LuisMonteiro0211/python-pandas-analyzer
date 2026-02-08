import os
from pathlib import Path
from src.services.service import process_spreadsheet
from dotenv import load_dotenv
from src.helpers.helper import check_environment_variables

def start():
    load_dotenv() ##Carrega as variáveis de ambiente do arquivo .env
    list_of_variables = [
        'DIRETORIO_PLANILHA', 
        'DIRETORIO_EXPORT'
        ]
    
    try:
        check_environment_variables(list_of_variables)
    except ValueError as e:
        print(f"Variável de ambiente não encontrada: {e}")
        return

    path_planilha = Path(os.getenv('DIRETORIO_PLANILHA'))
    path_export = Path(os.getenv('DIRETORIO_EXPORT'))
    
    if not path_planilha.is_file():
        raise FileNotFoundError(f"Caminho informado {path_planilha} não é um arquivo válido")
        return
    
    if not path_export.is_dir():
        raise NotADirectoryError(f"Caminho informado {path_export} não é um diretório válido")
        return
        
    if not os.access(path_export, os.W_OK):
        raise PermissionError(f"Permissão negada para acessar o diretório {path_export}")
        return

    process_spreadsheet(path_planilha)

if __name__ == "__main__":
    start()