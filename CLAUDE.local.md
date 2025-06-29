# internal.invalid.md - TARGET-ORACLE-WMS PROJECT SPECIFICS

**Hierarquia**: **PROJECT-SPECIFIC**  
**Projeto**: Target Oracle WMS - Enterprise Warehouse Data Loader & Business Intelligence  
**Status**: PRODUCTION READY - Active warehouse data processing  
**Framework**: Singer Protocol + Oracle WMS + Business Logic + KPI Engine  
**Última Atualização**: 2025-06-26

**Referência Global**: `/home/marlonsc/CLAUDE.md` → Universal principles  
**Referência Workspace**: `../CLAUDE.md` → PyAuto workspace patterns  
**Referência Cross-Workspace**: `/home/marlonsc/internal.invalid.md` → Cross-workspace issues

---

## 🎯 PROJECT-SPECIFIC CONFIGURATION

### Virtual Environment Usage

```bash
# MANDATORY: Use workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate
# NOT project-specific venv
```

### Agent Coordination

```bash
# Read workspace coordination first
cat /home/marlonsc/pyauto/.token | tail -5
# Use project .token only for project-specific coordination
```

### Project-Specific Environment Variables

```bash
# Target Oracle WMS specific configurations
export TARGET_WMS_BASE_URL=https://wms.company.com
export TARGET_WMS_USERNAME=data_loader_user
export TARGET_WMS_PASSWORD=secure_wms_password
export TARGET_WMS_ENABLE_KPI_CALCULATION=true
export TARGET_WMS_ENABLE_ALERTS=true
export TARGET_WMS_EXPIRY_ALERT_DAYS=30
export TARGET_WMS_OUTPUT_PATH=./output
export TARGET_WMS_OUTPUT_FORMAT=json
export TARGET_WMS_BATCH_SIZE=1000
export TARGET_WMS_VALIDATION_MODE=strict
export TARGET_WMS_LOG_LEVEL=DEBUG
export TARGET_WMS_AUDIT_TRAIL=true
```

---

## 🏗️ TARGET ORACLE WMS ARCHITECTURE

### **Purpose & Role**

- **Enterprise Data Loader**: Advanced Singer target for warehouse management data loading
- **Business Intelligence Engine**: Real-time KPI calculation and warehouse analytics
- **Alert Generation System**: Multi-level alerting for inventory, orders, and operations
- **Multi-Destination Loader**: Files, databases, and WMS API support
- **Stream Intelligence Processor**: Specialized business logic per warehouse data type

### **Core Singer Components**

```python
# Target Oracle WMS structure
src/target_oracle_wms/
├── target.py            # Main Singer target implementation
├── sinks.py             # Standard WMS data sinks
├── sinks_advanced.py    # Advanced business logic sinks
├── auth.py              # WMS authentication
├── validation.py        # Data validation engine
└── business/            # Business logic modules
    ├── inventory.py     # Inventory KPIs and alerts
    ├── orders.py        # Order processing logic
    └── warehouse.py     # Warehouse operations analytics
```

### **Warehouse Business Intelligence Features**

- **Inventory KPIs**: Stock levels, turnover rates, expiry tracking
- **Order Analytics**: Fulfillment rates, processing times, bottleneck detection
- **Warehouse Metrics**: Location utilization, worker productivity, equipment efficiency
- **Alert Generation**: Multi-level alerts for critical warehouse events
- **Report Generation**: Automated business reports and insights

---

## 🔧 PROJECT-SPECIFIC TECHNICAL DETAILS

### **Development Commands**

```bash
# MANDATORY: Always from workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate

# Core development workflow
make install-dev       # Install development dependencies
make test              # Run comprehensive test suite
make test-unit         # Unit tests only
make test-integration  # Integration tests with WMS
make test-e2e          # End-to-end business logic tests
make lint              # Code quality checks
make format            # Code formatting

# Singer target operations
cat inventory_data.jsonl | target-oracle-wms --config config.json
target-oracle-wms --config config.json --input warehouse_data.jsonl
```

### **WMS Business Logic Testing**

```bash
# Test KPI calculation and alerting
echo '{"type":"RECORD","stream":"inventory","record":{"sku":"TEST-001","quantity":100,"expiry_date":"2024-12-31"}}' | \
  target-oracle-wms --config config.json --enable-kpis

# Test alert generation
echo '{"type":"RECORD","stream":"inventory","record":{"sku":"EXPIRY-001","quantity":50,"expiry_date":"2024-01-01"}}' | \
  target-oracle-wms --config config.json --enable-alerts

# Test multi-destination loading
target-oracle-wms --config config.json --output-format json --output-format csv --input test_data.jsonl
```

### **Warehouse Analytics Testing**

```bash
# Test inventory analytics
target-oracle-wms --config config.json --calculate-inventory-kpis --input inventory_stream.jsonl

# Test order processing analytics
target-oracle-wms --config config.json --calculate-order-kpis --input orders_stream.jsonl

# Test warehouse operations metrics
target-oracle-wms --config config.json --calculate-warehouse-metrics --input operations_stream.jsonl
```

---

## 🚨 PROJECT-SPECIFIC KNOWN ISSUES

### **WMS Business Logic Challenges**

- **KPI Calculation Performance**: Complex warehouse metrics computation overhead
- **Real-time Alert Generation**: Balancing alert sensitivity with noise reduction
- **Multi-Stream Correlation**: Correlating data across inventory, orders, and operations
- **Data Quality Validation**: Ensuring warehouse data integrity and consistency
- **Batch Processing Scalability**: Handling millions of warehouse transactions efficiently

### **Singer Protocol WMS Considerations**

```python
# WMS-specific Singer target patterns
class WMSTargetSingerPatterns:
    """Production patterns for WMS Singer target implementation."""

    def calculate_warehouse_kpis_efficiently(self, records: list):
        """Calculate warehouse KPIs with optimized performance."""
        # Batch KPI calculations to reduce overhead
        kpi_calculator = WarehouseKPICalculator(
            batch_size=self.config.batch_size,
            enable_caching=True,
            parallel_processing=True
        )

        # Calculate inventory KPIs
        inventory_kpis = kpi_calculator.calculate_inventory_metrics(
            records=records,
            metrics=[
                "stock_levels",
                "turnover_rate",
                "expiry_tracking",
                "abc_analysis"
            ]
        )

        # Calculate order KPIs
        order_kpis = kpi_calculator.calculate_order_metrics(
            records=records,
            metrics=[
                "fulfillment_rate",
                "processing_time",
                "bottleneck_detection",
                "customer_satisfaction"
            ]
        )

        return CombinedWarehouseKPIs(inventory_kpis, order_kpis)

    def generate_warehouse_alerts(self, kpis, thresholds):
        """Generate intelligent warehouse alerts."""
        alert_engine = WarehouseAlertEngine(
            thresholds=thresholds,
            escalation_rules=self.config.alert_escalation,
            notification_channels=self.config.notification_channels
        )

        alerts = []

        # Critical inventory alerts
        if kpis.inventory.low_stock_items:
            alerts.append(alert_engine.create_critical_alert(
                type="low_stock",
                items=kpis.inventory.low_stock_items,
                severity="critical"
            ))

        # Expiry alerts with multi-level warnings
        expiry_alerts = alert_engine.generate_expiry_alerts(
            items=kpis.inventory.expiring_items,
            warning_days=[30, 14, 7, 1]  # Multi-level warnings
        )
        alerts.extend(expiry_alerts)

        # Order processing alerts
        if kpis.orders.fulfillment_rate < thresholds.min_fulfillment_rate:
            alerts.append(alert_engine.create_warning_alert(
                type="low_fulfillment",
                current_rate=kpis.orders.fulfillment_rate,
                target_rate=thresholds.min_fulfillment_rate
            ))

        return alerts

    def implement_multi_destination_loading(self, processed_records):
        """Load data to multiple destinations efficiently."""
        loading_tasks = []

        # File output loading
        if self.config.enable_file_output:
            loading_tasks.append(
                self.load_to_files(processed_records, self.config.output_format)
            )

        # WMS API loading
        if self.config.enable_wms_api:
            loading_tasks.append(
                self.load_to_wms_api(processed_records, self.config.wms_config)
            )

        # Database loading
        if self.config.enable_database:
            loading_tasks.append(
                self.load_to_database(processed_records, self.config.db_config)
            )

        # Execute all loading tasks concurrently
        return asyncio.gather(*loading_tasks)
```

### **Production WMS Edge Cases**

```bash
# Common WMS target issues
1. KPI Calculation Bottlenecks: Complex calculations slowing data loading
2. Alert Flooding: Too many alerts overwhelming notification systems
3. Data Correlation Failures: Missing references between related streams
4. Memory Exhaustion: Large warehouse datasets exceeding memory limits
5. Multi-Destination Synchronization: Inconsistency across multiple outputs
```

---

## 🎯 PROJECT-SPECIFIC SUCCESS METRICS

### **Singer Protocol WMS Compliance**

- **Data Loading Throughput**: >100,000 warehouse records/minute loading rate
- **KPI Calculation Performance**: <10 seconds for comprehensive warehouse KPIs
- **Alert Generation Latency**: <30 seconds from threshold breach to alert
- **Data Quality Rate**: 99.9% data validation pass rate
- **Multi-Destination Consistency**: 100% consistency across all output destinations

### **Warehouse Business Intelligence Goals**

- **Real-time KPI Availability**: 95% of warehouse KPIs available within 5 minutes
- **Alert Accuracy**: 99% accurate alert generation with <2% false positives
- **Business Insight Coverage**: 100% coverage of critical warehouse metrics
- **Scalability Performance**: Linear scaling with warehouse transaction volume
- **Integration Reliability**: 99.9% successful integration with warehouse systems

---

## 🔗 PROJECT-SPECIFIC INTEGRATIONS

### **Singer Ecosystem Integration**

- **Tap Compatibility**: Works with all Singer-compliant warehouse data taps
- **Meltano Plugin**: Official Meltano Hub plugin for warehouse data loading
- **Schema Evolution**: Automatic adaptation to warehouse data schema changes
- **State Management**: Advanced loading state tracking for incremental processing

### **PyAuto Ecosystem Integration**

- **tap-oracle-wms**: Perfect companion for Oracle WMS data extraction and loading
- **flext-oracle-wms**: Unified FLX orchestrator with Singer target integration
- **flext-http-oracle-wms**: Direct WMS API integration for real-time operations
- **client-b-poc-oic-wms**: POC integration reference implementation

### **Warehouse Management Integration**

```python
# Production WMS target configuration
class ProductionWMSTarget:
    """Production WMS target for enterprise warehouse environments."""

    # Enterprise warehouse configuration
    PRODUCTION_CONFIG = {
        "base_url": "https://wms-prod.enterprise.com",
        "username": "${WMS_PROD_USER}",
        "password": "${WMS_PROD_PASSWORD}",

        # Business intelligence configuration
        "enable_kpi_calculation": True,
        "enable_alerts": True,
        "enable_reporting": True,
        "enable_analytics": True,

        # KPI calculation settings
        "kpi_settings": {
            "inventory_metrics": [
                "stock_levels",
                "turnover_rate",
                "abc_analysis",
                "expiry_tracking",
                "location_utilization"
            ],
            "order_metrics": [
                "fulfillment_rate",
                "processing_time",
                "on_time_delivery",
                "customer_satisfaction",
                "bottleneck_detection"
            ],
            "warehouse_metrics": [
                "worker_productivity",
                "equipment_utilization",
                "zone_efficiency",
                "task_completion_rate"
            ]
        },

        # Alert configuration
        "alert_settings": {
            "expiry_alert_days": [30, 14, 7, 1],
            "low_stock_threshold": 0.1,
            "fulfillment_rate_threshold": 0.95,
            "escalation_rules": {
                "critical": ["email", "sms", "slack"],
                "warning": ["email", "slack"],
                "info": ["email"]
            }
        },

        # Multi-destination loading
        "output_destinations": {
            "files": {
                "enabled": True,
                "formats": ["json", "csv", "parquet"],
                "path": "./warehouse_output"
            },
            "wms_api": {
                "enabled": True,
                "batch_size": 1000,
                "retry_attempts": 3
            },
            "database": {
                "enabled": True,
                "connection_string": "${WMS_DB_CONNECTION}",
                "table_prefix": "wms_"
            }
        }
    }
```

---

## 📊 PROJECT-SPECIFIC MONITORING

### **WMS Business Intelligence Metrics**

```python
# Key metrics for WMS target monitoring
TARGET_WMS_METRICS = {
    "kpi_calculation_duration": "Time to calculate warehouse KPIs",
    "alert_generation_latency": "Time from threshold breach to alert",
    "data_loading_throughput": "Warehouse records loaded per minute",
    "business_logic_overhead": "Performance overhead of business processing",
    "multi_destination_sync_time": "Time to sync across all destinations",
    "data_quality_score": "Percentage of records passing validation",
}
```

### **Warehouse Data Health Monitoring**

```bash
# Comprehensive WMS monitoring
target-oracle-wms --config config.json --health-check --detailed
target-oracle-wms --config config.json --validate-kpi-accuracy --test-data
target-oracle-wms --config config.json --test-alert-generation --simulate-thresholds
```

---

## 📋 PROJECT-SPECIFIC MAINTENANCE

### **Regular Maintenance Tasks**

- **Daily**: Monitor KPI calculation performance and alert accuracy
- **Weekly**: Review business logic effectiveness and optimize thresholds
- **Monthly**: Update warehouse data models and validation rules
- **Quarterly**: Performance optimization and business intelligence review

### **Singer Protocol Updates**

```bash
# Keep Singer SDK and WMS dependencies updated
pip install --upgrade singer-sdk requests pandas

# Validate Singer compliance
singer-check-target --target target-oracle-wms --config config.json
singer-validate-schema --schema wms-target-schema.json
```

### **Emergency Procedures**

```bash
# WMS target emergency troubleshooting
1. Test WMS connectivity: curl -I ${WMS_BASE_URL}/api/health
2. Validate KPI calculations: target-oracle-wms --config config.json --test-kpis
3. Check alert generation: target-oracle-wms --config config.json --test-alerts
4. Validate multi-destination sync: target-oracle-wms --config config.json --test-destinations
5. Reset business logic state: target-oracle-wms --config config.json --reset-kpi-state
```

---

**PROJECT SUMMARY**: Singer target empresarial para Oracle WMS com processamento avançado de lógica de negócio, cálculo de KPIs em tempo real, geração de alertas e carregamento multi-destino para operações de armazém.

**CRITICAL SUCCESS FACTOR**: Manter performance otimizada de processamento de dados warehouse com cálculo preciso de KPIs e geração inteligente de alertas para operações críticas de negócio.

---

_Última Atualização: 2025-06-26_  
_Próxima Revisão: Semanal durante operações críticas de warehouse_  
_Status: PRODUCTION READY - Processamento ativo de dados warehouse com business intelligence_
