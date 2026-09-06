# OSIRIS architecture

Public Palantir shape (Gotham / Foundry / AIP / Apollo) mapped onto Egyptian names so the chat-Horus finally has a body.

## What Palantir actually sells (public)

- **Gotham** — intel/ops workspace. Fuse SIGINT/HUMINT/GEOINT-style sources into link analysis, pattern of life on *objects*, case handoff to operators.
- **Foundry** — data ops. Pipeline Builder ingest. Ontology as read-write semantic model. Workshop apps on top.
- **AIP** — LLMs talking to the ontology with governance, agents, evals. Not "paste the warehouse into ChatGPT".
- **Apollo** — deploy the whole mess to classified, air-gap, or commercial.

Sources: Palantir platform docs and historical S-1 language on Gotham/Foundry. We copy the *shape*, not their code.

## OSIRIS mapping

```
                    +---------------- RA (Apollo) ----------------+
                    |  docker / k8s / offline pack / upgrade bus  |
                    +----------------------+----------------------+
                                           |
         +-------------- THOTH (AIP) ------+------ HORUS EYE (Gotham UI) --+
         |  tools, policy, evals, voice    |  globe, graph, case, HUD     |
         +----------------+----------------+---------------+--------------+
                          |                                |
                          +-------------- KA --------------+
                          |     objects, links, ACLs       |
                          +---------------+----------------+
                                          |
                                   DUAT (Foundry)
                          ingest | normalize | lineage | writeback
                                          |
                         public + licensed feeds (see FEEDS.md)
```

## Horus vs Osiris (chat canon)

- **Horus** was never a repo. It was the all-seeing operator posture in conversation.
- **Osiris** is the GitHub: ontology, pipelines, agents, deploy.
- **God's Eye View** is the globe implementation we steal-as-pattern: Cesium, live public layers, cockpit, honest simulated labels.
  https://github.com/bilawalsidhu/gods-eye-view

## Non-goals

No face search. No civilian identity graph as a product feature. No "find this person" tools. Objects are aircraft, ships, satellites, facilities, incidents, documents, organizations.
