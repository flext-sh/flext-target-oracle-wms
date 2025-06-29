# 📚 Target Oracle WMS - API Reference

> **Function**: Complete API reference for Oracle WMS Singer target implementation | **Audience**: Developers, Integration Engineers | **Status**: Enterprise Reference

[![Singer](https://img.shields.io/badge/singer-target-blue.svg)](https://www.singer.io/)
[![Oracle](https://img.shields.io/badge/oracle-WMS-red.svg)](https://www.oracle.com/cx/retail/warehouse-management/)
[![API](https://img.shields.io/badge/api-comprehensive-blue.svg)](../README.md)
[![Documentation](https://img.shields.io/badge/docs-comprehensive-blue.svg)](../README.md)

Complete API reference documentation for Oracle WMS Singer target, providing detailed interface specifications, sink definitions, and business logic APIs based on [Singer specification v1.0](https://hub.meltano.com/singer/spec) and [Oracle Retail WMS 25B API](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsab/).

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto](../../../README.md) → **📂 Project**: [Target Oracle WMS](../../README.md) → **📁 Docs**: [Documentation](../README.md) → **📄 Current**: API Reference

---

## 📋 **API Overview**

This reference covers all public APIs for Oracle WMS Singer target, implementing Singer specification compliance with enterprise-grade features for warehouse data processing and business logic.

### **API Categories**

- **Target Interface**: Core Singer target implementation and lifecycle
- **Sink Definitions**: All available Oracle WMS data sinks
- **Configuration Schema**: Complete configuration parameters and validation
- **Business Logic APIs**: KPI calculation and alerting interfaces
- **Output Management**: Multi-destination output handling
- **Performance APIs**: High-throughput processing and optimization

### **Singer Specification Compliance**

Based on [Singer v1.0 specification](https://hub.meltano.com/singer/spec):

- **Target Protocol**: Stream processing and record handling
- **State Protocol**: Bookmark management and persistence
- **Schema Protocol**: JSON Schema v7 compliance
- **Configuration Protocol**: Singer target configuration
- **Message Protocol**: JSON Lines input processing

---

## 🔧 **Core Target Interface**

### **TargetOracleWMS Class**

Primary target implementation following Singer SDK patterns:

```python
from singer_sdk import Target, Sink
from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class TargetOracleWMS(Target):
    """
    Oracle WMS Singer target with enterprise business logic processing.

    Provides comprehensive warehouse data processing with KPI calculation,
    alerting, and multi-output capabilities for Oracle Retail WMS systems.

    Based on Oracle Retail WMS 25B REST API specification:
    https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsab/
    """

    name = "target-oracle-wms"
    config_jsonschema = PropertiesList(
        # Required Configuration
        Property(
            "base_url",
            StringType,
            required=True,
            description="Oracle WMS API base URL (e.g., 'https://wms.company.com')"
        ),
        Property(
            "username",
            StringType,
            required=True,
            description="WMS authentication username"
        ),
        Property(
            "password",
            StringType,
            required=True,
            secret=True,
            description="WMS authentication password"
        ),

        # Business Logic Configuration
        Property(
            "enable_kpi_calculation",
            BooleanType,
            default=True,
            description="Enable business KPI calculation"
        ),
        Property(
            "enable_alerts",
            BooleanType,
            default=True,
            description="Enable business alert generation"
        ),
        Property(
            "expiry_alert_days",
            IntegerType,
            default=30,
            description="Days before expiry to generate alerts (1-365)"
        ),

        # Output Configuration
        Property(
            "output_path",
            StringType,
            default="./output",
            description="Output directory for file outputs"
        ),
        Property(
            "output_format",
            StringType,
            default="json",
            allowed_values=["json", "csv", "parquet", "excel"],
            description="Default output file format"
        ),
        Property(
            "database_url",
            StringType,
            description="Database connection URL for database outputs"
        ),
        Property(
            "enable_wms_updates",
            BooleanType,
            default=False,
            description="Enable closed-loop updates back to WMS"
        ),

        # Performance Configuration
        Property(
            "batch_size",
            IntegerType,
            default=1000,
            description="Records per batch for processing (100-10000)"
        ),
        Property(
            "max_workers",
            IntegerType,
            default=4,
            description="Maximum concurrent workers (1-10)"
        ),
        Property(
            "memory_limit_mb",
            IntegerType,
            default=512,
            description="Memory limit in MB (128-2048)"
        ),

        # Advanced Configuration
        Property(
            "analytics_outputs",
            ObjectType(),
            description="Analytics platform configuration"
        ),
        Property(
            "alert_rules",
            ObjectType(),
            description="Custom alert rule configuration"
        ),
        Property(
            "kpi_config",
            ObjectType(),
            description="KPI calculation configuration"
        )
    ).to_dict()

    def get_sink_class(self, stream_name: str) -> Type[Sink]:
        """
        Get appropriate sink class for stream type.

        Implements intelligent stream routing based on WMS entity types
        with specialized business logic processing.

        Args:
            stream_name: Name of the stream to process

        Returns:
            Type[Sink]: Specialized sink class for the stream type

        Example:
            >>> target = TargetOracleWMS(config=config)
            >>> sink_class = target.get_sink_class("inventory")
            >>> print(sink_class.__name__)  # InventorySink
        """

    def get_sink(self, stream_name: str, record: dict, schema: dict, key_properties: list) -> Sink:
        """
        Create sink instance with business logic configuration.

        Initializes sink with KPI calculators, alert generators,
        and output handlers based on stream type and configuration.

        Args:
            stream_name: Name of the stream
            record: Sample record for initialization
            schema: JSON Schema for the stream
            key_properties: List of key property names

        Returns:
            Sink: Configured sink instance for processing
        """
```

### **Configuration Validation**

```python
class ConfigValidator:
    """
    Configuration validation with enterprise-grade checks.

    Validates all configuration parameters with business
    rules and connectivity testing.
    """

    @staticmethod
    def validate_config(config: Dict[str, Any]) -> ValidationResult:
        """
        Validate complete configuration with comprehensive checks.

        Args:
            config: Configuration dictionary

        Returns:
            ValidationResult: Validation status and details

        Raises:
            ConfigurationError: If critical configuration errors found

        Example:
            >>> result = ConfigValidator.validate_config(config)
            >>> if not result.is_valid:
            ...     for error in result.errors:
            ...         print(f"Error: {error}")
        """
        errors = []
        warnings = []

        # Required field validation
        required_fields = ["base_url", "username", "password"]
        for field in required_fields:
            if not config.get(field):
                errors.append(f"Missing required field: {field}")

        # URL validation
        if base_url := config.get("base_url"):
            if not base_url.startswith(("http://", "https://")):
                errors.append("base_url must start with http:// or https://")

        # Numeric range validation
        if batch_size := config.get("batch_size"):
            if not 100 <= batch_size <= 10000:
                warnings.append("batch_size should be between 100-10000 for optimal performance")

        # Memory limit validation
        if memory_limit := config.get("memory_limit_mb"):
            if memory_limit < 128:
                warnings.append("memory_limit_mb below 128MB may cause performance issues")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
```

---

## 📊 **Sink Specifications**

### **Base WMSSink Class**

```python
class WMSSink(Sink):
    """
    Base sink class for Oracle WMS entities.

    Provides common functionality for all WMS sinks including
    business logic processing, output handling, and monitoring.
    """

    def __init__(self, target: Target, stream_name: str, schema: dict, key_properties: list):
        super().__init__(target, stream_name, schema, key_properties)
        self.config = target.config
        self.business_logic_engine = BusinessLogicEngine(self.config)
        self.output_manager = OutputManager(self.config)
        self.performance_monitor = PerformanceMonitor()

    def process_record(self, record: Dict[str, Any], context: Dict) -> None:
        """
        Process record with comprehensive business logic and output handling.

        Implements enterprise-grade record processing with validation,
        transformation, KPI calculation, and multi-output routing.

        Args:
            record: Input record to process
            context: Processing context information

        Raises:
            ProcessingError: If record processing fails
            ValidationError: If record validation fails
        """

    def process_batch(self, records: List[Dict[str, Any]]) -> None:
        """
        Process multiple records in batch for performance optimization.

        Implements batch-level analytics and optimizations including
        portfolio analysis, trend detection, and bulk operations.

        Args:
            records: List of records to process as a batch
        """
```

### **InventorySink**

```python
class InventorySink(WMSSink):
    """
    Specialized sink for inventory stream processing.

    Implements inventory-specific business logic including
    valuation, ABC analysis, and expiry management.
    """

    supported_streams = ["inventory", "lots", "locations", "cycle_counts", "adjustments"]

    def __init__(self, target: Target, stream_name: str, schema: dict, key_properties: list):
        super().__init__(target, stream_name, schema, key_properties)
        self.inventory_calculator = InventoryKPICalculator(self.config)
        self.expiry_manager = ExpiryAlertManager(self.config)

    def process_record(self, record: Dict[str, Any], context: Dict) -> None:
        """
        Process inventory record with specialized business logic.

        Applies inventory valuation, ABC classification, expiry analysis,
        and generates inventory-specific alerts and KPIs.

        Args:
            record: Inventory record to process
            context: Processing context
        """

    def calculate_inventory_kpis(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate inventory-specific KPIs.

        Args:
            record: Inventory record

        Returns:
            Dict[str, Any]: Calculated KPIs including turnover, valuation, etc.

        Example:
            >>> kpis = sink.calculate_inventory_kpis(record)
            >>> print(f"Turnover ratio: {kpis['turnover_ratio']}")
        """
        return {
            "inventory_turnover": self._calculate_turnover_ratio(record),
            "carrying_cost_ratio": self._calculate_carrying_cost(record),
            "abc_classification": self._calculate_abc_class(record),
            "stockout_risk": self._assess_stockout_risk(record),
            "days_of_supply": self._calculate_days_of_supply(record),
            "inventory_accuracy": self._calculate_accuracy(record)
        }

    def generate_inventory_alerts(self, record: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate inventory-specific alerts.

        Args:
            record: Inventory record

        Returns:
            List[Dict[str, Any]]: Generated alerts
        """
        alerts = []

        # Low stock alert
        if self._is_low_stock(record):
            alerts.append({
                "type": "low_stock",
                "severity": "high",
                "item_id": record.get("item_id"),
                "current_quantity": record.get("available_quantity"),
                "reorder_point": record.get("reorder_point"),
                "message": f"Low stock alert for {record.get('item_id')}"
            })

        # Expiry alert
        if expiry_alert := self.expiry_manager.check_expiry(record):
            alerts.append(expiry_alert)

        # Overstock alert
        if self._is_overstock(record):
            alerts.append({
                "type": "overstock",
                "severity": "medium",
                "item_id": record.get("item_id"),
                "current_quantity": record.get("on_hand_quantity"),
                "max_level": record.get("max_stock_level"),
                "message": f"Overstock condition for {record.get('item_id')}"
            })

        return alerts
```

### **OrderSink**

```python
class OrderSink(WMSSink):
    """
    Specialized sink for order stream processing.

    Implements order-specific business logic including
    fulfillment analysis, cycle time calculation, and performance metrics.
    """

    supported_streams = ["orders", "order_lines", "shipments", "allocations", "picks"]

    def __init__(self, target: Target, stream_name: str, schema: dict, key_properties: list):
        super().__init__(target, stream_name, schema, key_properties)
        self.order_calculator = OrderKPICalculator(self.config)
        self.fulfillment_analyzer = FulfillmentAnalyzer(self.config)

    def calculate_order_kpis(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate order-specific KPIs.

        Args:
            record: Order record

        Returns:
            Dict[str, Any]: Calculated KPIs including fulfillment metrics
        """
        return {
            "fulfillment_rate": self._calculate_fulfillment_rate(record),
            "perfect_order_rate": self._calculate_perfect_order_rate(record),
            "cycle_time_hours": self._calculate_cycle_time(record),
            "on_time_delivery_rate": self._calculate_otd_rate(record),
            "order_accuracy": self._calculate_order_accuracy(record),
            "cost_per_order": self._calculate_cost_per_order(record)
        }

    def analyze_order_performance(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze order performance across multiple records.

        Args:
            records: List of order records

        Returns:
            Dict[str, Any]: Performance analysis results
        """
        return {
            "average_cycle_time": self._calculate_avg_cycle_time(records),
            "fulfillment_trends": self._analyze_fulfillment_trends(records),
            "customer_satisfaction": self._estimate_satisfaction(records),
            "bottleneck_analysis": self._identify_bottlenecks(records)
        }
```

### **WarehouseSink**

```python
class WarehouseSink(WMSSink):
    """
    Specialized sink for warehouse operations processing.

    Implements warehouse-specific business logic including
    productivity analysis, space utilization, and operational efficiency.
    """

    supported_streams = ["tasks", "workers", "equipment", "zones", "facilities"]

    def calculate_warehouse_kpis(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate warehouse operations KPIs.

        Args:
            record: Warehouse record

        Returns:
            Dict[str, Any]: Calculated warehouse KPIs
        """
        return {
            "space_utilization": self._calculate_space_utilization(record),
            "labor_productivity": self._calculate_labor_productivity(record),
            "equipment_efficiency": self._calculate_equipment_efficiency(record),
            "throughput_rate": self._calculate_throughput_rate(record),
            "operational_cost": self._calculate_operational_cost(record),
            "safety_score": self._calculate_safety_score(record)
        }

    def optimize_operations(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate operational optimization recommendations.

        Args:
            records: List of warehouse operation records

        Returns:
            Dict[str, Any]: Optimization recommendations
        """
        return {
            "layout_optimization": self._analyze_layout_efficiency(records),
            "resource_allocation": self._optimize_resource_allocation(records),
            "workflow_improvements": self._identify_workflow_improvements(records),
            "cost_reduction_opportunities": self._identify_cost_savings(records)
        }
```

---

## 🔐 **Business Logic APIs**

### **KPICalculator Interface**

```python
class KPICalculator:
    """
    Advanced KPI calculation engine for warehouse metrics.

    Implements comprehensive business intelligence calculations
    for inventory, orders, and warehouse operations.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.historical_data = HistoricalDataManager(config)

    def calculate_kpis(self, stream_name: str, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate stream-specific KPIs with historical context.

        Args:
            stream_name: Name of the stream
            record: Record to calculate KPIs for

        Returns:
            Dict[str, Any]: Calculated KPIs

        Example:
            >>> calculator = KPICalculator(config)
            >>> kpis = calculator.calculate_kpis("inventory", record)
            >>> print(f"Turnover: {kpis['inventory_turnover']}")
        """

    def get_benchmark_metrics(self, stream_name: str) -> Dict[str, Any]:
        """
        Get industry benchmark metrics for comparison.

        Args:
            stream_name: Name of the stream

        Returns:
            Dict[str, Any]: Benchmark metrics
        """
        benchmarks = {
            "inventory": {
                "inventory_turnover": {"excellent": 12, "good": 8, "average": 4},
                "stockout_rate": {"excellent": 0.02, "good": 0.05, "average": 0.10}
            },
            "orders": {
                "fulfillment_rate": {"excellent": 0.98, "good": 0.95, "average": 0.90},
                "cycle_time_hours": {"excellent": 2, "good": 4, "average": 8}
            }
        }
        return benchmarks.get(stream_name, {})
```

### **AlertGenerator Interface**

```python
class AlertGenerator:
    """
    Intelligent alert generation system for WMS data.

    Implements multi-level alerting with business rules,
    thresholds, and escalation patterns.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.alert_rules = AlertRuleEngine(config)
        self.notification_manager = NotificationManager(config)

    def generate_alerts(self, stream_name: str, record: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate alerts based on business rules and thresholds.

        Args:
            stream_name: Name of the stream
            record: Record to check for alerts

        Returns:
            List[Dict[str, Any]]: Generated alerts

        Example:
            >>> generator = AlertGenerator(config)
            >>> alerts = generator.generate_alerts("inventory", record)
            >>> for alert in alerts:
            ...     print(f"{alert['severity']}: {alert['message']}")
        """

    def configure_alert_rules(self, rules: Dict[str, Any]) -> None:
        """
        Configure custom alert rules.

        Args:
            rules: Alert rule configuration

        Example:
            >>> rules = {
            ...     "low_stock": {"threshold": 10, "severity": "high"},
            ...     "expiry": {"days": 7, "severity": "critical"}
            ... }
            >>> generator.configure_alert_rules(rules)
        """
        self.alert_rules.update_rules(rules)

    def get_alert_history(self, hours: int = 24) -> List[Dict[str, Any]]:
        """
        Get alert history for specified time period.

        Args:
            hours: Number of hours to look back

        Returns:
            List[Dict[str, Any]]: Alert history
        """
        return self.alert_rules.get_history(hours)
```

---

## 🚀 **Output Handler APIs**

### **OutputManager Interface**

```python
class OutputManager:
    """
    Enterprise output management system for multi-destination routing.

    Provides flexible output routing to files, databases, APIs,
    and analytics platforms with format transformation.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.handlers = self._initialize_handlers()

    def write_to_file(self, record: Dict[str, Any], stream_name: str, format_type: str) -> None:
        """
        Write record to file in specified format.

        Args:
            record: Record to write
            stream_name: Name of the stream
            format_type: Output format (json, csv, parquet, excel)

        Raises:
            OutputError: If write operation fails

        Example:
            >>> manager = OutputManager(config)
            >>> manager.write_to_file(record, "inventory", "json")
        """

    def write_to_database(self, record: Dict[str, Any], stream_name: str) -> None:
        """
        Write record to configured database.

        Args:
            record: Record to write
            stream_name: Name of the stream

        Example:
            >>> manager.write_to_database(record, "inventory")
        """

    def send_to_analytics(self, record: Dict[str, Any], platform: str) -> None:
        """
        Send record to analytics platform.

        Args:
            record: Record to send
            platform: Analytics platform name

        Example:
            >>> manager.send_to_analytics(record, "tableau")
        """

    def update_wms(self, record: Dict[str, Any], stream_name: str) -> None:
        """
        Update Oracle WMS via API with processed data.

        Args:
            record: Processed record to update
            stream_name: Name of the stream

        Example:
            >>> manager.update_wms(processed_record, "inventory")
        """
```

### **FileHandler Interface**

```python
class FileHandler:
    """
    Advanced file output handler with compression and partitioning.

    Provides high-performance file writing with support for
    multiple formats and enterprise-grade features.
    """

    supported_formats = ["json", "csv", "parquet", "excel"]

    def write_record(self, record: Dict[str, Any], stream_name: str, format_type: str, config: Dict[str, Any]) -> None:
        """
        Write record to file with enterprise features.

        Args:
            record: Record to write
            stream_name: Name of the stream
            format_type: Output format
            config: Output configuration
        """

    def write_batch(self, records: List[Dict[str, Any]], stream_name: str, format_type: str, config: Dict[str, Any]) -> None:
        """
        Write multiple records in batch for performance.

        Args:
            records: List of records to write
            stream_name: Name of the stream
            format_type: Output format
            config: Output configuration
        """

    def get_output_stats(self, stream_name: str) -> Dict[str, Any]:
        """
        Get output statistics for stream.

        Args:
            stream_name: Name of the stream

        Returns:
            Dict[str, Any]: Output statistics
        """
        return {
            "records_written": self._count_records(stream_name),
            "files_created": self._count_files(stream_name),
            "total_size_mb": self._calculate_size(stream_name),
            "compression_ratio": self._calculate_compression(stream_name)
        }
```

---

## 📈 **Performance APIs**

### **PerformanceMonitor Interface**

```python
class PerformanceMonitor:
    """
    Comprehensive performance monitoring for target operations.

    Provides metrics collection, analysis, and optimization
    recommendations for warehouse data processing.
    """

    def __init__(self):
        self.metrics = {}
        self.start_time = time.time()

    def track_processing(self, stream_name: str) -> ContextManager:
        """
        Track processing performance for a stream.

        Args:
            stream_name: Name of the stream

        Returns:
            ContextManager: Performance tracking context

        Example:
            >>> monitor = PerformanceMonitor()
            >>> with monitor.track_processing("inventory") as tracker:
            ...     # Process records
            ...     pass
            >>> print(f"Processing time: {tracker.duration}s")
        """

    def get_performance_metrics(self, stream_name: str = None) -> Dict[str, Any]:
        """
        Get performance metrics for stream or all streams.

        Args:
            stream_name: Optional stream name filter

        Returns:
            Dict[str, Any]: Performance metrics
        """
        return {
            "throughput_records_per_second": self._calculate_throughput(stream_name),
            "average_processing_time_ms": self._calculate_avg_time(stream_name),
            "memory_usage_mb": self._get_memory_usage(),
            "error_rate": self._calculate_error_rate(stream_name),
            "queue_depth": self._get_queue_depth(stream_name)
        }

    def get_optimization_recommendations(self) -> List[Dict[str, Any]]:
        """
        Get performance optimization recommendations.

        Returns:
            List[Dict[str, Any]]: Optimization recommendations
        """
        recommendations = []

        if self._is_memory_high():
            recommendations.append({
                "type": "memory",
                "priority": "high",
                "recommendation": "Reduce batch_size or increase memory_limit_mb",
                "expected_improvement": "20-30% memory reduction"
            })

        if self._is_throughput_low():
            recommendations.append({
                "type": "throughput",
                "priority": "medium",
                "recommendation": "Increase max_workers or batch_size",
                "expected_improvement": "15-25% throughput increase"
            })

        return recommendations
```

---

## 🔗 **Cross-References**

### **Singer Protocol Documentation**

- [Singer Specification v1.0](https://hub.meltano.com/singer/spec) - Official Singer protocol
- [JSON Schema v7](https://json-schema.org/draft-07/schema) - Schema validation specification
- [Meltano SDK Reference](https://sdk.meltano.com/) - SDK implementation patterns

### **Oracle WMS Documentation**

- [Oracle Retail WMS 25B REST API](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsab/) - Official API reference
- [Oracle WMS Integration Guide](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsig/) - Integration best practices

### **Related Documentation**

- [Architecture Guide](../architecture/README.md) - Technical architecture patterns
- [Implementation Guides](../guides/README.md) - Step-by-step implementation
- [Security Guide](../security/README.md) - Security implementation

---

**📚 API Reference**: Target Oracle WMS | **🏠 Root**: [PyAuto Home](../../../README.md) | **Framework**: Singer SDK 0.39.0+ | **Updated**: 2025-06-19
