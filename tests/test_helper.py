import pandas as pd
import pytest

from src.helpers.helper import (
    applying_filters,
    check_colunas,
    check_environment_variables,
    get_colunas,
    get_dataframe,
    get_valores_unicos,
    safe_name,
)
from src.models.filtro import Filtro


# --- get_dataframe ---

def test_get_dataframe_ok(monkeypatch):
    df_fake = pd.DataFrame({"SETOR": ["A"], "TURNO": ["Manha"]})

    monkeypatch.setattr("src.helpers.helper.Path.is_file", lambda _: True)
    monkeypatch.setattr("src.helpers.helper.pd.read_excel", lambda _: df_fake)

    df = get_dataframe("arquivo.xlsx")
    assert df.shape == (1, 2)


def test_get_dataframe_arquivo_inexistente(monkeypatch):
    monkeypatch.setattr("src.helpers.helper.Path.is_file", lambda _: False)

    with pytest.raises(FileNotFoundError, match="não encontrado"):
        get_dataframe("arquivo_inexistente.xlsx")


def test_get_dataframe_erro_leitura(monkeypatch):
    monkeypatch.setattr("src.helpers.helper.Path.is_file", lambda _: True)
    monkeypatch.setattr(
        "src.helpers.helper.pd.read_excel",
        lambda _: (_ for _ in ()).throw(Exception("erro de leitura")),
    )

    with pytest.raises(ValueError, match="Erro ao ler o arquivo"):
        get_dataframe("arquivo.xlsx")


# --- get_colunas ---

def test_get_colunas():
    df = pd.DataFrame({"SETOR": [], "TURNO": [], "NOME": []})
    colunas = get_colunas(df)
    assert colunas == ["SETOR", "TURNO", "NOME"]


# --- check_colunas ---

def test_check_colunas_existente():
    check_colunas(["SETOR", "TURNO"], "SETOR")


def test_check_colunas_inexistente():
    with pytest.raises(ValueError, match="não encontrada"):
        check_colunas(["SETOR"], "TURNO")


# --- get_valores_unicos ---

def test_get_valores_unicos():
    df = pd.DataFrame({"SETOR": ["A", "B", "A", "C"]})
    valores = get_valores_unicos(df, "SETOR")
    assert set(valores) == {"A", "B", "C"}


def test_get_valores_unicos_coluna_unica():
    df = pd.DataFrame({"TURNO": ["Manha", "Manha", "Manha"]})
    valores = get_valores_unicos(df, "TURNO")
    assert valores == ["Manha"]


# --- applying_filters ---

def test_applying_filters():
    df = pd.DataFrame({
        "SETOR": ["A", "B", "A"],
        "TURNO": ["Manha", "Noite", "Noite"],
    })
    filtro = Filtro(coluna="SETOR", dataframe=df, valor="A")
    filtrado = applying_filters(filtro)
    assert filtrado.shape[0] == 2


def test_applying_filters_sem_resultado():
    df = pd.DataFrame({
        "SETOR": ["A", "B"],
        "TURNO": ["Manha", "Noite"],
    })
    filtro = Filtro(coluna="SETOR", dataframe=df, valor="C")
    filtrado = applying_filters(filtro)
    assert filtrado.empty


# --- check_environment_variables ---

def test_check_environment_variables_ok(monkeypatch):
    monkeypatch.setenv("VAR_A", "valor_a")
    monkeypatch.setenv("VAR_B", "valor_b")
    check_environment_variables(["VAR_A", "VAR_B"])


def test_check_environment_variables_faltando(monkeypatch):
    monkeypatch.delenv("VAR_INEXISTENTE", raising=False)
    with pytest.raises(ValueError, match="VAR_INEXISTENTE"):
        check_environment_variables(["VAR_INEXISTENTE"])


# --- safe_name ---

def test_safe_name_com_caracteres_invalidos():
    assert safe_name('relatorio<setor>:turno?.xlsx') == "relatorio_setor__turno_.xlsx"


def test_safe_name_sem_caracteres_invalidos():
    assert safe_name("relatorio_normal.xlsx") == "relatorio_normal.xlsx"


def test_safe_name_com_espacos():
    assert safe_name("  nome com espaços  ") == "nome com espaços"
