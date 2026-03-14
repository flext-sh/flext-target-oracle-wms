"""Tests for FlextTargetFactory, FlextTargetMonitoringFactory, and convenience functions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import patch

from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    MonitoredTargetCreationRequest,
    TargetCreationRequest,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)

_PATCH_TARGET = "flext_target_oracle_wms.factory.SingerTargetOracleWMS"


class TestTargetCreationRequest:
    """Tests for TargetCreationRequest dataclass."""

    def test_required_fields(self) -> None:
        req = TargetCreationRequest(base_url="https://x", username="u", password="p")
        assert req.base_url == "https://x"
        assert req.environment == "development"
        assert req.preset is None
        assert req.additional_config is None

    def test_custom_environment(self) -> None:
        req = TargetCreationRequest(
            base_url="https://x", username="u", password="p", environment="production"
        )
        assert req.environment == "production"


class TestMonitoredTargetCreationRequest:
    """Tests for MonitoredTargetCreationRequest dataclass."""

    def test_default_monitor_name(self) -> None:
        req = MonitoredTargetCreationRequest(
            base_url="https://x", username="u", password="p"
        )
        assert req.monitor_name == "oracle_wms_target"

    def test_custom_monitor_name(self) -> None:
        req = MonitoredTargetCreationRequest(
            base_url="https://x", username="u", password="p", monitor_name="custom"
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
    def test_create_target_success(self, mock_cls) -> None:
        req = TargetCreationRequest(base_url="https://x", username="u", password="p")
        result = FlextTargetFactory.create_target(req)
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_target_with_preset(self, mock_cls) -> None:
        req = TargetCreationRequest(
            base_url="https://x", username="u", password="p", preset="testing"
        )
        result = FlextTargetFactory.create_target(req)
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_target_with_additional_config(self, mock_cls) -> None:
        req = TargetCreationRequest(
            base_url="https://x",
            username="u",
            password="p",
            additional_config={"custom_key": "custom_value"},
        )
        result = FlextTargetFactory.create_target(req)
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_from_config_dict_success(self, mock_cls) -> None:
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
        assert "base_url" in (result.error or "")

    def test_create_from_config_dict_missing_username(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "password": "p",
        })
        assert result.is_failure
        assert "username" in (result.error or "")

    def test_create_from_config_dict_missing_password(self) -> None:
        result = FlextTargetFactory.create_from_config_dict({
            "base_url": "https://x",
            "username": "u",
        })
        assert result.is_failure
        assert "password" in (result.error or "")


class TestFlextTargetMonitoringFactory:
    """Tests for FlextTargetMonitoringFactory."""

    def test_default_monitor_name(self) -> None:
        factory = FlextTargetMonitoringFactory()
        assert factory.monitor_name == "oracle_wms_target"

    def test_custom_monitor_name(self) -> None:
        factory = FlextTargetMonitoringFactory(monitor_name="custom")
        assert factory.monitor_name == "custom"

    @patch(_PATCH_TARGET)
    def test_create_monitored_target_success(self, mock_cls) -> None:
        factory = FlextTargetMonitoringFactory()
        req = MonitoredTargetCreationRequest(
            base_url="https://x", username="u", password="p"
        )
        result = factory.create_monitored_target(req)
        assert result.is_success


class TestConvenienceFunctions:
    """Tests for module-level convenience functions."""

    @patch(_PATCH_TARGET)
    def test_create_oracle_wms_target(self, mock_cls) -> None:
        result = create_oracle_wms_target(
            base_url="https://x", username="u", password="p"
        )
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_oracle_wms_target_with_preset(self, mock_cls) -> None:
        result = create_oracle_wms_target(
            base_url="https://x", username="u", password="p", preset="production"
        )
        assert result.is_success

    @patch(_PATCH_TARGET)
    def test_create_monitored_oracle_wms_target(self, mock_cls) -> None:
        req = MonitoredTargetCreationRequest(
            base_url="https://x", username="u", password="p"
        )
        result = create_monitored_oracle_wms_target(req)
        assert result.is_success
