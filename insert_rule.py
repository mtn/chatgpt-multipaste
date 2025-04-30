#!/usr/bin/env python3
import json
import sys
import os

# locate our rule.json next to this script
base = os.path.dirname(__file__)
rule_path = os.path.join(base, "rule.json")
rule = json.load(open(rule_path))

# load the user's karabiner.json
karabiner_path = sys.argv[1]
data = json.load(open(karabiner_path))

# inject the rule if it isn't already present
for profile in data.get("profiles", []):
    rules = profile.setdefault(
        "complex_modifications", {}).setdefault("rules", [])
    if not any(r.get("description") == rule["description"] for r in rules):
        rules.append(rule)

# write back
with open(karabiner_path, "w") as f:
    json.dump(data, f, indent=4)
