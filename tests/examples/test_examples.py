"""Test examples functionality - REAL implementation validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from tests import c, t, tm

_AUTO_GENERATED_FACETS: frozenset[str] = frozenset({
    "constants.py",
    "models.py",
    "protocols.py",
    "typings.py",
    "utilities.py",
})


def _parse_example(example_file: Path) -> ast.Module:
    return ast.parse(
        example_file.read_text(encoding="utf-8"),
        filename=str(example_file),
    )


def _module_docstring(tree: ast.Module) -> str:
    return ast.get_docstring(tree) or ""


def _module_functions(tree: ast.Module) -> list[ast.FunctionDef]:
    return [node for node in tree.body if isinstance(node, ast.FunctionDef)]


def _import_lines(content: str) -> list[str]:
    return [
        line.strip()
        for line in content.splitlines()
        if line.strip().startswith(("import ", "from "))
    ]


class TestsFlextTargetOracleWmsExamples:
    """Test examples for code quality and real API usage."""

    @staticmethod
    def test_examples_directory_exists(examples_dir: Path) -> None:
        """Test that examples directory exists and contains files."""
        tm.that(examples_dir.exists(), msg="Examples directory must exist")
        tm.that(examples_dir.is_dir(), msg="Examples path must be a directory")
        python_files = list(examples_dir.glob("*.py"))
        tm.that(
            len(python_files),
            gte=c.TargetOracleWms.Tests.MIN_EXAMPLE_FILE_COUNT,
            msg=("Must have the configured minimum example files"),
        )
        expected_files = [
            "example_01_basic_usage.py",
            "example_05_advanced_configuration.py",
            "example_02_batch_processing.py",
            "example_03_error_handling.py",
        ]
        for expected_file in expected_files:
            file_path = examples_dir / expected_file
            tm.that(
                file_path.exists(),
                msg=(f"Required example file {expected_file} must exist"),
            )

    @staticmethod
    def test_examples_use_real_imports(example_files: t.SequenceOf[Path]) -> None:
        """Test that examples use REAL flext-* imports, not fallbacks."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            import_lines = _import_lines(content)
            has_flext_core = any(
                "flext_core" in line or "flext_target_oracle_wms" in line
                for line in import_lines
            )
            has_target_import = any(
                "flext_target_oracle_wms" in line for line in import_lines
            )
            tm.that(
                has_flext_core,
                msg=(
                    f"{example_file.name} must import real flext primitives "
                    "(flext_core or the flext_target_oracle_wms facade)"
                ),
            )
            tm.that(
                has_target_import,
                msg=(f"{example_file.name} must import from flext_target_oracle_wms"),
            )
            forbidden_patterns = [
                "type: ignore[import-not-found]",
                "import fallback",
                "except ImportError:",
                "mock_",
                "placeholder_",
                "TODO:",
                "FIXME:",
                "HACK:",
            ]
            for pattern in forbidden_patterns:
                tm.that(content, lacks=pattern)

    @staticmethod
    def test_examples_have_comprehensive_docstrings(
        example_files: t.SequenceOf[Path],
    ) -> None:
        """Require module docs everywhere and comprehensive example docs."""
        for example_file in example_files:
            tree = _parse_example(example_file)
            module_docstring = _module_docstring(tree)
            tm.that(
                module_docstring.strip(),
                truth=True,
                msg=f"{example_file.name} docstring is empty",
            )
            if example_file.name in _AUTO_GENERATED_FACETS:
                continue
            tm.that(
                len(module_docstring),
                gt=c.TargetOracleWms.Tests.MIN_MODULE_DOCSTRING_LENGTH,
                msg=f"{example_file.name} docstring too short",
            )
            tm.that(
                "PRODUCTION" in module_docstring.upper()
                or "REAL" in module_docstring.upper(),
                msg=(
                    f"{example_file.name} must emphasize production/real implementation"
                ),
            )
            module_functions = _module_functions(tree)
            function_count = len(module_functions)
            documented_functions = sum(
                1
                for function in module_functions
                if (func_docstring := ast.get_docstring(function))
                and len(func_docstring)
                > c.TargetOracleWms.Tests.MIN_FUNCTION_DOCSTRING_LENGTH
            )
            if function_count > 0:
                doc_ratio = documented_functions / function_count
                tm.that(
                    doc_ratio,
                    gte=c.TargetOracleWms.Tests.MIN_DOCUMENTED_FUNCTION_RATIO,
                    msg=(
                        f"{example_file.name} must meet "
                        "the configured documentation ratio"
                    ),
                )

    @staticmethod
    def test_examples_use_await_patterns(
        example_files: t.SequenceOf[Path],
    ) -> None:
        """Test that examples with async functions use proper await patterns."""
        for example_file in example_files:
            tree = _parse_example(example_file)
            async_functions = [
                node for node in tree.body if isinstance(node, ast.AsyncFunctionDef)
            ]
            has_async_function = bool(async_functions)
            has_await = any(
                isinstance(node, ast.Await)
                for function in async_functions
                for node in ast.walk(function)
            )
            if has_async_function:
                tm.that(
                    has_await,
                    msg=(
                        f"{example_file.name} has async functions "
                        "but no await statements"
                    ),
                )

    @staticmethod
    def test_examples_implement_error_handling(
        example_files: t.SequenceOf[Path],
    ) -> None:
        """Test that examples implement proper error handling."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            has_try_except = "try:" in content and "except" in content
            has_flext_result_check = any(
                token in content for token in (".success", ".is_success", ".is_failure")
            )
            if "error" in content.lower():
                tm.that(
                    has_try_except or has_flext_result_check,
                    msg=(
                        f"{example_file.name} mentions errors but has no error handling"
                    ),
                )

    @staticmethod
    def test_examples_use_realistic_config(
        example_files: t.SequenceOf[Path],
    ) -> None:
        """Test that examples use realistic configuration patterns."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            config_patterns = [
                "base_url",
                "username",
                "password",
                "environment",
                "batch_size",
            ]
            has_config = False
            for pattern in config_patterns:
                if pattern in content:
                    has_config = True
                    break
            if "settings" in content.lower():
                tm.that(
                    has_config,
                    msg=(
                        f"{example_file.name} mentions settings but has no "
                        "realistic configuration"
                    ),
                )
            oracle_patterns = ["oracle", "wms", "FlextTargetOracleWms"]
            has_oracle_pattern = False
            for pattern in oracle_patterns:
                if pattern in content:
                    has_oracle_pattern = True
                    break
            tm.that(
                has_oracle_pattern,
                msg=(f"{example_file.name} must contain Oracle WMS specific patterns"),
            )

    @staticmethod
    def test_examples_have_main_execution_blocks(
        example_files: t.SequenceOf[Path],
    ) -> None:
        """Require main blocks in runnable examples, not imported support facades."""
        for example_file in example_files:
            if example_file.name in _AUTO_GENERATED_FACETS:
                continue
            content = example_file.read_text(encoding="utf-8")
            tm.that(content, has='if __name__ == "__main__":')
            main_patterns = ["u.Cli.print(", "run(", "run_", "demonstrate_"]
            has_main_execution = False
            for pattern in main_patterns:
                if pattern in content:
                    has_main_execution = True
                    break
            tm.that(
                has_main_execution,
                msg=(f"{example_file.name} main block must execute examples"),
            )

    """Test that examples can be imported without errors."""

    @staticmethod
    def test_examples_are_importable() -> None:
        """Test that examples can be imported (syntax validation)."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))
        for example_file in example_files:
            if example_file.name == "__init__.py":
                continue
            try:
                content = example_file.read_text(encoding="utf-8")
                compiled = compile(content, str(example_file), "exec")
            except SyntaxError as e:
                pytest.fail(f"Syntax error in {example_file.name}: {e}")
            try:
                tm.that(compiled, none=False)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                pytest.fail(f"Parse error in {example_file.name}: {e}")

    """Test examples directory structure and organization."""

    @staticmethod
    def test_examples_readme_exists() -> None:
        """Test that examples README exists and is comprehensive."""
        examples_dir = Path(__file__).parents[2] / "examples"
        readme_path = examples_dir / "README.md"
        tm.that(readme_path.exists(), msg="Examples directory must have README.md")
        readme_content = readme_path.read_text(encoding="utf-8")
        tm.that(
            len(readme_content),
            gt=c.TargetOracleWms.Tests.MIN_README_LENGTH,
            msg=("README must meet the configured minimum length"),
        )
        required_sections = [
            "Examples Overview",
            "Running the Examples",
            "Configuration",
            "Performance",
            "Security",
        ]
        for section in required_sections:
            tm.that(readme_content, has=section)

    @staticmethod
    def test_examples_follow_naming_convention() -> None:
        """Test that examples follow proper naming conventions."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))
        for example_file in example_files:
            if example_file.name == "__init__.py":
                continue
            name = example_file.stem
            tm.that(
                name.islower(), msg=f"Example {example_file.name} must use lowercase"
            )
            tm.that(
                "_" in name or name.isalpha(),
                msg=(f"Example {example_file.name} must use snake_case"),
            )
            tm.that(
                len(name),
                gte=c.TargetOracleWms.Tests.MIN_EXAMPLE_STEM_LENGTH,
                msg=(f"Example {example_file.name} name too short"),
            )

    @staticmethod
    def test_examples_have_proper_headers() -> None:
        """Test that examples have proper file headers."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))
        for example_file in example_files:
            if example_file.name == "__init__.py":
                continue
            if example_file.name in _AUTO_GENERATED_FACETS:
                continue
            content = example_file.read_text(encoding="utf-8")
            lines = content.split("\n")
            tm.that(
                lines[0].startswith("#!/usr/bin/env python3"),
                msg=(f"{example_file.name} must have proper shebang"),
            )
            tm.that(
                any("Copyright" in line for line in lines[:20]),
                msg=(f"{example_file.name} must have copyright notice"),
            )
            tm.that(
                any("MIT" in line for line in lines[:20]),
                msg=(f"{example_file.name} must have MIT license notice"),
            )

    """Test that examples properly integrate with flext-* ecosystem."""

    @staticmethod
    def test_examples_use_flext_result_pattern() -> None:
        """Test that examples use r pattern correctly."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            if "import r" in content or "from flext_core import r" in content:
                tm.that(
                    ".is_success" in content or ".is_failure" in content,
                    msg=(f"{example_file.name} uses r but not .is_success/.is_failure"),
                )
                tm.that(
                    ".error" in content or ".value" in content,
                    msg=(
                        f"{example_file.name} must check result.error or result.value"
                    ),
                )

    @staticmethod
    def test_examples_use_flext_logging() -> None:
        """Test that examples use flext-core logging correctly."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            if "FlextLogger" in content:
                tm.that(content, has="logger = u.fetch_logger(__name__)")
                tm.that(
                    "logger.info(" in content or "logger.error(" in content,
                    msg=(f"{example_file.name} must actually use the logger"),
                )
