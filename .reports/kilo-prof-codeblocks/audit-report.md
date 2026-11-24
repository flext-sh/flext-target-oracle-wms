# Docs Audit Report

Scope: flext-target-oracle-wms
Files scanned: 40
Issues: 4

| file | type | severity | message |
| --- | --- | --- | --- |
| docs/security/snyk-sast-triage.md | python_codeblock | medium | block #0: invalid-syntax: Unexpected indentation
 --> docs/security/snyk-sast-triage.md#block0.py:1:1
  |
1 |        31
  | ^^^^^^^
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block0.py:1:1
  |
1 |        31
  | ^^^^^^^
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block0.py:2:1
  |
1 |        31
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
  | ^^^^^^^
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
  |

invalid-syntax: Simple statements must be separated by newlines or semicolons
 --> docs/security/snyk-sast-triage.md#block0.py:2:12
  |
1 |        31
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
  |            ^^^^^^^^
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block0.py:3:16
  |
1 |        31
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
  |                ^^^^^^^^^^
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block0.py:3:26
  |
1 |        31
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
  |                          ^
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block0.py:4:16
  |
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
  |                ^^^^^^^^^^
5 | >>>    35      "password": "wms_pass",
6 |        36  })
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block0.py:4:26
  |
2 |        32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
  |                          ^
5 | >>>    35      "password": "wms_pass",
6 |        36  })
  |

invalid-syntax: Expected `,`, found `>>`
 --> docs/security/snyk-sast-triage.md#block0.py:5:1
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  | ^^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |

missing-whitespace-around-bitwise-or-shift-operator: Missing whitespace around bitwise or shift operator
 --> docs/security/snyk-sast-triage.md#block0.py:5:1
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  | ^^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |
help: Add missing whitespace

invalid-syntax: Expected `,`, found `>`
 --> docs/security/snyk-sast-triage.md#block0.py:5:3
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |   ^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |

missing-whitespace-around-operator: Missing whitespace around operator
 --> docs/security/snyk-sast-triage.md#block0.py:5:3
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |   ^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |
help: Add missing whitespace

multiple-spaces-after-operator: Multiple spaces after operator
 --> docs/security/snyk-sast-triage.md#block0.py:5:4
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |    ^^^^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |
help: Replace with single space

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block0.py:5:16
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |                ^^^^^^^^^^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block0.py:5:26
  |
3 |        33      "base_url": "https://wms.example.oraclecloud.com",
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
  |                          ^
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |

whitespace-before-close-bracket: Whitespace before '}'
 --> docs/security/snyk-sast-triage.md#block0.py:6:10
  |
4 |        34      "username": "wms_user",
5 | >>>    35      "password": "wms_pass",
6 |        36  })
  |          ^^
7 |        37  BATCH_SIZE: Final[int] = 100
8 |        38
  |
help: Remove whitespace before '}'

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block0.py:7:1
  |
5 | >>>    35      "password": "wms_pass",
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  | ^^^^^^^
8 |        38
9 |        39
  |

invalid-syntax: Simple statements must be separated by newlines or semicolons
 --> docs/security/snyk-sast-triage.md#block0.py:7:12
  |
5 | >>>    35      "password": "wms_pass",
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
  |            ^^^^^^^^^^
8 |        38
9 |        39
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block0.py:8:1
  |
6 |        36  })
7 |        37  BATCH_SIZE: Final[int] = 100
8 |        38
  | ^^^^^^^
9 |        39
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block0.py:9:1
  |
7 |        37  BATCH_SIZE: Final[int] = 100
8 |        38
9 |        39
  | ^^^^^^^

Found 20 errors. |
| docs/security/snyk-sast-triage.md | python_codeblock | medium | block #1: invalid-syntax: Unexpected indentation
 --> docs/security/snyk-sast-triage.md#block1.py:1:1
  |
1 |        27
  | ^^^^^^^
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block1.py:1:1
  |
1 |        27
  | ^^^^^^^
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block1.py:2:1
  |
1 |        27
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
  | ^^^^^^^
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
  |

invalid-syntax: Simple statements must be separated by newlines or semicolons
 --> docs/security/snyk-sast-triage.md#block1.py:2:12
  |
1 |        27
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
  |            ^^^^^^^^^^^^^^^
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block1.py:3:16
  |
1 |        27
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
  |                ^^^^^^^^^^
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block1.py:3:26
  |
1 |        27
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
  |                          ^
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block1.py:4:16
  |
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
  |                ^^^^^^^^^^
5 | >>>    31      "password": "wms_batch_pass",
6 |        32  }
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block1.py:4:26
  |
2 |        28  _BATCH_WMS_AUTH: t.JsonDict = {
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
  |                          ^
5 | >>>    31      "password": "wms_batch_pass",
6 |        32  }
  |

invalid-syntax: Expected `,`, found `>>`
 --> docs/security/snyk-sast-triage.md#block1.py:5:1
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  | ^^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |

missing-whitespace-around-bitwise-or-shift-operator: Missing whitespace around bitwise or shift operator
 --> docs/security/snyk-sast-triage.md#block1.py:5:1
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  | ^^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |
help: Add missing whitespace

invalid-syntax: Expected `,`, found `>`
 --> docs/security/snyk-sast-triage.md#block1.py:5:3
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |   ^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |

missing-whitespace-around-operator: Missing whitespace around operator
 --> docs/security/snyk-sast-triage.md#block1.py:5:3
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |   ^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |
help: Add missing whitespace

multiple-spaces-after-operator: Multiple spaces after operator
 --> docs/security/snyk-sast-triage.md#block1.py:5:4
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |    ^^^^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |
help: Replace with single space

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block1.py:5:16
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |                ^^^^^^^^^^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block1.py:5:26
  |
3 |        29      "base_url": "https://wms.example.oraclecloud.com",
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
  |                          ^
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |

whitespace-before-close-bracket: Whitespace before '}'
 --> docs/security/snyk-sast-triage.md#block1.py:6:10
  |
4 |        30      "username": "wms_batch_user",
5 | >>>    31      "password": "wms_batch_pass",
6 |        32  }
  |          ^^
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
  |
help: Remove whitespace before '}'

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block1.py:7:1
  |
5 | >>>    31      "password": "wms_batch_pass",
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  | ^^^^^^^
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
9 |        35      "batch_size": 500,
  |

invalid-syntax: Simple statements must be separated by newlines or semicolons
 --> docs/security/snyk-sast-triage.md#block1.py:7:12
  |
5 | >>>    31      "password": "wms_batch_pass",
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
  |            ^^^^^^^^^^^^
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
9 |        35      "batch_size": 500,
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block1.py:8:16
  |
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
  |                ^^^^^^^^^^
9 |        35      "batch_size": 500,
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block1.py:8:26
  |
6 |        32  }
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
  |                          ^
9 |        35      "batch_size": 500,
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block1.py:9:16
  |
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
9 |        35      "batch_size": 500,
  |                ^^^^^^^^^^^^

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block1.py:9:28
  |
7 |        33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
9 |        35      "batch_size": 500,
  |                            ^

invalid-syntax: unexpected EOF while parsing
 --> docs/security/snyk-sast-triage.md#block1.py:9:35
  |
8 |        34      "wms_auth": _BATCH_WMS_AUTH,
9 |        35      "batch_size": 500,
  |                                  ^

Found 23 errors. |
| docs/security/snyk-sast-triage.md | python_codeblock | medium | block #2: invalid-syntax: Unexpected indentation
 --> docs/security/snyk-sast-triage.md#block2.py:1:1
  |
1 |        33
  | ^^^^^^^
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block2.py:1:1
  |
1 |        33
  | ^^^^^^^
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block2.py:2:1
  |
1 |        33
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
  | ^^^^^^^
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
  |

invalid-syntax: Simple statements must be separated by newlines or semicolons
 --> docs/security/snyk-sast-triage.md#block2.py:2:12
  |
1 |        33
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
  |            ^^^^^^^^^^^^^
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block2.py:3:16
  |
1 |        33
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
  |                ^^^^^^^^^^
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block2.py:3:26
  |
1 |        33
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
  |                          ^
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block2.py:4:16
  |
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
  |                ^^^^^^^^^^
5 | >>>    37      "password": "wms_target_pass",
6 |        38  })
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block2.py:4:26
  |
2 |        34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
  |                          ^
5 | >>>    37      "password": "wms_target_pass",
6 |        38  })
  |

invalid-syntax: Expected `,`, found `>>`
 --> docs/security/snyk-sast-triage.md#block2.py:5:1
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  | ^^
6 |        38  })
7 |        39
  |

missing-whitespace-around-bitwise-or-shift-operator: Missing whitespace around bitwise or shift operator
 --> docs/security/snyk-sast-triage.md#block2.py:5:1
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  | ^^
6 |        38  })
7 |        39
  |
help: Add missing whitespace

invalid-syntax: Expected `,`, found `>`
 --> docs/security/snyk-sast-triage.md#block2.py:5:3
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |   ^
6 |        38  })
7 |        39
  |

missing-whitespace-around-operator: Missing whitespace around operator
 --> docs/security/snyk-sast-triage.md#block2.py:5:3
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |   ^
6 |        38  })
7 |        39
  |
help: Add missing whitespace

multiple-spaces-after-operator: Multiple spaces after operator
 --> docs/security/snyk-sast-triage.md#block2.py:5:4
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |    ^^^^
6 |        38  })
7 |        39
  |
help: Replace with single space

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block2.py:5:16
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |                ^^^^^^^^^^
6 |        38  })
7 |        39
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block2.py:5:26
  |
3 |        35      "base_url": "https://wms.example.oraclecloud.com",
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
  |                          ^
6 |        38  })
7 |        39
  |

whitespace-before-close-bracket: Whitespace before '}'
 --> docs/security/snyk-sast-triage.md#block2.py:6:10
  |
4 |        36      "username": "wms_target_user",
5 | >>>    37      "password": "wms_target_pass",
6 |        38  })
  |          ^^
7 |        39
8 |        40
  |
help: Remove whitespace before '}'

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block2.py:7:1
  |
5 | >>>    37      "password": "wms_target_pass",
6 |        38  })
7 |        39
  | ^^^^^^^
8 |        40
9 |        41  @flext_monitor_function(monitor)
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block2.py:8:1
  |
6 |        38  })
7 |        39
8 |        40
  | ^^^^^^^
9 |        41  @flext_monitor_function(monitor)
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block2.py:9:1
  |
7 |        39
8 |        40
9 |        41  @flext_monitor_function(monitor)
  | ^^^^^^^

missing-whitespace-around-arithmetic-operator: Missing whitespace around arithmetic operator
 --> docs/security/snyk-sast-triage.md#block2.py:9:12
  |
7 |        39
8 |        40
9 |        41  @flext_monitor_function(monitor)
  |            ^
help: Add missing whitespace

Found 20 errors. |
| docs/security/snyk-sast-triage.md | python_codeblock | medium | block #3: invalid-syntax: Unexpected indentation
 --> docs/security/snyk-sast-triage.md#block3.py:1:1
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
  | ^^^^^^^
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block3.py:1:1
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
  | ^^^^^^^
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
  |

invalid-syntax: Simple statements must be separated by newlines or semicolons
 --> docs/security/snyk-sast-triage.md#block3.py:1:24
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
  |                        ^
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block3.py:2:28
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
2 |        90                  "wms_auth": {
  |                            ^^^^^^^^^^
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block3.py:2:38
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
2 |        90                  "wms_auth": {
  |                                      ^
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block3.py:3:32
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
  |                                ^^^^^^^^^^
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block3.py:3:42
  |
1 |        89              m.TargetOracleWms.WmsTargetConfig.model_validate({
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
  |                                          ^
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block3.py:4:32
  |
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
  |                                ^^^^^^^^^^
5 | >>>    93                      "password": "oracle",
6 |        94                  }
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block3.py:4:42
  |
2 |        90                  "wms_auth": {
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
  |                                          ^
5 | >>>    93                      "password": "oracle",
6 |        94                  }
  |

invalid-syntax: Expected `,`, found `>>`
 --> docs/security/snyk-sast-triage.md#block3.py:5:1
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  | ^^
6 |        94                  }
7 |        95              })
  |

missing-whitespace-around-bitwise-or-shift-operator: Missing whitespace around bitwise or shift operator
 --> docs/security/snyk-sast-triage.md#block3.py:5:1
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  | ^^
6 |        94                  }
7 |        95              })
  |
help: Add missing whitespace

invalid-syntax: Expected `,`, found `>`
 --> docs/security/snyk-sast-triage.md#block3.py:5:3
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |   ^
6 |        94                  }
7 |        95              })
  |

missing-whitespace-around-operator: Missing whitespace around operator
 --> docs/security/snyk-sast-triage.md#block3.py:5:3
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |   ^
6 |        94                  }
7 |        95              })
  |
help: Add missing whitespace

multiple-spaces-after-operator: Multiple spaces after operator
 --> docs/security/snyk-sast-triage.md#block3.py:5:4
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |    ^^^^
6 |        94                  }
7 |        95              })
  |
help: Replace with single space

invalid-syntax: Expected `,`, found string
 --> docs/security/snyk-sast-triage.md#block3.py:5:32
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |                                ^^^^^^^^^^
6 |        94                  }
7 |        95              })
  |

invalid-syntax: Expected `,`, found `:`
 --> docs/security/snyk-sast-triage.md#block3.py:5:42
  |
3 |        91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
  |                                          ^
6 |        94                  }
7 |        95              })
  |

whitespace-before-close-bracket: Whitespace before '}'
 --> docs/security/snyk-sast-triage.md#block3.py:6:10
  |
4 |        92                      "username": "oracle",
5 | >>>    93                      "password": "oracle",
6 |        94                  }
  |          ^^^^^^^^^^^^^^^^^^
7 |        95              })
8 |        96          )
  |
help: Remove whitespace before '}'

invalid-syntax: Expected `,`, found int
 --> docs/security/snyk-sast-triage.md#block3.py:7:8
  |
5 | >>>    93                      "password": "oracle",
6 |        94                  }
7 |        95              })
  |        ^^
8 |        96          )
9 |        97
  |

whitespace-before-close-bracket: Whitespace before '}'
 --> docs/security/snyk-sast-triage.md#block3.py:7:10
  |
5 | >>>    93                      "password": "oracle",
6 |        94                  }
7 |        95              })
  |          ^^^^^^^^^^^^^^
8 |        96          )
9 |        97
  |
help: Remove whitespace before '}'

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block3.py:8:1
  |
6 |        94                  }
7 |        95              })
8 |        96          )
  | ^^^^^^^
9 |        97
  |

whitespace-before-close-bracket: Whitespace before ')'
 --> docs/security/snyk-sast-triage.md#block3.py:8:10
  |
6 |        94                  }
7 |        95              })
8 |        96          )
  |          ^^^^^^^^^^
9 |        97
  |
help: Remove whitespace before ')'

invalid-syntax: Expected a statement
 --> docs/security/snyk-sast-triage.md#block3.py:8:20
  |
6 |        94                  }
7 |        95              })
8 |        96          )
  |                    ^
9 |        97
  |

invalid-syntax: Expected a statement
 --> docs/security/snyk-sast-triage.md#block3.py:8:21
  |
6 |        94                  }
7 |        95              })
8 |        96          )
  |                     ^
9 |        97
  |

indentation-with-invalid-multiple: Indentation is not a multiple of 4
 --> docs/security/snyk-sast-triage.md#block3.py:9:1
  |
7 |        95              })
8 |        96          )
9 |        97
  | ^^^^^^^

Found 24 errors. |
