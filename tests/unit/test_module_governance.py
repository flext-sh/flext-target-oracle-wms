"""Governance checks for target-oracle-wms module structure."""

from __future__ import annotations

import importlib
import inspect
from collections.abc import Iterator
from pathlib import Path
from types import ModuleType

from tests.constants import c
from tests.models import m


def _package_root() -> Path:
    parent_depth = c.TargetOracleWms.Tests.PROJECT_ROOT_PARENT_DEPTH
    return Path(
        Path(__file__).resolve().parents[parent_depth]
        / c.TargetOracleWms.Tests.SRC_DIR
        / c.TargetOracleWms.Tests.PACKAGE_DIR
    )


def _iter_package_modules() -> list[Path]:
    return sorted(_package_root().rglob("*.py"))


def _module_dotted_name(module_path: Path) -> str:
    package_root = _package_root()
    relative = module_path.relative_to(package_root.parent)
    parts = relative.with_suffix("").parts
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _import_package_module(module_path: Path) -> ModuleType | None:
    try:
        return importlib.import_module(_module_dotted_name(module_path))
    except (ImportError, AttributeError):
        return None


def _module_top_level_attrs(module: ModuleType) -> Iterator[tuple[str, object]]:
    module_name = module.__name__
    for name, value in vars(module).items():
        if name.startswith("__") and name.endswith("__"):
            continue
        owner = getattr(value, "__module__", None)
        if owner is not None and owner != module_name:
            continue
        yield name, value


class TestsFlextTargetOracleWmsModuleGovernance:
    """Behavior contract for test_module_governance."""

    def test_package_modules_do_not_define_module_level_loggers(self) -> None:
        violations: list[str] = []
        for module_path in _iter_package_modules():
            module = _import_package_module(module_path)
            if module is None:
                continue
            for name, _ in _module_top_level_attrs(module):
                if name in {"logger", "_logger"}:
                    violations.append(
                        str(module_path.relative_to(_package_root().parent))
                    )
                    break
        assert not violations, (
            f"Module-level logger assignments are forbidden: {violations}"
        )

    def test_package_modules_do_not_define_unapproved_top_level_functions(self) -> None:
        violations: list[str] = []
        for module_path in _iter_package_modules():
            relative_module_path = str(module_path.relative_to(_package_root()))
            allowed_functions = c.TargetOracleWms.Tests.ALLOWED_MODULE_FUNCTIONS.get(
                relative_module_path,
                frozenset(),
            )
            module = _import_package_module(module_path)
            if module is None:
                continue
            unexpected_functions = sorted(
                name
                for name, value in _module_top_level_attrs(module)
                if inspect.isfunction(value) and name not in allowed_functions
            )
            if unexpected_functions:
                violations.append(
                    f"{module_path.relative_to(_package_root().parent)}: {unexpected_functions}",
                )
        assert not violations, (
            f"Top-level functions are forbidden outside approved entrypoints: {violations}"
        )

    def test_target_oracle_wms_namespace_does_not_define_local_singer_message_models(
        self,
    ) -> None:
        assert hasattr(m.TargetOracleWms, "SingerFieldSchema")
        assert hasattr(m.TargetOracleWms, "SingerSchemaProperties")
        assert not hasattr(m.TargetOracleWms, "SingerSchemaMessage")
        assert not hasattr(m.TargetOracleWms, "SingerRecordMessage")
        assert not hasattr(m.TargetOracleWms, "SingerCatalogEntry")
