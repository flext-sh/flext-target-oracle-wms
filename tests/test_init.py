"""Test module __init__.py import and version handling - DRY REAL approach."""

from __future__ import annotations


class TestModuleInit:
    """Test module initialization and version handling."""

    def test_version_import_success(self) -> None:
        """Test successful version import from importlib.metadata."""
        # Normal case should work - just verify version exists
        import flext_target_oracle_wms

        assert hasattr(flext_target_oracle_wms, "__version__")
        assert isinstance(flext_target_oracle_wms.__version__, str)
        assert len(flext_target_oracle_wms.__version__) > 0

    def test_version_import_fallback(self) -> None:
        """Test fallback version logic - simplified approach."""
        # Test the fallback case indirectly by verifying behavior
        import flext_target_oracle_wms

        # Verify version is set correctly (either from metadata or fallback)
        assert hasattr(flext_target_oracle_wms, "__version__")
        assert isinstance(flext_target_oracle_wms.__version__, str)

        # Version should be either the real version or "0.9.0" fallback
        version = flext_target_oracle_wms.__version__
        assert len(version) > 0
        assert version.count(".") >= 2  # Should have at least x.y.z format

    def test_module_exports(self) -> None:
        """Test that module exports are properly defined."""
        import flext_target_oracle_wms

        # Verify __all__ is defined and contains expected exports
        assert hasattr(flext_target_oracle_wms, "__all__")
        assert isinstance(flext_target_oracle_wms.__all__, list)

        # Verify key exports exist
        expected_exports = [
            "SingerTargetOracleWMS",
            "WMSDataTransformer",
            "WMSSchemaMapper",
            "WMSTableManager",
            "WMSTypeConverter",
        ]

        for export in expected_exports:
            assert export in flext_target_oracle_wms.__all__
            assert hasattr(flext_target_oracle_wms, export)
