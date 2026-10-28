"""Collects every practice paper into a single PAPERS dict, keyed by slug."""
import importlib
import os
import pkgutil

PAPERS = {}

_here = os.path.dirname(os.path.abspath(__file__))
for _mod in sorted(m.name for m in pkgutil.iter_modules([_here])):
    _m = importlib.import_module(f"content.{_mod}")
    if hasattr(_m, "PAPER"):
        PAPERS[_m.PAPER["slug"]] = _m.PAPER
    for _p in getattr(_m, "PAPERS", []):
        PAPERS[_p["slug"]] = _p
