#!/usr/bin/env python
"""Script for hyprland to launch apps on workspace creation"""

import subprocess
import time

apps_to_launch = [
    "kitty nvim",
    "kitty yazi",
    "kitty tty-clock -c",
]

for app in apps_to_launch:
    subprocess.run(f"{app} &> /dev/null &", shell=True)
    time.sleep(0.3)

time.sleep(0.5)
subprocess.run("hyprctl dispatch layoutmsg focusmaster", shell=True)
