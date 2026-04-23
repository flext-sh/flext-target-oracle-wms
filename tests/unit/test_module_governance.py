"""Governance checks for target-oracle-wms module structure."""

from __future__ import annotations

import ast
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1] / "src" / "flext_target_oracle_wms"
ALLOWED_MODULE_FUNCTIONS: dict[str, set[str]] = {
    "cli.py": {"main"},
}


def _iter_package_modules() -> list[Path]:
    return sorted(PACKAGE_ROOT.rglob("*.py"))


def _read_module_tree(module_path: Path) -> ast.Module:
    return ast.parse(module_path.read_text(encoding="utf-8"), filename=str(module_path))


def test_package_modules_do_not_define_module_level_loggers() -> None:
    violations: list[str] = []
    for module_path in _iter_package_modules():
        module_tree = _read_module_tree(module_path)
        for node in module_tree.body:
            if not isinstance(node, ast.Assign):
                continue
            if any(
                isinstance(target, ast.Name) and target.id == "logger"
                for target in node.targets
            ):
                violations.append(str(module_path.relative_to(PACKAGE_ROOT.parent)))
    assert not violations, (
        f"Module-level logger assignments are forbidden: {violations}"
    )


def test_package_modules_do_not_define_unapproved_top_level_functions() -> None:
    violations: list[str] = []
    for module_path in _iter_package_modules():
        relative_module_path = str(module_path.relative_to(PACKAGE_ROOT))
        allowed_functions = ALLOWED_MODULE_FUNCTIONS.get(relative_module_path, set())
        module_tree = _read_module_tree(module_path)
        unexpected_functions = sorted(
            node.name
            for node in module_tree.body
            if isinstance(node, ast.FunctionDef) and node.name not in allowed_functions
        )
        if unexpected_functions:
            violations.append(
                f"{module_path.relative_to(PACKAGE_ROOT.parent)}: {unexpected_functions}",
            )
    assert not violations, (
        f"Top-level functions are forbidden outside approved entrypoints: {violations}"
    )
