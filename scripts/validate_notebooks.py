from __future__ import annotations

import json
import re
from pathlib import Path

EXPECTED_NOTEBOOKS = {
    "theory.ipynb",
    "problem_statement.ipynb",
    "requirements.ipynb",
    "main.ipynb",
}

ABSOLUTE_PATH_RE = re.compile(
    r"(?:[A-Za-z]:\\\\|/home/|/Users/|/mnt/c/)"
)

errors: list[str] = []

lab_dirs = sorted(
    path
    for path in Path("labs").glob("*/*")
    if path.is_dir() and (path / "notebooks").is_dir()
)

if len(lab_dirs) != 8:
    errors.append(f"Expected 8 laboratory modules, found {len(lab_dirs)}.")

for lab_dir in lab_dirs:
    notebook_dir = lab_dir / "notebooks"
    notebook_paths = sorted(notebook_dir.glob("*.ipynb"))
    names = {path.name for path in notebook_paths}

    if names != EXPECTED_NOTEBOOKS:
        missing = sorted(EXPECTED_NOTEBOOKS - names)
        extra = sorted(names - EXPECTED_NOTEBOOKS)
        errors.append(
            f"{lab_dir}: notebook set mismatch; missing={missing}, extra={extra}"
        )

    for notebook_path in notebook_paths:
        try:
            notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{notebook_path}: invalid notebook JSON: {exc}")
            continue

        for cell_index, cell in enumerate(notebook.get("cells", []), start=1):
            source = "".join(cell.get("source", []))

            if "Zero to Mastery" in source:
                errors.append(
                    f"{notebook_path}:cell {cell_index}: forbidden phrase 'Zero to Mastery'."
                )

            if cell.get("cell_type") != "code" or not source.strip():
                continue

            if ABSOLUTE_PATH_RE.search(source):
                errors.append(
                    f"{notebook_path}:cell {cell_index}: machine-specific absolute path detected."
                )

            try:
                compile(
                    source,
                    f"{notebook_path}:cell {cell_index}",
                    "exec",
                )
            except SyntaxError as exc:
                errors.append(
                    f"{notebook_path}:cell {cell_index}: "
                    f"{exc.msg} (line {exc.lineno}, offset {exc.offset})"
                )

    main_path = notebook_dir / "main.ipynb"
    if main_path.exists():
        main_nb = json.loads(main_path.read_text(encoding="utf-8"))
        markdown = "\n".join(
            "".join(cell.get("source", []))
            for cell in main_nb.get("cells", [])
            if cell.get("cell_type") == "markdown"
        )
        if "## Final Analysis & Interpretation" not in markdown:
            errors.append(
                f"{main_path}: missing final 'Final Analysis & Interpretation' section."
            )

if errors:
    print("Notebook QA FAILED")
    for error in errors:
        print(f" - {error}")
    raise SystemExit(1)

print(
    f"Notebook QA passed: {len(lab_dirs)} labs, "
    f"{len(lab_dirs) * 4} notebooks, Python syntax validated."
)
