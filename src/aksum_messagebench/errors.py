# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Stable, payload-free diagnostic codes. Never render underlying exceptions."""


class BenchError(Exception):
    def __init__(self, code: str, exit_code: int):
        super().__init__(code)
        self.code = code
        self.exit_code = exit_code


PRECEDENCE = (5, 4, 2, 3, 1, 0)


def aggregate_exit(codes: list[int]) -> int:
    return next(code for code in PRECEDENCE if code in codes) if codes else 3
