from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files(tmp_path):
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    temp_file_1 = temp_dir / "temp_file_1.txt"
    temp_file_1.write_text("same file content")
    temp_file_2 = temp_dir / "temp_file_2.txt"
    temp_file_2.write_text("same file content")
    temp_file_3 = temp_dir / "temp_file_3.txt"
    temp_file_3.write_text("different file content")

    mock_context = {
        "all_files": [str(temp_file_1), str(temp_file_2), str(temp_file_3)]
    }

    result = find_duplicate_files(mock_context)

    assert result == [(str(temp_file_1), str(temp_file_2))]

    temp_file_4 = temp_dir / "temp_file_4.txt"
    temp_file_4.write_text("same file content")

    mock_context = {
        "all_files": [str(temp_file_1), str(temp_file_4),
                      f"{str(temp_dir)}/inexistent_file.py"]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(mock_context)
   
