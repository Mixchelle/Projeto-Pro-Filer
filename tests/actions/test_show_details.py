from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details(capsys, tmp_path):
    mock = {"base_path": "/home/teste/????"}
    file_path = tmp_path / "file01.py"
    file_path.touch()
    extension_path = tmp_path / "file01"
    extension_path.touch()

    tests = [
        {
            "context": {"base_path": str(file_path)},
            "expected_output": (
                f"File name: file01.py\n"
                f"File size in bytes: 0\n"
                f"File type: file\n"
                f"File extension: .py\n"
                f"Last modified date: {date.today()}\n"
            )
        },
        {
            "context": {"base_path": str(extension_path)},
            "expected_output": (
                f"File name: file01\n"
                f"File size in bytes: 0\n"
                f"File type: file\n"
                f"File extension: [no extension]\n"
                f"Last modified date: {date.today()}\n"
            )
        },
        {
            "context": mock,
            "expected_output": "File '????' does not exist\n"
        }
    ]

    for test in tests:
        show_details(test["context"])
        captured = capsys.readouterr()
        assert captured.out == test["expected_output"]
