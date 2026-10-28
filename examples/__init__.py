# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import s
    from flext_oracle_wms import e

    from examples.constants import ExamplesFlextTargetOracleWmsConstants
    from examples.example_01_basic_usage import FlextTargetOracleWmsExampleBasicUsage
    from examples.example_02_batch_processing import (
        FlextTargetOracleWmsExampleBatchProcessing,
    )
    from examples.example_03_error_handling import (
        FlextTargetOracleWmsExampleErrorHandling,
    )
    from examples.example_04_factory_usage import (
        FlextTargetOracleWmsExampleFactoryUsage,
    )
    from examples.example_05_advanced_configuration import (
        FlextTargetOracleWmsExampleAdvancedConfiguration,
    )
    from examples.models import ExamplesFlextTargetOracleWmsModels
    from examples.protocols import ExamplesFlextTargetOracleWmsProtocols
    from examples.typings import ExamplesFlextTargetOracleWmsTypes
    from examples.utilities import ExamplesFlextTargetOracleWmsUtilities, u
    from flext_target_oracle_wms import (
        api,
        build_lazy_import_map,
        c,
        cleanup_submodule_namespace,
        cli,
        config,
        core,
        d,
        h,
        install_lazy_exports,
        lazy,
        lazy_getattr,
        lazy_member,
        m,
        main,
        meltano,
        merge_lazy_imports,
        normalize_lazy_imports,
        oracle_wms,
        p,
        r,
        resolve_lazy_members,
        settings,
        t,
        target_oracle_wms,
        web,
        x,
    )


__all__: tuple[str, ...] = (
    "ExamplesFlextTargetOracleWmsConstants",
    "ExamplesFlextTargetOracleWmsModels",
    "ExamplesFlextTargetOracleWmsProtocols",
    "ExamplesFlextTargetOracleWmsTypes",
    "ExamplesFlextTargetOracleWmsUtilities",
    "FlextTargetOracleWmsExampleAdvancedConfiguration",
    "FlextTargetOracleWmsExampleBasicUsage",
    "FlextTargetOracleWmsExampleBatchProcessing",
    "FlextTargetOracleWmsExampleErrorHandling",
    "FlextTargetOracleWmsExampleFactoryUsage",
    "api",
    "build_lazy_import_map",
    "c",
    "cleanup_submodule_namespace",
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "install_lazy_exports",
    "lazy",
    "lazy_getattr",
    "lazy_member",
    "m",
    "main",
    "meltano",
    "merge_lazy_imports",
    "normalize_lazy_imports",
    "oracle_wms",
    "p",
    "r",
    "resolve_lazy_members",
    "s",
    "settings",
    "t",
    "target_oracle_wms",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "ExamplesFlextTargetOracleWmsConstants": ".constants",
        "ExamplesFlextTargetOracleWmsModels": ".models",
        "ExamplesFlextTargetOracleWmsProtocols": ".protocols",
        "ExamplesFlextTargetOracleWmsTypes": ".typings",
        "ExamplesFlextTargetOracleWmsUtilities": ".utilities",
        "FlextTargetOracleWmsExampleAdvancedConfiguration": (
            ".example_05_advanced_configuration"
        ),
        "FlextTargetOracleWmsExampleBasicUsage": ".example_01_basic_usage",
        "FlextTargetOracleWmsExampleBatchProcessing": ".example_02_batch_processing",
        "FlextTargetOracleWmsExampleErrorHandling": ".example_03_error_handling",
        "FlextTargetOracleWmsExampleFactoryUsage": ".example_04_factory_usage",
        "api": "flext_target_oracle_wms",
        "build_lazy_import_map": "flext_target_oracle_wms",
        "c": "flext_target_oracle_wms",
        "cleanup_submodule_namespace": "flext_target_oracle_wms",
        "cli": "flext_target_oracle_wms",
        "config": "flext_target_oracle_wms",
        "core": "flext_target_oracle_wms",
        "d": "flext_target_oracle_wms",
        "e": "flext_oracle_wms",
        "h": "flext_target_oracle_wms",
        "install_lazy_exports": "flext_target_oracle_wms",
        "lazy": "flext_target_oracle_wms",
        "lazy_getattr": "flext_target_oracle_wms",
        "lazy_member": "flext_target_oracle_wms",
        "m": "flext_target_oracle_wms",
        "main": "flext_target_oracle_wms",
        "meltano": "flext_target_oracle_wms",
        "merge_lazy_imports": "flext_target_oracle_wms",
        "normalize_lazy_imports": "flext_target_oracle_wms",
        "oracle_wms": "flext_target_oracle_wms",
        "p": "flext_target_oracle_wms",
        "r": "flext_target_oracle_wms",
        "resolve_lazy_members": "flext_target_oracle_wms",
        "s": "flext_meltano",
        "settings": "flext_target_oracle_wms",
        "t": "flext_target_oracle_wms",
        "target_oracle_wms": "flext_target_oracle_wms",
        "u": ".utilities",
        "web": "flext_target_oracle_wms",
        "x": "flext_target_oracle_wms",
    }),
    public_exports=__all__,
)
