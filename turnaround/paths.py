"""Cache locations that work both locally and on a read-only serverless host.

Repo caches (turnaround/cache/<name>) are read first. Writes go to the repo
cache when it is writable, otherwise to a temp directory (e.g. /tmp on
Vercel), which is fine because that data is disposable.
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_CACHE = HERE / "cache"
ON_VERCEL = bool(os.environ.get("VERCEL"))


def _writable(p: Path) -> bool:
    try:
        p.mkdir(parents=True, exist_ok=True)
        probe = p / ".write_test"
        probe.write_text("x")
        probe.unlink()
        return True
    except OSError:
        return False


def cache_dirs(name: str) -> tuple[Path, Path]:
    """(read_dir, write_dir) for a cache called `name`."""
    repo = REPO_CACHE / name
    if _writable(repo):
        return repo, repo
    tmp = Path(tempfile.gettempdir()) / "turnaround" / name
    tmp.mkdir(parents=True, exist_ok=True)
    return repo, tmp


def find(name: str, filename: str) -> Path | None:
    """First existing copy of a cached file (repo first, then temp)."""
    read_dir, write_dir = cache_dirs(name)
    for d in (read_dir, write_dir):
        p = d / filename
        if p.exists():
            return p
    return None


def is_fresh(name: str, p: Path | None, max_age_days: float) -> bool:
    """A cached file is fresh if it is young enough, or if it lives in a
    read-only repo cache (a deployed bundle: timestamps are meaningless there
    and the committed snapshot is the intended data)."""
    import time
    if p is None or not p.exists():
        return False
    read_dir, write_dir = cache_dirs(name)
    if read_dir != write_dir and p.parent == read_dir:
        return True
    return (time.time() - p.stat().st_mtime) < max_age_days * 86400
