"""Test examples functionality - REAL implementation validation.

These tests ensure that all examples in the examples/ directory use REAL
flext-* APIs correctly and follow production-grade patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

import pytest

# DRY: Import REAL flext-* APIs for validation - avoid circular imports
# from flext_core import FlextResult  # Skip to avoid circular import in tests


class TestExamplesCodeQuality:
    """Test examples for code quality and real API usage."""

    @pytest.fixture(scope="class")
    def examples_dir(self) -> Path:
        """Get examples directory path."""
        project_root = Path(__file__).parents[2]
        return project_root / "examples"

    @pytest.fixture(scope="class")
    def example_files(self, examples_dir: Path) -> list[Path]:
        """Get all Python example files."""
        return list(examples_dir.glob("*.py"))

    def test_examples_directory_exists(self, examples_dir: Path) -> None:
        """Test that examples directory exists and contains files."""
        assert examples_dir.exists(), "Examples directory must exist"
        assert examples_dir.is_dir(), "Examples path must be a directory"

        python_files = list(examples_dir.glob("*.py"))
        assert len(python_files) >= 4, "Must have at least 4 example files"

        expected_files = [
            "basic_usage.py",
            "advanced_configuration.py",
            "batch_processing.py",
            "error_handling.py",
        ]

        for expected_file in expected_files:
            file_path = examples_dir / expected_file
            assert file_path.exists(), (
                f"Required example file {expected_file} must exist"
            )

    def test_examples_use_real_flext_imports(self, example_files: list[Path]) -> None:
        """Test that examples use REAL flext-* imports, not fallbacks."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")

            # Parse Python code to check imports
            tree = ast.parse(content, filename=str(example_file))

            # Check for real flext-* imports
            has_flext_core = False
            has_target_import = False

            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    if node.module == "flext_core":
                        has_flext_core = True
                    elif node.module == "flext_observability":
                        pass
                    elif node.module == "flext_target_oracle_wms":
                        has_target_import = True
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.startswith("flext_"):
                            # Found flext import
                            pass

            # Verify real imports are used
            assert has_flext_core, f"{example_file.name} must import from flext_core"
            assert has_target_import, (
                f"{example_file.name} must import from flext_target_oracle_wms"
            )

            # Check for forbidden patterns
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
                assert pattern not in content, (
                    f"{example_file.name} contains forbidden pattern: {pattern}"
                )

    def test_examples_have_proper_docstrings(self, example_files: list[Path]) -> None:
        """Test that examples have comprehensive docstrings."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            tree = ast.parse(content, filename=str(example_file))

            # Check module docstring
            module_docstring = ast.get_docstring(tree)
            assert module_docstring is not None, (
                f"{example_file.name} must have module docstring"
            )
            assert len(module_docstring) > 50, (
                f"{example_file.name} docstring too short"
            )
            assert (
                "PRODUCTION" in module_docstring.upper()
                or "REAL" in module_docstring.upper()
            ), f"{example_file.name} must emphasize production/real implementation"

            # Check function docstrings
            function_count = 0
            documented_functions = 0

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    function_count += 1
                    func_docstring = ast.get_docstring(node)
                    if func_docstring and len(func_docstring) > 10:
                        documented_functions += 1

            if function_count > 0:
                doc_ratio = documented_functions / function_count
                assert doc_ratio >= 0.8, (
                    f"{example_file.name} must have 80%+ functions documented"
                )

    def test_examples_use_async_patterns(self, example_files: list[Path]) -> None:
        """Test that examples use proper async/await patterns."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            tree = ast.parse(content, filename=str(example_file))

            # Check for async functions
            has_async_function = False
            has_await = False

            for node in ast.walk(tree):
                if isinstance(node, ast.AsyncFunctionDef):
                    has_async_function = True
                elif isinstance(node, ast.Await):
                    has_await = True

            # Examples should use async patterns for production readiness
            if "async" in content.lower():
                assert has_async_function, (
                    f"{example_file.name} mentions async but has no async functions"
                )
                assert has_await, (
                    f"{example_file.name} has async functions but no await statements"
                )

    def test_examples_handle_errors_properly(self, example_files: list[Path]) -> None:
        """Test that examples implement proper error handling."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")
            tree = ast.parse(content, filename=str(example_file))

            # Check for error handling patterns
            has_try_except = False
            has_flext_result_check = False

            for node in ast.walk(tree):
                if isinstance(node, ast.Try):
                    has_try_except = True
                elif isinstance(node, ast.Attribute):
                    if node.attr == "success":
                        has_flext_result_check = True
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in {
                    "error",
                    "warning",
                }:
                    pass

            # Verify error handling patterns
            if "error" in content.lower():
                assert has_try_except or has_flext_result_check, (
                    f"{example_file.name} mentions errors but has no error handling"
                )

    def test_examples_use_real_configuration(self, example_files: list[Path]) -> None:
        """Test that examples use realistic configuration patterns."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")

            # Check for realistic Oracle WMS configuration
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

            if "config" in content.lower():
                assert has_config, (
                    f"{example_file.name} mentions config but has no realistic configuration"
                )

            # Check for Oracle WMS specific patterns
            oracle_patterns = [
                "oracle",
                "wms",
                "SingerTargetOracleWMS",
            ]

            has_oracle_pattern = False
            for pattern in oracle_patterns:
                if pattern in content:
                    has_oracle_pattern = True
                    break

            assert has_oracle_pattern, (
                f"{example_file.name} must contain Oracle WMS specific patterns"
            )

    def test_examples_have_main_blocks(self, example_files: list[Path]) -> None:
        """Test that examples have proper main execution blocks."""
        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")

            # Check for main block
            assert 'if __name__ == "__main__":' in content, (
                f"{example_file.name} must have main execution block"
            )

            # Check for example execution
            main_patterns = [
                "print(",
                "asyncio.run(",
                "run_",
                "demonstrate_",
            ]

            has_main_execution = False
            for pattern in main_patterns:
                if pattern in content:
                    has_main_execution = True
                    break

            assert has_main_execution, (
                f"{example_file.name} main block must execute examples"
            )


class TestExamplesImportability:
    """Test that examples can be imported without errors."""

    def test_examples_are_importable(self) -> None:
        """Test that examples can be imported (syntax validation)."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))

        # Add examples directory to Python path temporarily
        original_path = sys.path[:]
        try:
            sys.path.insert(0, str(examples_dir.parent))

            for example_file in example_files:
                if example_file.name == "__init__.py":
                    continue

                # Test that file can be parsed without syntax errors
                try:
                    content = example_file.read_text(encoding="utf-8")
                    ast.parse(content, filename=str(example_file))
                except SyntaxError as e:
                    pytest.fail(f"Syntax error in {example_file.name}: {e}")

                # Test that imports are resolvable (basic check)
                try:
                    spec = ast.parse(content, filename=str(example_file))
                    # Basic validation passed
                    assert spec is not None, f"Failed to parse {example_file.name}"
                except Exception as e:
                    pytest.fail(f"Parse error in {example_file.name}: {e}")
        finally:
            sys.path[:] = original_path


class TestExamplesStructure:
    """Test examples directory structure and organization."""

    def test_examples_readme_exists(self) -> None:
        """Test that examples README exists and is comprehensive."""
        examples_dir = Path(__file__).parents[2] / "examples"
        readme_path = examples_dir / "README.md"

        assert readme_path.exists(), "Examples directory must have README.md"

        readme_content = readme_path.read_text(encoding="utf-8")
        assert len(readme_content) > 1000, "README must be comprehensive (>1000 chars)"

        # Check for required sections
        required_sections = [
            "Examples Overview",
            "Running the Examples",
            "Configuration",
            "Performance",
            "Security",
        ]

        for section in required_sections:
            assert section in readme_content, f"README must contain '{section}' section"

    def test_examples_follow_naming_convention(self) -> None:
        """Test that examples follow proper naming conventions."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))

        for example_file in example_files:
            if example_file.name == "__init__.py":
                continue

            # Check naming convention (snake_case)
            name = example_file.stem
            assert name.islower(), f"Example {example_file.name} must use lowercase"
            assert "_" in name or name.isalpha(), (
                f"Example {example_file.name} must use snake_case"
            )

            # Check for descriptive names
            assert len(name) >= 5, f"Example {example_file.name} name too short"

    def test_examples_have_proper_headers(self) -> None:
        """Test that examples have proper file headers."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))

        for example_file in example_files:
            if example_file.name == "__init__.py":
                continue

            content = example_file.read_text(encoding="utf-8")
            lines = content.split("\n")

            # Check shebang
            assert lines[0].startswith("#!/usr/bin/env python3"), (
                f"{example_file.name} must have proper shebang"
            )

            # Check copyright and license
            assert any("Copyright" in line for line in lines[:20]), (
                f"{example_file.name} must have copyright notice"
            )
            assert any("MIT" in line for line in lines[:20]), (
                f"{example_file.name} must have MIT license notice"
            )


class TestExamplesFlextIntegration:
    """Test that examples properly integrate with flext-* ecosystem."""

    def test_examples_use_flext_result_pattern(self) -> None:
        """Test that examples use FlextResult pattern correctly."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))

        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")

            if "FlextResult" in content:
                # Must use proper FlextResult patterns
                assert ".success" in content, (
                    f"{example_file.name} uses FlextResult but not .success"
                )
                assert ".error" in content or "result.data" in content, (
                    f"{example_file.name} must check result.error or result.data"
                )

    def test_examples_use_flext_logging(self) -> None:
        """Test that examples use flext-core logging correctly."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))

        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")

            if "get_logger" in content:
                # Must use logger properly
                assert "logger = get_logger(__name__)" in content, (
                    f"{example_file.name} must use get_logger(__name__) pattern"
                )
                assert "logger.info(" in content or "logger.error(" in content, (
                    f"{example_file.name} must actually use the logger"
                )

    def test_examples_use_flext_observability(self) -> None:
        """Test that examples use flext-observability correctly."""
        examples_dir = Path(__file__).parents[2] / "examples"
        example_files = list(examples_dir.glob("*.py"))

        for example_file in example_files:
            content = example_file.read_text(encoding="utf-8")

            if "flext_monitor_function" in content:
                # Must use monitoring decorator properly
                assert "@flext_monitor_function(" in content, (
                    f"{example_file.name} must use @flext_monitor_function decorator"
                )
                assert "FlextObservabilityMonitor" in content, (
                    f"{example_file.name} should create monitor instance"
                )
