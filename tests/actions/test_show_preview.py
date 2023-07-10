from pro_filer.actions.main_actions import show_preview


def test_show_preview(capsys):
    tests = [
        {
            "context": {
                "all_files": [],
                "all_dirs": []
            },
            "expected_output": "Found 0 files and 0 directories\n"
        },
        {
            "context": {
                "all_files": ["src/__init__.py", "src/utils/__init__.py"],
                "all_dirs": ["src", "src/utils"]
            },
            "expected_output": (
                "Found 2 files and 2 directories\n"
                "First 5 files: ['src/__init__.py', 'src/utils/__init__.py']\n"
                "First 5 directories: ['src', 'src/utils']\n"
            )
        },
        {
            "context": {
                "all_files": [
                    "file1", "file2", "file3", "file4",
                    "file5", "file6", "file7", "file8"
                ],
                "all_dirs": [
                    "dir1", "dir2", "dir3", "dir4",
                    "dir5", "dir6", "dir7", "dir8"
                ]
            },
            "expected_output": (
                "Found 8 files and 8 directories\n"
                "First 5 files: ['file1', 'file2', 'file3', "
                "'file4', 'file5']\n"
                "First 5 directories: ['dir1', 'dir2', 'dir3', "
                "'dir4', 'dir5']\n"
            )
        }
    ]

    for test in tests:
        context = test["context"]
        expected_output = test["expected_output"]

        show_preview(context)
        captured = capsys.readouterr()

        assert captured.out == expected_output
