"""Tests for FlextTargetFactory, FlextTargetMonitoringFactory, and convenience functions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from flext_target_oracle_wms import m
from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)

_PATCH_TARGET = "flext_target_oracle_wms.factory.FlextTargetOracleWms"


class TestTargetCreationRequest:
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


class TestMonitoredTargetCreationRequest:
    """Tests for MonitoredTargetCreationRequest dataclass."""

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


class TestFlextTargetFactory:
    """Tests for FlextTargetFactory."""

    def test_presets_contain_expected_keys(self) -> None:
        assert set(FlextTargetFactory.PRESETS.keys()) == {
            "development",
            "production",
            "testing",
        }

    @patch(_PATCH_TARGET)
    def test_create_target_success(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        result = FlextTargetFactory.create_target(req)
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_target_with_preset(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            preset="testing",
            additional_config=None,
        )
        result = FlextTargetFactory.create_target(req)
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_target_with_additional_config(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config={"custom_key": "custom_value"},
        )
        result = FlextTargetFactory.create_target(req)
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_from_config_dict_success(self, _mock_cls: MagicMock) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "username": "u",
            "password": "p",
        })
        assert result.is_success

    def test_create_from_config_dict_missing_base_url(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "username": "u",
            "password": "p",
        })
        assert result.is_failure
        assert result.error is not None
        assert "base_url" in result.error

    def test_create_from_config_dict_missing_username(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "password": "p",
        })
        assert result.is_failure
        assert result.error is not None
        assert "username" in result.error

    def test_create_from_config_dict_missing_password(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "username": "u",
        })
        assert result.is_failure
        assert result.error is not None
        assert "password" in result.error


class TestFlextTargetMonitoringFactory:
    """Tests for FlextTargetMonitoringFactory."""

    def test_default_monitor_name(self) -> None:
        factory = FlextTargetMonitoringFactory()
        assert factory.monitor_name == "oracle_wms_target"

    def test_custom_monitor_name(self) -> None:
        factory = FlextTargetMonitoringFactory(monitor_name="custom")
        assert factory.monitor_name == "custom"

    @patch(_PATCH_TARGET)
    def test_create_monitored_target_success(self, _mock_cls: MagicMock) -> None:
        factory = FlextTargetMonitoringFactory()
        req = m.TargetOracleWms.MonitoredTargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        result = factory.create_monitored_target(req)
        assert result.is_success


class TestConvenienceFunctions:
    """Tests for module-level convenience functions."""

    @patch(_PATCH_TARGET)
    def test_create_oracle_wms_target(self, _mock_cls: MagicMock) -> None:
        result = create_oracle_wms_target(
            base_url="https://x",
            username="u",
            password="p",
        )
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_oracle_wms_target_with_preset(self, _mock_cls: MagicMock) -> None:
        result = create_oracle_wms_target(
            base_url="https://x",
            username="u",
            password="p",
            preset="production",
        )
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_monitored_oracle_wms_target(self, _mock_cls: MagicMock) -> None:
        req = m.TargetOracleWms.MonitoredTargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config=None,
        )
        result = create_monitored_oracle_wms_target(req)
        assert result.is_success
