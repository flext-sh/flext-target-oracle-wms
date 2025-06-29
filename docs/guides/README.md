# 📘 Target Oracle WMS - Implementation Guides

> **Function**: Step-by-step implementation guides for Oracle WMS Singer target with real-world business scenarios | **Audience**: Developers, Business Analysts | **Status**: Enterprise Reference

[![Singer](https://img.shields.io/badge/singer-target-blue.svg)](https://www.singer.io/)
[![Oracle](https://img.shields.io/badge/oracle-WMS-red.svg)](https://www.oracle.com/cx/retail/warehouse-management/)
[![Implementation](https://img.shields.io/badge/implementation-comprehensive-blue.svg)](../README.md)
[![Documentation](https://img.shields.io/badge/docs-comprehensive-blue.svg)](../README.md)

Comprehensive step-by-step implementation guides providing practical guidance for setting up, configuring, and operating Oracle WMS Singer target in production environments, with real-world business scenarios based on [Singer specification](https://hub.meltano.com/singer/spec) and [Oracle WMS 25B implementation guide](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsig/).

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto](../../../README.md) → **📂 Project**: [Target Oracle WMS](../../README.md) → **📁 Docs**: [Documentation](../README.md) → **📄 Current**: Implementation Guides

---

## 📋 **Guide Overview**

This section provides comprehensive implementation guidance covering all aspects of Oracle WMS Singer target deployment, from initial setup to advanced business logic configuration and production optimization.

### **Guide Categories**

- **Getting Started**: Installation, configuration, and first data loading
- **Business Logic Setup**: KPI configuration and custom rule development
- **Multi-Output Configuration**: Setting up file, database, and API outputs
- **Performance Tuning**: Optimization for high-volume data processing
- **Production Deployment**: Enterprise deployment patterns and monitoring
- **Troubleshooting**: Common issues and debugging procedures

### **Implementation Methodology**

Based on [Singer specification best practices](https://hub.meltano.com/singer/spec) and [Oracle WMS implementation guidelines](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsig/):

- **Incremental Implementation**: Start simple, add complexity progressively
- **Configuration Validation**: Validate each step before proceeding
- **Business-Driven Development**: Align technical implementation with business requirements
- **Production Readiness**: Every guide includes production considerations
- **Performance First**: Optimization strategies included throughout

---

## 🚀 **Getting Started**

### **Prerequisites Checklist**

Before implementing Oracle WMS Singer target, ensure these requirements are met:

#### **Environment Requirements**

```bash
# Python version check
python --version  # Requires Python 3.9+

# Singer SDK availability
pip show singer-sdk  # Requires singer-sdk 0.39.0+

# Oracle WMS connectivity
curl -I https://your-wms.company.com/api/health  # WMS API accessibility
```

#### **Oracle WMS Requirements**

| Component          | Requirement                    | Validation                 |
| ------------------ | ------------------------------ | -------------------------- |
| **WMS Version**    | Oracle Retail WMS 25B+         | Check API version endpoint |
| **API Access**     | REST API enabled               | Test with health endpoint  |
| **Authentication** | Valid credentials              | Authenticate successfully  |
| **Network Access** | Firewall rules configured      | Test connectivity          |
| **Permissions**    | Read access to target entities | Query test entities        |

#### **Business Requirements**

- **KPI Definitions**: Clearly defined business metrics
- **Alert Rules**: Business thresholds and notification requirements
- **Output Destinations**: Target systems for processed data
- **Data Quality Standards**: Validation and transformation rules

### **Installation Guide**

#### **Step 1: Install Target Package**

```bash
# Install from PyPI (recommended)
pip install target-oracle-wms

# Or install from source
git clone https://github.com/datacosmos-br/target-oracle-wms.git
cd target-oracle-wms
pip install -e .

# Verify installation
target-oracle-wms --version
```

#### **Step 2: Create Configuration File**

Create `config.json` with your Oracle WMS connection details:

```json
{
  "base_url": "https://your-wms.company.com",
  "username": "your_username",
  "password": "your_password",
  "enable_kpi_calculation": true,
  "enable_alerts": true,
  "output_path": "./output",
  "output_format": "json",
  "batch_size": 1000,
  "max_workers": 4
}
```

#### **Step 3: Test Connection**

```bash
# Test basic connectivity
target-oracle-wms --config config.json --test

# Validate configuration
target-oracle-wms --config config.json --validate-config

# Test with sample data
echo '{"type":"RECORD","stream":"inventory","record":{"item_id":"TEST001","quantity":100}}' | \
  target-oracle-wms --config config.json
```

#### **Step 4: First Data Loading**

Create a simple test pipeline:

```bash
# Using singer-python utilities
tap-csv --config tap_config.json --catalog catalog.json | \
  target-oracle-wms --config config.json

# Or with Meltano
meltano add target target-oracle-wms
meltano invoke target-oracle-wms --config config.json
```

### **Configuration Validation**

#### **Required Configuration Validation**

```python
# Python validation script
from target_oracle_wms.config import ConfigValidator

def validate_setup():
    """Validate complete target setup."""
    config = {
        "base_url": "https://your-wms.company.com",
        "username": "your_username",
        "password": "your_password"
    }

    result = ConfigValidator.validate_config(config)

    if not result.is_valid:
        print("❌ Configuration errors:")
        for error in result.errors:
            print(f"  - {error}")
        return False

    if result.warnings:
        print("⚠️ Configuration warnings:")
        for warning in result.warnings:
            print(f"  - {warning}")

    print("✅ Configuration is valid!")
    return True

if __name__ == "__main__":
    validate_setup()
```

#### **Connection Testing**

```bash
# Test Oracle WMS API connectivity
curl -X GET "https://your-wms.company.com/api/health" \
     -H "Authorization: Basic $(echo -n 'username:password' | base64)"

# Test target with minimal record
echo '{"type":"RECORD","stream":"test","record":{"id":1,"name":"test"}}' | \
  target-oracle-wms --config config.json --validate-records
```

---

## 💼 **Business Logic Setup**

### **KPI Configuration**

#### **Inventory KPIs**

Configure inventory-specific business metrics:

```json
{
  "kpi_config": {
    "inventory": {
      "turnover_calculation": {
        "enabled": true,
        "period_days": 365,
        "cost_basis": "average"
      },
      "abc_analysis": {
        "enabled": true,
        "a_threshold": 0.8,
        "b_threshold": 0.95
      },
      "stockout_risk": {
        "enabled": true,
        "lead_time_days": 14,
        "safety_stock_days": 7
      },
      "carrying_cost": {
        "enabled": true,
        "cost_rate": 0.25,
        "storage_cost_per_unit": 0.5
      }
    }
  }
}
```

#### **Order KPIs**

Configure order fulfillment metrics:

```json
{
  "kpi_config": {
    "orders": {
      "fulfillment_metrics": {
        "enabled": true,
        "perfect_order_criteria": {
          "complete": true,
          "on_time": true,
          "damage_free": true,
          "invoice_accurate": true
        }
      },
      "cycle_time_tracking": {
        "enabled": true,
        "stages": ["allocation", "picking", "packing", "shipping"],
        "sla_hours": {
          "allocation": 2,
          "picking": 4,
          "packing": 2,
          "shipping": 8
        }
      },
      "cost_tracking": {
        "enabled": true,
        "include_labor": true,
        "include_materials": true,
        "include_overhead": true
      }
    }
  }
}
```

#### **Warehouse Operations KPIs**

Configure operational efficiency metrics:

```json
{
  "kpi_config": {
    "warehouse": {
      "productivity_metrics": {
        "enabled": true,
        "lines_per_hour_target": 120,
        "picks_per_hour_target": 200,
        "accuracy_target": 0.995
      },
      "space_utilization": {
        "enabled": true,
        "target_utilization": 0.85,
        "alert_threshold": 0.95
      },
      "equipment_efficiency": {
        "enabled": true,
        "uptime_target": 0.95,
        "maintenance_tracking": true
      }
    }
  }
}
```

### **Alert Configuration**

#### **Inventory Alerts**

```json
{
  "alert_rules": {
    "inventory": {
      "low_stock": {
        "enabled": true,
        "threshold_type": "percentage",
        "threshold_value": 0.1,
        "severity": "high",
        "notification_channels": ["email", "slack"]
      },
      "expiry_warning": {
        "enabled": true,
        "days_before_expiry": 30,
        "severity": "medium",
        "notification_channels": ["email"]
      },
      "overstock": {
        "enabled": true,
        "threshold_multiplier": 2.0,
        "severity": "low",
        "notification_channels": ["slack"]
      },
      "negative_inventory": {
        "enabled": true,
        "severity": "critical",
        "notification_channels": ["email", "slack", "pager"]
      }
    }
  }
}
```

#### **Order Alerts**

```json
{
  "alert_rules": {
    "orders": {
      "sla_breach": {
        "enabled": true,
        "severity": "high",
        "notification_channels": ["email", "slack"]
      },
      "allocation_failure": {
        "enabled": true,
        "severity": "medium",
        "retry_attempts": 3,
        "notification_channels": ["slack"]
      },
      "shipping_delay": {
        "enabled": true,
        "threshold_hours": 24,
        "severity": "medium",
        "notification_channels": ["email"]
      }
    }
  }
}
```

### **Custom Business Rules**

#### **Example: Advanced Inventory Valuation**

```python
from target_oracle_wms import register_business_rule

@register_business_rule("inventory", "advanced_valuation")
def calculate_advanced_inventory_value(record: dict, context: dict) -> dict:
    """
    Calculate advanced inventory valuation with market adjustments.

    Implements FIFO/LIFO/Weighted Average methods with market value adjustments.
    """
    item_id = record.get("item_id")
    quantity = float(record.get("on_hand_quantity", 0))
    unit_cost = float(record.get("unit_cost", 0))

    # Get market price from external service
    market_price = context.get("market_prices", {}).get(item_id, unit_cost)

    # Calculate market adjustment
    market_adjustment = min(market_price, unit_cost * 1.1)  # Conservative ceiling

    # Apply valuation method
    valuation_method = context.get("valuation_method", "weighted_average")

    if valuation_method == "fifo":
        adjusted_value = calculate_fifo_value(record, market_adjustment)
    elif valuation_method == "lifo":
        adjusted_value = calculate_lifo_value(record, market_adjustment)
    else:
        adjusted_value = quantity * market_adjustment

    return {
        "inventory_value": adjusted_value,
        "market_adjustment": market_adjustment - unit_cost,
        "valuation_method": valuation_method,
        "market_price": market_price,
        "adjustment_percentage": (market_adjustment - unit_cost) / unit_cost if unit_cost > 0 else 0
    }

def calculate_fifo_value(record: dict, market_price: float) -> float:
    """Calculate FIFO inventory value."""
    # Implementation for FIFO calculation
    lot_details = record.get("lot_details", [])
    total_value = 0

    for lot in sorted(lot_details, key=lambda x: x.get("received_date", "")):
        lot_quantity = float(lot.get("quantity", 0))
        lot_cost = min(float(lot.get("cost", 0)), market_price)
        total_value += lot_quantity * lot_cost

    return total_value
```

#### **Example: Dynamic Reorder Point Calculation**

```python
@register_business_rule("inventory", "dynamic_reorder_point")
def calculate_dynamic_reorder_point(record: dict, context: dict) -> dict:
    """
    Calculate dynamic reorder point based on demand variability and lead time.

    Implements advanced statistical models for optimal inventory management.
    """
    item_id = record.get("item_id")

    # Get historical demand data
    demand_history = context.get("demand_history", {}).get(item_id, [])

    if len(demand_history) < 4:
        # Fallback to static reorder point
        return {"reorder_point": record.get("reorder_point", 0)}

    # Calculate demand statistics
    average_demand = sum(demand_history) / len(demand_history)
    demand_variance = sum((x - average_demand) ** 2 for x in demand_history) / len(demand_history)
    demand_std_dev = demand_variance ** 0.5

    # Get lead time statistics
    lead_time_days = context.get("lead_time_stats", {}).get(item_id, {})
    avg_lead_time = lead_time_days.get("average", 14)
    lead_time_std_dev = lead_time_days.get("std_dev", 2)

    # Calculate safety stock (95% service level)
    service_level_z = 1.65  # 95% service level
    safety_stock = service_level_z * (
        (avg_lead_time * demand_std_dev ** 2) +
        (average_demand ** 2 * lead_time_std_dev ** 2)
    ) ** 0.5

    # Calculate reorder point
    reorder_point = (average_demand * avg_lead_time) + safety_stock

    return {
        "reorder_point": max(reorder_point, 1),  # Minimum 1 unit
        "safety_stock": safety_stock,
        "average_demand": average_demand,
        "demand_variability": demand_std_dev / average_demand if average_demand > 0 else 0,
        "lead_time_average": avg_lead_time,
        "service_level": 0.95
    }
```

---

## 🔄 **Multi-Output Configuration**

### **File Output Setup**

#### **JSON Output Configuration**

```json
{
  "output_path": "./warehouse_data",
  "output_format": "json",
  "file_output_config": {
    "partition_by": "date",
    "compression": "gzip",
    "max_file_size_mb": 100,
    "include_metadata": true,
    "timestamp_format": "iso8601"
  }
}
```

#### **CSV Output Configuration**

```json
{
  "output_format": "csv",
  "csv_config": {
    "delimiter": ",",
    "quote_char": "\"",
    "escape_char": "\\",
    "include_headers": true,
    "date_format": "%Y-%m-%d %H:%M:%S"
  }
}
```

#### **Parquet Output Configuration**

```json
{
  "output_format": "parquet",
  "parquet_config": {
    "compression": "snappy",
    "row_group_size": 10000,
    "page_size": 1024,
    "use_dictionary": true,
    "write_statistics": true
  }
}
```

### **Database Output Setup**

#### **PostgreSQL Configuration**

```json
{
  "database_url": "postgresql://user:password@localhost:5432/warehouse",
  "database_config": {
    "schema": "wms_data",
    "batch_size": 1000,
    "upsert_strategy": "merge",
    "create_tables": true,
    "add_timestamps": true
  }
}
```

#### **Oracle Database Configuration**

```json
{
  "database_url": "oracle://user:password@localhost:1521/ORCL",
  "database_config": {
    "schema": "WMS_ANALYTICS",
    "batch_size": 500,
    "use_bulk_insert": true,
    "commit_frequency": 1000,
    "connection_pool_size": 5
  }
}
```

### **API Output Setup**

#### **REST API Configuration**

```json
{
  "api_outputs": {
    "analytics_platform": {
      "enabled": true,
      "endpoint": "https://analytics.company.com/api/wms/data",
      "auth_type": "bearer_token",
      "auth_token": "${ANALYTICS_API_TOKEN}",
      "batch_size": 100,
      "retry_attempts": 3,
      "timeout_seconds": 30
    }
  }
}
```

#### **Webhook Configuration**

```json
{
  "webhooks": {
    "alert_notifications": {
      "enabled": true,
      "url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK",
      "headers": {
        "Content-Type": "application/json"
      },
      "payload_template": {
        "text": "WMS Alert: {alert_type} - {message}",
        "channel": "#warehouse-alerts"
      }
    }
  }
}
```

### **Multi-Destination Routing**

#### **Stream-Based Routing**

```json
{
  "output_routing": {
    "inventory": {
      "primary": "database",
      "secondary": ["file", "api"],
      "filters": {
        "high_value_items": {
          "condition": "unit_cost > 1000",
          "destinations": ["api", "webhook"]
        }
      }
    },
    "orders": {
      "primary": "file",
      "secondary": ["database"],
      "filters": {
        "rush_orders": {
          "condition": "priority > 5",
          "destinations": ["webhook"]
        }
      }
    }
  }
}
```

---

## ⚡ **Performance Tuning**

### **Throughput Optimization**

#### **Batch Processing Configuration**

```json
{
  "performance_config": {
    "batch_size": 2000,
    "max_workers": 8,
    "memory_limit_mb": 1024,
    "buffer_size": 10000,
    "flush_interval_seconds": 30
  }
}
```

#### **Parallel Processing Setup**

```python
from target_oracle_wms.performance import PerformanceOptimizer

def configure_high_throughput():
    """Configure target for high-throughput processing."""
    config = {
        "base_url": "https://wms.company.com",
        "username": "service_account",
        "password": "secure_password",

        # Performance optimizations
        "batch_size": 5000,          # Large batches for efficiency
        "max_workers": 12,           # Parallel processing
        "memory_limit_mb": 2048,     # Increased memory limit
        "enable_caching": True,      # Cache metadata and lookups
        "cache_ttl": 3600,          # 1-hour cache TTL

        # Connection pooling
        "connection_pool_size": 10,
        "max_connections": 20,
        "connection_timeout": 30,

        # Output optimization
        "output_buffer_size": 20000,
        "compress_outputs": True,
        "parallel_writes": True
    }

    return config
```

#### **Memory Management**

```python
def configure_memory_efficient():
    """Configure target for memory-efficient processing."""
    config = {
        # Reduce memory footprint
        "batch_size": 500,           # Smaller batches
        "max_workers": 4,            # Fewer workers
        "memory_limit_mb": 256,      # Limited memory
        "streaming_mode": True,      # Stream processing

        # Garbage collection tuning
        "gc_frequency": 100,         # Collect garbage every 100 records
        "clear_cache_frequency": 1000,  # Clear caches periodically

        # Disk-based processing
        "use_temp_files": True,
        "temp_dir": "/tmp/wms_processing",
        "cleanup_temp_files": True
    }

    return config
```

### **Monitoring and Metrics**

#### **Performance Monitoring Setup**

```python
from target_oracle_wms.monitoring import PerformanceMonitor

def setup_monitoring():
    """Set up comprehensive performance monitoring."""
    monitor = PerformanceMonitor()

    # Track processing metrics
    monitor.track_metrics([
        "records_per_second",
        "batch_processing_time",
        "memory_usage",
        "error_rate",
        "queue_depth"
    ])

    # Set up alerts
    monitor.add_alert("throughput_low", {
        "condition": "records_per_second < 1000",
        "severity": "warning",
        "cooldown_minutes": 5
    })

    monitor.add_alert("memory_high", {
        "condition": "memory_usage_mb > 1500",
        "severity": "critical",
        "cooldown_minutes": 1
    })

    return monitor

# Usage in target
monitor = setup_monitoring()

with monitor.track_processing("inventory") as tracker:
    # Process inventory records
    for batch in inventory_batches:
        process_batch(batch)
        tracker.record_batch(len(batch))
```

#### **Optimization Recommendations**

```python
def get_optimization_recommendations(monitor: PerformanceMonitor) -> list:
    """Get performance optimization recommendations."""
    recommendations = []

    metrics = monitor.get_performance_metrics()

    # Throughput optimization
    if metrics["records_per_second"] < 1000:
        recommendations.append({
            "type": "throughput",
            "recommendation": "Increase batch_size to 2000-5000",
            "expected_improvement": "20-40% throughput increase"
        })

    # Memory optimization
    if metrics["memory_usage_mb"] > 1000:
        recommendations.append({
            "type": "memory",
            "recommendation": "Enable streaming_mode or reduce batch_size",
            "expected_improvement": "30-50% memory reduction"
        })

    # Worker optimization
    if metrics["queue_depth"] > 1000:
        recommendations.append({
            "type": "workers",
            "recommendation": "Increase max_workers (current CPU cores + 2)",
            "expected_improvement": "15-25% throughput increase"
        })

    return recommendations
```

---

## 🚀 **Production Deployment**

### **Container Deployment**

#### **Docker Configuration**

```dockerfile
# Dockerfile for production deployment
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install target package
RUN pip install -e .

# Create non-root user
RUN useradd -m -u 1000 wms && chown -R wms:wms /app
USER wms

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD target-oracle-wms --config /app/config/config.json --health-check

# Default command
CMD ["target-oracle-wms", "--config", "/app/config/config.json"]
```

#### **Docker Compose Configuration**

```yaml
version: "3.8"

services:
  target-oracle-wms:
    build: .
    container_name: target-oracle-wms
    restart: unless-stopped
    environment:
      - WMS_BASE_URL=${WMS_BASE_URL}
      - WMS_USERNAME=${WMS_USERNAME}
      - WMS_PASSWORD=${WMS_PASSWORD}
      - LOG_LEVEL=INFO
    volumes:
      - ./config:/app/config:ro
      - ./output:/app/output
      - ./logs:/app/logs
    networks:
      - wms-network
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15
    container_name: wms-postgres
    restart: unless-stopped
    environment:
      - POSTGRES_DB=wms_analytics
      - POSTGRES_USER=wms_user
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - wms-network

  redis:
    image: redis:7-alpine
    container_name: wms-redis
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    networks:
      - wms-network

volumes:
  postgres_data:
  redis_data:

networks:
  wms-network:
    driver: bridge
```

### **Kubernetes Deployment**

#### **Deployment Configuration**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: target-oracle-wms
  namespace: warehouse
spec:
  replicas: 3
  selector:
    matchLabels:
      app: target-oracle-wms
  template:
    metadata:
      labels:
        app: target-oracle-wms
    spec:
      containers:
        - name: target-oracle-wms
          image: target-oracle-wms:latest
          ports:
            - containerPort: 8080
          env:
            - name: WMS_BASE_URL
              valueFrom:
                secretKeyRef:
                  name: wms-secrets
                  key: base_url
            - name: WMS_USERNAME
              valueFrom:
                secretKeyRef:
                  name: wms-secrets
                  key: username
            - name: WMS_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: wms-secrets
                  key: password
          resources:
            requests:
              memory: "512Mi"
              cpu: "250m"
            limits:
              memory: "1Gi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
          volumeMounts:
            - name: config-volume
              mountPath: /app/config
            - name: output-volume
              mountPath: /app/output
      volumes:
        - name: config-volume
          configMap:
            name: wms-config
        - name: output-volume
          persistentVolumeClaim:
            claimName: wms-output-pvc
```

#### **ConfigMap Configuration**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: wms-config
  namespace: warehouse
data:
  config.json: |
    {
      "base_url": "${WMS_BASE_URL}",
      "username": "${WMS_USERNAME}",
      "password": "${WMS_PASSWORD}",
      "enable_kpi_calculation": true,
      "enable_alerts": true,
      "batch_size": 2000,
      "max_workers": 6,
      "memory_limit_mb": 768,
      "output_path": "/app/output",
      "database_url": "postgresql://wms_user:${POSTGRES_PASSWORD}@postgres:5432/wms_analytics"
    }
```

### **Monitoring and Observability**

#### **Prometheus Metrics**

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
records_processed = Counter('wms_records_processed_total', 'Total records processed', ['stream'])
processing_time = Histogram('wms_processing_seconds', 'Time spent processing records')
active_connections = Gauge('wms_active_connections', 'Active WMS connections')
error_count = Counter('wms_errors_total', 'Total errors', ['error_type'])

def setup_prometheus_metrics():
    """Set up Prometheus metrics collection."""
    # Start metrics server
    start_http_server(8000)

    # Register custom metrics
    from target_oracle_wms.monitoring import MetricsCollector

    collector = MetricsCollector()
    collector.register_counter(records_processed)
    collector.register_histogram(processing_time)
    collector.register_gauge(active_connections)
    collector.register_counter(error_count)

    return collector
```

#### **Logging Configuration**

```yaml
# logging.yaml
version: 1
formatters:
  structured:
    format: '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s", "extra": %(extra)s}'
handlers:
  console:
    class: logging.StreamHandler
    formatter: structured
    stream: ext://sys.stdout
  file:
    class: logging.handlers.RotatingFileHandler
    formatter: structured
    filename: /app/logs/target-oracle-wms.log
    maxBytes: 10485760 # 10MB
    backupCount: 5
loggers:
  target_oracle_wms:
    level: INFO
    handlers: [console, file]
    propagate: false
  singer_sdk:
    level: WARNING
    handlers: [console, file]
    propagate: false
root:
  level: INFO
  handlers: [console]
```

---

## 🔧 **Troubleshooting**

### **Common Issues and Solutions**

#### **Connection Issues**

**Problem**: `ConnectionError: Unable to connect to Oracle WMS API`

```bash
# Diagnosis
curl -v https://your-wms.company.com/api/health
nslookup your-wms.company.com
telnet your-wms.company.com 443

# Solution
# 1. Check network connectivity
ping your-wms.company.com

# 2. Verify SSL certificate
openssl s_client -connect your-wms.company.com:443 -servername your-wms.company.com

# 3. Test with curl
curl -k -u "username:password" https://your-wms.company.com/api/health
```

**Problem**: `AuthenticationError: Invalid credentials`

```python
# Verification script
import requests
from base64 import b64encode

def test_authentication():
    """Test WMS authentication."""
    credentials = b64encode(b"username:password").decode()
    headers = {"Authorization": f"Basic {credentials}"}

    response = requests.get(
        "https://your-wms.company.com/api/health",
        headers=headers,
        timeout=30
    )

    if response.status_code == 200:
        print("✅ Authentication successful")
    elif response.status_code == 401:
        print("❌ Invalid credentials")
    else:
        print(f"⚠️ Unexpected response: {response.status_code}")
```

#### **Performance Issues**

**Problem**: Low throughput (< 1000 records/second)

```json
// Optimization configuration
{
  "batch_size": 5000,
  "max_workers": 12,
  "memory_limit_mb": 2048,
  "enable_caching": true,
  "connection_pool_size": 10,
  "parallel_writes": true
}
```

**Problem**: High memory usage

```json
// Memory-efficient configuration
{
  "batch_size": 500,
  "max_workers": 4,
  "streaming_mode": true,
  "gc_frequency": 100,
  "use_temp_files": true
}
```

#### **Data Quality Issues**

**Problem**: Missing or invalid data

```python
def validate_data_quality():
    """Comprehensive data quality validation."""
    from target_oracle_wms.validation import DataValidator

    validator = DataValidator()

    # Add validation rules
    validator.add_rule("inventory", "quantity_positive",
                      lambda r: r.get("quantity", 0) >= 0)
    validator.add_rule("orders", "valid_status",
                      lambda r: r.get("status") in ["OPEN", "ALLOCATED", "PICKED", "SHIPPED"])

    # Validate stream
    validation_results = validator.validate_stream("inventory", records)

    if not validation_results.is_valid:
        print("❌ Data quality issues:")
        for error in validation_results.errors:
            print(f"  - {error}")
```

### **Debug Mode Setup**

#### **Enable Debug Logging**

```json
{
  "log_level": "DEBUG",
  "debug_mode": true,
  "debug_output_path": "./debug",
  "save_raw_records": true,
  "trace_processing": true
}
```

#### **Debug Tools**

```bash
# Enable trace mode
export SINGER_DEBUG=1
export WMS_DEBUG_MODE=1

# Run with verbose output
target-oracle-wms --config config.json --debug --trace

# Save debug information
target-oracle-wms --config config.json --debug-output ./debug_logs
```

### **Health Checks**

#### **System Health Validation**

```python
def comprehensive_health_check():
    """Run comprehensive system health check."""
    checks = {
        "wms_connectivity": test_wms_connection(),
        "database_connectivity": test_database_connection(),
        "memory_usage": check_memory_usage(),
        "disk_space": check_disk_space(),
        "configuration": validate_configuration(),
        "dependencies": check_dependencies()
    }

    all_healthy = all(checks.values())

    print("🏥 System Health Check Results:")
    for check_name, status in checks.items():
        icon = "✅" if status else "❌"
        print(f"  {icon} {check_name}")

    return all_healthy
```

---

## 🔗 **Cross-References**

### **Related Documentation**

- [Architecture Guide](../architecture/README.md) - Technical architecture and design patterns
- [API Reference](../api/README.md) - Complete API specification and examples
- [Security Guide](../security/README.md) - Security implementation and best practices
- [Performance Patterns](../patterns/README.md) - Advanced patterns and optimizations

### **External Resources**

- [Singer Specification](https://hub.meltano.com/singer/spec) - Official Singer protocol documentation
- [Oracle WMS 25B Implementation Guide](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsig/) - Oracle's official implementation guide
- [Meltano Documentation](https://docs.meltano.com/) - Meltano platform documentation

### **Business Intelligence Resources**

- [Warehouse KPI Best Practices](https://www.smartsheet.com/content/kpi-dashboard-best-practices) - Industry standard KPI definitions
- [Supply Chain Metrics](https://www.ibm.com/topics/supply-chain-management) - Comprehensive supply chain metrics
- [Oracle WMS Performance Tuning](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmspt/) - Performance optimization guide

---

**📘 Implementation Guides**: Target Oracle WMS | **🏠 Root**: [PyAuto Home](../../../README.md) | **Framework**: Singer SDK 0.39.0+ | **Updated**: 2025-06-19
