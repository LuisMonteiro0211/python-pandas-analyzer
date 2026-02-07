import pandas as pd

from src.helpers.helper import applying_filters, check_colunas, get_dataframe
from src.models.filtro import Filtro


def test_get_dataframe_ok(monkeypatch):
    df_fake = pd.DataFrame({"Setor": ["A"], "Turno": ["Manha"]})

    monkeypatch.setattr("src.helpers.helper.Path.is_file", lambda _: True)
    monkeypatch.setattr("src.helpers.helper.pd.read_excel", lambda _: df_fake)

    df = get_dataframe("arquivo.xlsx")
    assert df.shape == (1, 2)


def test_get_dataframe_arquivo_inexistente(monkeypatch):
    monkeypatch.setattr("src.helpers.helper.Path.is_file", lambda _: False)

    try:
        get_dataframe("arquivo_inexistente.xlsx")
        assert False, "Esperava FileNotFoundError"
    except FileNotFoundError:
        assert True


def test_get_dataframe_erro_leitura(monkeypatch):
    def fake_read_excel(_):
        raise Exception("erro")

    monkeypatch.setattr("src.helpers.helper.Path.is_file", lambda _: True)
    monkeypatch.setattr("src.helpers.helper.pd.read_excel", fake_read_excel)

    try:
        get_dataframe("arquivo.xlsx")
        assert False, "Esperava ValueError"
    except ValueError:
        assert True


def test_check_colunas_inexistente():
    colunas = ["Setor"]

    try:
        check_colunas(colunas, "Turno")
        assert False, "Esperava ValueError"
    except ValueError:
        assert True


def test_applying_filters():
    df = pd.DataFrame(
        {
            "Setor": ["A", "B", "A"],
            "Turno": ["Manha", "Noite", "Noite"],
        }
    )
    filtro = Filtro(coluna="Setor", dataframe=df, valor="A")
    filtrado = applying_filters(filtro)
    assert filtrado.shape[0] == 2