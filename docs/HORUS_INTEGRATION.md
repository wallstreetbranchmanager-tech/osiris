# Horus zip → OSIRIS

The complete package is `HORUS-Intel-OSINT-Complete.zip` (Horus-Handoff, 11 Aug 2026).
It is not this git history. This repo is the Palantir-shaped body that zip never had.

## Contract

Horus rule: **Horus watches. Meridian bets.**
OSIRIS rule: **Horus writes objects. OSIRIS stores objects. Meridian still bets.**

Feed Horus already emits:

- path: `data/meridian_feed/latest.json`
- schema: `horus-meridian-feed/v1`
- fields used: `events[]`, `alerts[]`, `cross_signals[]`, `movement`, `summary`, `produced_at`
- never: buy/sell, size, tickets

## Map zip files → OSIRIS layers

| Zip path | OSIRIS |
|---|---|
| `Horus/horus_meridian_feed.py` | DUAT publisher |
| `Horus/Horus_eagle_core.py` | DUAT collector |
| `Horus/Horus_aircraft_density.py` | Aircraft objects |
| `Horus-voice/Horus-globe.html` | HORUS Eye (interim globe) |
| `bridge/horus_intel_brain.py` | Meridian context only |
| `osiris/bridge/osiris_ingest_horus.py` | DUAT → KA |
| `osiris/bridge/horus_publish_ka.py` | drop into Horus tree |

Not imported here: `Horus_alpr.py`, `Horus_people_osint.py`, operator locate tooling.

## Run

From a machine that has the zip extracted and has produced a feed:

```bash
export HORUS_FEED_PATH=/path/to/Horus/data/meridian_feed/latest.json
python bridge/osiris_ingest_horus.py
# writes data/ka/objects.json
```

Or from inside the Horus folder after Eagle publish:

```python
import horus_publish_ka
horus_publish_ka.publish_ka()
```
