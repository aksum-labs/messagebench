# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def root():
    return ROOT


@pytest.fixture
def source(root):
    return root / "corpus/positive/identity.source.xml"


@pytest.fixture
def contract(root):
    return root / "contracts/pacs008-preserve.json"


@pytest.fixture
def change_contract(contract, tmp_path):
    def change(fn):
        doc = json.loads(contract.read_text())
        fn(doc)
        path = tmp_path / "contract.json"
        path.write_text(json.dumps(doc))
        return path

    return change
