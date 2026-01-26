from helpers.helper import get_dataframe, get_colunas, check_colunas, get_setores, applying_filters, get_turnos
from models.filtro import Filtro

def process_spreadsheet(path: str) -> None:
    ##Adicona a planilha em memória
    #TODO: Adicionar tratamento de erro para caso a planilha não seja encontrada
    df = get_dataframe(path)

    ##Verifica se as colunas necessárias estão presentes
    colunas = get_colunas(df)
    check_colunas(colunas, 'Setor')
    check_colunas(colunas, 'Turno')

    ##Obtém os setores
    setores = get_setores(df)

    for setor in setores:
        filtro_setor = Filtro(coluna='Setor', dataframe=df, valor=setor)
        df_setor = applying_filters(filtro_setor)
        #print(df_setor.shape)
        ##Obtendo os turnos
        turnos = get_turnos(df_setor)
        for turno in turnos:
            filtro_turno = Filtro(coluna='Turno', dataframe=df_setor, valor=turno)
            df_turno = applying_filters(filtro_turno)
            print(f"Setor: {setor}, Turno: {turno}, Quantidade: {df_turno.shape[0]}")

        


if __name__ == "__main__":
    process_spreadsheet('./dados_ficticios_2025.xlsx')