"""Module skeleton for TestsFlextTargetOracleWmsUtilities.

Test utilities for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import secrets
from typing import TYPE_CHECKING

from flext_tests import FlextTestsUtilities

from flext_target_oracle_wms import FlextTargetOracleWmsUtilities
from tests import c, m, t

if TYPE_CHECKING:
    from pathlib import Path


class TestsFlextTargetOracleWmsUtilities(
    FlextTestsUtilities,
    FlextTargetOracleWmsUtilities,
):
    """Test utilities for flext-target-oracle-wms."""

    class TargetOracleWms(FlextTargetOracleWmsUtilities.TargetOracleWms):
        """Target Oracle WMS test namespace over the production utilities."""

        class Tests:
            """Scenario builders shared by the target-oracle-wms test tiers."""

            @staticmethod
            def valid_config() -> t.JsonMapping:
                """Build a valid target config with a per-build generated secret.

                Returns:
                    The resulting ``t.JsonMapping``.

                """
                tests = c.TargetOracleWms.Tests
                return {
                    "wms_auth": {
                        "base_url": tests.WMS_BASE_URL,
                        "username": tests.WMS_USERNAME,
                        "password": secrets.token_urlsafe(tests.WMS_SECRET_BYTES),
                    },
                }

            @staticmethod
            def valid_config_json() -> str:
                """Serialize a valid target config as JSON text.

                Returns:
                    The resulting ``str``.

                """
                return (
                    TestsFlextTargetOracleWmsUtilities
                    .json_mapping_adapter()
                    .dump_json(
                        TestsFlextTargetOracleWmsUtilities.TargetOracleWms.Tests.valid_config()
                    )
                    .decode()
                )

            @staticmethod
            def write_config_file(config_json: str, tmp_path: Path) -> str:
                """Write ``config_json`` inside the fixture-owned ``tmp_path``.

                Returns:
                    The resulting ``str``.

                """
                config_file = tmp_path / c.TargetOracleWms.Tests.CONFIG_FILE_NAME
                config_file.write_text(config_json, encoding=c.DEFAULT_ENCODING)
                return str(config_file)

            @staticmethod
            def schema_msg(
                stream: str | None = None,
                key_properties: t.StrSequence | None = None,
            ) -> m.Meltano.SingerSchemaMessage:
                """Build a Singer SCHEMA message for ``stream``.

                Returns:
                    The resulting ``m.Meltano.SingerSchemaMessage``.

                """
                return m.Meltano.SingerSchemaMessage.model_validate({
                    "type": c.Meltano.SingerMessageType.SCHEMA,
                    c.ProcessingMode.STREAM: stream
                    or c.TargetOracleWms.Tests.DEFAULT_STREAM,
                    "schema": {"type": "object"},
                    "key_properties": key_properties or ["id"],
                })

            @staticmethod
            def record_msg(
                stream: str | None = None,
                record: t.JsonMapping | None = None,
            ) -> m.Meltano.SingerRecordMessage:
                """Build a Singer RECORD message for ``stream``.

                Returns:
                    The resulting ``m.Meltano.SingerRecordMessage``.

                """
                return m.Meltano.SingerRecordMessage(
                    type=c.Meltano.SingerMessageType.RECORD,
                    stream=stream or c.TargetOracleWms.Tests.DEFAULT_STREAM,
                    record=record or {"id": c.ParserBooleanToken.ONE},
                )

            @staticmethod
            def state_msg(
                value: t.JsonMapping | None = None,
            ) -> m.Meltano.SingerStateMessage:
                """Build a Singer STATE message; empty bookmarks when ``value`` is None.

                Returns:
                    The resulting ``m.Meltano.SingerStateMessage``.

                """
                return m.Meltano.SingerStateMessage.model_validate({
                    "type": c.Meltano.SingerMessageType.STATE,
                    "value": dict(value) if value is not None else {"bookmarks": {}},
                })


u = TestsFlextTargetOracleWmsUtilities
__all__: list[str] = ["TestsFlextTargetOracleWmsUtilities", "u"]
