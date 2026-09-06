# KA — ontology

Palantir's trick is not the map. It is the **object**.
A flight is not a row. It is an object with links: operator, tail, last position, nearby vessels, destination airport, NOTAM, news event.

## Object types (v0)

| Type | Key | Properties (min) | Links |
|---|---|---|---|
| Aircraft | icao24 / hex | callsign, alt, vel, heading, source, freshness | operated_by, departed, arriving, nearby |
| Vessel | mmsi | name, dest, sog, source | flag_state, dest_port, nearby |
| Satellite | norad | class, tle_epoch | overflies |
| Facility | osm_id | kind, lat, lon | hosts_camera, near_event |
| Event | uuid | kind (quake/fire/launch), time, geom | near_facility, near_track |
| Document | hash | title, url, collected_at | mentions_object |
| Case | uuid | title, owner, status | contains |

## Honesty fields (required)

Every object carries:

- `source`
- `collected_at`
- `freshness` (`live` | `delayed` | `simulated` | `reconstructed` | `stale`)
- `confidence` 0-1

If you cannot fill those, it does not enter KA.

## Writes

Operators can attach notes and case membership. They cannot invent positions. Positions come from feeds or are tagged `reconstructed`.
