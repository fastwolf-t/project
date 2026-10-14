from unittest.mock import Mock, patch

from src.utils import (read_json_file, read_transactions_from_csv,
                       read_transactions_from_excel)


def test_read_json_file_not_found():
    result = read_json_file("nonexistent.json")

    assert result == []


def test_read_json_file_empty(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    result = read_json_file(str(file_path))

    assert result == []


def test_read_json_file_not_list(tmp_path):
    file_path = tmp_path / "object.json"
    file_path.write_text('{"amount": "100"}', encoding="utf-8")

    result = read_json_file(str(file_path))

    assert result == []


def test_read_json_file_list(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text(
        '[{"amount": "100", "currency": "USD"}]',
        encoding="utf-8",
    )

    result = read_json_file(str(file_path))

    assert result == [{"amount": "100", "currency": "USD"}]


def test_read_transactions_from_csv() -> None:
    """Проверяет чтение транзакций из CSV."""
    expected = [{"id": 1, "amount": 100}]
    mock_df = Mock()
    mock_df.to_dict.return_value = expected

    with patch("src.utils.pd.read_csv", return_value=mock_df) as mock_read:
        result = read_transactions_from_csv("data/transactions.csv")

    assert result == expected
    mock_read.assert_called_once_with("data/transactions.csv")


def test_read_transactions_from_excel() -> None:
    """Проверяет чтение транзакций из Excel."""
    expected = [{"id": 2, "amount": 200}]
    mock_df = Mock()
    mock_df.to_dict.return_value = expected

    with patch("src.utils.pd.read_excel", return_value=mock_df) as mock_read:
        result = read_transactions_from_excel("data/transactions_excel.xlsx")

    assert result == expected
    mock_read.assert_called_once_with("data/transactions_excel.xlsx")
