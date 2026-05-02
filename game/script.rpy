# ── Characters & Variables ────────────────────────
default player_name = ""
default player_pronoun = "she"
default player_pronoun_cap = "She"
default player_possessive = "her"
default suspicion = 0

define player = Character("[player_name]", color="#44aaff")
define officer = Character("Officer", color="#aaaaaa")
define agent = Character("Agent", color="#ff4444")
define lisa = Character("Lisa", color="#ff88cc")
define marcus = Character("Marcus", color="#88ff88")

# ── Image Definitions ────────────────────────────
image bg_s01     = "images/S01_bg.png"
image bg_s01_phone = "images/S01_phone.png"
image bg_s01_paperwork = "images/S01_paperwork.png"
image bg_s02     = "images/S02_bg.png"
image bg_s03     = "images/S03_bg.png"
image bg_s04     = "images/S04_bg.png"
image bg_s04_phone = "images/S04_phone.png"
image bg_s05     = "images/S05_bg.png"
image bg_s06     = "images/S06_bg.png"
image bg_s06_phone = "images/S06_phone.png"
image bg_s07     = "images/S07_bg.png"
image bg_s07_phone = "images/S07_phone.png"
image bg_s08     = "images/S08_bg.png"
image bg_s08_empty = "images/S08_emptyOffice.png"
image bg_airplane = "images/airplane.png"
image bg_airport  = "images/airport.png"

# ── Screens ──────────────────────────────────────

screen suspicion_bar():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 60  # Move down to avoid overlapping with Quit button
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
    show screen quit_button
    
    # ── Character Setup ────────────────────────────
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
# IMAGE: game/images/bg/bg_street.png
# ══════════════════════════════════════════════
label s01:
    # scene bg_s01 — S01_bg.png
    scene bg_s01
    
    "[[Bright morning. You walk down a busy street in your home country. Phone to ear.]"

    # show bg_s01_phone — S01_phone.png (전화 통화 장면)
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

    # scene bg_s01 — S01_bg.png (대사관 입구로 이동)
    scene bg_s01

    "[[You approach the embassy gates.]"

    player "Okay I gotta go. Wish me luck."

    lisa "Don't need it. Go get it!"

    jump s02

# ══════════════════════════════════════════════
# SCENE: S02 — The Interview
# ACT:   Act 1 — Home Country
# CHARS: Player, Officer
# IMAGE: game/images/bg/bg_embassy.png
# ══════════════════════════════════════════════
label s02:
    # scene bg_s02 — S02_bg.png
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
# IMAGE: game/images/bg/bg_embassy.png
# ══════════════════════════════════════════════
label s03:
    # scene bg_s03 — S03_bg.png
    scene bg_s03

    officer "[[stamps paperwork] Welcome to Hopeford."

    "[[You exhale and smile for the first time all day.]"
    
    jump s04

# ══════════════════════════════════════════════
# SCENE: S04 — Settled In
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Marcus, Lisa (video call)
# IMAGE: game/images/bg/bg_apartment.png
# ══════════════════════════════════════════════
label s04:
    # scene bg_s04 — S04_bg.png
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

    # scene bg_s04_phone — S04_phone.png (리사 화상통화)
    scene bg_s04_phone

    "[[Player's phone buzzes — Lisa, video calling.]"

    lisa "BESTIEEE show me the apartment again I need to live vicariously."

    menu:
        "Let me give you the full tour! Balcony view and everything.":
            " [Posts a story tagged with location] "
            $ suspicion += 1
            jump s05
        "I'll send pics later, promise. Tell me about your week first.":
            jump s05

# ══════════════════════════════════════════════
# SCENE: S05 — First Indications
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Marcus
# IMAGE: game/images/bg/bg_office.png
# ══════════════════════════════════════════════
label s05:
    # scene bg_s05 — S05_bg.png
    scene bg_s05

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
            $ suspicion += 2
            jump s06
        "What are you doing? Like, to prepare?":
            $ suspicion = max(0, suspicion - 1)
            jump s06

# ══════════════════════════════════════════════
# SCENE: S06 — Lisa Calls
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Lisa (video call)
# IMAGE: game/images/bg/bg_apartment_living.png
# ══════════════════════════════════════════════
label s06:
    # scene bg_s06 — S06_bg.png
    scene bg_s06

    "[[You sit in your apartment living room. Late evening. News of disappearances and civil unrest has been circulating the news and all social platforms. Lisa is on video call from back home.]"

    # scene bg_s06_phone — S06_phone.png (리사 영상통화)
    scene bg_s06_phone

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
            jump s07
        "You're being dramatic. The news exaggerates everything.":
            $ suspicion += 2
            jump s07
        "...maybe you're right. Let me think about it.":
            jump s07

# ══════════════════════════════════════════════
# SCENE: S07 — Know Your Rights
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player (solo)
# IMAGE: game/images/bg/bg_bedroom_night.png
# ══════════════════════════════════════════════
label s07:
    # scene bg_s07 — S07_bg.png
    scene bg_s07

    "[[A few hours after the phone call. You are scrolling your phone in bed and see a post from a neighbor's community group: 'Know Your Rights' workshop tomorrow at the community center.]"

    # scene bg_s07_phone — S07_phone.png (폰 보는 장면)
    scene bg_s07_phone

    menu:
        "I'll go. Can't hurt to know.":
            $ suspicion = max(0, suspicion - 1)
            "[[You learned about warrant requirements.]"
            jump s08
        "I'm too tired. I'll catch the next one.":
            $ suspicion += 1
            jump s08

# ══════════════════════════════════════════════
# SCENE: S08 — Marcus Leaves
# ACT:   Act 2 — Life in Hopeford
# CHARS: Player, Marcus
# IMAGE: game/images/bg/bg_office.png
# ══════════════════════════════════════════════
label s08:
    # scene bg_s08 — S08_bg.png
    scene bg_s08

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

    # scene bg_s08_empty — S08_emptyOffice.png (마커스 퇴장 후 빈 사무실)
    scene bg_s08_empty

    show screen suspicion_bar
    jump s09

# ══════════════════════════════════════════════
# SCENE: S09 — The Knock
# ACT:   Act 3 — The Raid
# CHARS: Player, Voice outside
# IMAGE: game/images/bg/bg_bedroom_black.png
# ══════════════════════════════════════════════
label s09:
    # S09: 해당 배경 이미지 없음 — scene bg black 유지
    scene bg black
    
    "[[Pitch black bedroom. Pounding on the door. Player jolts awake.]"

    "Voice (outside)" "OPEN UP. AGENTS."

    player "[[whispered] Oh god. Oh god oh god oh god."

    "[[More pounding. The door shakes in its frame.]"

    "Voice" "WE HAVE A WARRANT. OPEN THE DOOR NOW."
    
    jump scene_door

# ── Door Scene ────────────────────────────────────
label scene_door:
    if suspicion >= 10:
        jump ending_arrested

    "A loud knock at the door."

    menu:
        "Open the door calmly":
            $ suspicion += 2
            jump scene_agent
        "Peek through the window first":
            $ suspicion += 1
            jump scene_agent
        "Don't answer":
            $ suspicion += 4
            jump scene_agent

# ── Agent Scene ───────────────────────────────
label scene_agent:
    if suspicion >= 10:
        jump ending_arrested

    agent "Federal Agents. Open up."

    menu:
        "Show your documents immediately":
            $ suspicion += 3
            agent "We'll need you to come with us anyway."
            jump scene_question
        "Ask to see their warrant":
            $ suspicion += 2
            agent "We don't need one."
            jump scene_question
        "Say nothing and call your lawyer":
            $ suspicion += 1
            agent "That's your right. But we're not leaving."
            jump scene_question

# ── Interrogation Scene ───────────────────────────
label scene_question:
    if suspicion >= 10:
        jump ending_arrested

    agent "How long have you been in this country?"

    menu:
        "Ten years. I have every document you need.":
            $ suspicion += 2
            jump scene_final
        "I'd like to speak to a lawyer before answering.":
            $ suspicion += 1
            jump scene_final
        "You have no right to ask me that.":
            $ suspicion += 4
            jump scene_final

# ── Final Scene ───────────────────────────────────
label scene_final:
    if suspicion >= 10:
        jump ending_arrested

    "A neighbor opens their door and starts recording."
    "Others in the hallway stop and watch."
    "The agents hesitate."

    menu:
        "Step back inside and shut the door":
            $ suspicion += 2
            jump ending_check
        "Stay calm. Let the neighbors witness.":
            $ suspicion -= 2
            jump ending_check

# ── Ending Check ──────────────────────────────────
label ending_check:
    if suspicion >= 10:
        jump ending_arrested
    else:
        jump ending_escaped

# ── Arrested Ending ───────────────────────────────
label ending_arrested:
    hide screen suspicion_bar
    hide screen quit_button
    # scene bg_apartment
    scene bg black
    "The agents move forward."
    player "[player_name] is handcuffed."
    "[player_possessive.capitalize()] documents are ignored."
    "10 years. Gone in minutes."
    " "
    "[[ ARRESTED ]"
    " "
    "Over 32,000 legal residents are detained by enforcement agencies each year."
    "Many have valid visas, jobs, families, and lives."
    "This is one of their stories."
    
    show screen game_over_screen
    pause
    return

# ── Escaped Ending ────────────────────────────────
label ending_escaped:
    hide screen suspicion_bar
    hide screen quit_button
    # scene bg_apartment
    scene bg black
    "The agents back down."
    "The neighbors don't stop watching."
    player "[player_name] closes the door slowly."
    "[player_possessive.capitalize()] hands are still shaking."
    "But [player_pronoun] is still here."
    " "
    "[[ YOU SURVIVED - FOR NOW ]"
    " "
    "Millions of legal residents live with this fear every day."
    "Not because of what they did."
    "But because of where they were born."
    return