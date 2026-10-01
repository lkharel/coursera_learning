# Python Test Automation Learning Project

A clean learning project for Python, pytest, Black, Ruff, file I/O, and
log parsing.

## Structure

```text
test-automation/
├── .vscode/
│   └── settings.json
├── learning/
│   └── reading_writing_files/
│       ├── decorators/
│       ├── append_to_a_file.py
│       ├── my_first_file.txt
│       └── write_to_a_file.py
├── log_processor/
│   ├── sample_logs/
│   │   └── sample_pre_processing.log
│   ├── __init__.py
│   ├── elements.py
│   └── log_parser.py
├── src/
│   ├── __init__.py
│   └── application.py
├── tests/
│   ├── conftest.py
│   ├── test_application.py
│   └── test_tex_237.py
├── .gitignore
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run checks

```bash
python -m black --check .
python -m ruff check .
python -m pytest
```

To format and auto-fix safe lint issues:

```bash
python -m black .
python -m ruff check . --fix
```

## Log parser input

By default, the log test reads:

```text
log_processor/sample_logs/sample_pre_processing.log
```

To use a real run directory without changing test code, set
`RUN_DIRECTORY` before running pytest.

macOS/Linux:

```bash
export RUN_DIRECTORY=/storage/share/user/repo/output/RUN_JUST_PERFORMED
python -m pytest tests/test_tex_237.py -v -s
```

Windows PowerShell:

```powershell
$env:RUN_DIRECTORY="C:\path\to\RUN_JUST_PERFORMED"
python -m pytest tests\test_tex_237.py -v -s
```

The parser searches for the first file matching:

```text
sample_pre_processing*.log
```

It ignores the header and starts reading after:

```text
------------------------
```
