# Scenario — [Game Title TBD]

> Working document. Story is not finalized.
> Last updated: 2026-05-02

---

## Story Overview

A legal immigrant's journey — from a hopeful walk to a visa interview in their home country, to a life built abroad, to the moment everything is threatened by a government raid.

---

## Act 1 — Beginning (Home Country)

**Scenes:**
- Player walks down the street in their home country on the way to a visa interview
- The interview takes place — tension, hope, paperwork
- Visa approved — paperwork in hand

**Tone:** Hopeful, nervous, determined

**Status:** Not yet implemented in script.rpy

---

## Act 2 — Middle (New Country)

**Scenes:**
- Time passes — player builds a life (job, friends, family)
- Normal daily life, a sense of belonging
- Political shift — a new leader takes power (authoritarian, hostile to immigrants)
- News and warnings begin: raids targeting immigrants, even legal ones
- Anxiety and tension build in the player's community

**Tone:** Warm → Uneasy → Fearful

**Status:** Partially implemented — `scene_timeskip` covers the time jump but lacks the political buildup and tension arc

---

## Act 3 — Climax (The Raid)

**Scenes:**
- ICE agents arrive at the player's door
- Choices about how to respond (open door, peek, ignore)
- Confrontation with agents — documents, rights, lawyer
- Neighbors witness the scene

**Tone:** Terrifying, disempowering, urgent

**Status:** Implemented — `scene_door`, `scene_agent`, `scene_question`, `scene_final`

---

## Act 4 — Ending

**Two endings based on Suspicion meter (0–100):**

| Ending | Condition | Description |
|--------|-----------|-------------|
| Arrested | suspicion >= 100 | Player is handcuffed. Documents ignored. 10 years gone. |
| Survived | suspicion < 100 | Agents back down. Neighbors watching. Player closes the door, hands shaking. |

**Status:** Implemented — `ending_arrested`, `ending_escaped`

---

## What Needs to Be Written

- [ ] Act 1 full dialogue — home country, visa interview scene
- [ ] Act 2 full dialogue — daily life montage, political shift, news/warnings
- [ ] Expand Act 3 to better convey fear and disorientation
- [ ] Confirm all suspicion deltas
- [ ] Finalize game title
- [ ] Epilogue text for both endings (stat screen / closing message)
