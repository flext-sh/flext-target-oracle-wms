"""Quality and structural validation tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
from tests.constants import c
from tests.models import m
from tests.protocols import p
from tests.utilities import u


class TestsFlextTargetOracleWmsQuality:
    """Verify m.* namespace access."""

    def test_m_is_models_class(self) -> None:
        assert m is not None

    def test_target_oracle_wms_namespace_exists(self) -> None:
        assert m.TargetOracleWms is not None

    def test_wms_target_config_accessible(self) -> None:
        assert m.TargetOracleWms.WmsTargetConfig is not None

    def test_wms_authentication_config_accessible(self) -> None:
        assert m.TargetOracleWms.WmsAuthenticationConfig is not None

    def test_singer_field_schema_accessible(self) -> None:
        assert m.TargetOracleWms.SingerFieldSchema is not None

    def test_singer_schema_properties_accessible(self) -> None:
        assert m.TargetOracleWms.SingerSchemaProperties is not None

    def test_meltano_namespace_inherited(self) -> None:
        assert m.Meltano is not None

    def test_oracle_wms_namespace_inherited(self) -> None:
        assert m.OracleWms is not None

    def test_c_is_constants_class(self) -> None:
        assert c is not None

    def test_load_methods_accessible(self) -> None:
        assert c.TargetOracleWms.LoadMethods.Method.APPEND_ONLY == "APPEND_ONLY"
        assert c.TargetOracleWms.LoadMethods.Method.UPSERT == "UPSERT"

    def test_valid_load_methods_is_set(self) -> None:
        assert "APPEND_ONLY" in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS
        assert "MERGE" in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS

    def test_oracle_wms_defaults(self) -> None:
        assert c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE > 0
        assert c.TargetOracleWms.OracleWms.DEFAULT_TIMEOUT > 0

    def test_p_is_protocols_class(self) -> None:
        assert p is not None

    def test_wms_data_loading_protocol_exists(self) -> None:
        assert p.TargetOracleWms.WmsDataLoading is not None

    def test_data_transformation_protocol_exists(self) -> None:
        assert p.TargetOracleWms.DataTransformation is not None

    def test_target_creation_request_accessible(self) -> None:
        assert m.TargetOracleWms.TargetCreationRequest is not None

    def test_monitored_target_creation_request_accessible(self) -> None:
        assert m.TargetOracleWms.MonitoredTargetCreationRequest is not None

    def test_target_name(self) -> None:
        assert u.TargetOracleWms.Target.name == "target-oracle-wms"

    def test_cli_defaults(self) -> None:
        cli = FlextTargetOracleWmsCli()
        assert cli.name == "target-oracle-wms"
        assert cli.version

    def test_catalog_manager_instantiates(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
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
