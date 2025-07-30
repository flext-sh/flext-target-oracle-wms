#!/usr/bin/env python3
"""Factory usage example - Demonstrating easier flext-* library usage.

This example shows how the FlextTargetFactory makes Oracle WMS targets
easier to create and use, following SOLID principles and best practices.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import json
from typing import Any

# DRY: Import REAL flext-* APIs
from flext_core import get_logger
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

# Import factory patterns for easier usage
from flext_target_oracle_wms import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)

# Get logger using flext-core patterns
logger = get_logger(__name__)

# Monitor using flext-observability
monitor = FlextObservabilityMonitor("factory_usage_example")


@flext_monitor_function("example_factory_usage")
async def demonstrate_factory_patterns() -> None:
    """Demonstrate various factory patterns for easier library usage."""
    logger.info("🏭 Starting Oracle WMS Target Factory Usage Examples")
    
    # Example 1: Simple target creation using convenience function
    logger.info("\n📝 Example 1: Simple Target Creation")
    simple_target_result = create_oracle_wms_target(
        base_url="https://simple.wms.oracle.com",
        username="simple_user",
        password="simple_password",
        environment="demo"
    )
    
    if simple_target_result.is_success:
        logger.info("✅ Simple target created successfully")
        simple_target = simple_target_result.data
        logger.info(f"Target config: {simple_target.config}")
    else:
        logger.error(f"❌ Simple target creation failed: {simple_target_result.error}")
    
    # Example 2: Development target with preset
    logger.info("\n🔧 Example 2: Development Target with Preset")
    dev_target_result = FlextTargetFactory.create_development_target(
        base_url="https://dev.wms.oracle.com",
        # Override some development defaults
        batch_size=50,
        custom_debug_mode=True
    )
    
    if dev_target_result.is_success:
        logger.info("✅ Development target created with optimized settings")
        dev_target = dev_target_result.data
        # Development preset automatically sets dev-friendly options
        logger.info(f"Batch size: {dev_target.config.get('batch_size')}")
        logger.info(f"Table prefix: {dev_target.config.get('table_prefix')}")
        logger.info(f"Verify SSL: {dev_target.config.get('verify_ssl')}")
    else:
        logger.error(f"❌ Development target creation failed: {dev_target_result.error}")
    
    # Example 3: Production target with strict settings
    logger.info("\n🚀 Example 3: Production Target with Strict Settings") 
    prod_target_result = FlextTargetFactory.create_production_target(
        base_url="https://prod.wms.oracle.com",
        username="prod_user",
        password="prod_password",
        # Production-specific overrides
        connection_pool_size=20,
        enable_audit_logging=True
    )
    
    if prod_target_result.is_success:
        logger.info("✅ Production target created with strict settings")
        prod_target = prod_target_result.data
        # Production preset automatically sets production-grade options
        logger.info(f"Batch size: {prod_target.config.get('batch_size')}")
        logger.info(f"Max retries: {prod_target.config.get('max_retries')}")
        logger.info(f"Verify SSL: {prod_target.config.get('verify_ssl')}")
        logger.info(f"Timeout: {prod_target.config.get('timeout')}")
    else:
        logger.error(f"❌ Production target creation failed: {prod_target_result.error}")
    
    # Example 4: Testing target with minimal settings
    logger.info("\n🧪 Example 4: Testing Target with Minimal Settings")
    test_target_result = FlextTargetFactory.create_testing_target(
        # Uses sensible test defaults
        test_mode=True,
        fast_execution=True
    )
    
    if test_target_result.is_success:
        logger.info("✅ Testing target created with minimal settings")
        test_target = test_target_result.data
        # Testing preset optimized for fast test execution
        logger.info(f"Batch size: {test_target.config.get('batch_size')}")
        logger.info(f"Enable logging: {test_target.config.get('enable_logging')}")
        logger.info(f"Max retries: {test_target.config.get('max_retries')}")
    else:
        logger.error(f"❌ Testing target creation failed: {test_target_result.error}")
    
    # Example 5: Configuration-based target creation
    logger.info("\n📋 Example 5: Configuration-based Target Creation")
    config_dict = {
        "base_url": "https://config.wms.oracle.com",
        "username": "config_user",
        "password": "config_password",
        "environment": "staging",
        "preset": "staging",
        "custom_field": "custom_value",
        "enable_compression": True
    }
    
    config_target_result = FlextTargetFactory.create_from_config_dict(config_dict)
    
    if config_target_result.is_success:
        logger.info("✅ Configuration-based target created successfully")
        config_target = config_target_result.data
        logger.info(f"Environment: {config_target.config.get('environment')}")
        logger.info(f"Custom field: {config_target.config.get('custom_field')}")
    else:
        logger.error(f"❌ Configuration-based target creation failed: {config_target_result.error}")
    
    # Example 6: Monitored target with observability
    logger.info("\n📊 Example 6: Monitored Target with Observability")
    monitored_target_result = create_monitored_oracle_wms_target(
        base_url="https://monitored.wms.oracle.com",
        username="monitored_user",
        password="monitored_password",
        environment="production",
        preset="production",
        monitor_name="prod_wms_monitor"
    )
    
    if monitored_target_result.is_success:
        logger.info("✅ Monitored target created with observability integration")
        monitored_target = monitored_target_result.data
        
        # Demonstrate monitoring capabilities
        logger.info("🔍 Target has built-in monitoring for:")
        logger.info("  - Setup/cleanup operations")
        logger.info("  - Record processing metrics")
        logger.info("  - Performance timing")
        logger.info("  - Success/failure counters")
    else:
        logger.error(f"❌ Monitored target creation failed: {monitored_target_result.error}")
    
    # Example 7: Advanced monitoring factory usage
    logger.info("\n🏭 Example 7: Advanced Monitoring Factory")
    monitoring_factory = FlextTargetMonitoringFactory("advanced_monitor")
    
    advanced_monitored_result = monitoring_factory.create_monitored_target(
        base_url="https://advanced.wms.oracle.com", 
        username="advanced_user",
        password="advanced_password",
        preset="production",
        connection_pool_monitoring=True,
        performance_profiling=True
    )
    
    if advanced_monitored_result.is_success:
        logger.info("✅ Advanced monitored target created")
        logger.info("🔧 Features enabled:")
        logger.info("  - Connection pool monitoring")
        logger.info("  - Performance profiling")
        logger.info("  - Automatic error tracking")
        logger.info("  - Resource usage metrics")
    else:
        logger.error(f"❌ Advanced monitored target creation failed: {advanced_monitored_result.error}")


@flext_monitor_function("example_preset_comparison")
async def demonstrate_preset_differences() -> None:
    """Demonstrate differences between environment presets."""
    logger.info("\n🔍 Preset Comparison - How Factory Makes Configuration Easy")
    
    presets_to_compare = ["development", "staging", "production", "testing"]
    
    for preset_name in presets_to_compare:
        logger.info(f"\n📋 {preset_name.upper()} Preset Configuration:")
        preset_config = FlextTargetFactory.PRESETS[preset_name]
        
        for key, value in preset_config.items():
            logger.info(f"  {key}: {value}")
        
        # Show how preset optimizes for environment
        if preset_name == "development":
            logger.info("  💡 Optimized for: Fast feedback, easy debugging")
        elif preset_name == "staging":
            logger.info("  💡 Optimized for: Production-like testing, performance validation")
        elif preset_name == "production":
            logger.info("  💡 Optimized for: High performance, reliability, security")
        elif preset_name == "testing":
            logger.info("  💡 Optimized for: Fast test execution, minimal resources")


@flext_monitor_function("example_error_handling")
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
    if not error_result.is_success:
        logger.info(f"✅ Handled missing config gracefully: {error_result.error}")
    
    # Example 2: Unknown preset handling
    logger.info("\n⚠️  Example: Unknown Preset")
    unknown_preset_result = FlextTargetFactory.create_target(
        base_url="https://test.wms.oracle.com",
        username="test_user",
        password="test_password",
        preset="unknown_preset"
    )
    
    if unknown_preset_result.is_success:
        logger.info("✅ Unknown preset handled gracefully with fallback to defaults")
    else:
        logger.error(f"❌ Unexpected error: {unknown_preset_result.error}")


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
        "enable_sql_logging": True
    }
    logger.info(f"Custom Development Config: {json.dumps(custom_dev_config, indent=2)}")
    
    # Custom production configuration
    custom_prod_config = {
        **FlextTargetFactory.PRESETS["production"],
        "connection_pool_size": 50,
        "enable_clustering": True,
        "backup_strategy": "incremental"
    }
    logger.info(f"Custom Production Config: {json.dumps(custom_prod_config, indent=2)}")
    
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
        await demonstrate_factory_patterns()
        
        # Show preset differences
        await demonstrate_preset_differences()
        
        # Demonstrate error handling
        await demonstrate_error_handling()
        
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
        
    except Exception as e:
        logger.error(f"Factory usage example failed: {e}")
        raise


if __name__ == "__main__":
    """Run the factory usage examples."""
    print("🏭 Oracle WMS Target Factory - Usage Examples")
    print("=" * 50)
    
    asyncio.run(main())
    
    print("\n✅ Factory usage examples completed successfully!")
    print("💡 The FlextTargetFactory makes flext-* libraries much easier to use!")