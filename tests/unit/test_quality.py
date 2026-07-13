"""Quality and structural validation tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import tm

from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
from tests import c, m, p, u


class TestsFlextTargetOracleWmsQuality:
    """Verify m.* namespace access."""

    def test_m_is_models_class(self) -> None:
        tm.that(m, none=False)

    def test_target_oracle_wms_namespace_exists(self) -> None:
        tm.that(m.TargetOracleWms, none=False)

    def test_wms_target_config_accessible(self) -> None:
        tm.that(m.TargetOracleWms.WmsTargetConfig, none=False)

    def test_wms_authentication_config_accessible(self) -> None:
        tm.that(m.TargetOracleWms.WmsAuthenticationConfig, none=False)

    def test_singer_field_schema_accessible(self) -> None:
        tm.that(m.TargetOracleWms.SingerFieldSchema, none=False)

    def test_singer_schema_properties_accessible(self) -> None:
        tm.that(m.TargetOracleWms.SingerSchemaProperties, none=False)

    def test_meltano_namespace_inherited(self) -> None:
        tm.that(m.Meltano, none=False)

    def test_oracle_wms_namespace_inherited(self) -> None:
        tm.that(m.OracleWms, none=False)

    def test_c_is_constants_class(self) -> None:
        tm.that(c, none=False)

    def test_load_methods_accessible(self) -> None:
        tm.that(c.TargetOracleWms.LoadMethods.Method.APPEND_ONLY, eq="APPEND_ONLY")
        tm.that(c.TargetOracleWms.LoadMethods.Method.UPSERT, eq="UPSERT")

    def test_valid_load_methods_is_set(self) -> None:
        tm.that(c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS, has="APPEND_ONLY")
        tm.that(c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS, has="MERGE")

    def test_oracle_wms_defaults(self) -> None:
        assert c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE > 0
        assert c.TargetOracleWms.OracleWms.DEFAULT_TIMEOUT > 0

    def test_p_is_protocols_class(self) -> None:
        tm.that(p, none=False)

    def test_wms_data_loading_protocol_exists(self) -> None:
        tm.that(p.TargetOracleWms.WmsDataLoading, none=False)

    def test_data_transformation_protocol_exists(self) -> None:
        tm.that(p.TargetOracleWms.DataTransformation, none=False)

    def test_target_creation_request_accessible(self) -> None:
        tm.that(m.TargetOracleWms.TargetCreationRequest, none=False)

    def test_monitored_target_creation_request_accessible(self) -> None:
        tm.that(m.TargetOracleWms.MonitoredTargetCreationRequest, none=False)

    def test_target_name(self) -> None:
        tm.that(u.TargetOracleWms.Target.name, eq="target-oracle-wms")

    def test_cli_defaults(self) -> None:
        cli = FlextTargetOracleWmsCli()
        tm.that(cli.name, eq="target-oracle-wms")
        assert cli.version

    def test_catalog_manager_instantiates(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        tm.that(mgr, none=False)

    def test_table_manager_instantiates(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        tm.that(tm, none=False)

    def test_type_converter_instantiates(self) -> None:
        tc = u.TargetOracleWms.WMSTypeConverter()
        tm.that(tc, none=False)

    def test_data_transformer_instantiates(self) -> None:
        dt = u.TargetOracleWms.WMSDataTransformer()
        tm.that(dt, none=False)

    def test_schema_mapper_instantiates(self) -> None:
        sm = u.TargetOracleWms.WMSSchemaMapper()
        tm.that(sm, none=False)
