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

[Pitch black bedroom. POUNDING on the door. Player jolts awake.]

**Voice (outside):** "OPEN UP. FEDERAL AGENTS."

**Player:** [whispered] "Oh god. Oh god oh god oh god."

[More pounding. The door shakes in its frame.]

**Voice:** "WE HAVE A WARRANT. OPEN THE DOOR NOW."

> **Choice — branches permanently (paths do not reconverge):**

**S09A** — Grab phone and call Lisa. `[+0]` → S10A

**S09B** — Get documents from the bag first. `[+0]`
> *Note: BLOCKED if player did not choose S06A — option is greyed out / unavailable.*

**S09C** — Open the door — show them you have nothing to hide. `[+5]`
> *Note: Immediately leads to arrest sequence regardless of suspicion gauge.*

---

## Act 3 — The Raid

---

### Path A — Lisa on the Line

---

#### S10A — The Call

**Location:** Player's bedroom.
**Characters:** Player, Lisa (phone)

---

[You pick up your phone and dial the first number that comes to mind.]

**Lisa:** [groggy] "...what time is it—"

**Player:** "They're here. They're at my door."

**Lisa:** [instantly awake] "Documents. Do you have them?"

**Player:** "Yes. Yes I have them."

**Lisa:** "Don't open the door without seeing the warrant. Make them slide it under. I'm staying on the line."

**→ S11A**

---

#### S11A — Last Warning

**Location:** Player's front door.
**Characters:** Player, Voice outside

---

**Voice:** "LAST WARNING. WE WILL BREAK THE DOOR."

**→ S12A**

---

#### S12A — Demand the Warrant

**Location:** Player's front door.
**Characters:** Player

---

**Player:** "I need to see the warrant first. Slide it under the door, please." `[-1, capped at 0]`
> *Note: If player attended workshop (chose S07A), this option is **bolded** and shows: "You remember the workshop. You know your rights."*

**→ S13A**

---

#### S13A — Check Suspicion Gauge

> **Suspicion ≤ 5** → Ending A 🟢
> **Suspicion > 5** → Ending B 🔴

---

#### Ending A — Lisa on phone · documents prepared · low suspicion 🟢

**Voice (outside):** "Slide it under? Fine."

[Folded paper slides under the door. You pick it up, hands shaking. Phone wedged at shoulder.]

**Player:** [whispered] "Okay. It's here."

**Lisa:** "Read it. Slowly. Tell me what it says."

**Player:** "Hopeford District Court. Case number. There's a signature — 'Magistrate Judge.' My name. My address."

**Lisa:** [exhales] "Okay. That's a real one. They have legal authority. You open the door, hands visible, no sudden moves. Give them the documents. Stay calm. The second they let you, you call me back."

**Player:** "Lisa I—"

**Lisa:** "I know. You've done everything right so far. Keep doing it."

[You set the phone on the entry table, still on speaker. Hand on the deadbolt. Click. The door opens.]

**Agent 1:** "Step back. Hands where I can see them."

**Player:** "I have my documents. Reaching slowly."

[You hand over the folder. An agent flips through. Another scans the apartment.]

**Agent 1:** "Visa. Employment authorization. Lease." [pause] "All in order."

**Agent 2:** "On paper."

**Agent 1:** "Where do you work?"

**Player:** "I'd like to speak with a lawyer before answering any more questions."

[A long, evaluating beat.]

**Agent 1:** [finally] "Smart. Documents check out. We're done here."

**Agent 2:** "You sure? We could—"

**Agent 1:** "I said we're done."

[Door clicks shut. Player slides the deadbolt. Slides down to the floor.]

**Lisa (phone):** "Are they gone?"

**Player:** [whisper] "They're gone."

**Lisa:** "Oh thank goodness. Thank goodness."

**Player:** "I heard them. Down the hall. The neighbors. There was a kid—"

**Lisa:** "I know. You're safe."

**Player:** "Am I?"

[You did everything right. This time.]

---

#### Ending B — Lisa on phone · documents prepared · high suspicion 🔴

**Voice (outside):** "Slide it under? Fine."

[Folded paper slides under the door. You pick it up, hands shaking. Phone wedged at shoulder.]

**Player:** [whispered] "Okay. It's here."

**Lisa:** "Read it. Slowly. Tell me what it says."

**Player:** "Hopeford District Court. Case number. There's a signature — 'Magistrate Judge.' My name. My address."

**Lisa:** [exhales] "Okay. That's a real one. They have legal authority. You open the door, hands visible, no sudden moves. Give them the documents. Stay calm. The second they let you, you call me back."

**Player:** "Lisa I—"

**Lisa:** "I know. You've done everything right so far. Keep doing it."

[You set the phone on the entry table, still on speaker. Hand on the deadbolt. Click. The door opens.]

**Agent 1:** "Step back. Hands visible."

**Player:** "I have documents — they're right here, I have a Visa, I work at Hopeford, I—"

**Agent 1:** "Slow down. Hands on the table. Folder over here."

[You put the folder down too quickly. It slides. Papers fan out. Player reaches to gather them—]

**Agent 2:** "Don't touch anything. Step back."

**Player:** "Sorry — sorry, I just—"

**Agent 1:** "Where do you work?"

**Player:** "Hopeford Technologies. Software engineer. Five years."

**Agent 1:** "Anyone else live here?"

**Player:** "No, just me. A coworker comes over sometimes — Marcus — but he doesn't live here, he—"

**Agent 1:** "Marcus has a last name?"

**Player:** "Martinez. Or Martins, I — it's late, I'm sorry—"

**Agent 2:** "You don't know your coworker's last name."

**Player:** "I do, I just—"

**Agent 1:** "This entry stamp. When did you last leave the country?"

**Player:** "I haven't — I mean, there was a layover, last spring, to see my mom — but I came right back, it's all in the file—"

**Agent 2:** "You didn't disclose that."

**Player:** "I'm disclosing it now—"

**Agent 1:** "You're going to come with us. Sort this out at the facility."

**Player:** "What — no, my papers are right there, you looked at them—"

**Agent 1:** "Turn around. Hands behind your back."

**Lisa (phone):** "Wait — what's happening? Hello?? Please—"

[An agent walks to the table. Picks up the phone. Looks at Lisa's contact photo. Ends the call.]

**Agent 2:** "You won't be needing this."

[Cuffs click. You are led out. Past the documents fanned across the table — open, useless, left behind. Past the balcony.]

[In the hallway, the neighbors. A woman crying. A child asking where mama is going. You try to catch the woman's eye. She looks away.]

[In the van. No windows. You try to remember Lisa's number. Try to remember the lawyer's name you were supposed to memorize. Try to remember why you ever thought paper could protect you.]

[You did everything right. It wasn't enough.]

---

### Path B — Alone

---

#### S10B — Last Warning

**Location:** Player's front door.
**Characters:** Player, Voice outside

---

**Voice:** "LAST WARNING. WE WILL BREAK THE DOOR."

**→ S11B**

---

#### S11B — Panic

**Location:** Player's front door.
**Characters:** Player

---

**Player:** "O-okay! I'm opening it! Please don't break it down!" `[+2]`

**→ S12B**

---

#### S12B — The Door Opens

**Location:** Player's bedroom → front door.
**Characters:** Player, Agent 1, Agent 2

---

**Player:** [to yourself] "Okay okay okay—"

[You scramble for the bag. Knock something off the dresser. Find the documents — half of them. Where's the lease? Where's the—]

**Voice:** "ON THREE. ONE—"

**Player:** "I'M COMING — I'M COMING, PLEASE—"

[You run to the door. Don't ask for a warrant. Don't check anything. Just turn the lock and pull it open.]

**Agent 1:** "Down on the ground. NOW."

**Player:** "I have papers — I have papers—"

**→ S13B**

---

#### S13B — Check Suspicion Gauge

> **Suspicion ≤ 5** → Ending C 🟢
> **Suspicion > 5** → Ending D 🔴

---

#### Ending C — no Lisa · documents prepared · low suspicion 🟢

[An agent takes the folder. Flips through methodically. Another walks the apartment perimeter. You keep your hands at your sides. You don't speak.]

**Agent 1:** "Visa. Authorization. Lease." [looks up] "Where do you work?"

**Player:** "I'd like to speak with a lawyer before answering questions."

[The agent holds the look. You hold it back. Don't fill the silence. Don't apologize. Don't explain.]

**Agent 1:** [hands back the folder] "Have a good night."

**Agent 2:** "That's it?"

**Agent 1:** "That's it."

[They leave. You close the door. Lock it. Stand there for a long time.]

[You walk to the phone. Pick it up. Stare at Lisa's name. Don't call. Not yet.]

[Instead you sit on the edge of the bed. Hands flat on your knees. Listening to the building — the shouting down the hall, the engines outside, the morning that hasn't come yet.]

[You survived alone. You don't know if that's a relief or the loneliest thing you've ever felt.]

[You did everything right. This time.]

---

#### Ending D — no Lisa · documents prepared · high suspicion 🔴

**Agent 1:** "GROUND. NOW."

[You're forced to your knees. Half the papers are on the floor where they fell.]

**Agent 2:** [walking past Player into the apartment] "Clear the back."

**Player:** "Wait — please — they're in the bedroom, my Visa is in the bedroom—"

**Agent 1:** "Don't move."

[The agent returns from the bedroom holding the folder. Hands it to his partner. He doesn't even open it.]

**Agent 1:** "Up. Hands behind your back."

**Player:** "But you didn't even — you didn't look at them—"

**Agent 1:** "You can present them at the facility."

**Player:** "Which facility? Where are you taking me? I have work — I have to call someone — I haven't called anyone—"

**Agent 1:** "Walk."

[Cuffs. Cold. Final.]

[As you're led out, you pass the kitchen. Phone on the counter, dark. Lisa's name not on the screen. Nobody knows. Nobody knows yet. Past the balcony — the one you cried about to your mom. Past the fridge with the photos. Past Marcus's empty apartment two doors down. He saw this coming. He told you.]

[In the van, you try to think of who will notice you're gone. Your team won't realize until Monday morning. Your landlord, maybe never. Your mother — when she calls Sunday and no one picks up.]

[You mouth Lisa's number to yourself, over and over. You think you remember it. You're not sure.]

[You did everything right. It wasn't enough. And no one knew to look for you.]

---

### Path C — Opened the Door

---

#### S10C — Ending E (opened door immediately) 🔴

> *Note: Triggered regardless of suspicion gauge — choosing S09C bypasses all gauge checks.*

[The pounding has barely registered. You, half-asleep, fumble to the door. Not thinking. Not grabbing your phone. Not asking for a warrant. Just turn the deadbolt because someone is at the door and someone at the door means open it.]

[The door swings open. Three agents flood in before you can even step back.]

**Agent 1:** "ON THE GROUND."

**Player:** "Wait — what — I—"

**Agent 1:** "GROUND."

[Before you can process what is happening, you're on the ground. Knee in your back. Hands wrenched behind. The apartment fills with flashlight beams, voices, radios.]

**Agent 2:** "Clear left."

**Agent 3:** "Clear right."

**Player:** "I have a Visa — I have papers — please, they're in the bedroom, please let me—"

**Agent 1:** "Quiet."

**Player:** "I'm legal — I'm legal — I work at Hopeford, I have an employer, please—"

**Agent 1:** "You opened the door. We didn't force entry. You consented. Anything in this apartment is fair search now."

**Player:** "I didn't — I didn't consent, I just — I just opened the door—"

**Agent 1:** "Same thing."

[An agent emerges from the bedroom with the document folder but doesn't hand it to anyone. Just sets it on the counter.]

**Player:** "My papers — they're right there—"

**Agent 1:** "Up."

[You are hauled to your feet. Cuffed. Walked toward the door.]

**Player:** "Please — please can I get my phone — please can I call someone — please—"

**Agent 1:** "Walk."

[As you cross the threshold, you turn your head — try to see the apartment one more time. The balcony. The fridge with the photos. The folder on the counter, untouched, irrelevant. The phone on the nightstand. Lisa's number locked inside it.]

[In the hallway, an agent is already photographing your open door. Evidence of consent.]

[In the van, no windows. You can't stop replaying it. The pounding. The door. How easy it was. How you handed it all over without a single question. How nothing — not the Visa, not the job, not the years of paperwork — mattered the second you turned that deadbolt.]

[You think about Marcus. "Don't open the door. Not even a crack. Promise me." You had promised.]

[The door was the only protection you had. You opened it.]

---

## Act 4 — Endings

| Ending | Path | Condition | Result |
|--------|------|-----------|--------|
| A | Path A (Lisa) | suspicion ≤ 5 | Escaped 🟢 |
| B | Path A (Lisa) | suspicion > 5 | Arrested 🔴 |
| C | Path B (Alone) | suspicion ≤ 5 | Escaped 🟢 |
| D | Path B (Alone) | suspicion > 5 | Arrested 🔴 |
| E | Path C (Open door) | gauge bypassed | Arrested 🔴 |
