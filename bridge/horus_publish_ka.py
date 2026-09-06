"""Drop this next to horus_meridian_feed.py inside the Horus zip tree.

After Eagle writes data/meridian_feed/latest.json, call publish_ka().
Writes data/ka/objects.json in OSIRIS KA shape.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

try:
    import Horus_config as config
    DATA_DIR = getattr(config, "DATA_DIR", "data")
except Exception:
    DATA_DIR = "data"

FEED = Path(DATA_DIR) / "meridian_feed" / "latest.json"
OUT = Path(DATA_DIR) / "ka" / "objects.json"


def publish_ka(feed_path: str | os.PathLike | None = None) -> dict:
    src = Path(feed_path) if feed_path else FEED
    if not src.is_file():
        payload = {
            "schema": "osiris-ka/v0",
            "ok": False,
            "note": "no meridian feed yet",
            "ingested_at": datetime.now(timezone.utc).isoformat(),
            "objects": [],
        }
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(payload, indent=2))
        return payload

    feed = json.loads(src.read_text())
    objects = []
    produced = feed.get("produced_at")
    for ev in feed.get("events") or []:
        objects.append(
            {
                "type": "Event",
                "key": ev.get("url") or ev.get("title"),
                "title": ev.get("title"),
                "source": ev.get("source") or "horus",
                "collected_at": ev.get("seendate") or produced,
                "freshness": "delayed",
                "properties": ev,
            }
        )
    movement = feed.get("movement") or {}
    objects.append(
        {
            "type": "Event",
            "key": "movement",
            "title": "public track density",
            "source": "horus-movement",
            "collected_at": produced,
            "freshness": "live",
            "properties": movement,
        }
    )
    payload = {
        "schema": "osiris-ka/v0",
        "ok": True,
        "ingested_at": datetime.now(timezone.utc).isoformat(),
        "horus_schema": feed.get("schema"),
        "object_count": len(objects),
        "objects": objects[:200],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2))
    return payload


if __name__ == "__main__":
    print(json.dumps(publish_ka(), indent=2)[:500])
