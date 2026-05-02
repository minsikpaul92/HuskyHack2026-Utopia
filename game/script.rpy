# ── Characters & Variables ────────────────────────
default player_name = ""
default player_pronoun = "she"
default player_pronoun_cap = "She"
default player_possessive = "her"
default suspicion = 0
default s06_documents_ready = False
default s07_workshop = False

define player = Character("[player_name]", color="#44aaff")
define officer = Character("Officer", color="#aaaaaa")
define agent = Character("Agent 1", color="#ff4444")
define agent2 = Character("Agent 2", color="#dd2222")
define agent3 = Character("Agent 3", color="#bb1111")
define lisa = Character("Lisa", color="#ff88cc")
define marcus = Character("Marcus", color="#88ff88")

# ── Image Definitions ────────────────────────────
image bg_s01          = "images/S01_bg.png"
image bg_s01_phone    = "images/S01_phone.png"
image bg_s01_paperwork= "images/S01_paperwork.png"
image bg_s02          = "images/S02_bg.png"
image bg_s03          = "images/S03_bg.png"
image bg_s04          = "images/S04_bg.png"
image bg_s04_phone    = "images/S04_phone.png"
image bg_s05          = "images/S05_bg.png"
image bg_s06          = "images/S06_bg.png"
image bg_s06_phone    = "images/S06_phone.png"
image bg_s07          = "images/S07_bg.png"
image bg_s07_phone    = "images/S07_phone.png"
image bg_s08          = "images/S08_bg.png"
image bg_s08_empty    = "images/S08_emptyOffice.png"
image bg_airplane     = "images/airplane.png"
image bg_airport      = "images/airport.png"
image bg_s09a_phone   = "images/S09A_PHONE.png"
image bg_s09_slamming = "images/S09_slamming.png"
image bg_s09_door     = "images/S09_door.png"
image bg_s12a_paper   = "images/S12A_paper.png"
image bg_s12b_serious = "images/S12B_serious_police.png"
image bg_s09          = "images/S09_bg.png"
image bg_s14a_police  = "images/S14A_police.png"
image bg_s14b_docs    = "images/S14B_police_documents.png"
image bg_black        = Solid("#000000")
image bg_title        = "images/title.png"
image bg_disclaimer   = "images/disclaimer.png"

# ── Screens ──────────────────────────────────────

screen suspicion_bar():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 60
        vbox:
            text "Suspicion" size 20 color "#ffffff"
            bar value suspicion range 10 xsize 200 ysize 20 left_bar "#ff4444" right_bar "#333333"

screen quit_button():
    frame:
        xalign 0.0
        yalign 0.0
        xoffset 20
        yoffset 20
        background "#00000088"
        padding (10, 5)
        textbutton "Exit Game" action Quit(confirm=True)

screen game_over_screen():
    modal True
    add Solid("#000000cc")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        text "ARRESTED" size 80 color "#ff4444"
        text "10 years. Gone in minutes." size 30 color "#ffffff"
        hbox:
            xalign 0.5
            spacing 40
            textbutton "Try Again" action Start() text_size 40 text_hover_color "#ff4444"
            textbutton "Quit to Menu" action MainMenu() text_size 40 text_hover_color "#ff4444"

# ── Start ─────────────────────────────────────────
label start:
    scene bg_title
    pause

    scene bg_disclaimer
    pause

    scene bg_black
    show screen quit_button
    $ player_name = renpy.input("What is your name?", length=20)
    $ player_name = player_name.strip() or "Maria"

    menu:
        "Select your pronouns:"
        "She / Her":
            $ player_pronoun = "she"
            $ player_pronoun_cap = "She"
            $ player_possessive = "her"
        "He / Him":
            $ player_pronoun = "he"
            $ player_pronoun_cap = "He"
            $ player_possessive = "his"
        "They / Them":
            $ player_pronoun = "they"
            $ player_pronoun_cap = "They"
            $ player_possessive = "their"

    jump s01

# ══════════════════════════════════════════════
# SCENE: S01 — The Street
# ACT:   Act 1 — Home Country
# CHARS: Player, Lisa (phone)
# ══════════════════════════════════════════════
label s01:
    scene bg_s01
    play music "audio/S01-city-street.mp3"

    "[[Bright morning. You walk down a busy street in your home country. Phone to ear.]"

    scene bg_s01_phone

    player "Yeah this is more nerve-wracking than it should honestly."
    player "I really hope I get that Visa."
    player "Hopeford is like, my only hope of making it in the Tech world right now."

    lisa "Bestie relaaaax you're gonna do fine."
    lisa "No one is as hard working as you."
    lisa "Like literally no one."

    player "I know, I know."
    player "I just keep thinking about all the ways it could go wrong."

    lisa "What if you stop spiraling and breathe?"
    lisa "You got the job offer."
    lisa "This is just a formality."
    lisa "When you get it, first round of drinks at that rooftop place is on you."

    player "When, huh?"

    lisa "WHEN. Manifest it bestie."

    scene bg_s01

    "[[You approach the embassy gates.]"

    player "Okay I gotta go. Wish me luck."

    lisa "Don't need it. Go get it!"

    stop music fadeout 1.0
    jump s02

# ══════════════════════════════════════════════
# SCENE: S02 — The Interview
# ACT:   Act 1 — Home Country
# CHARS: Player, Officer
# ══════════════════════════════════════════════
label s02:
    scene bg_s02

    "[[Scene change to office.]"

    officer "Job offer from Hopeford Technologies."
    officer "Software engineer."
    officer "Salary looks competitive."

    player "Yes sir."

    officer "Why Hopeford?"

    menu:
        "It's the best opportunity in my field. I've worked toward this for years.":
            jump s03
        "Honestly? It's my only real shot. There's nothing like this back home.":
            jump s03

# ══════════════════════════════════════════════
# SCENE: S03 — Approved
# ACT:   Act 1 — Home Country
# CHARS: Player, Officer
# ══════════════════════════════════════════════
label s03:
    scene bg_s03
    play sound "audio/S02-approval-stamp.mp3"

    officer "[[stamps paperwork] Welcome to Hopeford."

    "[[You exhale and smile for the first time all day.]"

    jump s04

# ══════════════════════════════════════════════
# SCENE: S04 — Settled In
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Marcus, Lisa (video call)
# ══════════════════════════════════════════════
label s04:
    scene bg_s04

    "[[6 months later, you are lounging in your modest apartment.]"
    "[[Marcus, a coworker from Hopeford, is over with takeout.]"

    marcus "So how you liking it? Real talk."

    player "Honestly? Better than I thought."
    player "The work's hard but the team's good."
    player "And I actually have a balcony, Marcus."
    player "A balcony."

    marcus "Look at you. Living the dream."

    player "I called my mom yesterday and she cried."
    player "In a good way."
    player "I think."

    marcus "That's beautiful man. You earned this."

    scene bg_s04_phone
    play sound "audio/S04-phone-buzz.mp3"

    "[[Player's phone buzzes — Lisa, video calling.]"

    lisa "BESTIEEE show me the apartment again I need to live vicariously."

    menu:
        "Let me give you the full tour! Balcony view and everything.":
            "[[Posts a story tagged with location]"
            $ suspicion += 1
            jump s05
        "I'll send pics later, promise. Tell me about your week first.":
            jump s05

# ══════════════════════════════════════════════
# SCENE: S05 — First Indications
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Marcus
# ══════════════════════════════════════════════
label s05:
    scene bg_s05
    play music "audio/S05-muffledTV.mp3"

    "[[5 years later, you are sitting in the office break room.]"
    "[[A TV plays in the background.]"
    "[[Marcus stares at it.]"
    "[[The country's new leader at a podium, gesturing forcefully.]"

    "News Anchor" "...sweeping new enforcement measures effective immediately. The administration says—"

    marcus "You hearing this?"

    player "Yeah. I mean — it's a lot of talk, right? Politicians say stuff."

    marcus "This one's different. My uncle's been here thirty years. Thirty. He's scared, man."

    player "But we're legal. We have papers."

    marcus "Yeah. So does my uncle."

    "[[Awkward silence. The TV drones on.]"

    menu:
        "You think I should be worried?":
            jump s06
        "They can't just go after people with valid Visas. That's not how it works.":
            $ suspicion += 3
            jump s06
        "What are you doing? Like, to prepare?":
            $ suspicion = max(0, suspicion - 1)
            jump s06

# ══════════════════════════════════════════════
# SCENE: S06 — Lisa Calls
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Lisa (video call)
# ══════════════════════════════════════════════
label s06:
    scene bg_s06
    stop music fadeout 2.0

    "[[You sit in your apartment living room. Late evening. News of disappearances and civil unrest has been circulating the news and all social platforms. Lisa is on video call from back home.]"

    scene bg_s06_phone
    play sound "audio/phone-beep.mp3"

    lisa "[player_name] I'm just gonna say it. Come home."

    player "Lisa—"

    lisa "I've been reading the news."
    lisa "Like all of it."
    lisa "It's bad."
    lisa "It's really bad."

    player "I have a job here. A career. I can't just—"

    lisa "I know."
    lisa "I know what you've built."
    lisa "I'm not saying forever."
    lisa "I'm saying — until things calm down."

    player "And if they don't calm down?"

    lisa "[[long pause] Then at least you'd be safe."

    "[[You walk to the window, looking out at the city — your city, now — reminiscing the feeling of hope you felt when you first set foot on this land. Now...]"

    menu:
        "I hear you. I'm gonna keep my documents on me from now on. Just in case.":
            $ s06_documents_ready = True
            jump s07
        "You're being dramatic. The news exaggerates everything.":
            $ suspicion += 3
            jump s07
        "...maybe you're right. Let me think about it.":
            jump s07

# ══════════════════════════════════════════════
# SCENE: S07 — Know Your Rights
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player (solo)
# ══════════════════════════════════════════════
label s07:
    scene bg_s07

    "[[A few hours after the phone call. You are scrolling your phone in bed and see a post from a neighbor's community group: 'Know Your Rights' workshop tomorrow at the community center.]"

    scene bg_s07_phone

    menu:
        "I'll go. Can't hurt to know.":
            $ suspicion = max(0, suspicion - 2)
            $ s07_workshop = True
            "[[You learned about warrant requirements.]"
            jump s08
        "I'm too tired. I'll catch the next one.":
            $ suspicion += 2
            jump s08

# ══════════════════════════════════════════════
# SCENE: S08 — Marcus Leaves
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Marcus
# ══════════════════════════════════════════════
label s08:
    scene bg_s08
    play sound "audio/S08-packing-sounds.mp3"

    "[[You enter the office, getting ready for another day's work. You notice Marcus is packing up his desk.]"

    player "Wait — what's happening? Why are you packing?"

    marcus "Going to stay with family. Out of state. For a while."

    player "Marcus, you're scaring me."

    marcus "Three buildings on the east side last night."
    marcus "They're not even pretending to check status anymore."
    marcus "They take you, then you prove it."
    marcus "From inside."

    player "Inside where?"

    marcus "One of those facilities."
    marcus "Hours away."
    marcus "No phone."
    marcus "They cuffed a guy with full residency, man."
    marcus "Full. Residency."

    stop sound
    play sound "audio/S08-zipper.mp3"
    "[[Marcus zips his bag, stops, and looks at you.]"

    marcus "Listen."
    marcus "If they come — don't open the door."
    marcus "Make them show the warrant."
    marcus "Read it."
    marcus "A real one has your name on it and a judge's signature."
    marcus "Not just a department stamp."
    marcus "If a judge didn't sign it, they cannot legally come in."

    player "...okay."

    marcus "Promise me."

    player "I promise."

    "[[Marcus leaves. The office feels emptier than it should.]"

    scene bg_s08_empty

    show screen suspicion_bar
    jump s09

# ══════════════════════════════════════════════
# SCENE: S09 — The Knock
# ACT:   Act 3 — The Raid
# ══════════════════════════════════════════════
label s09:
    scene bg_s09
    play sound "audio/S09-door-pounding1.mp3"

    "[[Pitch black bedroom. POUNDING on the door. Player jolts awake.]"

    "Voice (outside)" "OPEN UP. FEDERAL AGENTS."

    player "[[whispered] Oh god. Oh god oh god oh god."

    "[[More pounding. The door shakes in its frame.]"

    play sound "audio/S09-door-pounding1.mp3"

    "Voice" "WE HAVE A WARRANT. OPEN THE DOOR NOW."

    menu:
        "Grab phone and call Lisa.":
            jump s10a
        "Get documents from the bag first." if s06_documents_ready:
            jump s10b
        "Open the door — show them you have nothing to hide.":
            $ suspicion += 5
            jump s10c

# ══════════════════════════════════════════════
# PATH A — Lisa on the Line
# ══════════════════════════════════════════════
label s10a:
    scene bg_s09a_phone
    "[[You pick up your phone and dial the first number that comes to mind.]"
    play sound "audio/phone-beep.mp3"

    lisa "[[groggy] ...what time is it—"

    player "They're here. They're at my door."

    lisa "[[instantly awake] Documents. Do you have them?"

    player "Yes. Yes I have them."

    lisa "Don't open the door without seeing the warrant. Make them slide it under. I'm staying on the line."

    "Voice" "LAST WARNING. WE WILL BREAK THE DOOR."

    if s07_workshop:
        "[[You remember the workshop. You know your rights.]"

    scene bg_s12a_paper
    player "I need to see the warrant first. Slide it under the door, please."
    $ suspicion = max(0, suspicion - 1)

    if suspicion > 5:
        jump ending_b
    else:
        jump ending_a

# ── Ending A — Lisa · low suspicion 🟢 ──────────────
label ending_a:

    "Voice (outside)" "Slide it under? Fine."

    play sound "audio/S14A-paper-rustling.mp3"
    "[[Folded paper slides under the door. You pick it up, hands shaking. Phone wedged at shoulder.]"

    scene bg_s09a_phone

    player "[[whispered] Okay. It's here."

    lisa "Read it. Slowly. Tell me what it says."

    player "Hopeford District Court. Case number. There's a signature — 'Magistrate Judge.' My name. My address."

    lisa "[[exhales] Okay. That's a real one. They have legal authority. You open the door, hands visible, no sudden moves. Give them the documents. Stay calm. The second they let you, you call me back."

    player "Lisa I—"

    lisa "I know. You've done everything right so far. Keep doing it."

    "[[You set the phone on the entry table, still on speaker. Hand on the deadbolt. Click. The door opens.]"

    play sound "audio/S14A-door-open.mp3"
    scene bg_s14a_police

    agent "Step back. Hands where I can see them."

    player "I have my documents. Reaching slowly."

    "[[You hand over the folder. An agent flips through. Another scans the apartment.]"

    agent "Visa. Employment authorization. Lease."

    agent "All in order."

    agent2 "On paper."

    agent "Where do you work?"

    player "I'd like to speak with a lawyer before answering any more questions."

    "[[A long, evaluating beat.]"

    agent "[[finally] Smart. Documents check out. We're done here."

    agent2 "You sure? We could—"

    agent "I said we're done."

    play sound "audio/S14A-door-close.mp3"
    "[[Door clicks shut. Player slides the deadbolt. Slides down to the floor.]"

    scene bg_s09_door
    play music "audio/S14A-neighbours-crying.mp3"

    lisa "Are they gone?"

    player "[[whisper] They're gone."

    lisa "Oh thank goodness. Thank goodness."

    player "I heard them. Down the hall. The neighbors. There was a kid—"

    lisa "I know. You're safe."

    player "Am I?"

    stop music fadeout 3.0
    "[[You did everything right. This time.]"

    " "
    "[[ YOU SURVIVED ]"
    " "
    "Millions of legal residents live with this fear every day."
    "Not because of what they did."
    "But because of where they were born."
    jump ending_message

# ── Ending B — Lisa · high suspicion 🔴 ─────────────
label ending_b:

    "Voice (outside)" "Slide it under? Fine."

    play sound "audio/S14A-paper-rustling.mp3"
    "[[Folded paper slides under the door. You pick it up, hands shaking. Phone wedged at shoulder.]"

    scene bg_s09a_phone

    player "[[whispered] Okay. It's here."

    lisa "Read it. Slowly. Tell me what it says."

    player "Hopeford District Court. Case number. There's a signature — 'Magistrate Judge.' My name. My address."

    lisa "[[exhales] Okay. That's a real one. They have legal authority. You open the door, hands visible, no sudden moves. Give them the documents. Stay calm. The second they let you, you call me back."

    player "Lisa I —"

    lisa "I know. You've done everything right so far. Keep doing it."

    "[[You set the phone on the entry table, still on speaker. Hand on the deadbolt. Click. The door opens.]"

    play sound "audio/S14A-door-open.mp3"
    scene bg_s14a_police

    agent "Step back. Hands visible."

    player "I have documents — they're right here, I have a Visa, I work at Hopeford, I—"

    agent "Slow down. Hands on the table. Folder over here."

    "[[You put the folder down too quickly. It slides. Papers fan out. Player reaches to gather them—]"

    agent2 "Don't touch anything. Step back."

    player "Sorry — sorry, I just—"

    agent "Where do you work?"

    player "Hopeford Technologies. Software engineer. Five years."

    agent "Anyone else live here?"

    player "No, just me. A coworker comes over sometimes — Marcus — but he doesn't live here, he—"

    agent "Marcus has a last name?"

    player "Martinez. Or Martins, I — it's late, I'm sorry—"

    agent2 "You don't know your coworker's last name."

    player "I do, I just—"

    agent "This entry stamp. When did you last leave the country?"

    player "I haven't — I mean, there was a layover, last spring, to see my mom — but I came right back, it's all in the file—"

    agent2 "You didn't disclose that."

    player "I'm disclosing it now—"

    agent "You're going to come with us. Sort this out at the facility."

    player "What — no, my papers are right there, you looked at them—"

    agent "Turn around. Hands behind your back."

    lisa "Wait — what's happening? Hello?? Please—"

    "[[An agent walks to the table. Picks up the phone. Looks at Lisa's contact photo. Ends the call.]"

    scene bg_black
    agent2 "You won't be needing this."

    "[[Cuffs click. You are led out. Past the documents fanned across the table — open, useless, left behind. Past the balcony.]"

    "[[In the hallway, the neighbors. A woman crying. A child asking where mama is going. You try to catch the woman's eye. She looks away.]"

    "[[In the van. No windows. You try to remember Lisa's number. Try to remember the lawyer's name you were supposed to memorize. Try to remember why you ever thought paper could protect you.]"

    "[[You did everything right. It wasn't enough.]"

    " "
    "[[ ARRESTED ]"
    " "
    "Over 32,000 legal residents are detained by enforcement agencies each year."
    "Many have valid visas, jobs, families, and lives."
    "This is one of their stories."
    jump ending_message

# ══════════════════════════════════════════════
# PATH B — Alone
# ══════════════════════════════════════════════
label s10b:
    scene bg_s09_slamming
    play sound "audio/S09-door-pounding1.mp3"

    "Voice" "LAST WARNING. WE WILL BREAK THE DOOR."

    player "O-okay! I'm opening it! Please don't break it down!"
    $ suspicion += 2

    player "[[to yourself] Okay okay okay—"

    play music "audio/S12B_backpack.mp3" noloop
    play sound "audio/S12B_looking_for_docs.mp3"

    "[[You scramble for the bag. Knock something off the dresser. Find the documents — half of them. Where's the lease? Where's the—]"

    "Voice" "ON THREE. ONE—"

    player "I'M COMING — I'M COMING, PLEASE—"

    "[[You run to the door. Don't ask for a warrant. Don't check anything. Just turn the lock and pull it open.]"

    stop music
    stop sound
    scene bg_s12b_serious
    play music "audio/S12B_police_chatter.mp3"
    play sound "audio/S14A-door-open.mp3"

    agent "Down on the ground. NOW."

    player "I have papers — I have papers—"

    if suspicion > 5:
        jump ending_d
    else:
        jump ending_c

# ── Ending C — Alone · low suspicion 🟢 ─────────────
label ending_c:

    "[[An agent takes the folder. Flips through methodically. Another walks the apartment perimeter. You keep your hands at your sides. You don't speak.]"

    agent "Visa. Authorization. Lease."

    agent "Where do you work?"

    player "I'd like to speak with a lawyer before answering questions."

    "[[The agent holds the look. You hold it back. Don't fill the silence. Don't apologize. Don't explain.]"

    scene bg_s14a_police
    agent "[[hands back the folder] Have a good night."

    agent2 "That's it?"

    agent "That's it."

    stop music fadeout 1.0
    play sound "audio/S14A-door-close.mp3"
    "[[They leave. You close the door. Lock it. Stand there for a long time.]"

    "[[You walk to the phone. Pick it up. Stare at Lisa's name. Don't call. Not yet.]"

    "[[Instead you sit on the edge of the bed. Hands flat on your knees. Listening to the building — the shouting down the hall, the engines outside, the morning that hasn't come yet.]"

    "[[You survived alone. You don't know if that's a relief or the loneliest thing you've ever felt.]"

    "[[You did everything right. This time.]"

    " "
    "[[ YOU SURVIVED ]"
    " "
    "Millions of legal residents live with this fear every day."
    "Not because of what they did."
    "But because of where they were born."
    jump ending_message

# ── Ending D — Alone · high suspicion 🔴 ────────────
label ending_d:

    scene bg_s14b_docs
    agent "GROUND. NOW."

    "[[You're forced to your knees. Half the papers are on the floor where they fell.]"

    agent2 "[[walking into the apartment] Clear the back."

    player "Wait — please — they're in the bedroom, my Visa is in the bedroom—"

    agent "Don't move."

    "[[The agent returns from the bedroom holding the folder. Hands it to his partner. He doesn't even open it.]"

    agent "Up. Hands behind your back."

    player "But you didn't even — you didn't look at them—"

    agent "You can present them at the facility."

    player "Which facility? Where are you taking me? I have work — I have to call someone — I haven't called anyone—"

    agent "Walk."

    stop music
    play sound "audio/S14B_handcuff.mp3"
    scene bg_black

    "[[Cuffs. Cold. Final.]"

    "[[As you're led out, you pass the kitchen. Phone on the counter, dark. Lisa's name not on the screen. Nobody knows. Nobody knows yet. Past the balcony — the one you cried about to your mom. Past the fridge with the photos. Past Marcus's empty apartment two doors down. He saw this coming. He told you.]"

    "[[In the van, you try to think of who will notice you're gone. Your team won't realize until Monday morning. Your landlord, maybe never. Your mother — when she calls Sunday and no one picks up.]"

    "[[You mouth Lisa's number to yourself, over and over. You think you remember it. You're not sure.]"

    "[[You did everything right. It wasn't enough. And no one knew to look for you.]"

    " "
    "[[ ARRESTED ]"
    " "
    "Over 32,000 legal residents are detained by enforcement agencies each year."
    "Many have valid visas, jobs, families, and lives."
    "This is one of their stories."
    jump ending_message

# ══════════════════════════════════════════════
# PATH C — Opened the Door (Ending E)
# ══════════════════════════════════════════════
label s10c:

    scene bg_s09_slamming
    "[[The pounding has barely registered. You, half-asleep, fumble to the door. Not thinking. Not grabbing your phone. Not asking for a warrant. Just turn the deadbolt because someone is at the door and someone at the door means open it.]"

    "[[The door swings open. Three agents flood in before you can even step back.]"

    scene bg_s14b_docs
    agent "ON THE GROUND."

    player "Wait — what — I—"

    agent "GROUND."

    scene bg_black
    "[[Before you can process what is happening, you're on the ground. Knee in your back. Hands wrenched behind. The apartment fills with flashlight beams, voices, radios.]"

    agent2 "Clear left."

    agent3 "Clear right."

    player "I have a Visa — I have papers — please, they're in the bedroom, please let me—"

    agent "Quiet."

    player "I'm legal — I'm legal — I work at Hopeford, I have an employer, please—"

    agent "You opened the door. We didn't force entry. You consented. Anything in this apartment is fair search now."

    player "I didn't — I didn't consent, I just — I just opened the door—"

    agent "Same thing."

    "[[An agent emerges from the bedroom with the document folder but doesn't hand it to anyone. Just sets it on the counter.]"

    player "My papers — they're right there—"

    agent "Up."

    "[[You are hauled to your feet. Cuffed. Walked toward the door.]"

    player "Please — please can I get my phone — please can I call someone — please—"

    agent "Walk."

    "[[As you cross the threshold, you turn your head — try to see the apartment one more time. The balcony. The fridge with the photos. The folder on the counter, untouched, irrelevant. The phone on the nightstand. Lisa's number locked inside it.]"

    "[[In the hallway, an agent is already photographing your open door. Evidence of consent.]"

    "[[In the van, no windows. You can't stop replaying it. The pounding. The door. How easy it was. How you handed it all over without a single question. How nothing — not the Visa, not the job, not the years of paperwork — mattered the second you turned that deadbolt.]"

    "[[You think about Marcus. 'Don't open the door. Not even a crack. Promise me.' You had promised.]"

    "[[The door was the only protection you had. You opened it.]"

    " "
    "[[ ARRESTED ]"
    " "
    "Over 32,000 legal residents are detained by enforcement agencies each year."
    "Many have valid visas, jobs, families, and lives."
    "This is one of their stories."
    jump ending_message

# ══════════════════════════════════════════════
# ENDING MESSAGE — shown after all endings
# ══════════════════════════════════════════════
label ending_message:
    scene bg_black
    stop music fadeout 2.0
    "As of April 2026, 70.8%% of people held in ICE detention have no criminal conviction."
    "Even among those with convictions, a majority are for minor offenses like traffic violations."
    "Unlike in criminal court, immigrants—including legal residents—have no right to a court-appointed lawyer."
    "Currently, over 60%% of people in detention are forced to represent themselves against expert government prosecutors, making administrative errors nearly impossible to fight."
    "Know your rights. Protect your family."
    return
