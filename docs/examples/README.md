# 💡 Target Oracle WMS - Examples & Tutorials

> **Function**: Practical examples and tutorials from basic to advanced business scenarios | **Audience**: All technical audiences | **Status**: Enterprise Reference

[![Singer](https://img.shields.io/badge/singer-target-blue.svg)](https://www.singer.io/)
[![Oracle](https://img.shields.io/badge/oracle-WMS-red.svg)](https://www.oracle.com/cx/retail/warehouse-management/)
[![Examples](https://img.shields.io/badge/examples-comprehensive-blue.svg)](../README.md)
[![Documentation](https://img.shields.io/badge/docs-comprehensive-blue.svg)](../README.md)

Comprehensive collection of practical examples and step-by-step tutorials demonstrating Oracle WMS Singer target implementation from basic data loading to advanced business scenarios, validated against [Singer specification](https://hub.meltano.com/singer/spec) and [Oracle WMS 25B use cases](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsig/).

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto](../../../README.md) → **📂 Project**: [Target Oracle WMS](../../README.md) → **📁 Docs**: [Documentation](../README.md) → **📄 Current**: Examples & Tutorials

---

## 📋 **Examples Overview**

This section provides hands-on examples covering all aspects of Oracle WMS Singer target usage, from simple data loading to complex business intelligence scenarios with real-world business logic implementation.

### **Example Categories**

- **Basic Data Loading**: Simple data loading examples for getting started
- **KPI Calculation**: Business metric calculation and analytics examples
- **Alert Configuration**: Alert rules and notification setup examples
- **Custom Business Logic**: Advanced business rule implementation
- **Multi-Pipeline Integration**: Complex ETL pipeline patterns and workflows
- **Production Scenarios**: Real-world deployment and operational examples

### **Tutorial Progression**

Examples are organized in progressive complexity:

1. **Beginner**: Basic setup and simple data loading
2. **Intermediate**: Business logic configuration and multi-output setup
3. **Advanced**: Custom business rules and complex integrations
4. **Expert**: Production deployment and performance optimization

---

## 🚀 **Basic Data Loading Examples**

### **Example 1: Simple Inventory Data Loading**

#### **Scenario**: Basic inventory data loading from CSV to Oracle WMS format

```bash
# Create sample inventory CSV
cat > inventory_sample.csv << EOF
item_id,location_id,quantity,unit_cost
ITEM001,LOC-A-01-01,100,25.50
ITEM002,LOC-A-01-02,75,18.25
ITEM003,LOC-B-02-01,200,12.75
EOF

# Convert CSV to Singer format
tap-csv --config tap_config.json --catalog catalog.json | \
  target-oracle-wms --config config.json
```

#### **Configuration Files**

**tap_config.json**:

```json
{
  "files": [
    {
      "entity": "inventory",
      "path": "inventory_sample.csv",
      "keys": ["item_id", "location_id"]
    }
  ]
}
```

**config.json**:

```json
{
  "base_url": "https://wms.company.com",
  "username": "wms_user",
  "password": "secure_password",
  "output_path": "./output",
  "output_format": "json",
  "enable_kpi_calculation": false,
  "enable_alerts": false
}
```

#### **Expected Output**

```json
{
  "type": "RECORD",
  "stream": "inventory",
  "record": {
    "item_id": "ITEM001",
    "location_id": "LOC-A-01-01",
    "quantity": 100,
    "unit_cost": 25.5,
    "total_value": 2550.0,
    "processed_at": "2025-06-19T10:30:00Z"
  }
}
```

### **Example 2: Order Data Processing**

#### **Scenario**: Processing order data with basic business logic

```python
# orders_example.py
import json
from datetime import datetime
from target_oracle_wms import TargetOracleWMS

def process_order_data():
    """Process sample order data with basic business logic."""

    # Sample order data
    order_records = [
        {
            "type": "RECORD",
            "stream": "orders",
            "record": {
                "order_id": "ORD-2025-001",
                "customer_id": "CUST-001",
                "order_date": "2025-06-19T08:00:00Z",
                "requested_ship_date": "2025-06-20T17:00:00Z",
                "priority": 5,
                "total_lines": 3,
                "status": "OPEN"
            }
        },
        {
            "type": "RECORD",
            "stream": "order_lines",
            "record": {
                "order_id": "ORD-2025-001",
                "line_number": 1,
                "item_id": "ITEM001",
                "ordered_quantity": 10,
                "unit_price": 25.50
            }
        }
    ]

    # Configuration
    config = {
        "base_url": "https://wms.company.com",
        "username": "wms_user",
        "password": "secure_password",
        "enable_kpi_calculation": True,
        "output_format": "json"
    }

    # Process records
    target = TargetOracleWMS(config=config)

    for record in order_records:
        target.process_record(record)

    print("✅ Order data processed successfully")

if __name__ == "__main__":
    process_order_data()
```

### **Example 3: Multi-Stream Processing**

#### **Scenario**: Processing multiple streams in a single pipeline

```bash
#!/bin/bash
# multi_stream_example.sh

# Configuration
CONFIG_FILE="config.json"
OUTPUT_DIR="./output"

# Create output directory
mkdir -p $OUTPUT_DIR

# Process inventory stream
echo "📦 Processing inventory data..."
cat inventory_data.jsonl | \
  target-oracle-wms --config $CONFIG_FILE \
                    --stream inventory \
                    --output-path $OUTPUT_DIR/inventory

# Process orders stream
echo "📋 Processing orders data..."
cat orders_data.jsonl | \
  target-oracle-wms --config $CONFIG_FILE \
                    --stream orders \
                    --output-path $OUTPUT_DIR/orders

# Process shipments stream
echo "🚚 Processing shipments data..."
cat shipments_data.jsonl | \
  target-oracle-wms --config $CONFIG_FILE \
                    --stream shipments \
                    --output-path $OUTPUT_DIR/shipments

echo "✅ All streams processed successfully"
```

---

## 📊 **KPI Calculation Examples**

### **Example 4: Inventory Turnover Analysis**

#### **Scenario**: Calculate inventory turnover ratios with historical context

```python
# inventory_kpi_example.py
from target_oracle_wms.business_logic import InventoryKPICalculator
from datetime import datetime, timedelta

def calculate_inventory_turnover():
    """Calculate comprehensive inventory turnover metrics."""

    # Sample inventory record
    inventory_record = {
        "item_id": "ITEM001",
        "location_id": "LOC-A-01-01",
        "on_hand_quantity": 150,
        "unit_cost": 25.50,
        "total_value": 3825.00,
        "last_update_date": "2025-06-19T10:30:00Z"
    }

    # Historical sales data (simulated)
    historical_context = {
        "sales_history": {
            "ITEM001": [
                {"date": "2025-05-19", "quantity_sold": 45},
                {"date": "2025-04-19", "quantity_sold": 52},
                {"date": "2025-03-19", "quantity_sold": 38},
                {"date": "2025-02-19", "quantity_sold": 41},
                {"date": "2025-01-19", "quantity_sold": 44}
            ]
        },
        "cost_of_goods_sold": {
            "ITEM001": 4590.00  # Last 12 months
        }
    }

    # Initialize KPI calculator
    config = {
        "turnover_period_days": 365,
        "minimum_history_months": 3
    }
    calculator = InventoryKPICalculator(config)

    # Calculate KPIs
    kpis = calculator.calculate_inventory_kpis(
        record=inventory_record,
        context=historical_context
    )

    # Display results
    print("📊 Inventory KPI Analysis")
    print(f"Item: {inventory_record['item_id']}")
    print(f"Inventory Turnover Ratio: {kpis['inventory_turnover']:.2f}")
    print(f"Days of Supply: {kpis['days_of_supply']:.1f}")
    print(f"ABC Classification: {kpis['abc_classification']}")
    print(f"Carrying Cost Ratio: {kpis['carrying_cost_ratio']:.2%}")
    print(f"Stockout Risk: {kpis['stockout_risk']:.2%}")

    return kpis

if __name__ == "__main__":
    kpis = calculate_inventory_turnover()
```

### **Example 5: Order Fulfillment Performance**

#### **Scenario**: Track order fulfillment metrics and cycle times

```python
# order_fulfillment_example.py
from target_oracle_wms.business_logic import OrderKPICalculator
from datetime import datetime

def analyze_order_fulfillment():
    """Analyze order fulfillment performance metrics."""

    # Sample order with fulfillment timeline
    order_record = {
        "order_id": "ORD-2025-001",
        "customer_id": "CUST-001",
        "order_date": "2025-06-18T08:00:00Z",
        "requested_ship_date": "2025-06-19T17:00:00Z",
        "actual_ship_date": "2025-06-19T15:30:00Z",
        "total_lines": 3,
        "total_quantity": 25,
        "status": "SHIPPED",
        "fulfillment_timeline": {
            "order_received": "2025-06-18T08:00:00Z",
            "allocation_completed": "2025-06-18T10:30:00Z",
            "picking_completed": "2025-06-19T09:15:00Z",
            "packing_completed": "2025-06-19T14:00:00Z",
            "shipped": "2025-06-19T15:30:00Z"
        }
    }

    # Business context
    performance_context = {
        "sla_requirements": {
            "allocation_hours": 4,
            "picking_hours": 16,
            "packing_hours": 4,
            "total_cycle_hours": 24
        },
        "quality_standards": {
            "accuracy_target": 0.995,
            "damage_rate_max": 0.002
        }
    }

    # Initialize calculator
    calculator = OrderKPICalculator(config={})

    # Calculate fulfillment KPIs
    kpis = calculator.calculate_order_kpis(
        record=order_record,
        context=performance_context
    )

    # Display results
    print("📋 Order Fulfillment Analysis")
    print(f"Order ID: {order_record['order_id']}")
    print(f"Cycle Time: {kpis['cycle_time_hours']:.1f} hours")
    print(f"On-Time Delivery: {'✅' if kpis['on_time_delivery_rate'] >= 1.0 else '❌'}")
    print(f"Perfect Order Rate: {kpis['perfect_order_rate']:.2%}")
    print(f"Fulfillment Rate: {kpis['fulfillment_rate']:.2%}")
    print(f"Cost per Order: ${kpis['cost_per_order']:.2f}")

    # SLA compliance check
    if kpis['cycle_time_hours'] <= performance_context['sla_requirements']['total_cycle_hours']:
        print("✅ SLA Compliance: PASSED")
    else:
        print("❌ SLA Compliance: FAILED")

    return kpis

if __name__ == "__main__":
    kpis = analyze_order_fulfillment()
```

### **Example 6: Warehouse Productivity Metrics**

#### **Scenario**: Calculate warehouse operational efficiency KPIs

```python
# warehouse_productivity_example.py
from target_oracle_wms.business_logic import WarehouseKPICalculator
from datetime import datetime, timedelta

def calculate_warehouse_productivity():
    """Calculate comprehensive warehouse productivity metrics."""

    # Sample warehouse operation data
    warehouse_records = [
        {
            "task_id": "PICK-001",
            "worker_id": "WRK-001",
            "task_type": "PICKING",
            "start_time": "2025-06-19T08:00:00Z",
            "end_time": "2025-06-19T10:30:00Z",
            "lines_processed": 75,
            "items_processed": 150,
            "accuracy_rate": 0.997
        },
        {
            "task_id": "PACK-001",
            "worker_id": "WRK-002",
            "task_type": "PACKING",
            "start_time": "2025-06-19T09:00:00Z",
            "end_time": "2025-06-19T11:00:00Z",
            "packages_processed": 45,
            "accuracy_rate": 0.998
        }
    ]

    # Performance context
    productivity_context = {
        "performance_targets": {
            "picks_per_hour": 120,
            "lines_per_hour": 60,
            "packages_per_hour": 25,
            "accuracy_target": 0.995
        },
        "space_utilization": {
            "total_locations": 10000,
            "occupied_locations": 8500,
            "reserved_locations": 500
        }
    }

    # Initialize calculator
    calculator = WarehouseKPICalculator(config={})

    # Process each task record
    total_productivity = {
        "total_hours": 0,
        "total_picks": 0,
        "total_lines": 0,
        "total_packages": 0,
        "accuracy_sum": 0,
        "task_count": 0
    }

    for record in warehouse_records:
        # Calculate task-specific KPIs
        kpis = calculator.calculate_warehouse_kpis(
            record=record,
            context=productivity_context
        )

        # Aggregate metrics
        start_time = datetime.fromisoformat(record['start_time'].replace('Z', '+00:00'))
        end_time = datetime.fromisoformat(record['end_time'].replace('Z', '+00:00'))
        hours_worked = (end_time - start_time).total_seconds() / 3600

        total_productivity['total_hours'] += hours_worked
        total_productivity['total_picks'] += record.get('items_processed', 0)
        total_productivity['total_lines'] += record.get('lines_processed', 0)
        total_productivity['total_packages'] += record.get('packages_processed', 0)
        total_productivity['accuracy_sum'] += record.get('accuracy_rate', 0)
        total_productivity['task_count'] += 1

        print(f"📋 Task: {record['task_id']} ({record['task_type']})")
        print(f"   Labor Productivity: {kpis['labor_productivity']:.1f}")
        print(f"   Throughput Rate: {kpis['throughput_rate']:.1f}")
        print(f"   Operational Cost: ${kpis['operational_cost']:.2f}")

    # Calculate overall productivity
    if total_productivity['total_hours'] > 0:
        overall_picks_per_hour = total_productivity['total_picks'] / total_productivity['total_hours']
        overall_lines_per_hour = total_productivity['total_lines'] / total_productivity['total_hours']
        overall_accuracy = total_productivity['accuracy_sum'] / total_productivity['task_count']

        print("\n📊 Overall Warehouse Productivity")
        print(f"Picks per Hour: {overall_picks_per_hour:.1f}")
        print(f"Lines per Hour: {overall_lines_per_hour:.1f}")
        print(f"Overall Accuracy: {overall_accuracy:.2%}")

        # Space utilization
        space_util = calculator.calculate_space_utilization(productivity_context['space_utilization'])
        print(f"Space Utilization: {space_util:.2%}")

    return total_productivity

if __name__ == "__main__":
    productivity = calculate_warehouse_productivity()
```

---

## 🚨 **Alert Configuration Examples**

### **Example 7: Inventory Alert Setup**

#### **Scenario**: Configure comprehensive inventory alerting system

```python
# inventory_alerts_example.py
from target_oracle_wms.alerts import AlertGenerator
from datetime import datetime, timedelta

def setup_inventory_alerts():
    """Configure comprehensive inventory alerting system."""

    # Alert configuration
    alert_config = {
        "alert_rules": {
            "inventory": {
                "low_stock": {
                    "enabled": True,
                    "threshold_type": "percentage",
                    "threshold_value": 0.15,  # 15% of reorder point
                    "severity": "high",
                    "notification_channels": ["email", "slack"],
                    "escalation_hours": 4
                },
                "expiry_warning": {
                    "enabled": True,
                    "days_before_expiry": [30, 14, 7, 1],
                    "severity_map": {
                        30: "low",
                        14: "medium",
                        7: "high",
                        1: "critical"
                    },
                    "notification_channels": ["email"]
                },
                "overstock": {
                    "enabled": True,
                    "threshold_multiplier": 2.5,  # 2.5x max stock level
                    "severity": "medium",
                    "notification_channels": ["slack"]
                }
            }
        },
        "notification_config": {
            "email": {
                "smtp_server": "smtp.company.com",
                "smtp_port": 587,
                "username": "alerts@company.com",
                "recipients": ["warehouse@company.com", "purchasing@company.com"]
            },
            "slack": {
                "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK",
                "channel": "#warehouse-alerts"
            }
        }
    }

    # Sample inventory data with potential alerts
    inventory_records = [
        {
            "item_id": "ITEM001",
            "location_id": "LOC-A-01-01",
            "on_hand_quantity": 15,
            "reorder_point": 100,
            "max_stock_level": 500,
            "expiration_date": "2025-07-15T00:00:00Z",
            "status": "ACTIVE"
        },
        {
            "item_id": "ITEM002",
            "location_id": "LOC-B-02-01",
            "on_hand_quantity": 1250,
            "reorder_point": 200,
            "max_stock_level": 500,
            "expiration_date": "2025-12-31T00:00:00Z",
            "status": "ACTIVE"
        },
        {
            "item_id": "ITEM003",
            "location_id": "LOC-C-03-01",
            "on_hand_quantity": 50,
            "reorder_point": 75,
            "max_stock_level": 300,
            "expiration_date": "2025-06-25T00:00:00Z",  # Expires in 6 days
            "status": "ACTIVE"
        }
    ]

    # Initialize alert generator
    alert_generator = AlertGenerator(alert_config)

    # Process records and generate alerts
    all_alerts = []

    for record in inventory_records:
        alerts = alert_generator.generate_alerts("inventory", record)
        all_alerts.extend(alerts)

        print(f"📦 Item: {record['item_id']}")
        print(f"   Quantity: {record['on_hand_quantity']}")
        print(f"   Alerts Generated: {len(alerts)}")

        for alert in alerts:
            print(f"   🚨 {alert['type'].upper()}: {alert['message']} ({alert['severity']})")

    # Send notifications
    alert_generator.send_notifications(all_alerts)

    print(f"\n📊 Alert Summary: {len(all_alerts)} alerts generated")
    return all_alerts

def create_custom_alert_rule():
    """Example of creating custom alert rule."""

    from target_oracle_wms.alerts import register_alert_rule

    @register_alert_rule("inventory", "abc_classification_alert")
    def check_abc_classification_stock(record: dict, context: dict) -> list:
        """Generate alerts based on ABC classification and stock levels."""
        alerts = []

        abc_class = record.get("abc_classification", "C")
        on_hand = float(record.get("on_hand_quantity", 0))
        reorder_point = float(record.get("reorder_point", 0))

        # A-class items: Critical, higher safety stock
        if abc_class == "A" and on_hand < (reorder_point * 1.5):
            alerts.append({
                "type": "abc_a_low_stock",
                "severity": "critical",
                "item_id": record.get("item_id"),
                "message": f"A-class item {record.get('item_id')} below safety threshold",
                "current_quantity": on_hand,
                "threshold": reorder_point * 1.5
            })

        # B-class items: Important, standard safety stock
        elif abc_class == "B" and on_hand < (reorder_point * 1.2):
            alerts.append({
                "type": "abc_b_low_stock",
                "severity": "high",
                "item_id": record.get("item_id"),
                "message": f"B-class item {record.get('item_id')} below threshold",
                "current_quantity": on_hand,
                "threshold": reorder_point * 1.2
            })

        return alerts

    print("✅ Custom ABC classification alert rule registered")

if __name__ == "__main__":
    alerts = setup_inventory_alerts()
    create_custom_alert_rule()
```

### **Example 8: Order Processing Alerts**

#### **Scenario**: Real-time order processing alert system

```python
# order_alerts_example.py
from target_oracle_wms.alerts import AlertGenerator
from datetime import datetime, timedelta

def setup_order_alerts():
    """Configure real-time order processing alerts."""

    # Order alert configuration
    alert_config = {
        "alert_rules": {
            "orders": {
                "sla_breach": {
                    "enabled": True,
                    "allocation_sla_hours": 4,
                    "picking_sla_hours": 8,
                    "packing_sla_hours": 2,
                    "shipping_sla_hours": 24,
                    "severity": "high",
                    "notification_channels": ["email", "slack", "webhook"]
                },
                "allocation_failure": {
                    "enabled": True,
                    "max_attempts": 3,
                    "retry_interval_minutes": 30,
                    "severity": "medium",
                    "notification_channels": ["slack"]
                },
                "high_priority_delay": {
                    "enabled": True,
                    "priority_threshold": 8,
                    "delay_threshold_minutes": 60,
                    "severity": "critical",
                    "notification_channels": ["email", "slack", "pager"]
                }
            }
        }
    }

    # Sample order data with timing issues
    order_records = [
        {
            "order_id": "ORD-2025-001",
            "priority": 9,  # High priority
            "status": "ALLOCATION_FAILED",
            "order_date": "2025-06-19T08:00:00Z",
            "allocation_attempts": 3,
            "last_allocation_attempt": "2025-06-19T10:30:00Z",
            "requested_ship_date": "2025-06-19T17:00:00Z"
        },
        {
            "order_id": "ORD-2025-002",
            "priority": 5,
            "status": "PICKING",
            "order_date": "2025-06-18T14:00:00Z",
            "allocation_completed": "2025-06-18T16:00:00Z",  # 2 hours (within SLA)
            "picking_started": "2025-06-19T08:00:00Z",
            "requested_ship_date": "2025-06-20T12:00:00Z"
        }
    ]

    # Initialize alert generator
    alert_generator = AlertGenerator(alert_config)

    # Process order records
    all_alerts = []
    current_time = datetime.utcnow()

    for record in order_records:
        # Add timing context
        context = {"current_time": current_time}

        alerts = alert_generator.generate_alerts("orders", record, context)
        all_alerts.extend(alerts)

        print(f"📋 Order: {record['order_id']} (Priority: {record['priority']})")
        print(f"   Status: {record['status']}")
        print(f"   Alerts: {len(alerts)}")

        for alert in alerts:
            severity_icon = {"low": "💛", "medium": "🟠", "high": "🔴", "critical": "🚨"}
            icon = severity_icon.get(alert['severity'], "⚪")
            print(f"   {icon} {alert['type']}: {alert['message']}")

    print(f"\n📊 Total Alerts Generated: {len(all_alerts)}")
    return all_alerts

if __name__ == "__main__":
    alerts = setup_order_alerts()
```

---

## 🔧 **Custom Business Logic Examples**

### **Example 9: Advanced Inventory Optimization**

#### **Scenario**: Implement AI-driven inventory optimization algorithms

```python
# advanced_inventory_optimization.py
from target_oracle_wms import register_business_rule
import numpy as np
from datetime import datetime, timedelta

@register_business_rule("inventory", "ai_optimization")
def optimize_inventory_levels(record: dict, context: dict) -> dict:
    """
    AI-driven inventory optimization with demand forecasting.

    Implements machine learning models for optimal stock level calculation.
    """
    item_id = record.get("item_id")
    current_stock = float(record.get("on_hand_quantity", 0))

    # Get historical data
    demand_history = context.get("demand_history", {}).get(item_id, [])
    seasonality_data = context.get("seasonality", {}).get(item_id, {})
    supplier_data = context.get("supplier_performance", {}).get(item_id, {})

    if len(demand_history) < 12:  # Need at least 12 periods
        return {"optimization_status": "insufficient_data"}

    # Demand forecasting using exponential smoothing
    forecast = calculate_exponential_smoothing_forecast(
        demand_history,
        periods=4,
        alpha=0.3,
        beta=0.1,
        gamma=0.1
    )

    # Calculate optimal stock levels
    service_level = context.get("service_level_target", 0.95)
    lead_time_variability = supplier_data.get("lead_time_std_dev", 2)
    demand_variability = np.std(demand_history[-12:])

    # Safety stock calculation with variability
    z_score = get_z_score_for_service_level(service_level)
    safety_stock = z_score * np.sqrt(
        (np.mean(demand_history[-6:]) * lead_time_variability**2) +
        (supplier_data.get("avg_lead_time", 14)**2 * demand_variability**2)
    )

    # Optimal order quantity (Economic Order Quantity + adjustments)
    annual_demand = sum(demand_history[-12:])
    ordering_cost = context.get("ordering_cost", 50)
    holding_cost_rate = context.get("holding_cost_rate", 0.25)
    unit_cost = float(record.get("unit_cost", 1))

    eoq = np.sqrt(
        (2 * annual_demand * ordering_cost) /
        (holding_cost_rate * unit_cost)
    )

    # Seasonality adjustment
    seasonal_factor = get_seasonal_adjustment(
        datetime.utcnow().month,
        seasonality_data
    )

    adjusted_eoq = eoq * seasonal_factor
    reorder_point = (np.mean(forecast) * supplier_data.get("avg_lead_time", 14)) + safety_stock
    max_stock = reorder_point + adjusted_eoq

    # Generate recommendations
    recommendations = []

    if current_stock < reorder_point:
        order_quantity = max_stock - current_stock
        recommendations.append({
            "action": "place_order",
            "quantity": order_quantity,
            "urgency": "high" if current_stock < safety_stock else "medium",
            "expected_stockout_date": calculate_stockout_date(current_stock, np.mean(forecast))
        })

    if current_stock > max_stock * 1.5:
        recommendations.append({
            "action": "reduce_stock",
            "excess_quantity": current_stock - max_stock,
            "suggestions": ["promotion", "transfer", "return_to_supplier"]
        })

    return {
        "optimization_results": {
            "current_stock": current_stock,
            "forecasted_demand": forecast,
            "optimal_reorder_point": reorder_point,
            "optimal_max_stock": max_stock,
            "optimal_order_quantity": adjusted_eoq,
            "safety_stock": safety_stock,
            "service_level": service_level,
            "seasonal_factor": seasonal_factor
        },
        "recommendations": recommendations,
        "confidence_score": calculate_confidence_score(demand_history, seasonality_data),
        "optimization_status": "completed"
    }

def calculate_exponential_smoothing_forecast(data: list, periods: int, alpha: float, beta: float, gamma: float) -> list:
    """Calculate demand forecast using triple exponential smoothing."""
    if len(data) < 24:  # Need at least 2 years for seasonality
        # Simple exponential smoothing
        forecast = [data[-1]]
        for _ in range(periods - 1):
            forecast.append(forecast[-1] * alpha + data[-1] * (1 - alpha))
        return forecast

    # Triple exponential smoothing implementation
    season_length = 12  # Monthly seasonality
    initial_trend = sum(data[season_length:2*season_length]) - sum(data[:season_length])
    initial_trend /= season_length**2

    # Initialize components
    level = sum(data[:season_length]) / season_length
    trend = initial_trend
    seasonal = [data[i] / level for i in range(season_length)]

    forecast = []

    # Generate forecast
    for h in range(1, periods + 1):
        forecast_value = (level + h * trend) * seasonal[(len(data) + h - 1) % season_length]
        forecast.append(max(0, forecast_value))  # Ensure non-negative

    return forecast

def get_z_score_for_service_level(service_level: float) -> float:
    """Get Z-score for given service level."""
    z_scores = {
        0.90: 1.28,
        0.95: 1.65,
        0.97: 1.88,
        0.99: 2.33,
        0.995: 2.58
    }
    return z_scores.get(service_level, 1.65)

def get_seasonal_adjustment(month: int, seasonality_data: dict) -> float:
    """Get seasonal adjustment factor for given month."""
    if not seasonality_data:
        return 1.0

    seasonal_factors = seasonality_data.get("monthly_factors", {})
    return seasonal_factors.get(str(month), 1.0)

def calculate_stockout_date(current_stock: float, daily_demand: float) -> str:
    """Calculate expected stockout date."""
    if daily_demand <= 0:
        return "N/A"

    days_until_stockout = current_stock / daily_demand
    stockout_date = datetime.utcnow() + timedelta(days=days_until_stockout)
    return stockout_date.isoformat()

def calculate_confidence_score(demand_history: list, seasonality_data: dict) -> float:
    """Calculate confidence score for optimization results."""
    base_score = min(len(demand_history) / 24, 1.0)  # More history = higher confidence

    # Adjust for demand variability
    if len(demand_history) >= 3:
        cv = np.std(demand_history) / np.mean(demand_history) if np.mean(demand_history) > 0 else 1
        variability_penalty = max(0, 1 - cv)
        base_score *= variability_penalty

    # Adjust for seasonality data availability
    if seasonality_data:
        base_score *= 1.1

    return min(base_score, 1.0)

# Example usage
def run_inventory_optimization_example():
    """Run comprehensive inventory optimization example."""

    # Sample data
    inventory_record = {
        "item_id": "WIDGET-001",
        "on_hand_quantity": 75,
        "unit_cost": 15.50,
        "reorder_point": 100,
        "max_stock_level": 500
    }

    context = {
        "demand_history": [45, 52, 38, 41, 44, 49, 55, 48, 42, 46, 51, 47,
                          58, 65, 52, 55, 59, 62, 68, 61, 57, 59, 64, 60],  # 24 months
        "seasonality": {
            "WIDGET-001": {
                "monthly_factors": {
                    "1": 0.9, "2": 0.85, "3": 0.95, "4": 1.05,
                    "5": 1.1, "6": 1.15, "7": 1.2, "8": 1.15,
                    "9": 1.1, "10": 1.05, "11": 1.0, "12": 0.95
                }
            }
        },
        "supplier_performance": {
            "WIDGET-001": {
                "avg_lead_time": 12,
                "lead_time_std_dev": 3,
                "on_time_delivery_rate": 0.92
            }
        },
        "service_level_target": 0.95,
        "ordering_cost": 75,
        "holding_cost_rate": 0.22
    }

    # Run optimization
    result = optimize_inventory_levels(inventory_record, context)

    print("🤖 AI-Driven Inventory Optimization Results")
    print(f"Item: {inventory_record['item_id']}")
    print(f"Current Stock: {result['optimization_results']['current_stock']}")
    print(f"Optimal Reorder Point: {result['optimization_results']['optimal_reorder_point']:.1f}")
    print(f"Optimal Max Stock: {result['optimization_results']['optimal_max_stock']:.1f}")
    print(f"Recommended Order Quantity: {result['optimization_results']['optimal_order_quantity']:.1f}")
    print(f"Safety Stock: {result['optimization_results']['safety_stock']:.1f}")
    print(f"Confidence Score: {result['confidence_score']:.2%}")

    print("\n📋 Recommendations:")
    for rec in result['recommendations']:
        print(f"   • {rec['action']}: {rec}")

if __name__ == "__main__":
    run_inventory_optimization_example()
```

### **Example 10: Supply Chain Optimization**

#### **Scenario**: Multi-location supply chain optimization and balancing

```python
# supply_chain_optimization.py
from target_oracle_wms import register_business_rule
import networkx as nx
from datetime import datetime, timedelta

@register_business_rule("warehouse", "supply_chain_optimization")
def optimize_supply_chain(record: dict, context: dict) -> dict:
    """
    Multi-location supply chain optimization with network analysis.

    Implements advanced algorithms for optimal inventory distribution.
    """
    facility_id = record.get("facility_id")

    # Get network data
    facilities = context.get("facilities", {})
    demand_forecast = context.get("demand_forecast", {})
    transportation_costs = context.get("transportation_costs", {})
    inventory_levels = context.get("current_inventory", {})

    # Build supply chain network
    supply_chain_graph = build_supply_chain_network(
        facilities, transportation_costs
    )

    # Calculate optimal distribution
    optimization_results = calculate_optimal_distribution(
        supply_chain_graph,
        inventory_levels,
        demand_forecast,
        context.get("constraints", {})
    )

    # Generate transfer recommendations
    transfer_recommendations = generate_transfer_recommendations(
        facility_id,
        optimization_results,
        context.get("transfer_rules", {})
    )

    return {
        "optimization_results": optimization_results,
        "transfer_recommendations": transfer_recommendations,
        "network_efficiency_score": calculate_network_efficiency(supply_chain_graph),
        "cost_savings_potential": calculate_cost_savings(optimization_results, transportation_costs)
    }

def build_supply_chain_network(facilities: dict, transportation_costs: dict) -> nx.Graph:
    """Build supply chain network graph."""
    G = nx.Graph()

    # Add facility nodes
    for facility_id, facility_data in facilities.items():
        G.add_node(facility_id, **facility_data)

    # Add transportation edges
    for route, cost_data in transportation_costs.items():
        from_facility, to_facility = route.split("->")
        G.add_edge(
            from_facility.strip(),
            to_facility.strip(),
            weight=cost_data.get("cost_per_unit", 0),
            transit_time=cost_data.get("transit_days", 1),
            capacity=cost_data.get("daily_capacity", float('inf'))
        )

    return G

def calculate_optimal_distribution(graph: nx.Graph, inventory: dict, demand: dict, constraints: dict) -> dict:
    """Calculate optimal inventory distribution across network."""
    results = {}

    # For each item, optimize distribution
    all_items = set()
    for facility_inventory in inventory.values():
        all_items.update(facility_inventory.keys())

    for item_id in all_items:
        item_results = optimize_item_distribution(
            graph, item_id, inventory, demand, constraints
        )
        results[item_id] = item_results

    return results

def optimize_item_distribution(graph: nx.Graph, item_id: str, inventory: dict, demand: dict, constraints: dict) -> dict:
    """Optimize distribution for a specific item."""
    # Get current inventory levels
    current_levels = {}
    for facility_id in graph.nodes():
        current_levels[facility_id] = inventory.get(facility_id, {}).get(item_id, 0)

    # Get demand forecast
    demand_levels = {}
    for facility_id in graph.nodes():
        demand_levels[facility_id] = demand.get(facility_id, {}).get(item_id, 0)

    # Simple optimization: balance supply and demand
    total_inventory = sum(current_levels.values())
    total_demand = sum(demand_levels.values())

    if total_inventory == 0:
        return {"status": "no_inventory", "transfers": []}

    # Calculate target levels based on demand ratio
    target_levels = {}
    for facility_id in graph.nodes():
        if total_demand > 0:
            demand_ratio = demand_levels[facility_id] / total_demand
            target_levels[facility_id] = total_inventory * demand_ratio
        else:
            target_levels[facility_id] = current_levels[facility_id]

    # Generate transfer plan
    transfers = []
    surplus_facilities = []
    deficit_facilities = []

    for facility_id in graph.nodes():
        difference = current_levels[facility_id] - target_levels[facility_id]
        if difference > 5:  # Surplus threshold
            surplus_facilities.append((facility_id, difference))
        elif difference < -5:  # Deficit threshold
            deficit_facilities.append((facility_id, -difference))

    # Match surplus with deficit
    surplus_facilities.sort(key=lambda x: x[1], reverse=True)
    deficit_facilities.sort(key=lambda x: x[1], reverse=True)

    for deficit_facility, deficit_amount in deficit_facilities:
        remaining_deficit = deficit_amount

        for i, (surplus_facility, surplus_amount) in enumerate(surplus_facilities):
            if remaining_deficit <= 0:
                break

            # Calculate transfer cost
            try:
                path_length = nx.shortest_path_length(
                    graph, surplus_facility, deficit_facility, weight='weight'
                )
                transfer_amount = min(remaining_deficit, surplus_amount)

                if transfer_amount > 0:
                    transfers.append({
                        "from_facility": surplus_facility,
                        "to_facility": deficit_facility,
                        "item_id": item_id,
                        "quantity": transfer_amount,
                        "cost": path_length * transfer_amount,
                        "priority": "high" if deficit_amount > 50 else "medium"
                    })

                    remaining_deficit -= transfer_amount
                    surplus_facilities[i] = (surplus_facility, surplus_amount - transfer_amount)

            except nx.NetworkXNoPath:
                continue  # No path between facilities

    return {
        "status": "optimized",
        "transfers": transfers,
        "current_levels": current_levels,
        "target_levels": target_levels,
        "total_transfer_cost": sum(t["cost"] for t in transfers)
    }

def generate_transfer_recommendations(facility_id: str, optimization_results: dict, transfer_rules: dict) -> list:
    """Generate specific transfer recommendations for a facility."""
    recommendations = []

    for item_id, item_results in optimization_results.items():
        if item_results["status"] != "optimized":
            continue

        # Find transfers involving this facility
        for transfer in item_results["transfers"]:
            if transfer["from_facility"] == facility_id or transfer["to_facility"] == facility_id:

                # Apply business rules
                min_transfer_quantity = transfer_rules.get("min_transfer_quantity", 10)
                if transfer["quantity"] < min_transfer_quantity:
                    continue

                recommendation = {
                    "type": "inventory_transfer",
                    "item_id": transfer["item_id"],
                    "from_facility": transfer["from_facility"],
                    "to_facility": transfer["to_facility"],
                    "quantity": transfer["quantity"],
                    "estimated_cost": transfer["cost"],
                    "priority": transfer["priority"],
                    "business_justification": generate_transfer_justification(transfer, item_results)
                }

                recommendations.append(recommendation)

    return recommendations

def generate_transfer_justification(transfer: dict, item_results: dict) -> str:
    """Generate business justification for transfer."""
    from_facility = transfer["from_facility"]
    to_facility = transfer["to_facility"]
    quantity = transfer["quantity"]

    current_from = item_results["current_levels"][from_facility]
    current_to = item_results["current_levels"][to_facility]
    target_from = item_results["target_levels"][from_facility]
    target_to = item_results["target_levels"][to_facility]

    justification = f"Transfer {quantity} units from {from_facility} to {to_facility}. "
    justification += f"Source has {current_from:.0f} (target: {target_from:.0f}), "
    justification += f"destination has {current_to:.0f} (target: {target_to:.0f}). "
    justification += f"This balances inventory with demand forecast."

    return justification

def calculate_network_efficiency(graph: nx.Graph) -> float:
    """Calculate supply chain network efficiency score."""
    if graph.number_of_nodes() < 2:
        return 1.0

    # Calculate various network metrics
    connectivity = nx.node_connectivity(graph)
    avg_path_length = nx.average_shortest_path_length(graph, weight='weight') if nx.is_connected(graph) else float('inf')
    density = nx.density(graph)

    # Normalize and combine metrics
    connectivity_score = min(connectivity / 3, 1.0)  # Normalize to max 3 connections
    path_efficiency = 1 / (1 + avg_path_length / 100) if avg_path_length != float('inf') else 0
    density_score = min(density * 2, 1.0)  # Prefer some connectivity but not fully connected

    efficiency_score = (connectivity_score + path_efficiency + density_score) / 3
    return efficiency_score

def calculate_cost_savings(optimization_results: dict, transportation_costs: dict) -> dict:
    """Calculate potential cost savings from optimization."""
    total_transfer_cost = 0
    total_transfers = 0

    for item_results in optimization_results.values():
        if item_results["status"] == "optimized":
            total_transfer_cost += item_results.get("total_transfer_cost", 0)
            total_transfers += len(item_results.get("transfers", []))

    # Estimate savings from reduced stockouts and overstock
    estimated_stockout_savings = total_transfers * 100  # $100 per avoided stockout
    estimated_carrying_cost_savings = total_transfer_cost * 0.25  # 25% carrying cost reduction

    return {
        "transfer_investment": total_transfer_cost,
        "estimated_stockout_savings": estimated_stockout_savings,
        "estimated_carrying_cost_savings": estimated_carrying_cost_savings,
        "net_savings": estimated_stockout_savings + estimated_carrying_cost_savings - total_transfer_cost,
        "roi_percentage": ((estimated_stockout_savings + estimated_carrying_cost_savings - total_transfer_cost) /
                          max(total_transfer_cost, 1)) * 100
    }

# Example usage
def run_supply_chain_optimization_example():
    """Run comprehensive supply chain optimization example."""

    # Sample network data
    context = {
        "facilities": {
            "DC-EAST": {"type": "distribution_center", "capacity": 10000},
            "DC-WEST": {"type": "distribution_center", "capacity": 8000},
            "STORE-001": {"type": "retail_store", "capacity": 500},
            "STORE-002": {"type": "retail_store", "capacity": 600},
            "PLANT-001": {"type": "manufacturing", "capacity": 15000}
        },
        "transportation_costs": {
            "PLANT-001 -> DC-EAST": {"cost_per_unit": 2.50, "transit_days": 2},
            "PLANT-001 -> DC-WEST": {"cost_per_unit": 4.00, "transit_days": 3},
            "DC-EAST -> STORE-001": {"cost_per_unit": 1.25, "transit_days": 1},
            "DC-EAST -> STORE-002": {"cost_per_unit": 1.75, "transit_days": 1},
            "DC-WEST -> STORE-001": {"cost_per_unit": 3.00, "transit_days": 2},
            "DC-WEST -> STORE-002": {"cost_per_unit": 1.50, "transit_days": 1}
        },
        "current_inventory": {
            "DC-EAST": {"WIDGET-001": 500, "GADGET-002": 300},
            "DC-WEST": {"WIDGET-001": 200, "GADGET-002": 800},
            "STORE-001": {"WIDGET-001": 25, "GADGET-002": 15},
            "STORE-002": {"WIDGET-001": 10, "GADGET-002": 40}
        },
        "demand_forecast": {
            "STORE-001": {"WIDGET-001": 100, "GADGET-002": 50},
            "STORE-002": {"WIDGET-001": 75, "GADGET-002": 25}
        },
        "transfer_rules": {
            "min_transfer_quantity": 20,
            "max_transfer_distance": 1000
        }
    }

    # Run optimization for DC-EAST
    warehouse_record = {"facility_id": "DC-EAST"}
    result = optimize_supply_chain(warehouse_record, context)

    print("🌐 Supply Chain Optimization Results")
    print(f"Network Efficiency Score: {result['network_efficiency_score']:.2%}")
    print(f"ROI Percentage: {result['cost_savings_potential']['roi_percentage']:.1f}%")

    print("\n📋 Transfer Recommendations:")
    for rec in result['transfer_recommendations']:
        print(f"   • {rec['item_id']}: {rec['from_facility']} → {rec['to_facility']}")
        print(f"     Quantity: {rec['quantity']}, Cost: ${rec['estimated_cost']:.2f}")
        print(f"     Priority: {rec['priority']}")

if __name__ == "__main__":
    run_supply_chain_optimization_example()
```

---

## 🔗 **Multi-Pipeline Integration Examples**

### **Example 11: Complete ETL Pipeline**

#### **Scenario**: End-to-end ETL pipeline with multiple sources and destinations

```bash
#!/bin/bash
# complete_etl_pipeline.sh

# Multi-source to multi-destination ETL pipeline
set -e

echo "🚀 Starting Complete ETL Pipeline"

# Configuration
PIPELINE_ID="wms-daily-$(date +%Y%m%d)"
CONFIG_DIR="./config"
OUTPUT_DIR="./output/${PIPELINE_ID}"
LOG_DIR="./logs/${PIPELINE_ID}"

# Create directories
mkdir -p $OUTPUT_DIR $LOG_DIR

# Step 1: Extract from multiple sources
echo "📥 Step 1: Data Extraction"

# Oracle WMS via REST API
tap-oracle-wms --config $CONFIG_DIR/tap_wms_config.json \
               --catalog $CONFIG_DIR/wms_catalog.json \
               --state $CONFIG_DIR/wms_state.json \
               > $OUTPUT_DIR/wms_data.jsonl \
               2> $LOG_DIR/tap_wms.log &

# CSV files
tap-csv --config $CONFIG_DIR/tap_csv_config.json \
        --catalog $CONFIG_DIR/csv_catalog.json \
        > $OUTPUT_DIR/csv_data.jsonl \
        2> $LOG_DIR/tap_csv.log &

# Database
tap-postgres --config $CONFIG_DIR/tap_postgres_config.json \
             --catalog $CONFIG_DIR/postgres_catalog.json \
             --state $CONFIG_DIR/postgres_state.json \
             > $OUTPUT_DIR/postgres_data.jsonl \
             2> $LOG_DIR/tap_postgres.log &

# Wait for all extractions to complete
wait

echo "✅ Data extraction completed"

# Step 2: Transform and load to WMS target
echo "🔄 Step 2: Transform and Load"

# Combine all streams
cat $OUTPUT_DIR/wms_data.jsonl \
    $OUTPUT_DIR/csv_data.jsonl \
    $OUTPUT_DIR/postgres_data.jsonl | \

# Apply transformations
meltano invoke dbt:run --vars '{pipeline_id: "'$PIPELINE_ID'"}' | \

# Load to multiple destinations
tee >(target-oracle-wms --config $CONFIG_DIR/target_wms_config.json \
                        --output-path $OUTPUT_DIR/wms_processed \
                        2> $LOG_DIR/target_wms.log) \
    >(target-postgres --config $CONFIG_DIR/target_postgres_config.json \
                      2> $LOG_DIR/target_postgres.log) \
    >(target-s3 --config $CONFIG_DIR/target_s3_config.json \
                2> $LOG_DIR/target_s3.log) \
    > /dev/null

echo "✅ Transform and load completed"

# Step 3: Data Quality Validation
echo "🔍 Step 3: Data Quality Validation"

python3 << EOF
import json
import sys
from pathlib import Path

def validate_pipeline_output():
    """Validate pipeline output quality."""
    output_dir = Path("$OUTPUT_DIR")

    # Check file existence
    required_files = [
        "wms_processed/inventory.json",
        "wms_processed/orders.json",
        "wms_processed/shipments.json"
    ]

    missing_files = []
    for file_path in required_files:
        if not (output_dir / file_path).exists():
            missing_files.append(file_path)

    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False

    # Validate record counts
    total_records = 0
    for json_file in output_dir.glob("wms_processed/*.json"):
        with open(json_file) as f:
            records = [line for line in f if line.strip()]
            record_count = len(records)
            print(f"📊 {json_file.name}: {record_count} records")
            total_records += record_count

    if total_records < 100:  # Minimum expected records
        print(f"⚠️ Low record count: {total_records}")
        return False

    print(f"✅ Pipeline validation passed: {total_records} total records")
    return True

if not validate_pipeline_output():
    sys.exit(1)
EOF

# Step 4: Generate Business Reports
echo "📊 Step 4: Generate Business Reports"

python3 << EOF
import json
from datetime import datetime
from pathlib import Path

def generate_business_reports():
    """Generate business intelligence reports."""
    output_dir = Path("$OUTPUT_DIR")

    # Load processed data
    inventory_data = []
    orders_data = []

    if (output_dir / "wms_processed/inventory.json").exists():
        with open(output_dir / "wms_processed/inventory.json") as f:
            inventory_data = [json.loads(line) for line in f if line.strip()]

    if (output_dir / "wms_processed/orders.json").exists():
        with open(output_dir / "wms_processed/orders.json") as f:
            orders_data = [json.loads(line) for line in f if line.strip()]

    # Generate inventory report
    total_inventory_value = sum(
        float(record.get("total_value", 0)) for record in inventory_data
    )

    low_stock_items = [
        record for record in inventory_data
        if float(record.get("on_hand_quantity", 0)) < float(record.get("reorder_point", 0))
    ]

    # Generate order report
    total_orders = len(orders_data)
    shipped_orders = [
        record for record in orders_data
        if record.get("status") == "SHIPPED"
    ]

    # Create summary report
    report = {
        "pipeline_id": "$PIPELINE_ID",
        "generated_at": datetime.utcnow().isoformat(),
        "inventory_summary": {
            "total_value": total_inventory_value,
            "total_items": len(inventory_data),
            "low_stock_items": len(low_stock_items),
            "low_stock_percentage": len(low_stock_items) / max(len(inventory_data), 1) * 100
        },
        "order_summary": {
            "total_orders": total_orders,
            "shipped_orders": len(shipped_orders),
            "fulfillment_rate": len(shipped_orders) / max(total_orders, 1) * 100
        }
    }

    # Save report
    with open(output_dir / "business_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("📈 Business Report Generated:")
    print(f"   Total Inventory Value: ${total_inventory_value:,.2f}")
    print(f"   Low Stock Items: {len(low_stock_items)} ({report['inventory_summary']['low_stock_percentage']:.1f}%)")
    print(f"   Order Fulfillment Rate: {report['order_summary']['fulfillment_rate']:.1f}%")

generate_business_reports()
EOF

# Step 5: Cleanup and Archival
echo "🧹 Step 5: Cleanup and Archival"

# Archive logs
tar -czf $LOG_DIR.tar.gz $LOG_DIR/
rm -rf $LOG_DIR/

# Update state files
cp $OUTPUT_DIR/wms_state.json $CONFIG_DIR/wms_state.json 2>/dev/null || true
cp $OUTPUT_DIR/postgres_state.json $CONFIG_DIR/postgres_state.json 2>/dev/null || true

echo "✅ Pipeline completed successfully"
echo "📁 Output available in: $OUTPUT_DIR"
echo "📋 Business report: $OUTPUT_DIR/business_report.json"
```

---

## 🏭 **Production Scenarios**

### **Example 12: High-Volume Production Deployment**

#### **Scenario**: Production deployment handling 1M+ records per day

```python
# production_deployment_example.py
from target_oracle_wms import TargetOracleWMS
from target_oracle_wms.monitoring import ProductionMonitor
from target_oracle_wms.resilience import CircuitBreaker, RetryHandler
import asyncio
import logging
from datetime import datetime

class ProductionWMSTarget:
    """Production-ready WMS target with enterprise features."""

    def __init__(self, config: dict):
        self.config = config
        self.target = TargetOracleWMS(config=config)
        self.monitor = ProductionMonitor(config)
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=5,
            recovery_timeout=60,
            expected_exception=Exception
        )
        self.retry_handler = RetryHandler(
            max_retries=3,
            backoff_factor=2,
            max_delay=300
        )
        self.logger = logging.getLogger(__name__)

    async def process_high_volume_stream(self, stream_name: str, records_generator):
        """Process high-volume data stream with production safeguards."""

        batch_size = self.config.get("batch_size", 5000)
        max_concurrent_batches = self.config.get("max_concurrent_batches", 4)

        batch = []
        batch_number = 0
        semaphore = asyncio.Semaphore(max_concurrent_batches)

        async with self.monitor.track_stream_processing(stream_name):
            async for record in records_generator:
                batch.append(record)

                if len(batch) >= batch_size:
                    batch_number += 1
                    await self._process_batch_with_resilience(
                        stream_name, batch.copy(), batch_number, semaphore
                    )
                    batch.clear()

            # Process remaining records
            if batch:
                batch_number += 1
                await self._process_batch_with_resilience(
                    stream_name, batch, batch_number, semaphore
                )

    async def _process_batch_with_resilience(self, stream_name: str, batch: list,
                                           batch_number: int, semaphore: asyncio.Semaphore):
        """Process batch with circuit breaker and retry logic."""

        async with semaphore:
            try:
                with self.circuit_breaker:
                    await self.retry_handler.execute(
                        self._process_batch_core,
                        stream_name, batch, batch_number
                    )

                self.logger.info(f"✅ Batch {batch_number} processed: {len(batch)} records")

            except Exception as e:
                self.logger.error(f"❌ Batch {batch_number} failed: {e}")
                await self._handle_batch_failure(stream_name, batch, batch_number, e)

    async def _process_batch_core(self, stream_name: str, batch: list, batch_number: int):
        """Core batch processing logic."""

        # Pre-processing validation
        valid_records = []
        invalid_records = []

        for record in batch:
            if self._validate_record(record):
                valid_records.append(record)
            else:
                invalid_records.append(record)

        if invalid_records:
            await self._handle_invalid_records(stream_name, invalid_records, batch_number)

        if not valid_records:
            return

        # Process valid records with business logic
        start_time = datetime.utcnow()

        processed_records = []
        for record in valid_records:
            try:
                processed_record = await self._apply_business_logic(stream_name, record)
                processed_records.append(processed_record)
            except Exception as e:
                self.logger.warning(f"Record processing failed: {e}")
                await self._handle_record_failure(stream_name, record, e)

        # Bulk output processing
        await self._bulk_output_processing(stream_name, processed_records)

        # Update metrics
        processing_time = (datetime.utcnow() - start_time).total_seconds()
        await self.monitor.record_batch_metrics(
            stream_name=stream_name,
            batch_size=len(batch),
            valid_records=len(valid_records),
            processed_records=len(processed_records),
            processing_time=processing_time
        )

    def _validate_record(self, record: dict) -> bool:
        """Validate record against business rules."""
        required_fields = ["type", "stream", "record"]

        for field in required_fields:
            if field not in record:
                return False

        # Stream-specific validation
        stream_name = record.get("stream")
        record_data = record.get("record", {})

        if stream_name == "inventory":
            return self._validate_inventory_record(record_data)
        elif stream_name == "orders":
            return self._validate_order_record(record_data)

        return True

    def _validate_inventory_record(self, record: dict) -> bool:
        """Validate inventory record."""
        required_fields = ["item_id", "location_id"]

        for field in required_fields:
            if not record.get(field):
                return False

        # Quantity validation
        quantity = record.get("on_hand_quantity", 0)
        if not isinstance(quantity, (int, float)) or quantity < 0:
            return False

        return True

    def _validate_order_record(self, record: dict) -> bool:
        """Validate order record."""
        required_fields = ["order_id"]

        for field in required_fields:
            if not record.get(field):
                return False

        return True

    async def _apply_business_logic(self, stream_name: str, record: dict) -> dict:
        """Apply stream-specific business logic."""

        if stream_name == "inventory":
            return await self._process_inventory_business_logic(record)
        elif stream_name == "orders":
            return await self._process_order_business_logic(record)
        else:
            return record

    async def _process_inventory_business_logic(self, record: dict) -> dict:
        """Apply inventory-specific business logic."""
        record_data = record["record"]

        # Calculate KPIs
        if self.config.get("enable_kpi_calculation", True):
            kpis = await self._calculate_inventory_kpis(record_data)
            record_data.update(kpis)

        # Generate alerts
        if self.config.get("enable_alerts", True):
            alerts = await self._generate_inventory_alerts(record_data)
            if alerts:
                record_data["alerts"] = alerts

        # Add processing metadata
        record_data["processed_at"] = datetime.utcnow().isoformat()
        record_data["processing_version"] = "1.0"

        return record

    async def _process_order_business_logic(self, record: dict) -> dict:
        """Apply order-specific business logic."""
        record_data = record["record"]

        # Calculate fulfillment metrics
        if self.config.get("enable_kpi_calculation", True):
            kpis = await self._calculate_order_kpis(record_data)
            record_data.update(kpis)

        # Check SLA compliance
        sla_status = await self._check_order_sla(record_data)
        record_data["sla_status"] = sla_status

        record_data["processed_at"] = datetime.utcnow().isoformat()

        return record

    async def _bulk_output_processing(self, stream_name: str, records: list):
        """Process outputs in bulk for performance."""

        if not records:
            return

        # Group by output destination
        file_records = []
        database_records = []
        api_records = []

        for record in records:
            # Determine routing based on configuration
            routing_config = self.config.get("output_routing", {}).get(stream_name, {})

            if "file" in routing_config.get("destinations", ["file"]):
                file_records.append(record)

            if "database" in routing_config.get("destinations", []):
                database_records.append(record)

            if "api" in routing_config.get("destinations", []):
                api_records.append(record)

        # Process outputs concurrently
        tasks = []

        if file_records:
            tasks.append(self._write_bulk_to_files(stream_name, file_records))

        if database_records:
            tasks.append(self._write_bulk_to_database(stream_name, database_records))

        if api_records:
            tasks.append(self._send_bulk_to_api(stream_name, api_records))

        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def _handle_batch_failure(self, stream_name: str, batch: list,
                                  batch_number: int, error: Exception):
        """Handle batch processing failure."""

        failure_record = {
            "stream_name": stream_name,
            "batch_number": batch_number,
            "batch_size": len(batch),
            "error": str(error),
            "timestamp": datetime.utcnow().isoformat(),
            "retry_count": getattr(error, 'retry_count', 0)
        }

        # Log failure
        self.logger.error(f"Batch failure: {failure_record}")

        # Save failed batch for replay
        failed_batch_path = f"./failed_batches/{stream_name}_{batch_number}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        await self._save_failed_batch(failed_batch_path, batch, failure_record)

        # Send alert
        await self.monitor.send_failure_alert(failure_record)

# Production configuration example
def create_production_config():
    """Create production-ready configuration."""
    return {
        # Connection settings
        "base_url": "https://wms-prod.company.com",
        "username": "prod_service_account",
        "password": "${WMS_PROD_PASSWORD}",

        # Performance settings
        "batch_size": 5000,
        "max_workers": 12,
        "max_concurrent_batches": 4,
        "memory_limit_mb": 4096,
        "connection_pool_size": 20,

        # Business logic settings
        "enable_kpi_calculation": True,
        "enable_alerts": True,
        "enable_business_rules": True,

        # Output settings
        "output_routing": {
            "inventory": {
                "destinations": ["file", "database", "api"],
                "file_format": "parquet",
                "database_schema": "wms_analytics",
                "api_endpoint": "analytics"
            },
            "orders": {
                "destinations": ["database", "webhook"],
                "database_schema": "wms_orders",
                "webhook_events": ["sla_breach", "allocation_failure"]
            }
        },

        # Monitoring settings
        "monitoring": {
            "enable_metrics": True,
            "metrics_endpoint": "localhost:8000",
            "log_level": "INFO",
            "alert_thresholds": {
                "error_rate": 0.05,
                "processing_time_p95": 300,
                "memory_usage": 0.8
            }
        },

        # Resilience settings
        "circuit_breaker": {
            "failure_threshold": 10,
            "recovery_timeout": 120
        },
        "retry_policy": {
            "max_retries": 5,
            "backoff_factor": 2,
            "max_delay": 600
        }
    }

# Usage example
async def run_production_example():
    """Run production-scale processing example."""

    config = create_production_config()
    production_target = ProductionWMSTarget(config)

    # Simulate high-volume data stream
    async def generate_test_records():
        """Generate test records for demonstration."""
        for i in range(10000):  # 10K records for demo
            yield {
                "type": "RECORD",
                "stream": "inventory",
                "record": {
                    "item_id": f"ITEM-{i:06d}",
                    "location_id": f"LOC-{i % 100:03d}",
                    "on_hand_quantity": 100 + (i % 500),
                    "unit_cost": 10.50 + (i % 20),
                    "reorder_point": 50 + (i % 100)
                }
            }

    print("🏭 Starting production-scale processing...")
    start_time = datetime.utcnow()

    await production_target.process_high_volume_stream(
        "inventory",
        generate_test_records()
    )

    end_time = datetime.utcnow()
    processing_time = (end_time - start_time).total_seconds()

    print(f"✅ Production processing completed in {processing_time:.2f} seconds")
    print(f"📊 Throughput: {10000 / processing_time:.0f} records/second")

if __name__ == "__main__":
    asyncio.run(run_production_example())
```

---

## 🔗 **Cross-References**

### **Related Documentation**

- [Implementation Guides](../guides/README.md) - Step-by-step implementation guidance
- [API Reference](../api/README.md) - Complete API specification and sink definitions
- [Architecture Guide](../architecture/README.md) - Technical architecture and design patterns
- [Security Guide](../security/README.md) - Security implementation and best practices

### **External Resources**

- [Singer Specification Examples](https://hub.meltano.com/singer/spec) - Official Singer protocol examples
- [Oracle WMS Use Cases](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmsig/) - Oracle's implementation examples
- [Meltano Tutorials](https://docs.meltano.com/tutorials/) - Meltano platform tutorials

### **Business Intelligence Examples**

- [Warehouse KPI Examples](https://www.smartsheet.com/content/warehouse-kpi-examples) - Industry standard KPI examples
- [Supply Chain Analytics](https://www.ibm.com/topics/supply-chain-analytics) - Advanced analytics patterns
- [Inventory Optimization](https://docs.oracle.com/en/industries/retail/inventory-optimization/) - Oracle inventory optimization examples

---

**💡 Examples & Tutorials**: Target Oracle WMS | **🏠 Root**: [PyAuto Home](../../../README.md) | **Framework**: Singer SDK 0.39.0+ | **Updated**: 2025-06-19
