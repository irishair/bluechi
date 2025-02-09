#!/usr/bin/python3
# SPDX-License-Identifier: CC0-1.0

from collections import namedtuple
import dasbus.connection

bus = dasbus.connection.SystemMessageBus()

NodeInfo = namedtuple("NodeInfo", ["name", "object_path", "status"])

manager = bus.get_proxy("org.eclipse.bluechi", "/org/eclipse/bluechi")
nodes = manager.ListNodes()
for n in nodes:
    info = NodeInfo(*n)
    print(f"Node: {info.name}, State: {info.status}")
