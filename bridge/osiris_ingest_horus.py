#!/usr/bin/env python3
"""OSIRIS DUAT ingest: Horus meridian_feed/v1 -> KA objects.

Facts only. No trading. No person objects.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_PATHS = [
    os.environ.get("HORUS_FEED_PATH", ""),
    os.environ.get("OSIRIS_FEED_PATH", ""),
    "data/meridian_feed/latest.json",
    "../Horus/data/meridian_feed/latest.json",
    "../Horus-Handoff/Horus/data/meridian_feed/latest.json",
]

OUT = Path(os.environ.get("OSIRIS_KA_PATH", "data/ka/objects.json"))


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_feed() -> dict:
    for p in DEFAULT_PATHS:
        if not p:
            continue
        path = Path(p)
        if not path.is_file():
            continue
        with path.open() as f:
            data = json.load(f)
        if str(data.get("schema", "")).startswith("horus-meridian-feed"):
            data["_loaded_from"] = str(path)
            return data
    return {}


def to_ka(feed: dict) -> dict:
    objects = []
    produced = feed.get("produced_at") or _now()
    for ev in feed.get("events") or []:
        objects.append(
            {
                "type": "Event" if ev.get("title") else "Document",
                "key": ev.get("url") or ev.get("title") or produced,
                "title": ev.get("title"),
                "url": ev.get("url"),
                "theme": ev.get("theme"),
                "source": ev.get("source") or "horus",
                "collected_at": ev.get("seendate") or produced,
                "freshness": "delayed",
                "confidence": min(1.0, float(ev.get("market_score") or 0.5)),
                "properties": {
                    "domain": ev.get("domain"),
                    "market_score": ev.get("market_score"),
                },
            }
        )
    movement = feed.get("movement") or {}
    if movement:
        objects.append(
            {
                "type": "Event",
                "key": "movement:" + produced,
                "title": "public track density",
                "source": "horus-movement",
                "collected_at": produced,
                "freshness": "live",
                "confidence": 0.6,
                "properties": {
                    "aircraft_visible": movement.get("aircraft_visible", 0),
                    "vessels_visible": movement.get("vessels_visible", 0),
                },
            }
        )
    for alert in feed.get("alerts") or []:
        if isinstance(alert, dict):
            objects.append(
                {
                    "type": "Event",
                    "key": str(alert.get("id") or alert.get("title") or alert)[:180],
                    "title": alert.get("title") or alert.get("message") or "alert",
                    "source": alert.get("source") or "horus-alert",
                    "collected_at": produced,
                    "freshness": "live",
                    "confidence": 0.7,
                    "properties": alert,
                }
            )
    return {
        "schema": "osiris-ka/v0",
        "ingested_at": _now(),
        "producer": "osiris_ingest_horus",
        "horus_schema": feed.get("schema"),
        "horus_produced_at": feed.get("produced_at"),
        "loaded_from": feed.get("_loaded_from"),
        "object_count": len(objects),
        "objects": objects[:200],
        "disclaimer": "Facts from Horus public-event feed only. No orders. No person objects.",
    }


def main() -> int:
    feed = load_feed()
    if not feed:
        ka = {
            "schema": "osiris-ka/v0",
            "ingested_at": _now(),
            "object_count": 0,
            "objects": [],
            "ok": False,
            "note": "Horus feed not present",
        }
    else:
        ka = to_ka(feed)
        ka["ok"] = True
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(ka, indent=2))
    print(f"wrote {OUT} objects={ka.get('object_count', 0)} ok={ka.get('ok')}")
    return 0 if ka.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
