#!/usr/bin/env python
# SPDX-License-Identifier: CC0-1.0
#
# vim:sw=4:ts=4:et
from bluechi.ext import Unit

response = Unit("my-node-name").enable_unit_files(
    ["chronyd.service", "bluechi-agent.service"]
)
if response.carries_install_info:
    print("The unit files included enablement information")
else:
    print("The unit files did not include any enablement information")

for change in response.changes:
    if change.change_type == "symlink":
        print(
            f"Created symlink {change.symlink_file}"
            " -> {enabled_service_info.symlink_dest}"
        )
    elif change.change_type == "unlink":
        print(f'Removed "{change.symlink_file}".')
