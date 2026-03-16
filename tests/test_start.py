import pytest
from pathlib import Path

from src.main.start import validate_paths


@pytest.fixture
def setup_paths(tmp_path):
    planilha = tmp_path / "dados.xlsx"
    planilha.write_text("fake")
    export_dir = tmp_path / "exports"
    export_dir.mkdir()
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    return planilha, export_dir, log_dir


def test_validate_paths_ok(setup_paths):
    planilha, export_dir, log_dir = setup_paths
    validate_paths(planilha, export_dir, log_dir)


def test_validate_paths_planilha_inexistente(setup_paths):
    _, export_dir, log_dir = setup_paths
    with pytest.raises(FileNotFoundError, match="não é um arquivo válido"):
        validate_paths(Path("/inexistente/planilha.xlsx"), export_dir, log_dir)


def test_validate_paths_export_dir_inexistente(setup_paths):
    planilha, _, log_dir = setup_paths
    with pytest.raises(NotADirectoryError, match="não é um diretório válido"):
        validate_paths(planilha, Path("/inexistente/exports"), log_dir)


def test_validate_paths_log_dir_inexistente(setup_paths):
    planilha, export_dir, _ = setup_paths
    with pytest.raises(NotADirectoryError, match="não é um diretório válido"):
        validate_paths(planilha, export_dir, Path("/inexistente/logs"))
