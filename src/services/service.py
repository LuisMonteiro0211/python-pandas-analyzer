import logging as lg
from datetime import datetime
from pathlib import Path

from src.helpers.helper import (
    applying_filters,
    check_colunas,
    export_to_excel,
    get_colunas,
    get_dataframe,
    get_valores_unicos,
    safe_name,
)
from src.models.export import Export
from src.models.filtro import Filtro

COLUNA_SETOR = "SETOR"
COLUNA_TURNO = "TURNO"


def process_spreadsheet(path: Path, export_dir: Path) -> None:
    """
    Processa a planilha aplicando filtros por setor e turno,
    e exporta um arquivo Excel para cada combinação.

    Args:
        path: Caminho da planilha de entrada.
        export_dir: Diretório onde os arquivos serão salvos.
    """
    logger = lg.getLogger(__name__)
    data_hoje = datetime.now().strftime("%d_%m_%Y")

    try:
        df = get_dataframe(path)
    except (ValueError, FileNotFoundError) as e:
        logger.error(str(e))
        return

    colunas = get_colunas(df)
    try:
        check_colunas(colunas, COLUNA_SETOR)
        check_colunas(colunas, COLUNA_TURNO)
        logger.info("Colunas obrigatórias '%s' e '%s' encontradas", COLUNA_SETOR, COLUNA_TURNO)
    except ValueError as e:
        logger.error(str(e))
        return

    setores = get_valores_unicos(df, COLUNA_SETOR)
    logger.info("Setores encontrados: %s", setores)

    for setor in setores:
        filtro_setor = Filtro(coluna=COLUNA_SETOR, dataframe=df, valor=setor)
        df_setor = applying_filters(filtro_setor)

        turnos = get_valores_unicos(df_setor, COLUNA_TURNO)
        logger.info("Turnos do setor '%s': %s", setor, turnos)

        for turno in turnos:
            filtro_turno = Filtro(coluna=COLUNA_TURNO, dataframe=df_setor, valor=turno)
            df_turno = applying_filters(filtro_turno)

            nome_arquivo = safe_name(f"Relatorio_{setor}_{turno}_{data_hoje}.xlsx")
            nome_aba = safe_name(setor)

            export_obj = Export(
                dataframe=df_turno,
                diretorio=export_dir,
                nome_arquivo=nome_arquivo,
                nome_aba=nome_aba,
            )

            export_to_excel(export_obj)
            logger.info(
                "Exportado: setor=%s, turno=%s, registros=%d, arquivo=%s",
                setor,
                turno,
                df_turno.shape[0],
                nome_arquivo,
            )

    logger.info("Processamento finalizado com sucesso")
