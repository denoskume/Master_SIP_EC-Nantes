from __future__ import annotations

import ast
import io
import json
import re
import tokenize
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
notebook_count = 0

lab_dirs = sorted(
    path
    for path in Path("labs").glob("*/*")
    if path.is_dir() and (path / "notebooks").is_dir()
)

for lab_dir in lab_dirs:
    notebook_dir = lab_dir / "notebooks"
    notebook_paths = sorted(notebook_dir.glob("*.ipynb"))
    notebook_count += len(notebook_paths)
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
                tree = ast.parse(
                    source,
                    filename=f"{notebook_path}:cell {cell_index}",
                    mode="exec",
                )
            except SyntaxError as exc:
                errors.append(
                    f"{notebook_path}:cell {cell_index}: "
                    f"{exc.msg} (line {exc.lineno}, offset {exc.offset})"
                )
                continue

            if notebook_path.name == "main.ipynb":
                try:
                    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
                    if any(token.type == tokenize.COMMENT for token in tokens):
                        errors.append(
                            f"{notebook_path}:cell {cell_index}: Python comment detected."
                        )
                except tokenize.TokenError as exc:
                    errors.append(
                        f"{notebook_path}:cell {cell_index}: tokenization error: {exc}"
                    )

                for node in ast.walk(tree):
                    if isinstance(
                        node,
                        (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef),
                    ):
                        body = getattr(node, "body", [])
                        if (
                            body
                            and isinstance(body[0], ast.Expr)
                            and isinstance(body[0].value, ast.Constant)
                            and isinstance(body[0].value.value, str)
                        ):
                            errors.append(
                                f"{notebook_path}:cell {cell_index}: docstring detected."
                            )
                            break

if errors:
    print("Notebook QA FAILED")
    for error in errors:
        print(f" - {error}")
    raise SystemExit(1)

print(
    f"Notebook QA passed: {len(lab_dirs)} labs, "
    f"{notebook_count} notebooks, Python syntax validated, "
    "main notebooks contain no Python comments or docstrings."
)
