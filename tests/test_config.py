"""Testes do carregamento da chave da API do OpenAlex (nunca do config.yaml versionado)."""

from scripts import config


def test_env_var_takes_precedence(monkeypatch, tmp_path):
    key_file = tmp_path / "key.txt"
    key_file.write_text("from-file\n")
    monkeypatch.setattr(config, "REPO_ROOT", tmp_path)
    monkeypatch.setenv("OPENALEX_API_KEY", " from-env ")
    assert config._openalex_api_key({"api_key_file": "key.txt"}) == "from-env"


def test_key_file_is_read_and_stripped(monkeypatch, tmp_path):
    (tmp_path / "key.txt").write_text("abc123\n")
    monkeypatch.setattr(config, "REPO_ROOT", tmp_path)
    monkeypatch.delenv("OPENALEX_API_KEY", raising=False)
    assert config._openalex_api_key({"api_key_file": "key.txt"}) == "abc123"


def test_missing_key_means_free_budget(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "REPO_ROOT", tmp_path)
    monkeypatch.delenv("OPENALEX_API_KEY", raising=False)
    assert config._openalex_api_key({}) is None


def test_google_service_account_path_is_relative_to_repo(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "REPO_ROOT", tmp_path)
    path = config._google_service_account_file({"service_account_file": "credentials/sa.json"})
    assert path == tmp_path / "credentials" / "sa.json"


def test_google_service_account_absent_means_none():
    assert config._google_service_account_file({}) is None
