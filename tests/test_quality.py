"""Quality and structural validation tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_wms import (
    FlextTargetOracleWms,
    FlextTargetOracleWmsCatalogManager,
    FlextTargetOracleWmsCli,
    FlextTargetOracleWmsModels,
    FlextTargetOracleWmsProtocols,
    m,
    p,
    u,
)
from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants, c


class TestModelsNamespace:
    """Verify m.* namespace access."""

    def test_m_is_models_class(self) -> None:
        assert m is FlextTargetOracleWmsModels

    def test_target_oracle_wms_namespace_exists(self) -> None:
        assert hasattr(m, "TargetOracleWms")

    def test_wms_target_config_accessible(self) -> None:
        assert hasattr(m.TargetOracleWms, "WmsTargetConfig")

    def test_wms_authentication_config_accessible(self) -> None:
        assert hasattr(m.TargetOracleWms, "WmsAuthenticationConfig")

    def test_wms_target_result_accessible(self) -> None:
        assert hasattr(m.TargetOracleWms, "WmsTargetResult")

    def test_singer_field_schema_accessible(self) -> None:
        assert hasattr(m.TargetOracleWms, "SingerFieldSchema")

    def test_singer_schema_properties_accessible(self) -> None:
        assert hasattr(m.TargetOracleWms, "SingerSchemaProperties")

    def test_meltano_namespace_inherited(self) -> None:
        assert hasattr(m, "Meltano")
        assert hasattr(m.Meltano, "SingerSchemaMessage")
        assert hasattr(m.Meltano, "SingerRecordMessage")
        assert hasattr(m.Meltano, "SingerStateMessage")
        assert hasattr(m.Meltano, "SingerCatalogEntry")

    def test_oracle_wms_namespace_inherited(self) -> None:
        assert hasattr(m, "OracleWms")


class TestConstantsNamespace:
    """Verify c.* namespace access."""

    def test_c_is_constants_class(self) -> None:
        assert c is FlextTargetOracleWmsConstants

    def test_load_methods_accessible(self) -> None:
        assert c.TargetOracleWms.LoadMethods.APPEND_ONLY == "APPEND_ONLY"
        assert c.TargetOracleWms.LoadMethods.UPSERT == "UPSERT"

    def test_valid_load_methods_is_set(self) -> None:
        assert "APPEND_ONLY" in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS
        assert "MERGE" in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS

    def test_oracle_wms_defaults(self) -> None:
        assert c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE > 0
        assert c.TargetOracleWms.OracleWms.DEFAULT_TIMEOUT > 0


class TestProtocolsNamespace:
    """Verify p.* namespace access."""

    def test_p_is_protocols_class(self) -> None:
        assert p is FlextTargetOracleWmsProtocols

    def test_data_loading_protocol_exists(self) -> None:
        assert hasattr(p.TargetOracleWms, "WmsDataLoading")

    def test_data_transformation_protocol_exists(self) -> None:
        assert hasattr(p.TargetOracleWms, "DataTransformation")


class TestClassAttributes:
    """Verify class attributes and defaults."""

    def test_target_name(self) -> None:
        assert FlextTargetOracleWms.name == "target-oracle-wms"

    def test_cli_defaults(self) -> None:
        cli = FlextTargetOracleWmsCli()
        assert cli.name == "target-oracle-wms"
        assert cli.version == "0.9.0"

    def test_catalog_manager_instantiates(self) -> None:
        mgr = FlextTargetOracleWmsCatalogManager()
        assert mgr is not None

    def test_table_manager_instantiates(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        assert tm is not None

    def test_type_converter_instantiates(self) -> None:
        tc = u.TargetOracleWms.WMSTypeConverter()
        assert tc is not None

    def test_data_transformer_instantiates(self) -> None:
        dt = u.TargetOracleWms.WMSDataTransformer()
        assert dt is not None

    def test_schema_mapper_instantiates(self) -> None:
        sm = u.TargetOracleWms.WMSSchemaMapper()
        assert sm is not None
