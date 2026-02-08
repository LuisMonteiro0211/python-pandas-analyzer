from src.helpers.helper import get_dataframe, get_colunas, check_colunas, get_setores, applying_filters, get_turnos, export_to_excel, check_environment_variables
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

    try:
        df = get_dataframe(path)
    except (ValueError, FileNotFoundError) as e:
        logger.error(f"{e}")
        return


    ##Verifica se as colunas necessárias estão presentes
    colunas = get_colunas(df)
    try:
        check_colunas(colunas, 'Setor')
        check_colunas(colunas, 'Turno')
    except ValueError as e:
        logger.error(f"{e}")
        return

    ##Obtém os setores
    setores = get_setores(df)

    for setor in setores:
        filtro_setor = Filtro(coluna='Setor', dataframe=df, valor=setor)
        df_setor = applying_filters(filtro_setor)

        ##Obtendo os turnos
        turnos = get_turnos(df_setor)

        for turno in turnos:
            filtro_turno = Filtro(coluna='Turno', dataframe=df_setor, valor=turno)
            df_turno = applying_filters(filtro_turno)

            object_to_export = Export(
                dataframe= df_turno,
                diretorio=Path(getenv('DIRETORIO_EXPORT')),
                nome_arquivo= f"Relatorio_{setor}_{turno}_{datetime.now().strftime('%d_%m_%Y')}.xlsx",
                nome_pasta= f"{setor}_{turno}"
            )
            export_to_excel(object_to_export)

            logger.info(f"Setor: {setor}, Turno: {turno}, Quantidade: {df_turno.shape[0]}")

    logger.info(f"Processo finalizado com sucesso")


if __name__ == "__main__":
    process_spreadsheet('./dados_ficticios_2025.xlsx')