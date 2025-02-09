#!/usr/bin/env python
# SPDX-License-Identifier: CC0-1.0
#
# vim:sw=4:ts=4:et
from dasbus.typing import Variant
from bluechi.api import Node

Node("my-node-name").set_unit_properties(
    "ldconfig.service", False, [("CPUWeight", Variant("t", 18446744073709551615))]
)
