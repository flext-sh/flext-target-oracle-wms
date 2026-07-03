"""Tests for FlextTargetFactory, FlextTargetMonitoringFactory, and convenience functions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from flext_target_oracle_wms._constants import factory as target_factory_constants
from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
)
from tests.constants import c
from tests.models import m


class TestsFlextTargetOracleWmsOracleWmsFactory:
    """Tests for TargetCreationRequest dataclass."""

    def test_required_fields(self) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        assert req.base_url == "https://x"
        assert req.environment == "development"
        assert req.preset is None
        assert req.additional_config is None

    def test_custom_environment(self) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            environment="production",
            additional_config=None,
        )
        assert req.environment == "production"

    def test_default_monitor_name(self) -> None:
        req = m.TargetOracleWms.MonitoredTargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        assert req.monitor_name == "oracle_wms_target"

    def test_custom_monitor_name(self) -> None:
        req = m.TargetOracleWms.MonitoredTargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            monitor_name="custom",
            additional_config=None,
        )
        assert req.monitor_name == "custom"

    def test_presets_contain_expected_keys(self) -> None:
        assert set(target_factory_constants.PRESETS.keys()) == {
            "development",
            "production",
            "testing",
        }

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_target_success(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        result = FlextTargetFactory.create_target(req)
        assert result.success

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_target_with_preset(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            preset="testing",
            additional_config=None,
        )
        result = FlextTargetFactory.create_target(req)
        assert result.success

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_target_with_additional_config(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config={"custom_key": "custom_value"},
        )
        result = FlextTargetFactory.create_target(req)
        assert result.success

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_from_config_dict_success(self, _mock_cls: MagicMock) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "username": "u",
            "password": "p",
        })
        assert result.success

    def test_create_from_config_dict_missing_base_url(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "username": "u",
            "password": "p",
        })
        assert result.failure
        assert result.error is not None
        assert "base_url" in result.error

    def test_create_from_config_dict_missing_username(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "password": "p",
        })
        assert result.failure
        assert result.error is not None
        assert "username" in result.error

    def test_create_from_config_dict_missing_password(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "username": "u",
        })
        assert result.failure
        assert result.error is not None
        assert "password" in result.error

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_monitored_target_success(self, _mock_cls: MagicMock) -> None:
        factory = FlextTargetMonitoringFactory()
        req = m.TargetOracleWms.MonitoredTargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        result = factory.create_monitored_target(req)
        assert result.success

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_oracle_wms_target(self, _mock_cls: MagicMock) -> None:
        result = FlextTargetMonitoringFactory.create_oracle_wms_target(
            base_url="https://x",
            username="u",
            password="p",
        )
        assert result.success

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_oracle_wms_target_with_preset(self, _mock_cls: MagicMock) -> None:
        result = FlextTargetMonitoringFactory.create_oracle_wms_target(
            base_url="https://x",
            username="u",
            password="p",
            preset="production",
        )
        assert result.success

    @patch(c.TargetOracleWms.Tests.PATCH_TARGET)
    def test_create_monitored_oracle_wms_target(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.MonitoredTargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        result = FlextTargetMonitoringFactory.create_monitored_oracle_wms_target(req)
        assert result.success
