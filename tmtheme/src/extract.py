#!/bin/env python

# This script is for extracting the names and
# scopes from a tmTheme file. It also strips the
# color values to make it easier to read and add
# your own.

import plistlib
import sys
import yaml
import re

def process(d, func):
    for k, v in d.items():
        if isinstance(v, dict):
            process(v, func)
        elif isinstance(v, str):
            print("found str")
            d[k] = func(v)
def grep_color(s: str):
    if re.match(r"#[0-9a-fA-F]{6}", s):
        print("matched regex")
        return None
    else:
        return s

path = sys.argv[1]
out = []

with open(path, "rb") as f:
    theme = plistlib.load(f)
name: str = theme.get("name", "Unknown Theme")
name = name.replace(" ", "_")
theme = theme.get("settings", [])
out = []
for d in theme:
    process(d, grep_color)
    out.append(d)
print(f"Theme: {name}\n")
print("Scopes: \n")

with open(f"{name}.yml", "w") as f:
    yaml.dump(out, f)
