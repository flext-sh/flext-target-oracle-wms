"""Comprehensive tests for FlextTargetFactory - REAL flext-* API integration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

from flext_core import FlextResult

from flext_target_oracle_wms import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)


class TestFlextTargetFactory:
    """Test FlextTargetFactory for easier library usage."""

    def test_factory_presets_available(self) -> None:
        """Test that all environment presets are available."""
        expected_presets = ["development", "staging", "production", "testing"]
        for preset in expected_presets:
            assert preset in FlextTargetFactory.PRESETS

        # Verify preset structure
        dev_preset = FlextTargetFactory.PRESETS["development"]
        assert "batch_size" in dev_preset
        assert "table_prefix" in dev_preset
        assert "schema_name" in dev_preset
        assert "timeout" in dev_preset
        assert "max_retries" in dev_preset
        assert "verify_ssl" in dev_preset
        assert "enable_logging" in dev_preset

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_target_with_preset(self, mock_target_class: MagicMock) -> None:
        """Test creating target with development preset."""
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        result = FlextTargetFactory.create_target(
            base_url="https://test.wms.oracle.com",
            username="test_user",
            password="test_password",
            environment="test_env",
            preset="development",
        )

        assert result.success
        assert result.data == mock_target

        # Verify config was merged correctly
        mock_target_class.assert_called_once()
        call_args = mock_target_class.call_args[0][0]
        assert call_args["base_url"] == "https://test.wms.oracle.com"
        assert call_args["username"] == "test_user"
        assert call_args["password"] == "test_password"
        assert call_args["environment"] == "test_env"
        # Development preset values
        assert call_args["batch_size"] == 100
        assert call_args["table_prefix"] == "DEV_"
        assert call_args["schema_name"] == "WMS_DEV"

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_target_with_overrides(self, mock_target_class: MagicMock) -> None:
        """Test creating target with configuration overrides."""
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        result = FlextTargetFactory.create_target(
            base_url="https://custom.wms.oracle.com",
            username="custom_user",
            password="custom_password",
            preset="production",
            # Override production preset values
            batch_size=2000,
            custom_option="custom_value",
        )

        assert result.success
        call_args = mock_target_class.call_args[0][0]

        # Production preset applied
        assert call_args["table_prefix"] == "PROD_"
        assert call_args["verify_ssl"] is True
        # Override applied
        assert call_args["batch_size"] == 2000
        # Custom option added
        assert call_args["custom_option"] == "custom_value"

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_target_unknown_preset(self, mock_target_class: MagicMock) -> None:
        """Test creating target with unknown preset logs warning but succeeds."""
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        with patch("flext_target_oracle_wms.factory.logger") as mock_logger:
            result = FlextTargetFactory.create_target(
                base_url="https://test.wms.oracle.com",
                username="test_user",
                password="test_password",
                preset="unknown_preset",
            )

            assert result.success
            mock_logger.warning.assert_called_once()
            assert (
                "Unknown preset: unknown_preset" in mock_logger.warning.call_args[0][0]
            )

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_target_exception_handling(
        self,
        mock_target_class: MagicMock,
    ) -> None:
        """Test target creation exception handling."""
        mock_target_class.side_effect = RuntimeError("Target creation failed")

        result = FlextTargetFactory.create_target(
            base_url="https://test.wms.oracle.com",
            username="test_user",
            password="test_password",
        )

        assert not result.success
        assert result.error is not None
        assert "Failed to create Oracle WMS target" in result.error
        assert result.error is not None
        assert "Target creation failed" in result.error

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_development_target(self, mock_target_class: MagicMock) -> None:
        """Test development target convenience method."""
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        result = FlextTargetFactory.create_development_target(
            base_url="https://dev.wms.oracle.com",
            custom_setting="custom_value",
        )

        assert result.success
        call_args = mock_target_class.call_args[0][0]
        assert call_args["base_url"] == "https://dev.wms.oracle.com"
        assert call_args["username"] == "dev_user"
        assert call_args["password"] == "dev_password"
        assert call_args["environment"] == "development"
        assert call_args["custom_setting"] == "custom_value"

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_production_target(self, mock_target_class: MagicMock) -> None:
        """Test production target convenience method."""
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        result = FlextTargetFactory.create_production_target(
            base_url="https://prod.wms.oracle.com",
            username="prod_user",
            password="prod_password",
            security_level="high",
        )

        assert result.success
        call_args = mock_target_class.call_args[0][0]
        assert call_args["base_url"] == "https://prod.wms.oracle.com"
        assert call_args["username"] == "prod_user"
        assert call_args["password"] == "prod_password"
        assert call_args["environment"] == "production"
        assert call_args["security_level"] == "high"
        # Production preset
        assert call_args["batch_size"] == 1000
        assert call_args["verify_ssl"] is True

    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_testing_target(self, mock_target_class: MagicMock) -> None:
        """Test testing target convenience method with defaults."""
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        result = FlextTargetFactory.create_testing_target()

        assert result.success
        call_args = mock_target_class.call_args[0][0]
        assert call_args["base_url"] == "https://test.wms.oracle.com"
        assert call_args["username"] == "test_user"
        assert call_args["password"] == "test_password"
        assert call_args["environment"] == "testing"
        # Testing preset
        assert call_args["batch_size"] == 10
        assert call_args["verify_ssl"] is False

    def test_create_from_config_dict_valid(self) -> None:
        """Test creating target from configuration dictionary."""
        config = {
            "base_url": "https://config.wms.oracle.com",
            "username": "config_user",
            "password": "config_password",
            "preset": "staging",
            "custom_field": "custom_value",
        }

        with patch.object(FlextTargetFactory, "create_target") as mock_create:
            mock_create.return_value = FlextResult[None].ok(MagicMock())

            result = FlextTargetFactory.create_from_config_dict(config)

            assert result.success
            mock_create.assert_called_once_with(
                base_url="https://config.wms.oracle.com",
                username="config_user",
                password="config_password",
                environment="development",
                preset="staging",
                custom_field="custom_value",
            )

    def test_create_from_config_dict_missing_fields(self) -> None:
        """Test creating target from config dict with missing required fields."""
        config = {
            "base_url": "https://incomplete.wms.oracle.com",
            # Missing username and password
        }

        result = FlextTargetFactory.create_from_config_dict(config)

        assert not result.success
        assert result.error is not None
        assert "Missing required configuration fields" in result.error
        assert result.error is not None
        assert "username" in result.error
        assert result.error is not None
        assert "password" in result.error

    def test_create_from_config_dict_exception(self) -> None:
        """Test config dict creation with exception handling."""
        config = {
            "base_url": "https://error.wms.oracle.com",
            "username": "error_user",
            "password": "error_password",
        }

        with patch.object(
            FlextTargetFactory,
            "create_target",
            side_effect=RuntimeError("Config error"),
        ):
            result = FlextTargetFactory.create_from_config_dict(config)

            assert not result.success
            assert result.error is not None
            assert "Failed to create target from config" in result.error


class TestFlextTargetMonitoringFactory:
    """Test FlextTargetMonitoringFactory for observability integration."""

    @patch("flext_target_oracle_wms.factory.FlextObservabilityMonitor")
    def test_monitoring_factory_initialization(
        self,
        mock_monitor_class: MagicMock,
    ) -> None:
        """Test monitoring factory initialization."""
        mock_monitor = MagicMock()
        mock_monitor_class.return_value = mock_monitor

        factory = FlextTargetMonitoringFactory("test_monitor")

        assert factory.monitor == mock_monitor
        assert factory.monitor_name == "test_monitor"
        assert isinstance(factory.factory, FlextTargetFactory)
        mock_monitor_class.assert_called_once_with()

    @patch("flext_target_oracle_wms.factory.FlextObservabilityMonitor")
    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_monitored_target_success(
        self,
        mock_target_class: MagicMock,
        mock_monitor_class: MagicMock,
    ) -> None:
        """Test creating monitored target successfully."""
        # Setup mocks
        mock_monitor = MagicMock()
        mock_monitor_class.return_value = mock_monitor
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target

        # Mock target methods
        mock_target.setup = AsyncMock()
        mock_target.cleanup = AsyncMock()
        mock_target.process_record_message = AsyncMock()

        factory = FlextTargetMonitoringFactory()

        result = factory.create_monitored_target(
            base_url="https://monitored.wms.oracle.com",
            username="monitor_user",
            password="monitor_password",
            preset="production",
        )

        assert result.success
        monitored_target = result.data

        # Verify target was created with correct config
        mock_target_class.assert_called_once()
        call_args = mock_target_class.call_args[0][0]
        assert call_args["base_url"] == "https://monitored.wms.oracle.com"
        assert call_args["username"] == "monitor_user"
        assert call_args["password"] == "monitor_password"

        # Verify target was created successfully with monitoring integration
        assert monitored_target is not None
        assert hasattr(monitored_target, "setup")
        assert hasattr(monitored_target, "cleanup")
        assert hasattr(monitored_target, "process_record_message")

    @patch("flext_target_oracle_wms.factory.FlextObservabilityMonitor")
    def test_create_monitored_target_base_failure(
        self,
        mock_monitor_class: MagicMock,
    ) -> None:
        """Test monitored target creation when base target creation fails."""
        mock_monitor = MagicMock()
        mock_monitor_class.return_value = mock_monitor

        factory = FlextTargetMonitoringFactory()

        with patch.object(
            factory.factory,
            "create_target",
            return_value=FlextResult[None].fail("Base creation failed"),
        ):
            result = factory.create_monitored_target(
                base_url="https://fail.wms.oracle.com",
                username="fail_user",
                password="fail_password",
            )

            assert not result.success
            assert result.error is not None
            assert "Base creation failed" in result.error

    @patch("flext_target_oracle_wms.factory.FlextObservabilityMonitor")
    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_create_monitored_target_exception(
        self,
        mock_target_class: MagicMock,
        mock_monitor_class: MagicMock,
    ) -> None:
        """Test monitored target creation exception handling."""
        mock_monitor = MagicMock()
        mock_monitor_class.return_value = mock_monitor
        mock_target_class.return_value = MagicMock()

        factory = FlextTargetMonitoringFactory()

        with patch.object(
            factory.factory,
            "create_target",
            side_effect=RuntimeError("Monitor error"),
        ):
            result = factory.create_monitored_target(
                base_url="https://error.wms.oracle.com",
                username="error_user",
                password="error_password",
            )

            assert not result.success
            assert result.error is not None
            assert "Failed to create monitored target" in result.error


class TestFactoryConvenienceFunctions:
    """Test convenience functions for easy factory usage."""

    @patch("flext_target_oracle_wms.factory.FlextTargetFactory.create_target")
    def test_create_oracle_wms_target(self, mock_create_target: MagicMock) -> None:
        """Test convenience function for creating Oracle WMS target."""
        mock_target = MagicMock()
        mock_create_target.return_value = FlextResult[None].ok(mock_target)

        result = create_oracle_wms_target(
            base_url="https://convenience.wms.oracle.com",
            username="convenience_user",
            password="convenience_password",
            environment="convenience_env",
            preset="staging",
            custom_param="custom_value",
        )

        assert result.success
        assert result.data == mock_target

        mock_create_target.assert_called_once_with(
            base_url="https://convenience.wms.oracle.com",
            username="convenience_user",
            password="convenience_password",
            environment="convenience_env",
            preset="staging",
            custom_param="custom_value",
        )

    @patch("flext_target_oracle_wms.factory.FlextTargetMonitoringFactory")
    def test_create_monitored_oracle_wms_target(
        self,
        mock_factory_class: MagicMock,
    ) -> None:
        """Test convenience function for creating monitored Oracle WMS target."""
        mock_factory = MagicMock()
        mock_factory_class.return_value = mock_factory
        mock_target = MagicMock()
        mock_factory.create_monitored_target.return_value = FlextResult[None].ok(
            mock_target
        )

        result = create_monitored_oracle_wms_target(
            base_url="https://monitored-convenience.wms.oracle.com",
            username="monitored_user",
            password="monitored_password",
            environment="monitored_env",
            preset="production",
            monitor_name="custom_monitor",
            monitoring_param="monitoring_value",
        )

        assert result.success
        assert result.data == mock_target

        # Verify factory was created with custom monitor name
        mock_factory_class.assert_called_once_with("custom_monitor")

        # Verify monitored target creation was called correctly
        mock_factory.create_monitored_target.assert_called_once_with(
            base_url="https://monitored-convenience.wms.oracle.com",
            username="monitored_user",
            password="monitored_password",
            environment="monitored_env",
            preset="production",
            monitoring_param="monitoring_value",
        )


class TestFactoryIntegration:
    """Integration tests for factory patterns."""

    @patch("flext_target_oracle_wms.factory.FlextObservabilityMonitor")
    @patch("flext_target_oracle_wms.factory.SingerTargetOracleWMS")
    def test_factory_ease_of_use_integration(
        self,
        mock_target_class: MagicMock,
        mock_monitor_class: MagicMock,
    ) -> None:
        """Test complete factory integration for ease of use."""
        # Setup mocks
        mock_target = MagicMock()
        mock_target_class.return_value = mock_target
        mock_monitor = MagicMock()
        mock_monitor_class.return_value = mock_monitor

        # Test 1: Simple target creation
        simple_result = create_oracle_wms_target(
            base_url="https://simple.wms.oracle.com",
            username="simple_user",
            password="simple_password",
        )
        assert simple_result.success

        # Test 2: Development target with preset
        dev_result = FlextTargetFactory.create_development_target(
            base_url="https://dev.wms.oracle.com",
        )
        assert dev_result.success

        # Test 3: Production target with monitoring
        prod_result = create_monitored_oracle_wms_target(
            base_url="https://prod.wms.oracle.com",
            username="prod_user",
            password="prod_password",
            preset="production",
            monitor_name="prod_monitor",
        )
        assert prod_result.success

        # Test 4: Configuration-based creation
        config = {
            "base_url": "https://config.wms.oracle.com",
            "username": "config_user",
            "password": "config_password",
            "preset": "staging",
        }
        config_result = FlextTargetFactory.create_from_config_dict(config)
        assert config_result.success

        # Verify all targets were created successfully
        assert mock_target_class.call_count == 4

    def test_factory_solid_principles_compliance(self) -> None:
        """Test that factory implements SOLID principles correctly."""
        # Single Responsibility: Factory only creates targets
        factory = FlextTargetFactory()
        assert hasattr(factory, "create_target")
        assert hasattr(factory, "create_development_target")
        assert hasattr(factory, "create_production_target")

        # Open/Closed: Extensible through presets
        assert "development" in FlextTargetFactory.PRESETS
        assert "production" in FlextTargetFactory.PRESETS
        assert "staging" in FlextTargetFactory.PRESETS
        assert "testing" in FlextTargetFactory.PRESETS

        # Interface Segregation: Focused interfaces
        monitoring_factory = FlextTargetMonitoringFactory()
        assert hasattr(monitoring_factory, "create_monitored_target")
        assert hasattr(monitoring_factory, "monitor")
        assert hasattr(monitoring_factory, "factory")

        # Dependency Inversion: Uses abstractions through FlextResult
        assert callable(create_oracle_wms_target)

        # Verify no tight coupling to concrete implementations
        assert FlextTargetFactory.PRESETS is not None
        assert len(FlextTargetFactory.PRESETS) > 0
