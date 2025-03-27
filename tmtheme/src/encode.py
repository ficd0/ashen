#!/bin/env python

# This script takes a yaml file
# with textmate highlight style array
# and outputs a tmTheme file.

import plistlib
import sys
import yaml

mapping_path= sys.argv[2]
with open(mapping_path, "r") as f:
    mapping: dict[str, str] = yaml.load(f, yaml.Loader)

def process(d, func):
    for k, v in d.items():
        if isinstance(v, dict):
            process(v, func)
        elif isinstance(v, str):
            d[k] = func(v)
def grep_color(s: str):
    if s in mapping:
        return mapping[s]
    else:
        return s

theme_path= sys.argv[1]

with open(theme_path, "r") as f:
    scopes: list[dict[str, str | dict[str, str]]] = yaml.load(f, yaml.Loader)
theme: dict[str, str | list] = {
    "name": "Ashen",
    "semanticClass": "theme.dark.ashen",
    "uuid": "b3437e78-ba04-4c87-b602-b41da2f987f8",
    "author": "Daniel Fichtinger",
    "colorSpaceName": "sRGB",
}
for i in range(len(scopes)):
    cur = scopes[i]
    process(cur, grep_color)
    scopes[i] = cur
theme["settings"] = scopes

with open("ashen.tmTheme", "wb") as f:
    plistlib.dump(theme, f)




