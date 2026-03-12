import os
from pathlib import Path

from dotenv import load_dotenv

from src.helpers.helper import check_environment_variables
from src.helpers.log import setup_logging
from src.services.service import process_spreadsheet

import logging as lg

REQUIRED_ENV_VARS = [
    "DIRETORIO_PLANILHA",
    "DIRETORIO_EXPORT",
    "DIRETORIO_LOG",
]


def validate_paths(path_planilha: Path, path_export: Path, path_log: Path) -> None:
    """
    Valida se os caminhos configurados existem e possuem as permissões necessárias.

    Raises:
        FileNotFoundError: Se a planilha não existir.
        NotADirectoryError: Se os diretórios de export/log não existirem.
        PermissionError: Se não houver permissão de escrita nos diretórios.
    """
    if not path_planilha.is_file():
        raise FileNotFoundError(
            f"Caminho informado {path_planilha} não é um arquivo válido"
        )

    for path, label in [(path_export, "export"), (path_log, "log")]:
        if not path.is_dir():
            raise NotADirectoryError(
                f"Caminho informado {path} não é um diretório válido"
            )
        if not os.access(path, os.W_OK):
            raise PermissionError(
                f"Permissão negada para acessar o diretório {path}"
            )


def start() -> None:
    load_dotenv()

    try:
        check_environment_variables(REQUIRED_ENV_VARS)
    except ValueError as e:
        print(f"[ERRO] {e}")
        return

    path_planilha = Path(os.getenv("DIRETORIO_PLANILHA"))
    path_export = Path(os.getenv("DIRETORIO_EXPORT"))
    path_log = Path(os.getenv("DIRETORIO_LOG"))

    try:
        validate_paths(path_planilha, path_export, path_log)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print(f"[ERRO] {e}")
        return

    setup_logging(path_log)
    logger = lg.getLogger(__name__)

    logger.info("Variáveis de ambiente e caminhos validados com sucesso")
    process_spreadsheet(path_planilha, path_export)
    logger.info("Execução finalizada")


if __name__ == "__main__":
    start()
