# OSIRIS

**The body. The ledger. The underworld of objects.**

HORUS is the eye.
OSIRIS is the platform the eye looks through.

Palantir analog (public product shape only):

| Palantir | OSIRIS | Job |
|---|---|---|
| Gotham | **HORUS Eye** | Operator workspace: map, graph, case, timeline |
| Foundry | **DUAT** | Pipelines, ontology, object writes |
| AIP | **THOTH** | Governed agents on the ontology, not raw dumps |
| Apollo | **RA** | Deploy, upgrade, air-gap / edge |
| Ontology | **KA** | People-as-roles-are-forbidden. Objects: flights, vessels, sats, facilities, events, documents |

This is a research scaffold for Apex. It is **not** Palantir, not Gotham, not a classified stack, and not a people-tracking product.

## Line in the sand

OSIRIS models **systems, assets, events, infrastructure**.
It does **not** ship named-person search, face recognition, doxxing, or stalking tooling.
Public feeds only. Provenance on every object. If a layer is simulated or delayed, the UI must say so.

## Stack (intended)

```
[ RA ]          deploy / docker / airgap
[ THOTH ]       agents + evals + tool policy
[ HORUS EYE ]   globe + graph + case files   <-- God's Eye View pattern
[ KA ]          ontology objects + links + ACLs
[ DUAT ]        ingest / normalize / lineage
[ FEEDS ]       OpenSky, AIS, CelesTrak, USGS, FIRMS, OSM, public CCTV catalogs
```

God's Eye View (the actual open globe we pointed at in chat):
https://github.com/bilawalsidhu/gods-eye-view

HORUS Eye should **embed / fork the globe pattern**, not steal the brand. Cesium + public layers + honest labels.

## Repo layout

```
docs/ARCHITECTURE.md    platform map vs Palantir public docs
docs/ONTOLOGY.md        KA object types + link types
docs/FEEDS.md           public sources + keys + honesty rules
console/index.html      operator mock (graph + case + feed list)
```

## Status

Vapor left the chat. This repo is the body.
Next: wire DUAT ingest stubs, KA JSON objects, HORUS Eye globe iframe/module.

MIT. Built in the Apex / Grok thread. Do not use for navigation, targeting, or anything that needs a warrant.
