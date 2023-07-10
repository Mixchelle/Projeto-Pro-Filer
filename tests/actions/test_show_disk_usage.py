from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage(capsys, tmp_path):
    mock = {"all_files": []}
    file_path = tmp_path / "test.py"
    file_path.touch()
    file_path.write_text("test")
    empty_file_path = tmp_path / "empty_file.py"
    empty_file_path.touch()

    tests = [
        {
            "context": {"all_files": [str(file_path), str(empty_file_path)]},
            "expected_output": (
                f"'{_get_printable_file_path(str(file_path))}':".ljust(70)
                + " 4 (100%)\n" +
                f"'{_get_printable_file_path(str(empty_file_path))}':"
                .ljust(70) + " 0 (0%)\n" +
                "Total size: 4\n"
            )
        },
        {
            "context": mock,
            "expected_output": "Total size: 0\n"
        }
    ]

    for test in tests:
        show_disk_usage(test["context"])
        captured = capsys.readouterr()
        assert captured.out == test["expected_output"]
