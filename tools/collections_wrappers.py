#!/usr/bin/env python3

from typing import Iterable, Dict
from itertools import groupby


def group_by(iterable: Iterable, key=None) -> Dict:
    groups = {}
    for k, subgroup in groupby(iterable, key=key):
        group = groups.get(k, [])
        group.extend(subgroup)
        groups[k] = group
    return groups
