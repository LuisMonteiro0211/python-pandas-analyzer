import os
from pathlib import Path
from src.services.service import process_spreadsheet
from dotenv import load_dotenv


def start():
    load_dotenv() ##Carrega as variáveis de ambiente do arquivo .env
    DIRETORIO_PLANILHA = Path(os.getenv('DIRETORIO_PLANILHA'))
    process_spreadsheet(DIRETORIO_PLANILHA)

if __name__ == "__main__":
    start()