from csv_inspector.cli import main


def test_cli_info(tmp_path, monkeypatch, capsys):
    csv_file = tmp_path / "users.csv"
    csv_file.write_text(
        "name,age\nFedor,19\nAlex,20\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        ["csv-inspector", "info", str(csv_file)],
    )

    assert main() == 0

    output = capsys.readouterr().out

    assert "Rows: 2" in output
    assert "Columns: 2" in output
