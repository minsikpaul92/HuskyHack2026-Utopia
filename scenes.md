# Scenes — [Game Title TBD]

> Detailed scene-by-scene dialogue and branching.
> Last updated: 2026-05-02
>
> Format guide:
> - `[action]` = narration / stage direction
> - `Choice A/B/C` = player choice (note suspicion delta)
> - `→` = leads to next scene ID
> - `+N / -N` = suspicion change
>
> Naming convention: `S01`, `S02A`, `S02B`, `S03` ...
> - Image files: TBD
> - Ren'Py labels: `label s01`, `label s02a`

---

## Act 1 — Home Country

---

### S01 — The Street

**Location:** Busy street, home country. Bright morning.
**Image:** TBD
**Characters:** Player, Lisa (phone)

---

[Bright morning. You walk down a busy street in your home country. Phone to ear.]

**Player:** "Yeah this is more nerve-wracking than it should honestly. I really hope I get that Visa. Hopeford is like, my only hope of making it in the Tech world right now."

**Lisa:** "Bestie relaaaax you're gonna do fine. No one is as hard working as you. Like literally no one."

**Player:** "I know, I know. I just keep thinking about all the ways it could go wrong."

**Lisa:** "What if you stop spiraling and breathe? You got the job offer. This is just a formality. When you get it, first round of drinks at that rooftop place is on you."

**Player:** "When, huh?"

**Lisa:** "WHEN. Manifest it bestie."

[You approach the embassy gates.]

**Player:** "Okay I gotta go. Wish me luck."

**Lisa:** "Don't need it. Go get it!"

**→ S02**

---

### S02 — The Interview

**Location:** Embassy office.
**Image:** TBD
**Characters:** Player, Officer

---

[Scene change to office.]

**Officer:** "Job offer from Hopeford Technologies. Software engineer. Salary looks competitive."

**Player:** "Yes sir."

**Officer:** "Why Hopeford?"

> **Choice — same image, converges to S03:**

**S02A** — "It's the best opportunity in my field. I've worked toward this for years." `[+0]` → S03

**S02B** — "Honestly? It's my only real shot. There's nothing like this back home." `[+0]` → S03

---

### S03 — Approved

**Location:** Embassy office (continued).
**Image:** TBD
**Characters:** Player, Officer

---

**Officer:** [stamps paperwork] "Welcome to Hopeford."

[You exhale and smile for the first time all day.]

**→ S04**

---

## Act 2 — Life in Hopeford

---

### S04 — Settled In

**Location:** Player's apartment. 6 months after arrival.
**Image:** TBD
**Characters:** Player, Marcus, Lisa (video call)

---

[6 months later, you are lounging in your modest apartment. Marcus, a coworker from Hopeford, is over with takeout.]

**Marcus:** "So how you liking it? Real talk."

**Player:** "Honestly? Better than I thought. The work's hard but the team's good. And I actually have a balcony, Marcus. A balcony."

**Marcus:** "Look at you. Living the dream."

**Player:** "I called my mom yesterday and she cried. In a good way. I think."

**Marcus:** "That's beautiful man. You earned this."

[Player's phone buzzes — Lisa, video calling.]

**Lisa:** "BESTIEEE show me the apartment again I need to live vicariously."

> **Choice — converges to S05:**

**S04A** — "Let me give you the full tour! Balcony view and everything." — posts a story tagged with location `[+1]`
> *Note: geotagged post — will matter later (TBD)*

**S04B** — "I'll send pics later, promise. Tell me about your week first." `[+0]` → S05

**→ S05**

---

### S05 — First Indications

**Location:** Office break room. 5 years after arrival.
**Image:** TBD
**Characters:** Player, Marcus

---

[5 years later, you are sitting in the office break room. A TV plays in the background. Marcus stares at it. The country's new leader at a podium, gesturing forcefully.]

**News Anchor:** "...sweeping new immigration enforcement measures effective immediately. The administration says—"

**Marcus:** "You hearing this?"

**Player:** "Yeah. I mean — it's a lot of talk, right? Politicians say stuff."

**Marcus:** "This one's different. My uncle's been here thirty years. Thirty. He's scared, man."

**Player:** "But we're legal. We have papers."

**Marcus:** "Yeah. So does my uncle."

[Awkward silence. The TV drones on.]

> **Choice — converges to S06:**

**S05A** — "You think I should be worried?" `[+0]` → S06

**S05B** — "They can't just go after people with valid Visas. That's not how it works." `[+2]`
> *Note: reveals dangerous naivety — player will be less prepared*

**S05C** — "What are you doing? Like, to prepare?" `[-1, capped at 0]`
> *Note: shows player is starting to take it seriously*

**→ S06**

---

### S06 — Lisa Calls

**Location:** Player's apartment living room. Late evening.
**Image:** TBD
**Characters:** Player, Lisa (video call)

---

[You sit in your apartment living room. Late evening. News of disappearances and civil unrest has been circulating the news and all social platforms. Lisa is on video call from back home.]

**Lisa:** "[player_name] I'm just gonna say it. Come home."

**Player:** "Lisa—"

**Lisa:** "I've been reading the news. Like all of it. It's bad. It's really bad."

**Player:** "I have a job here. A career. I can't just—"

**Lisa:** "I know. I know what you've built. I'm not saying forever. I'm saying — until things calm down."

**Player:** "And if they don't calm down?"

**Lisa:** [long pause] "Then at least you'd be safe."

[You walk to the window, looking out at the city — your city, now — reminiscing the feeling of hope you felt when you first set foot on this land. Now...]

> **Choice — converges to S07:**

**S06A** — "I hear you. I'm gonna keep my documents on me from now on. Just in case." `[+0]` → S07

**S06B** — "You're being dramatic. The news exaggerates everything." `[+2]` → S07

**S06C** — "...maybe you're right. Let me think about it." `[+0]` → S07

---

### S07 — Know Your Rights

**Location:** Player's apartment. Later that night.
**Image:** TBD
**Characters:** Player (solo)

---

[A few hours after the phone call. You are scrolling your phone in bed and see a post from a neighbor's community group: "Know Your Rights" workshop tomorrow at the community center.]

> **Choice — converges to S08:**

**S07A** — "I'll go. Can't hurt to know." `[-1, capped at 0]`
> *Note: UNLOCKS warrant knowledge — affects climax flavor text but not suspicion gauge (TBD)*

**S07B** — "I'm too tired. I'll catch the next one." `[+1]` → S08

**→ S08**

---

### S08 — Marcus Leaves

**Location:** Office.
**Image:** TBD
**Characters:** Player, Marcus

---

[You enter the office, getting ready for another day's work. You notice Marcus is packing up his desk.]

**Player:** "Wait — what's happening? Why are you packing?"

**Marcus:** "Going to stay with family. Out of state. For a while."

**Player:** "Marcus, you're scaring me."

**Marcus:** "Three buildings on the east side last night. They're not even pretending to check status anymore. They take you, then you prove it. From inside."

**Player:** "Inside where?"

**Marcus:** "One of those facilities. Hours away. No phone. They cuffed a guy with full residency, man. Full. Residency."

[Marcus zips his bag, stops, and looks at you.]

**Marcus:** "Listen. If they come — don't open the door. Make them show the warrant. Read it. A real one has your name on it and a judge's signature. Not just a department stamp. If a judge didn't sign it, they cannot legally come in."

**Player:** "...okay."

**Marcus:** "Promise me."

**Player:** "I promise."

[Marcus leaves. The office feels emptier than it should.]

**→ S09**

---

### S09 — The Knock

**Location:** Player's bedroom. Night.
**Image:** TBD
**Characters:** Player, Voice outside

---

[Pitch black bedroom. Pounding on the door. Player jolts awake.]

**Voice (outside):** "OPEN UP. FEDERAL AGENTS."

**Player:** [whispered] "Oh god. Oh god oh god oh god."

[More pounding. The door shakes in its frame.]

**Voice:** "WE HAVE A WARRANT. OPEN THE DOOR NOW."

**→ S_DOOR (The Raid — see script.rpy: scene_door)**

---

## Act 3 — The Raid

| Scene ID | Ren'Py label | Status |
|----------|--------------|--------|
| S_DOOR | scene_door | Implemented |
| S_AGENT | scene_agent | Implemented |
| S_QUESTION | scene_question | Implemented |
| S_FINAL | scene_final | Implemented |

---

## Act 4 — Endings

| Scene ID | Ren'Py label | Condition | Status |
|----------|--------------|-----------|--------|
| S_END_A | ending_arrested | suspicion >= 100 | Implemented |
| S_END_B | ending_escaped | suspicion < 100 | Implemented |
