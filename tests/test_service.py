import pandas as pd
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.services.service import process_spreadsheet


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "SETOR": ["Logistica", "Logistica", "TI", "TI"],
        "TURNO": ["Manha", "Noite", "Manha", "Noite"],
        "VALOR": [10, 20, 30, 40],
    })


@pytest.fixture
def tmp_export_dir(tmp_path):
    return tmp_path / "exports"


def test_process_spreadsheet_exporta_arquivos(sample_df, tmp_export_dir, monkeypatch):
    tmp_export_dir.mkdir()

    monkeypatch.setattr(
        "src.services.service.get_dataframe",
        lambda _: sample_df,
    )

    process_spreadsheet(Path("planilha.xlsx"), tmp_export_dir)

    arquivos = list(tmp_export_dir.glob("*.xlsx"))
    assert len(arquivos) == 4


def test_process_spreadsheet_arquivo_invalido(tmp_path, monkeypatch):
    def fake_get_dataframe(_):
        raise FileNotFoundError("Arquivo não encontrado")

    monkeypatch.setattr(
        "src.services.service.get_dataframe",
        fake_get_dataframe,
    )

    process_spreadsheet(Path("inexistente.xlsx"), tmp_path)


def test_process_spreadsheet_coluna_faltando(tmp_path, monkeypatch):
    df_sem_coluna = pd.DataFrame({"SETOR": ["A"], "OUTRO": [1]})

    monkeypatch.setattr(
        "src.services.service.get_dataframe",
        lambda _: df_sem_coluna,
    )

    process_spreadsheet(Path("planilha.xlsx"), tmp_path)
