"""Quality and structural validation tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import c as meltano_c
from flext_tests import tm

from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
from tests import c, m, p, u


class TestsFlextTargetOracleWmsQuality:
    """Verify m.* namespace access."""

    @staticmethod
    def test_m_is_models_class() -> None:
        """Test m is models class."""
        tm.that(m, none=False)

    @staticmethod
    def test_target_oracle_wms_namespace_exists() -> None:
        """Test target oracle wms namespace exists."""
        tm.that(m.TargetOracleWms, none=False)

    @staticmethod
    def test_wms_target_config_accessible() -> None:
        """Test wms target config accessible."""
        tm.that(m.TargetOracleWms.WmsTargetConfig, none=False)

    @staticmethod
    def test_wms_authentication_config_accessible() -> None:
        """Test wms authentication config accessible."""
        tm.that(m.TargetOracleWms.WmsAuthenticationConfig, none=False)

    @staticmethod
    def test_singer_field_schema_accessible() -> None:
        """Test singer field schema accessible."""
        tm.that(m.TargetOracleWms.SingerFieldSchema, none=False)

    @staticmethod
    def test_singer_schema_properties_accessible() -> None:
        """Test singer schema properties accessible."""
        tm.that(m.TargetOracleWms.SingerSchemaProperties, none=False)

    @staticmethod
    def test_meltano_namespace_inherited() -> None:
        """Test meltano namespace inherited."""
        tm.that(m.Meltano, none=False)

    @staticmethod
    def test_oracle_wms_namespace_inherited() -> None:
        """Test oracle wms namespace inherited."""
        tm.that(m.OracleWms, none=False)

    @staticmethod
    def test_c_is_constants_class() -> None:
        """Test c is constants class."""
        tm.that(c, none=False)

    @staticmethod
    def test_load_methods_accessible() -> None:
        """Test load methods accessible."""
        tm.that(c.TargetOracleWms.LoadMethods.Method.APPEND_ONLY, eq="APPEND_ONLY")
        tm.that(c.TargetOracleWms.LoadMethods.Method.UPSERT, eq="UPSERT")

    @staticmethod
    def test_oracle_wms_defaults_derive_from_meltano_ssot() -> None:
        """Target defaults mirror the flext-meltano constants SSOT they derive from."""
        tm.that(
            c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE,
            eq=meltano_c.Meltano.BATCH_DEFAULT_DEFAULT_BATCH_SIZE,
        )

    @staticmethod
    def test_p_is_protocols_class() -> None:
        """Test p is protocols class."""
        tm.that(p, none=False)

    @staticmethod
    def test_target_name() -> None:
        """Test target name."""
        tm.that(u.TargetOracleWms.Target.name, eq=c.TargetOracleWms.TARGET_NAME)

    @staticmethod
    def test_cli_defaults() -> None:
        """Test cli defaults."""
        cli = FlextTargetOracleWmsCli()
        tm.that(cli.name, eq=c.TargetOracleWms.TARGET_NAME)
        assert cli.version

    @staticmethod
    def test_catalog_manager_instantiates() -> None:
        """Test catalog manager instantiates."""
        mgr = u.TargetOracleWms.CatalogManager()
        tm.that(mgr, is_=u.TargetOracleWms.CatalogManager)

    @staticmethod
    def test_table_manager_instantiates() -> None:
        """Test table manager instantiates."""
        manager = u.TargetOracleWms.WMSTableManager()
        tm.that(manager, is_=u.TargetOracleWms.WMSTableManager)

    @staticmethod
    def test_type_converter_instantiates() -> None:
        """Test type converter instantiates."""
        tc = u.TargetOracleWms.WMSTypeConverter()
        tm.that(tc, is_=u.TargetOracleWms.WMSTypeConverter)

    @staticmethod
    def test_data_transformer_instantiates() -> None:
        """Test data transformer instantiates."""
        dt = u.TargetOracleWms.WMSDataTransformer()
        tm.that(dt, is_=u.TargetOracleWms.WMSDataTransformer)
