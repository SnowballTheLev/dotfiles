#!/usr/bin/env python3

import json
import subprocess

"""
Get Focused Workspace then Assign Custom Workspace Names.
"""

workspace_names = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX"
}

def get_focused_workspace():
    try:
        i3_workspaces = json.loads(subprocess.check_output(["i3-msg", "-t", "get_workspaces"]))
        for workspace in i3_workspaces:
            if workspace["focused"]:
                return workspace["num"]
    except Exception as e:
        return None

def get_workspace_name(workspace_num):
    return workspace_names.get(workspace_num, workspace_names)

focused_workspace = get_focused_workspace()
if focused_workspace is not None:
    print(get_workspace_name(focused_workspace))
