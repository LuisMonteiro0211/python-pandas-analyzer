import logging as lg
from pathlib import Path


def setup_logging(log_dir: Path) -> None:
    """
    Configura o logging da aplicação para gravar em arquivo.

    Args:
        log_dir: Diretório onde o arquivo de log será criado.
    """
    lg.basicConfig(
        level=lg.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_dir / "app.log",
        filemode="a",
        encoding="utf-8",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
