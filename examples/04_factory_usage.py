#!/usr/bin/env python3
"""Factory usage example - PRODUCTION-ready flext-* library usage.

This example shows how the FlextTargetFactory makes Oracle WMS targets
easier to create and use in REAL production environments, following SOLID
principles and best practices with REAL flext-oracle-wms API integration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import json
import os
from collections.abc import Coroutine
from typing import cast

from flext_core import FlextLogger
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

# Import factory patterns for easier usage
from flext_target_oracle_wms import (
    FlextTargetFactory,
    create_oracle_wms_target,
)

# Get logger using flext-core patterns
logger = FlextLogger(__name__)

# Monitor using flext-observability
monitor = FlextObservabilityMonitor()

# Constants for demo configuration
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD", "demo_password")


async def _demonstrate_simple_target() -> None:
    """Demonstrate simple target creation using convenience function."""
    logger.info("\n📝 Example 1: Simple Target Creation")
    simple_target_result = create_oracle_wms_target(
        base_url="https://simple.wms.oracle.com",
        username="simple_user",
        password=DEMO_PASSWORD,
        environment="demo",
    )

    if simple_target_result.success and simple_target_result.data:
        logger.info("✅ Simple target created successfully")
        simple_target = simple_target_result.data
        logger.info("Target config: %s", simple_target.config)
    else:
        logger.error(
            "❌ Simple target creation failed: %s",
            simple_target_result.error or "Unknown error",
        )


async def _demonstrate_development_target() -> None:
    """Demonstrate development target with preset."""
    logger.info("\n🔧 Example 2: Development Target with Preset")
    dev_target_result = FlextTargetFactory.create_development_target(
        base_url="https://dev.wms.oracle.com",
        # Override some development defaults
        batch_size=50,
        custom_debug_mode=True,
    )

    if dev_target_result.success and dev_target_result.data:
        logger.info("✅ Development target created with optimized settings")
        dev_target = dev_target_result.data
        # Development preset automatically sets dev-friendly options
        logger.info("Batch size: %s", dev_target.config.get("batch_size"))
        logger.info("Table prefix: %s", dev_target.config.get("table_prefix"))
        logger.info("Verify SSL: %s", dev_target.config.get("verify_ssl"))
    else:
        logger.error(
            "❌ Development target creation failed: %s",
            dev_target_result.error,
        )


async def _demonstrate_production_target() -> None:
    """Demonstrate production target with strict settings."""
    logger.info("\n🚀 Example 3: Production Target with Strict Settings")
    prod_target_result = FlextTargetFactory.create_production_target(
        base_url="https://prod.wms.oracle.com",
        username="prod_user",
        password=DEMO_PASSWORD,
        # Production-specific overrides
        connection_pool_size=20,
        enable_audit_logging=True,
    )

    if prod_target_result.success and prod_target_result.data:
        logger.info("✅ Production target created with strict settings")
        prod_target = prod_target_result.data
        # Production preset automatically sets production-grade options
        logger.info("Batch size: %s", prod_target.config.get("batch_size"))
        logger.info("Max retries: %s", prod_target.config.get("max_retries"))
        logger.info("Verify SSL: %s", prod_target.config.get("verify_ssl"))
        logger.info("Timeout: %s", prod_target.config.get("timeout"))
    else:
        logger.error(
            "❌ Production target creation failed: %s",
            prod_target_result.error,
        )


async def _demonstrate_testing_target() -> None:
    """Demonstrate testing target with minimal settings."""
    logger.info("\n🧪 Example 4: Testing Target with Minimal Settings")
    test_target_result = FlextTargetFactory.create_testing_target(
        test_mode=True,
        fast_execution=True,
    )

    if test_target_result.success and test_target_result.data:
        logger.info("✅ Testing target created with minimal settings")
        test_target = test_target_result.data
        logger.info("Batch size: %s", test_target.config.get("batch_size"))
        logger.info("Enable logging: %s", test_target.config.get("enable_logging"))
        logger.info("Max retries: %s", test_target.config.get("max_retries"))
    else:
        logger.error("❌ Testing target creation failed: %s", test_target_result.error)


async def _demonstrate_config_target() -> None:
    """Demonstrate configuration-based target creation."""
    logger.info("\n📋 Example 5: Configuration-based Target Creation")
    config_dict = {
        "base_url": "https://config.wms.oracle.com",
        "username": "config_user",
        "password": DEMO_PASSWORD,
        "environment": "staging",
        "preset": "staging",
        "custom_field": "custom_value",
        "enable_compression": True,
    }

    config_target_result = FlextTargetFactory.create_from_config_dict(config_dict)
    if config_target_result.success and config_target_result.data:
        logger.info("✅ Configuration-based target created successfully")
        config_target = config_target_result.data
        logger.info("Environment: %s", config_target.config.get("environment"))
        logger.info("Custom field: %s", config_target.config.get("custom_field"))
    else:
        logger.error(
            "❌ Configuration-based target creation failed: %s",
            config_target_result.error,
        )


@flext_monitor_function(monitor)
async def demonstrate_factory_patterns() -> None:
    """Demonstrate various factory patterns for easier library usage."""
    logger.info("🏭 Starting Oracle WMS Target Factory Usage Examples")

    await _demonstrate_simple_target()
    await _demonstrate_development_target()
    await _demonstrate_production_target()
    await _demonstrate_testing_target()
    await _demonstrate_config_target()


@flext_monitor_function(monitor)
async def demonstrate_preset_differences() -> None:
    """Demonstrate differences between environment presets."""
    logger.info("\n🔍 Preset Comparison - How Factory Makes Configuration Easy")

    presets_to_compare = ["development", "staging", "production", "testing"]

    for preset_name in presets_to_compare:
        logger.info("\n📋 %s Preset Configuration:", preset_name.upper())
        preset_config = FlextTargetFactory.PRESETS[preset_name]

        for key, value in preset_config.items():
            logger.info("  %s: %s", key, value)

        # Show how preset optimizes for environment
        if preset_name == "development":
            logger.info("  💡 Optimized for: Fast feedback, easy debugging")
        elif preset_name == "staging":
            logger.info(
                "  💡 Optimized for: Production-like testing, performance validation",
            )
        elif preset_name == "production":
            logger.info("  💡 Optimized for: High performance, reliability, security")
        elif preset_name == "testing":
            logger.info("  💡 Optimized for: Fast test execution, minimal resources")


@flext_monitor_function(monitor)
async def demonstrate_error_handling() -> None:
    """Demonstrate factory error handling patterns."""
    logger.info("\n⚠️  Error Handling Examples")

    # Example 1: Missing required configuration
    logger.info("\n❌ Example: Missing Required Configuration")
    incomplete_config = {
        "base_url": "https://incomplete.wms.oracle.com",
        # Missing username and password
    }

    error_result = FlextTargetFactory.create_from_config_dict(incomplete_config)
    if not error_result.success:
        logger.info("✅ Handled missing config gracefully: %s", error_result.error)

    # Example 2: Unknown preset handling
    logger.info("\n⚠️  Example: Unknown Preset")
    unknown_preset_result = FlextTargetFactory.create_target(
        base_url="https://test.wms.oracle.com",
        username="test_user",
        password=DEMO_PASSWORD,
        preset="unknown_preset",
    )

    if unknown_preset_result.success:
        logger.info("✅ Unknown preset handled gracefully with fallback to defaults")
    else:
        logger.error("❌ Unexpected error: %s", unknown_preset_result.error)


def demonstrate_configuration_flexibility() -> None:
    """Demonstrate configuration flexibility and customization."""
    logger.info("\n🔧 Configuration Flexibility Examples")

    # Show how factory enables easy customization while maintaining defaults
    logger.info("\n📝 Creating custom configurations with factory:")

    # Custom development configuration
    custom_dev_config = {
        **FlextTargetFactory.PRESETS["development"],
        "debug_mode": True,
        "log_level": "DEBUG",
        "enable_sql_logging": True,
    }
    logger.info(
        "Custom Development Config: %s",
        json.dumps(custom_dev_config, indent=2),
    )

    # Custom production configuration
    custom_prod_config = {
        **FlextTargetFactory.PRESETS["production"],
        "connection_pool_size": 50,
        "enable_clustering": True,
        "backup_strategy": "incremental",
    }
    logger.info(
        "Custom Production Config: %s",
        json.dumps(custom_prod_config, indent=2),
    )

    logger.info("\n💡 Benefits of Factory Pattern:")
    logger.info("  ✅ Sensible defaults for each environment")
    logger.info("  ✅ Easy customization without losing base configuration")
    logger.info("  ✅ Consistent configuration across projects")
    logger.info("  ✅ Type-safe configuration with validation")
    logger.info("  ✅ Built-in error handling and logging")


async def main() -> None:
    """Run all factory usage examples."""
    logger.info("🎯 Oracle WMS Target Factory Usage Examples")
    logger.info("=" * 50)

    try:
        # Demonstrate core factory patterns
        await cast("Coroutine[object, object, object]", demonstrate_factory_patterns())

        # Show preset differences
        await cast(
            "Coroutine[object, object, object]", demonstrate_preset_differences()
        )

        # Demonstrate error handling
        await cast("Coroutine[object, object, object]", demonstrate_error_handling())

        # Show configuration flexibility
        demonstrate_configuration_flexibility()

        logger.info("\n🎉 Factory Usage Examples Completed Successfully!")
        logger.info("\n📚 Key Takeaways:")
        logger.info("  🏭 FlextTargetFactory simplifies target creation")
        logger.info("  🎛️  Environment presets provide sensible defaults")
        logger.info("  📊 Monitoring factory adds observability easily")
        logger.info("  🔧 Configuration-based creation enables flexibility")
        logger.info("  ⚡ Convenience functions reduce boilerplate code")
        logger.info("  🛡️  Built-in error handling improves reliability")

    except Exception:
        logger.exception("Factory usage example failed")
        raise


if __name__ == "__main__":
    """Run the factory usage examples."""

    asyncio.run(main())
