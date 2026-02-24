from src.helpers.helper import get_dataframe, get_colunas, check_colunas, get_setores, applying_filters, get_turnos, export_to_excel, check_environment_variables, safe_name
from src.models.filtro import Filtro
from src.models.export import Export
from datetime import datetime
from os import getenv
from pathlib import Path
import logging as lg

def process_spreadsheet(path: Path) -> None:
    """
    Processa a planilha aplicando filtros por setor e turno, e retorna a quantidade de dados filtrados.

    Fluxo de execução:
    1. Obtém o dataframe a partir do caminho da planilha
    2. Verifica se as colunas necessárias estão presentes
    3. Obtém os setores
    4. Para cada setor, obtém os turnos
    5. Para cada turno, obtém os dados

    Args:
        path: Caminho da planilha
    """
    logger = lg.getLogger(__name__)
    data_hoje = datetime.now().strftime('%d_%m')

    try:
        df = get_dataframe(path)
    except (ValueError, FileNotFoundError) as e:
        logger.error(f"{e}")
        return


    ##Verifica se as colunas necessárias estão presentes
    colunas = get_colunas(df)
    try:
        check_colunas(colunas, 'SETOR')
        logger.info(f"Coluna 'Setor' encontrada")
        check_colunas(colunas, 'TURNO')
        logger.info(f"Coluna 'TURNO' encontrada")
    except ValueError as e:
        logger.error(f"{e}")
        return

    ##Obtém os setores
    setores = get_setores(df)
    logger.info(f"Obtendo os setores")
    for setor in setores:
        filtro_setor = Filtro(coluna='SETOR', dataframe=df, valor=setor)
        df_setor = applying_filters(filtro_setor)

        ##Obtendo os turnos
        turnos = get_turnos(df_setor)
        logger.info(f"Obtendo os turnos")
        for i, turno in enumerate(turnos, start=1):
            filtro_turno = Filtro(coluna='TURNO', dataframe=df_setor, valor=turno)
            df_turno = applying_filters(filtro_turno)
            logger.info(f"Aplicando filtros para o turno {turno}")
            nome_arquivo_safe = safe_name(f"{setor}_{i}_{data_hoje}.xlsx")
            nome_pasta_safe = safe_name(setor)
            
            object_to_export = Export(
                dataframe= df_turno,
                diretorio=Path(getenv('DIRETORIO_EXPORT')),
                nome_arquivo= nome_arquivo_safe,
                nome_pasta= nome_pasta_safe
            )
            logger.info(f"Exportando o relatório para o setor {setor} e turno {turno}")
            export_to_excel(object_to_export)

            logger.info(f"Setor: {setor}, Turno: {turno}, Quantidade: {df_turno.shape[0]}")

    logger.info(f"Processo finalizado com sucesso")


if __name__ == "__main__":
    pass
