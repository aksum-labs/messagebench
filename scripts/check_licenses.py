"""Check reviewed runtime distribution metadata; not a legal opinion or native binary audit."""

import importlib.metadata as metadata

approved = {
    "attrs": "MIT",
    "jsonschema": "MIT",
    "jsonschema-specifications": "MIT",
    "lxml": "BSD-3-Clause",
    "referencing": "MIT",
    "rpds-py": "MIT",
    "typing_extensions": "PSF-2.0",
}
for name, expected in approved.items():
    dist = metadata.distribution(name)
    declared = dist.metadata.get("License-Expression") or dist.metadata.get("License")
    if declared != expected:
        raise SystemExit("Runtime license metadata changed or absent; review " + name)
print("Seven runtime distribution license declarations match reviewed policy.")
print(
    "Native-component and standards-asset obligations remain in the rights register "
    "and native-build docs."
)
