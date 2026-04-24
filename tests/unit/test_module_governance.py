"""Governance checks for target-oracle-wms module structure."""

from __future__ import annotations

import ast
from pathlib import Path

from tests import c, m


def _package_root() -> Path:
    parent_depth = int(c.TargetOracleWms.Tests.PROJECT_ROOT_PARENT_DEPTH)
    return (
        Path(__file__).resolve().parents[parent_depth]
        / c.TargetOracleWms.Tests.SRC_DIR
        / c.TargetOracleWms.Tests.PACKAGE_DIR
    )


def _iter_package_modules() -> list[Path]:
    return sorted(_package_root().rglob("*.py"))


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
                violations.append(str(module_path.relative_to(_package_root().parent)))
    assert not violations, (
        f"Module-level logger assignments are forbidden: {violations}"
    )


def test_package_modules_do_not_define_unapproved_top_level_functions() -> None:
    violations: list[str] = []
    for module_path in _iter_package_modules():
        relative_module_path = str(module_path.relative_to(_package_root()))
        allowed_functions = c.TargetOracleWms.Tests.ALLOWED_MODULE_FUNCTIONS.get(
            relative_module_path,
            frozenset(),
        )
        module_tree = _read_module_tree(module_path)
        unexpected_functions = sorted(
            node.name
            for node in module_tree.body
            if isinstance(node, ast.FunctionDef) and node.name not in allowed_functions
        )
        if unexpected_functions:
            violations.append(
                f"{module_path.relative_to(_package_root().parent)}: {unexpected_functions}",
            )
    assert not violations, (
        f"Top-level functions are forbidden outside approved entrypoints: {violations}"
    )


def test_target_oracle_wms_namespace_does_not_define_local_singer_message_models() -> (
    None
):
    assert hasattr(m.TargetOracleWms, "SingerFieldSchema")
    assert hasattr(m.TargetOracleWms, "SingerSchemaProperties")
    assert not hasattr(m.TargetOracleWms, "SingerSchemaMessage")
    assert not hasattr(m.TargetOracleWms, "SingerRecordMessage")
    assert not hasattr(m.TargetOracleWms, "SingerCatalogEntry")
