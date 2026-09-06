# OSIRIS

**The body. The ledger. The underworld of objects.**

HORUS is the eye (the Aug 2026 Intel/OSINT handoff zip).
OSIRIS is the platform the eye writes into.

## Live wiring (this commit)

Horus already publishes `data/meridian_feed/latest.json` (`schema: horus-meridian-feed/v1`).
That feed is **facts only**. No buy/sell.

OSIRIS now consumes it:

```
Horus Eagle cycle
    → data/meridian_feed/latest.json
        → osiris/bridge/osiris_ingest_horus.py
            → data/ka/objects.json   (Event + Document + movement counts)
                → console/index.html  (operator mock)
                → Meridian brains stay untouched (still optional)
```

Drop-in for the zip tree:

- copy `bridge/horus_publish_ka.py` next to `horus_meridian_feed.py`
- after each Eagle publish, call `publish_ka()`
- OSIRIS reads KA objects, not raw people modules

People / ALPR / locate modules from the zip stay **out of this repo**. Public events, aircraft counts, vessels, docs only.

## Palantir shape

| Palantir | OSIRIS | Horus zip |
|---|---|---|
| Gotham | HORUS Eye | `Horus-voice/Horus-globe.html` + World Monitor |
| Foundry | DUAT | Eagle cycle + `horus_meridian_feed.py` |
| Ontology | KA | `bridge/osiris_ingest_horus.py` |
| AIP | THOTH | agent on KA objects |
| Apollo | RA | handoff PDFs / later docker |

God's Eye View globe pattern: https://github.com/bilawalsidhu/gods-eye-view

## Line

Systems, assets, events, infrastructure. No named-person product surface here.
MIT. Apex / Grok thread.
