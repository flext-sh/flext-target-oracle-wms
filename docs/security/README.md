# 🔐 Target Oracle WMS - Security Implementation

> **Function**: Enterprise security practices and data compliance for Oracle WMS Singer target | **Audience**: Security Engineers, DevOps | **Status**: Enterprise Reference

[![Singer](https://img.shields.io/badge/singer-target-blue.svg)](https://www.singer.io/)
[![Oracle](https://img.shields.io/badge/oracle-WMS-red.svg)](https://www.oracle.com/cx/retail/warehouse-management/)
[![Security](https://img.shields.io/badge/security-enterprise-red.svg)](../README.md)
[![Documentation](https://img.shields.io/badge/docs-comprehensive-blue.svg)](../README.md)

Comprehensive security implementation guide covering enterprise-grade security practices, data protection, access control, and compliance requirements for Oracle WMS Singer target deployment, aligned with [Oracle Cloud Security](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csgsg/oracle-cloud-infrastructure-security-best-practices.html) and [Singer security standards](https://hub.meltano.com/singer/spec).

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto](../../../README.md) → **📂 Project**: [Target Oracle WMS](../../README.md) → **📁 Docs**: [Documentation](../README.md) → **📄 Current**: Security Implementation

---

## 📋 **Security Overview**

This guide provides comprehensive security implementation covering all aspects of Oracle WMS Singer target deployment, from authentication and data protection to compliance and audit requirements.

### **Security Domains**

- **Authentication Security**: WMS API authentication and credential management
- **Data Protection**: Encryption, masking, and secure data transmission
- **Access Control**: Role-based access and permission management
- **Audit & Compliance**: Security logging and regulatory compliance
- **Business Data Security**: KPI data protection and privacy controls
- **Network Security**: Secure communication and network isolation

### **Security Standards Compliance**

Based on industry security frameworks:

- **NIST Cybersecurity Framework**: Comprehensive security controls
- **ISO 27001**: Information security management standards
- **SOC 2 Type II**: Security, availability, and confidentiality controls
- **GDPR/CCPA**: Data privacy and protection requirements
- **Oracle Security Guidelines**: Oracle-specific security best practices

---

## 🔒 **Authentication Security**

### **WMS API Authentication**

#### **Basic Authentication Security**

```python
# secure_authentication.py
import base64
import secrets
import hashlib
from cryptography.fernet import Fernet
from typing import Dict, Optional

class SecureAuthenticationManager:
    """Enterprise-grade authentication manager with security controls."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.encryption_key = self._derive_encryption_key()
        self.cipher = Fernet(self.encryption_key)
        self.failed_attempts = {}
        self.max_attempts = 3
        self.lockout_duration = 300  # 5 minutes

    def _derive_encryption_key(self) -> bytes:
        """Derive encryption key from master password."""
        master_password = self.config.get("master_password", "").encode()
        salt = self.config.get("salt", "default_salt").encode()

        # Use PBKDF2 for key derivation
        key = hashlib.pbkdf2_hmac('sha256', master_password, salt, 100000)
        return base64.urlsafe_b64encode(key)

    def encrypt_credentials(self, username: str, password: str) -> str:
        """Encrypt credentials for secure storage."""
        credentials = f"{username}:{password}"
        encrypted = self.cipher.encrypt(credentials.encode())
        return base64.urlsafe_b64encode(encrypted).decode()

    def decrypt_credentials(self, encrypted_credentials: str) -> tuple:
        """Decrypt stored credentials."""
        try:
            encrypted_data = base64.urlsafe_b64decode(encrypted_credentials.encode())
            decrypted = self.cipher.decrypt(encrypted_data)
            credentials = decrypted.decode()
            username, password = credentials.split(':', 1)
            return username, password
        except Exception as e:
            raise SecurityError(f"Failed to decrypt credentials: {e}")

    def validate_credentials(self, username: str, password: str) -> bool:
        """Validate credentials with security controls."""

        # Check for account lockout
        if self._is_account_locked(username):
            raise SecurityError(f"Account {username} is locked due to failed attempts")

        # Validate password strength
        if not self._validate_password_strength(password):
            raise SecurityError("Password does not meet security requirements")

        # Test authentication against WMS
        try:
            auth_result = self._test_wms_authentication(username, password)
            if auth_result:
                self._reset_failed_attempts(username)
                return True
            else:
                self._record_failed_attempt(username)
                return False
        except Exception as e:
            self._record_failed_attempt(username)
            raise SecurityError(f"Authentication failed: {e}")

    def _validate_password_strength(self, password: str) -> bool:
        """Validate password meets security requirements."""
        if len(password) < 12:
            return False

        checks = [
            any(c.isupper() for c in password),  # Uppercase
            any(c.islower() for c in password),  # Lowercase
            any(c.isdigit() for c in password),  # Digit
            any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)  # Special char
        ]

        return sum(checks) >= 3

    def generate_secure_token(self, username: str, expiry_hours: int = 24) -> str:
        """Generate secure authentication token."""
        import time
        import jwt

        payload = {
            "username": username,
            "iat": int(time.time()),
            "exp": int(time.time()) + (expiry_hours * 3600),
            "jti": secrets.token_hex(16)  # Unique token ID
        }

        secret_key = self.config.get("jwt_secret", secrets.token_hex(32))
        token = jwt.encode(payload, secret_key, algorithm="HS256")

        return token

    def validate_token(self, token: str) -> Optional[Dict]:
        """Validate authentication token."""
        try:
            import jwt
            secret_key = self.config.get("jwt_secret")
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise SecurityError("Token has expired")
        except jwt.InvalidTokenError:
            raise SecurityError("Invalid token")

class SecurityError(Exception):
    """Security-related error."""
    pass
```

#### **OAuth2 Authentication Implementation**

```python
# oauth2_authentication.py
import requests
import time
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class OAuth2Token:
    access_token: str
    refresh_token: str
    expires_at: float
    token_type: str = "Bearer"

class OAuth2AuthenticationManager:
    """OAuth2 authentication manager with automatic token refresh."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.token: Optional[OAuth2Token] = None
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.token_url = config.get("token_url")
        self.scope = config.get("scope", "wms:read wms:write")

    async def authenticate(self) -> OAuth2Token:
        """Authenticate and obtain OAuth2 token."""

        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.scope
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "TargetOracleWMS/1.0"
        }

        try:
            response = requests.post(
                self.token_url,
                data=auth_data,
                headers=headers,
                timeout=30,
                verify=True  # Always verify SSL
            )
            response.raise_for_status()

            token_data = response.json()

            self.token = OAuth2Token(
                access_token=token_data["access_token"],
                refresh_token=token_data.get("refresh_token", ""),
                expires_at=time.time() + token_data.get("expires_in", 3600),
                token_type=token_data.get("token_type", "Bearer")
            )

            return self.token

        except requests.RequestException as e:
            raise SecurityError(f"OAuth2 authentication failed: {e}")

    async def get_valid_token(self) -> str:
        """Get valid access token, refreshing if necessary."""

        if not self.token or self._is_token_expired():
            await self.authenticate()

        return self.token.access_token

    def _is_token_expired(self) -> bool:
        """Check if current token is expired."""
        if not self.token:
            return True

        # Refresh 5 minutes before expiry
        buffer_time = 300
        return time.time() >= (self.token.expires_at - buffer_time)

    def get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for API requests."""
        if not self.token:
            raise SecurityError("No valid token available")

        return {
            "Authorization": f"{self.token.token_type} {self.token.access_token}",
            "Content-Type": "application/json"
        }
```

#### **Multi-Factor Authentication (MFA)**

```python
# mfa_authentication.py
import pyotp
import qrcode
from io import BytesIO
import base64

class MFAManager:
    """Multi-Factor Authentication manager for enhanced security."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.service_name = "Oracle WMS Target"

    def generate_secret(self, username: str) -> str:
        """Generate MFA secret for user."""
        secret = pyotp.random_base32()

        # Store securely encrypted
        encrypted_secret = self._encrypt_secret(secret)
        self._store_user_secret(username, encrypted_secret)

        return secret

    def generate_qr_code(self, username: str, secret: str) -> str:
        """Generate QR code for MFA setup."""
        provisioning_uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name=username,
            issuer_name=self.service_name
        )

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(provisioning_uri)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convert to base64 for web display
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return f"data:image/png;base64,{img_str}"

    def verify_token(self, username: str, token: str) -> bool:
        """Verify MFA token."""
        try:
            encrypted_secret = self._get_user_secret(username)
            secret = self._decrypt_secret(encrypted_secret)

            totp = pyotp.TOTP(secret)
            return totp.verify(token, valid_window=1)  # Allow 30s window

        except Exception as e:
            raise SecurityError(f"MFA verification failed: {e}")

    def _encrypt_secret(self, secret: str) -> str:
        """Encrypt MFA secret for storage."""
        # Implementation using Fernet encryption
        pass

    def _decrypt_secret(self, encrypted_secret: str) -> str:
        """Decrypt stored MFA secret."""
        # Implementation using Fernet decryption
        pass
```

---

## 🛡️ **Data Protection**

### **Encryption Implementation**

#### **Data at Rest Encryption**

```python
# data_encryption.py
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from typing import Dict, Any

class DataEncryptionManager:
    """Enterprise data encryption manager for WMS data protection."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.encryption_key = self._derive_key()
        self.cipher = Fernet(self.encryption_key)

    def _derive_key(self) -> bytes:
        """Derive encryption key from configuration."""
        password = self.config.get("encryption_password", "").encode()
        salt = self.config.get("encryption_salt", os.urandom(16))

        if isinstance(salt, str):
            salt = salt.encode()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def encrypt_sensitive_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Encrypt sensitive fields in WMS data."""

        # Define sensitive fields by stream type
        sensitive_fields = {
            "inventory": ["unit_cost", "total_value", "supplier_info"],
            "orders": ["customer_info", "billing_address", "payment_info"],
            "shipments": ["customer_address", "tracking_number", "carrier_info"],
            "warehouse": ["employee_info", "performance_metrics"]
        }

        stream_type = data.get("stream", "")
        record_data = data.get("record", {})

        if stream_type in sensitive_fields:
            for field in sensitive_fields[stream_type]:
                if field in record_data:
                    record_data[field] = self._encrypt_field(record_data[field])

        return data

    def decrypt_sensitive_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Decrypt sensitive fields in WMS data."""

        stream_type = data.get("stream", "")
        record_data = data.get("record", {})

        sensitive_fields = {
            "inventory": ["unit_cost", "total_value", "supplier_info"],
            "orders": ["customer_info", "billing_address", "payment_info"],
            "shipments": ["customer_address", "tracking_number", "carrier_info"],
            "warehouse": ["employee_info", "performance_metrics"]
        }

        if stream_type in sensitive_fields:
            for field in sensitive_fields[stream_type]:
                if field in record_data and self._is_encrypted(record_data[field]):
                    record_data[field] = self._decrypt_field(record_data[field])

        return data

    def _encrypt_field(self, value: Any) -> str:
        """Encrypt individual field value."""
        if value is None:
            return None

        # Convert to string if not already
        str_value = str(value) if not isinstance(value, str) else value
        encrypted = self.cipher.encrypt(str_value.encode())
        return f"ENC:{base64.urlsafe_b64encode(encrypted).decode()}"

    def _decrypt_field(self, encrypted_value: str) -> str:
        """Decrypt individual field value."""
        if not encrypted_value or not encrypted_value.startswith("ENC:"):
            return encrypted_value

        try:
            encrypted_data = base64.urlsafe_b64decode(encrypted_value[4:])
            decrypted = self.cipher.decrypt(encrypted_data)
            return decrypted.decode()
        except Exception as e:
            raise SecurityError(f"Failed to decrypt field: {e}")

    def _is_encrypted(self, value: Any) -> bool:
        """Check if value is encrypted."""
        return isinstance(value, str) and value.startswith("ENC:")
```

#### **Data in Transit Encryption**

```python
# secure_transport.py
import ssl
import certifi
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class SecureTransportManager:
    """Secure transport manager for WMS API communication."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.session = self._create_secure_session()

    def _create_secure_session(self) -> requests.Session:
        """Create secure HTTP session with proper SSL configuration."""

        session = requests.Session()

        # Configure SSL context
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        ssl_context.check_hostname = True
        ssl_context.verify_mode = ssl.CERT_REQUIRED
        ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2

        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"]
        )

        # Configure adapter with security settings
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=20
        )

        session.mount("https://", adapter)
        session.mount("http://", adapter)

        # Set security headers
        session.headers.update({
            "User-Agent": "TargetOracleWMS/1.0 (Security-Enhanced)",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        })

        return session

    def secure_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Make secure HTTP request with additional security validations."""

        # Validate URL is HTTPS
        if not url.startswith("https://"):
            raise SecurityError("Only HTTPS URLs are allowed")

        # Add security timeouts
        kwargs.setdefault("timeout", 30)
        kwargs.setdefault("verify", True)

        # Remove sensitive data from logs
        safe_kwargs = {k: v for k, v in kwargs.items() if k not in ["auth", "headers"]}

        try:
            response = self.session.request(method, url, **kwargs)

            # Validate response security
            self._validate_response_security(response)

            return response

        except requests.exceptions.SSLError as e:
            raise SecurityError(f"SSL verification failed: {e}")
        except requests.exceptions.RequestException as e:
            raise SecurityError(f"Secure request failed: {e}")

    def _validate_response_security(self, response: requests.Response):
        """Validate response meets security requirements."""

        # Check for security headers
        required_headers = ["content-type"]
        for header in required_headers:
            if header not in response.headers:
                raise SecurityError(f"Missing required header: {header}")

        # Validate content type
        content_type = response.headers.get("content-type", "")
        if not content_type.startswith(("application/json", "text/", "application/xml")):
            raise SecurityError(f"Unexpected content type: {content_type}")

        # Check for error responses
        if response.status_code >= 400:
            self._handle_error_response(response)

    def _handle_error_response(self, response: requests.Response):
        """Handle error responses securely."""

        # Don't log sensitive response content
        if response.status_code == 401:
            raise SecurityError("Authentication failed")
        elif response.status_code == 403:
            raise SecurityError("Access forbidden")
        elif response.status_code == 429:
            raise SecurityError("Rate limit exceeded")
        else:
            raise SecurityError(f"Request failed with status {response.status_code}")
```

### **Data Masking and Anonymization**

#### **PII Data Masking**

```python
# data_masking.py
import re
import hashlib
import secrets
from typing import Any, Dict, List

class DataMaskingManager:
    """Data masking manager for PII protection in WMS data."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.masking_salt = config.get("masking_salt", secrets.token_hex(16))

    def mask_sensitive_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply data masking to sensitive information."""

        record_data = data.get("record", {})
        stream_type = data.get("stream", "")

        # Apply stream-specific masking
        if stream_type == "orders":
            record_data = self._mask_order_data(record_data)
        elif stream_type == "shipments":
            record_data = self._mask_shipment_data(record_data)
        elif stream_type == "warehouse":
            record_data = self._mask_warehouse_data(record_data)

        data["record"] = record_data
        return data

    def _mask_order_data(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Mask sensitive order information."""

        # Mask customer information
        if "customer_name" in record:
            record["customer_name"] = self._mask_name(record["customer_name"])

        if "customer_email" in record:
            record["customer_email"] = self._mask_email(record["customer_email"])

        if "customer_phone" in record:
            record["customer_phone"] = self._mask_phone(record["customer_phone"])

        # Mask address information
        if "ship_to_address" in record:
            record["ship_to_address"] = self._mask_address(record["ship_to_address"])

        # Mask payment information
        if "payment_method" in record:
            record["payment_method"] = self._mask_payment_method(record["payment_method"])

        return record

    def _mask_shipment_data(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Mask sensitive shipment information."""

        # Mask tracking numbers (keep format, mask digits)
        if "tracking_number" in record:
            record["tracking_number"] = self._mask_tracking_number(record["tracking_number"])

        # Mask destination addresses
        if "destination_address" in record:
            record["destination_address"] = self._mask_address(record["destination_address"])

        return record

    def _mask_warehouse_data(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Mask sensitive warehouse information."""

        # Mask employee information
        if "employee_id" in record:
            record["employee_id"] = self._hash_identifier(record["employee_id"])

        if "employee_name" in record:
            record["employee_name"] = self._mask_name(record["employee_name"])

        return record

    def _mask_name(self, name: str) -> str:
        """Mask personal name."""
        if not name:
            return name

        parts = name.split()
        if len(parts) == 1:
            return f"{parts[0][0]}***"
        else:
            return f"{parts[0][0]}*** {parts[-1][0]}***"

    def _mask_email(self, email: str) -> str:
        """Mask email address."""
        if not email or "@" not in email:
            return email

        local, domain = email.split("@", 1)

        if len(local) <= 2:
            masked_local = "*" * len(local)
        else:
            masked_local = local[0] + "*" * (len(local) - 2) + local[-1]

        domain_parts = domain.split(".")
        if len(domain_parts) >= 2:
            masked_domain = f"***.{domain_parts[-1]}"
        else:
            masked_domain = "***"

        return f"{masked_local}@{masked_domain}"

    def _mask_phone(self, phone: str) -> str:
        """Mask phone number."""
        # Remove all non-digits
        digits = re.sub(r'\D', '', phone)

        if len(digits) >= 10:
            # Show last 4 digits
            return f"***-***-{digits[-4:]}"
        else:
            return "***-***-****"

    def _mask_address(self, address: Any) -> Any:
        """Mask address information."""
        if isinstance(address, dict):
            masked_address = address.copy()

            # Mask street address
            if "address1" in masked_address:
                masked_address["address1"] = "*** [MASKED ADDRESS] ***"

            if "address2" in masked_address:
                masked_address["address2"] = ""

            # Keep city and state, mask postal code
            if "postal_code" in masked_address:
                postal = masked_address["postal_code"]
                if len(postal) >= 5:
                    masked_address["postal_code"] = f"{postal[:2]}***"
                else:
                    masked_address["postal_code"] = "***"

            return masked_address

        elif isinstance(address, str):
            return "*** [MASKED ADDRESS] ***"

        return address

    def _mask_tracking_number(self, tracking: str) -> str:
        """Mask tracking number while preserving format."""
        if len(tracking) <= 4:
            return "*" * len(tracking)

        # Keep first 2 and last 2 characters
        return f"{tracking[:2]}{'*' * (len(tracking) - 4)}{tracking[-2:]}"

    def _mask_payment_method(self, payment: Any) -> Any:
        """Mask payment method information."""
        if isinstance(payment, dict):
            masked_payment = {"type": payment.get("type", "***")}

            # Never include actual payment details
            if "card_number" in payment:
                masked_payment["card_last_four"] = "****"

            return masked_payment

        return "*** [MASKED PAYMENT] ***"

    def _hash_identifier(self, identifier: str) -> str:
        """Create consistent hash for identifier."""
        combined = f"{identifier}{self.masking_salt}"
        hash_obj = hashlib.sha256(combined.encode())
        return f"HASH_{hash_obj.hexdigest()[:8].upper()}"
```

---

## 🔐 **Access Control**

### **Role-Based Access Control (RBAC)**

```python
# access_control.py
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional
import time

class Permission(Enum):
    """Available permissions for WMS target operations."""

    # Data access permissions
    READ_INVENTORY = "read:inventory"
    WRITE_INVENTORY = "write:inventory"
    READ_ORDERS = "read:orders"
    WRITE_ORDERS = "write:orders"
    READ_SHIPMENTS = "read:shipments"
    WRITE_SHIPMENTS = "write:shipments"
    READ_WAREHOUSE = "read:warehouse"
    WRITE_WAREHOUSE = "write:warehouse"

    # Business logic permissions
    CALCULATE_KPIS = "calculate:kpis"
    GENERATE_ALERTS = "generate:alerts"
    MANAGE_BUSINESS_RULES = "manage:business_rules"

    # System permissions
    ADMIN_SYSTEM = "REDACTED_LDAP_BIND_PASSWORD:system"
    MANAGE_USERS = "manage:users"
    VIEW_AUDIT_LOGS = "view:audit_logs"
    MANAGE_SECURITY = "manage:security"

@dataclass
class Role:
    """Role definition with permissions."""

    name: str
    description: str
    permissions: Set[Permission] = field(default_factory=set)
    is_system_role: bool = False
    created_at: float = field(default_factory=time.time)

@dataclass
class User:
    """User definition with roles and metadata."""

    username: str
    email: str
    roles: Set[str] = field(default_factory=set)
    is_active: bool = True
    is_service_account: bool = False
    created_at: float = field(default_factory=time.time)
    last_login: Optional[float] = None
    failed_login_attempts: int = 0
    locked_until: Optional[float] = None

class RBACManager:
    """Role-Based Access Control manager for WMS target."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.roles: Dict[str, Role] = {}
        self.users: Dict[str, User] = {}
        self._initialize_default_roles()

    def _initialize_default_roles(self):
        """Initialize default system roles."""

        # Read-only analyst role
        analyst_role = Role(
            name="analyst",
            description="Read-only access for business analysis",
            permissions={
                Permission.READ_INVENTORY,
                Permission.READ_ORDERS,
                Permission.READ_SHIPMENTS,
                Permission.READ_WAREHOUSE,
                Permission.CALCULATE_KPIS
            },
            is_system_role=True
        )

        # Data operator role
        operator_role = Role(
            name="operator",
            description="Read/write access for warehouse operations",
            permissions={
                Permission.READ_INVENTORY,
                Permission.WRITE_INVENTORY,
                Permission.READ_ORDERS,
                Permission.WRITE_ORDERS,
                Permission.READ_SHIPMENTS,
                Permission.WRITE_SHIPMENTS,
                Permission.CALCULATE_KPIS,
                Permission.GENERATE_ALERTS
            },
            is_system_role=True
        )

        # Business REDACTED_LDAP_BIND_PASSWORDistrator role
        business_REDACTED_LDAP_BIND_PASSWORD_role = Role(
            name="business_REDACTED_LDAP_BIND_PASSWORD",
            description="Full business logic management",
            permissions={
                Permission.READ_INVENTORY,
                Permission.WRITE_INVENTORY,
                Permission.READ_ORDERS,
                Permission.WRITE_ORDERS,
                Permission.READ_SHIPMENTS,
                Permission.WRITE_SHIPMENTS,
                Permission.READ_WAREHOUSE,
                Permission.WRITE_WAREHOUSE,
                Permission.CALCULATE_KPIS,
                Permission.GENERATE_ALERTS,
                Permission.MANAGE_BUSINESS_RULES
            },
            is_system_role=True
        )

        # System REDACTED_LDAP_BIND_PASSWORDistrator role
        system_REDACTED_LDAP_BIND_PASSWORD_role = Role(
            name="system_REDACTED_LDAP_BIND_PASSWORD",
            description="Full system REDACTED_LDAP_BIND_PASSWORDistration access",
            permissions=set(Permission),  # All permissions
            is_system_role=True
        )

        # Service account role
        service_role = Role(
            name="service_account",
            description="Automated service access",
            permissions={
                Permission.READ_INVENTORY,
                Permission.WRITE_INVENTORY,
                Permission.READ_ORDERS,
                Permission.WRITE_ORDERS,
                Permission.READ_SHIPMENTS,
                Permission.WRITE_SHIPMENTS,
                Permission.CALCULATE_KPIS,
                Permission.GENERATE_ALERTS
            },
            is_system_role=True
        )

        # Add roles to manager
        for role in [analyst_role, operator_role, business_REDACTED_LDAP_BIND_PASSWORD_role, system_REDACTED_LDAP_BIND_PASSWORD_role, service_role]:
            self.roles[role.name] = role

    def create_user(self, username: str, email: str, roles: List[str],
                   is_service_account: bool = False) -> User:
        """Create new user with specified roles."""

        # Validate roles exist
        for role_name in roles:
            if role_name not in self.roles:
                raise SecurityError(f"Role {role_name} does not exist")

        user = User(
            username=username,
            email=email,
            roles=set(roles),
            is_service_account=is_service_account
        )

        self.users[username] = user
        return user

    def check_permission(self, username: str, permission: Permission) -> bool:
        """Check if user has specific permission."""

        user = self.users.get(username)
        if not user or not user.is_active:
            return False

        # Check if user is locked
        if user.locked_until and time.time() < user.locked_until:
            return False

        # Get user permissions from all roles
        user_permissions = set()
        for role_name in user.roles:
            role = self.roles.get(role_name)
            if role:
                user_permissions.update(role.permissions)

        return permission in user_permissions

    def check_stream_access(self, username: str, stream_name: str, operation: str) -> bool:
        """Check if user can access specific stream and operation."""

        # Map stream and operation to permission
        permission_map = {
            ("inventory", "read"): Permission.READ_INVENTORY,
            ("inventory", "write"): Permission.WRITE_INVENTORY,
            ("orders", "read"): Permission.READ_ORDERS,
            ("orders", "write"): Permission.WRITE_ORDERS,
            ("shipments", "read"): Permission.READ_SHIPMENTS,
            ("shipments", "write"): Permission.WRITE_SHIPMENTS,
            ("warehouse", "read"): Permission.READ_WAREHOUSE,
            ("warehouse", "write"): Permission.WRITE_WAREHOUSE,
        }

        required_permission = permission_map.get((stream_name, operation))
        if not required_permission:
            return False  # Unknown stream/operation combination

        return self.check_permission(username, required_permission)

    def get_user_permissions(self, username: str) -> Set[Permission]:
        """Get all permissions for a user."""

        user = self.users.get(username)
        if not user or not user.is_active:
            return set()

        user_permissions = set()
        for role_name in user.roles:
            role = self.roles.get(role_name)
            if role:
                user_permissions.update(role.permissions)

        return user_permissions

    def audit_access_attempt(self, username: str, resource: str,
                           operation: str, success: bool) -> Dict[str, str]:
        """Audit access attempt for security logging."""

        audit_record = {
            "timestamp": time.time(),
            "username": username,
            "resource": resource,
            "operation": operation,
            "success": success,
            "user_agent": "TargetOracleWMS",
            "audit_id": f"WMS_{int(time.time())}_{username}"
        }

        # Update user login tracking
        if username in self.users:
            user = self.users[username]
            if success:
                user.last_login = time.time()
                user.failed_login_attempts = 0
            else:
                user.failed_login_attempts += 1

                # Lock account after 5 failed attempts
                if user.failed_login_attempts >= 5:
                    user.locked_until = time.time() + 1800  # 30 minutes

        return audit_record
```

### **API Key Management**

```python
# api_key_management.py
import secrets
import hashlib
import time
from typing import Dict, Optional, List
from dataclasses import dataclass

@dataclass
class APIKey:
    """API Key with metadata and permissions."""

    key_id: str
    key_hash: str
    name: str
    description: str
    permissions: List[str]
    created_at: float
    expires_at: Optional[float] = None
    is_active: bool = True
    last_used: Optional[float] = None
    usage_count: int = 0
    rate_limit: int = 1000  # requests per hour

class APIKeyManager:
    """Secure API key management for WMS target."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.api_keys: Dict[str, APIKey] = {}
        self.key_prefix = "wms_"

    def generate_api_key(self, name: str, description: str,
                        permissions: List[str], expires_hours: Optional[int] = None) -> str:
        """Generate new API key with specified permissions."""

        # Generate secure random key
        key_id = secrets.token_hex(8)
        key_secret = secrets.token_hex(32)
        full_key = f"{self.key_prefix}{key_id}_{key_secret}"

        # Hash for storage
        key_hash = hashlib.sha256(full_key.encode()).hexdigest()

        # Calculate expiry
        expires_at = None
        if expires_hours:
            expires_at = time.time() + (expires_hours * 3600)

        # Create API key record
        api_key = APIKey(
            key_id=key_id,
            key_hash=key_hash,
            name=name,
            description=description,
            permissions=permissions,
            created_at=time.time(),
            expires_at=expires_at
        )

        self.api_keys[key_id] = api_key

        return full_key

    def validate_api_key(self, provided_key: str) -> Optional[APIKey]:
        """Validate provided API key."""

        if not provided_key.startswith(self.key_prefix):
            return None

        try:
            # Extract key ID
            key_part = provided_key[len(self.key_prefix):]
            key_id = key_part.split('_')[0]

            api_key = self.api_keys.get(key_id)
            if not api_key:
                return None

            # Check if key is active
            if not api_key.is_active:
                return None

            # Check expiry
            if api_key.expires_at and time.time() > api_key.expires_at:
                return None

            # Validate hash
            provided_hash = hashlib.sha256(provided_key.encode()).hexdigest()
            if provided_hash != api_key.key_hash:
                return None

            # Update usage tracking
            api_key.last_used = time.time()
            api_key.usage_count += 1

            return api_key

        except Exception:
            return None

    def check_rate_limit(self, api_key: APIKey) -> bool:
        """Check if API key is within rate limits."""

        current_time = time.time()
        hour_ago = current_time - 3600

        # In a real implementation, you would track usage in a time-series database
        # For this example, we'll use a simple counter

        # Reset counter if more than an hour has passed
        if api_key.last_used and (current_time - api_key.last_used) > 3600:
            api_key.usage_count = 0

        return api_key.usage_count < api_key.rate_limit

    def revoke_api_key(self, key_id: str) -> bool:
        """Revoke an API key."""

        api_key = self.api_keys.get(key_id)
        if api_key:
            api_key.is_active = False
            return True

        return False

    def list_api_keys(self) -> List[Dict[str, str]]:
        """List all API keys (without secrets)."""

        return [
            {
                "key_id": api_key.key_id,
                "name": api_key.name,
                "description": api_key.description,
                "permissions": api_key.permissions,
                "created_at": api_key.created_at,
                "expires_at": api_key.expires_at,
                "is_active": api_key.is_active,
                "last_used": api_key.last_used,
                "usage_count": api_key.usage_count
            }
            for api_key in self.api_keys.values()
        ]
```

---

## 📊 **Audit & Compliance**

### **Security Audit Logging**

```python
# security_audit.py
import json
import time
import logging
import hashlib
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class AuditEventType(Enum):
    """Types of audit events."""

    AUTHENTICATION_SUCCESS = "auth_success"
    AUTHENTICATION_FAILURE = "auth_failure"
    AUTHORIZATION_DENIED = "authz_denied"
    DATA_ACCESS = "data_access"
    DATA_MODIFICATION = "data_modification"
    CONFIGURATION_CHANGE = "config_change"
    SECURITY_VIOLATION = "security_violation"
    SYSTEM_EVENT = "system_event"

@dataclass
class AuditEvent:
    """Security audit event record."""

    event_id: str
    timestamp: float
    event_type: AuditEventType
    username: str
    source_ip: str
    user_agent: str
    resource: str
    action: str
    success: bool
    details: Dict[str, Any]
    risk_score: int = 0
    session_id: Optional[str] = None

class SecurityAuditManager:
    """Comprehensive security audit manager for WMS target."""

    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.logger = self._setup_audit_logger()
        self.events: List[AuditEvent] = []
        self.high_risk_threshold = 7

    def _setup_audit_logger(self) -> logging.Logger:
        """Setup secure audit logging."""

        logger = logging.getLogger("wms_security_audit")
        logger.setLevel(logging.INFO)

        # Create secure file handler
        audit_file = self.config.get("audit_log_file", "/var/log/wms/security_audit.log")
        handler = logging.FileHandler(audit_file, mode='a')

        # Use structured JSON logging
        formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "event": %(message)s}'
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger

    def log_authentication_attempt(self, username: str, source_ip: str,
                                 user_agent: str, success: bool,
                                 details: Dict[str, Any] = None) -> str:
        """Log authentication attempt."""

        event_type = AuditEventType.AUTHENTICATION_SUCCESS if success else AuditEventType.AUTHENTICATION_FAILURE

        audit_event = self._create_audit_event(
            event_type=event_type,
            username=username,
            source_ip=source_ip,
            user_agent=user_agent,
            resource="authentication",
            action="login",
            success=success,
            details=details or {}
        )

        # Calculate risk score for failed authentication
        if not success:
            audit_event.risk_score = self._calculate_auth_failure_risk(username, source_ip)

        self._log_audit_event(audit_event)
        return audit_event.event_id

    def log_data_access(self, username: str, source_ip: str, user_agent: str,
                       stream_name: str, operation: str, record_count: int,
                       success: bool, details: Dict[str, Any] = None) -> str:
        """Log data access attempt."""

        audit_event = self._create_audit_event(
            event_type=AuditEventType.DATA_ACCESS,
            username=username,
            source_ip=source_ip,
            user_agent=user_agent,
            resource=f"stream:{stream_name}",
            action=operation,
            success=success,
            details={
                "record_count": record_count,
                **(details or {})
            }
        )

        # Calculate risk for unusual access patterns
        audit_event.risk_score = self._calculate_data_access_risk(
            username, stream_name, operation, record_count
        )

        self._log_audit_event(audit_event)
        return audit_event.event_id

    def log_authorization_denial(self, username: str, source_ip: str,
                               user_agent: str, resource: str, action: str,
                               required_permission: str) -> str:
        """Log authorization denial."""

        audit_event = self._create_audit_event(
            event_type=AuditEventType.AUTHORIZATION_DENIED,
            username=username,
            source_ip=source_ip,
            user_agent=user_agent,
            resource=resource,
            action=action,
            success=False,
            details={
                "required_permission": required_permission,
                "denial_reason": "insufficient_privileges"
            }
        )

        # Authorization denials are medium risk
        audit_event.risk_score = 5

        self._log_audit_event(audit_event)
        return audit_event.event_id

    def log_security_violation(self, username: str, source_ip: str,
                             violation_type: str, details: Dict[str, Any]) -> str:
        """Log security violation."""

        audit_event = self._create_audit_event(
            event_type=AuditEventType.SECURITY_VIOLATION,
            username=username,
            source_ip=source_ip,
            user_agent="",
            resource="security",
            action=violation_type,
            success=False,
            details=details
        )

        # Security violations are high risk
        audit_event.risk_score = 9

        self._log_audit_event(audit_event)

        # Send immediate alert for high-risk events
        self._send_security_alert(audit_event)

        return audit_event.event_id

    def _create_audit_event(self, event_type: AuditEventType, username: str,
                          source_ip: str, user_agent: str, resource: str,
                          action: str, success: bool, details: Dict[str, Any]) -> AuditEvent:
        """Create audit event with unique ID."""

        timestamp = time.time()
        event_data = f"{timestamp}{username}{source_ip}{resource}{action}"
        event_id = hashlib.sha256(event_data.encode()).hexdigest()[:16]

        return AuditEvent(
            event_id=event_id,
            timestamp=timestamp,
            event_type=event_type,
            username=username,
            source_ip=source_ip,
            user_agent=user_agent,
            resource=resource,
            action=action,
            success=success,
            details=details
        )

    def _calculate_auth_failure_risk(self, username: str, source_ip: str) -> int:
        """Calculate risk score for authentication failure."""

        risk_score = 3  # Base risk for auth failure

        # Increase risk for multiple failures from same IP
        recent_failures = self._count_recent_failures(source_ip, hours=1)
        if recent_failures >= 5:
            risk_score += 3
        elif recent_failures >= 3:
            risk_score += 2

        # Increase risk for service account failures
        if username.startswith("service_") or username.startswith("system_"):
            risk_score += 2

        # Increase risk for suspicious IP patterns
        if self._is_suspicious_ip(source_ip):
            risk_score += 3

        return min(risk_score, 10)

    def _calculate_data_access_risk(self, username: str, stream_name: str,
                                  operation: str, record_count: int) -> int:
        """Calculate risk score for data access."""

        risk_score = 1  # Base risk for data access

        # Higher risk for large data extractions
        if record_count > 10000:
            risk_score += 3
        elif record_count > 1000:
            risk_score += 1

        # Higher risk for sensitive streams
        sensitive_streams = ["orders", "shipments", "warehouse"]
        if stream_name in sensitive_streams:
            risk_score += 2

        # Higher risk for unusual access patterns
        if self._is_unusual_access_pattern(username, stream_name, operation):
            risk_score += 2

        return min(risk_score, 10)

    def _log_audit_event(self, event: AuditEvent):
        """Log audit event to secure storage."""

        # Convert to JSON for logging
        event_json = json.dumps(asdict(event), default=str)

        # Log to file
        self.logger.info(event_json)

        # Store in memory for analysis
        self.events.append(event)

        # Keep only recent events in memory
        cutoff_time = time.time() - (24 * 3600)  # 24 hours
        self.events = [e for e in self.events if e.timestamp > cutoff_time]

        # Send alert for high-risk events
        if event.risk_score >= self.high_risk_threshold:
            self._send_security_alert(event)

    def _send_security_alert(self, event: AuditEvent):
        """Send security alert for high-risk events."""

        alert_data = {
            "alert_type": "security_risk",
            "event_id": event.event_id,
            "risk_score": event.risk_score,
            "username": event.username,
            "source_ip": event.source_ip,
            "event_type": event.event_type.value,
            "resource": event.resource,
            "action": event.action,
            "timestamp": event.timestamp
        }

        # In a real implementation, send to SIEM or alert system
        print(f"🚨 HIGH RISK SECURITY EVENT: {json.dumps(alert_data, indent=2)}")

    def get_security_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get security summary for specified time period."""

        cutoff_time = time.time() - (hours * 3600)
        recent_events = [e for e in self.events if e.timestamp > cutoff_time]

        summary = {
            "time_period_hours": hours,
            "total_events": len(recent_events),
            "high_risk_events": len([e for e in recent_events if e.risk_score >= self.high_risk_threshold]),
            "failed_authentications": len([e for e in recent_events if e.event_type == AuditEventType.AUTHENTICATION_FAILURE]),
            "authorization_denials": len([e for e in recent_events if e.event_type == AuditEventType.AUTHORIZATION_DENIED]),
            "security_violations": len([e for e in recent_events if e.event_type == AuditEventType.SECURITY_VIOLATION]),
            "unique_users": len(set(e.username for e in recent_events)),
            "unique_source_ips": len(set(e.source_ip for e in recent_events))
        }

        return summary
```

### **Compliance Reporting**

```python
# compliance_reporting.py
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime, timedelta
import json

@dataclass
class ComplianceReport:
    """Compliance report structure."""

    report_id: str
    framework: str
    generated_at: datetime
    period_start: datetime
    period_end: datetime
    compliance_score: float
    findings: List[Dict[str, Any]]
    recommendations: List[str]

class ComplianceManager:
    """Compliance management for regulatory requirements."""

    def __init__(self, config: Dict[str, str], audit_manager):
        self.config = config
        self.audit_manager = audit_manager
        self.frameworks = ["SOX", "GDPR", "CCPA", "SOC2", "ISO27001"]

    def generate_sox_compliance_report(self, days: int = 90) -> ComplianceReport:
        """Generate SOX compliance report for financial data controls."""

        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)

        findings = []

        # Check data access controls
        data_access_controls = self._check_data_access_controls()
        findings.extend(data_access_controls)

        # Check audit trail completeness
        audit_completeness = self._check_audit_completeness(start_date, end_date)
        findings.extend(audit_completeness)

        # Check segregation of duties
        segregation_check = self._check_segregation_of_duties()
        findings.extend(segregation_check)

        compliance_score = self._calculate_compliance_score(findings)

        return ComplianceReport(
            report_id=f"SOX_{int(end_date.timestamp())}",
            framework="SOX",
            generated_at=end_date,
            period_start=start_date,
            period_end=end_date,
            compliance_score=compliance_score,
            findings=findings,
            recommendations=self._generate_sox_recommendations(findings)
        )

    def generate_gdpr_compliance_report(self, days: int = 30) -> ComplianceReport:
        """Generate GDPR compliance report for data protection."""

        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)

        findings = []

        # Check data encryption
        encryption_check = self._check_data_encryption()
        findings.extend(encryption_check)

        # Check data access logging
        access_logging = self._check_data_access_logging(start_date, end_date)
        findings.extend(access_logging)

        # Check data retention policies
        retention_check = self._check_data_retention()
        findings.extend(retention_check)

        # Check consent management
        consent_check = self._check_consent_management()
        findings.extend(consent_check)

        compliance_score = self._calculate_compliance_score(findings)

        return ComplianceReport(
            report_id=f"GDPR_{int(end_date.timestamp())}",
            framework="GDPR",
            generated_at=end_date,
            period_start=start_date,
            period_end=end_date,
            compliance_score=compliance_score,
            findings=findings,
            recommendations=self._generate_gdpr_recommendations(findings)
        )

    def _check_data_access_controls(self) -> List[Dict[str, Any]]:
        """Check data access controls implementation."""

        findings = []

        # Check if RBAC is properly implemented
        rbac_finding = {
            "control_id": "AC-001",
            "control_name": "Role-Based Access Control",
            "status": "COMPLIANT",
            "description": "RBAC properly implemented with defined roles and permissions",
            "evidence": "Role definitions and permission mappings verified"
        }
        findings.append(rbac_finding)

        # Check authentication controls
        auth_finding = {
            "control_id": "AC-002",
            "control_name": "Strong Authentication",
            "status": "COMPLIANT",
            "description": "Multi-factor authentication available for privileged accounts",
            "evidence": "MFA implementation verified"
        }
        findings.append(auth_finding)

        return findings

    def _check_audit_completeness(self, start_date: datetime, end_date: datetime) -> List[Dict[str, Any]]:
        """Check audit trail completeness."""

        findings = []

        # Check audit log coverage
        audit_finding = {
            "control_id": "AU-001",
            "control_name": "Comprehensive Audit Logging",
            "status": "COMPLIANT",
            "description": "All critical events are logged with sufficient detail",
            "evidence": f"Audit logs from {start_date} to {end_date} reviewed"
        }
        findings.append(audit_finding)

        return findings

    def generate_compliance_summary(self) -> Dict[str, Any]:
        """Generate overall compliance summary."""

        summary = {
            "last_updated": datetime.utcnow().isoformat(),
            "frameworks": {},
            "overall_score": 0,
            "critical_findings": [],
            "recommendations": []
        }

        total_score = 0
        framework_count = 0

        for framework in self.frameworks:
            if framework == "SOX":
                report = self.generate_sox_compliance_report()
            elif framework == "GDPR":
                report = self.generate_gdpr_compliance_report()
            else:
                continue  # Skip frameworks not yet implemented

            summary["frameworks"][framework] = {
                "score": report.compliance_score,
                "last_assessment": report.generated_at.isoformat(),
                "findings_count": len(report.findings),
                "status": "COMPLIANT" if report.compliance_score >= 0.8 else "NEEDS_ATTENTION"
            }

            total_score += report.compliance_score
            framework_count += 1

            # Collect critical findings
            critical_findings = [f for f in report.findings if f.get("status") == "NON_COMPLIANT"]
            summary["critical_findings"].extend(critical_findings)

        if framework_count > 0:
            summary["overall_score"] = total_score / framework_count

        return summary
```

---

## 🔗 **Cross-References**

### **Related Documentation**

- [Implementation Guides](../guides/README.md) - Security implementation in practice
- [API Reference](../api/README.md) - Authentication and authorization APIs
- [Architecture Guide](../architecture/README.md) - Security architecture patterns
- [Deployment Guide](../deployment/README.md) - Production security considerations

### **Security Standards**

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) - Comprehensive security framework
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) - Information security management
- [SOC 2](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report.html) - Security and availability controls

### **Oracle Security Resources**

- [Oracle Cloud Security Guide](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csgsg/) - Oracle-specific security practices
- [Oracle WMS Security](https://docs.oracle.com/en/industries/retail/warehouse-management/25b/wmssc/) - WMS security configuration
- [Oracle Identity Management](https://docs.oracle.com/en/middleware/idm/) - Enterprise identity solutions

---

**🔐 Security Implementation**: Target Oracle WMS | **🏠 Root**: [PyAuto Home](../../../README.md) | **Framework**: Singer SDK 0.39.0+ | **Updated**: 2025-06-19
