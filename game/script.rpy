default player_name = ""
default player_pronoun = "she"
default player_pronoun_cap = "She"
default player_possessive = "her"
default suspicion = 0

define o = Character("Immigration Officer", color="#aaaaaa")
define a = Character("ICE Agent", color="#ff4444")
define m = Character("[player_name]", color="#44aaff")

screen suspicion_bar():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        vbox:
            text "Suspicion" size 20 color "#ffffff"
            bar value suspicion range 100 xsize 200 ysize 20 left_bar "#ff4444" right_bar "#333333"

screen quit_button():
    frame:
        xalign 1.0
        yalign 1.0
        xoffset -20
        yoffset -20
        background "#00000088"
        padding (10, 5)
        textbutton "Quit" action Quit()

# ── Start ─────────────────────────────────────────
label start:
    scene bg airport
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

    jump scene_airport

# ── Airport Scene ─────────────────────────────────
label scene_airport:
    scene bg airport

    "[player_name] has just landed in the United States."
    "[player_pronoun_cap] clutches [player_possessive] documents tightly."
    "Years of paperwork. Interviews. Waiting. All for this moment."

    o "Next."
    o "Name?"
    m "[player_name]."
    o "Purpose of stay?"

    menu:
        "Work visa. I have all the documents.":
            o "Mm. How long do you intend to stay?"
            m "As long as my visa allows. I want to build a life here."
            o "..."
            o "Everything checks out. Welcome to the United States."
            "[player_name] exhales for the first time in hours."

    "Years pass."
    "A job. A home. A community."
    "[player_name] has built [player_possessive] life here — legally, carefully, quietly."

    jump scene_timeskip

# ── Time Skip ─────────────────────────────────────
label scene_timeskip:
    scene bg apartment

    "[[ 10 YEARS LATER ]"
    " "
    "It's 6:47 AM."
    "[player_name]'s apartment. A quiet morning."
    "[player_pronoun_cap] is getting ready for work."
    "Today feels like any other day."

    show screen suspicion_bar
    jump scene_door

# ── Door Scene ────────────────────────────────────
label scene_door:
    if suspicion >= 100:
        jump ending_arrested

    "A loud knock at the door."

    menu:
        "Open the door calmly":
            $ suspicion += 20
            jump scene_agent
        "Peek through the window first":
            $ suspicion += 10
            jump scene_agent
        "Don't answer":
            $ suspicion += 40
            jump scene_agent

# ── ICE Agent Scene ───────────────────────────────
label scene_agent:
    if suspicion >= 100:
        jump ending_arrested

    a "ICE. Open up."

    menu:
        "Show your documents immediately":
            $ suspicion += 30
            a "We'll need you to come with us anyway."
            jump scene_question
        "Ask to see their warrant":
            $ suspicion += 20
            a "We don't need one."
            jump scene_question
        "Say nothing and call your lawyer":
            $ suspicion += 10
            a "That's your right. But we're not leaving."
            jump scene_question

# ── Interrogation Scene ───────────────────────────
label scene_question:
    if suspicion >= 100:
        jump ending_arrested

    a "How long have you been in this country?"

    menu:
        "Ten years. I have every document you need.":
            $ suspicion += 25
            jump scene_final
        "I'd like to speak to a lawyer before answering.":
            $ suspicion += 10
            jump scene_final
        "You have no right to ask me that.":
            $ suspicion += 40
            jump scene_final

# ── Final Scene ───────────────────────────────────
label scene_final:
    if suspicion >= 100:
        jump ending_arrested

    "A neighbor opens their door and starts recording."
    "Others in the hallway stop and watch."
    "The agents hesitate."

    menu:
        "Step back inside and shut the door":
            $ suspicion += 25
            jump ending_check
        "Stay calm. Let the neighbors witness.":
            $ suspicion -= 20
            jump ending_check

# ── Ending Check ──────────────────────────────────
label ending_check:
    if suspicion >= 100:
        jump ending_arrested
    else:
        jump ending_escaped

# ── Arrested Ending ───────────────────────────────
label ending_arrested:
    hide screen suspicion_bar
    hide screen quit_button
    scene bg apartment
    "The agents move forward."
    "[player_name] is handcuffed."
    "[player_possessive.capitalize()] documents are ignored."
    "10 years. Gone in minutes."
    " "
    "[[ ARRESTED ]"
    " "
    "In 2025, over 32,000 legal immigrants were detained by ICE."
    "Many had valid visas. Many had jobs, families, and lives here."
    "This is one of their stories."
    return

# ── Escaped Ending ────────────────────────────────
label ending_escaped:
    hide screen suspicion_bar
    hide screen quit_button
    scene bg apartment
    "The agents back down."
    "The neighbors don't stop watching."
    "[player_name] closes the door slowly."
    "[player_possessive.capitalize()] hands are still shaking."
    "But [player_pronoun] is still here."
    " "
    "[[ YOU SURVIVED - FOR NOW ]"
    " "
    "Millions of legal immigrants live with this fear every day."
    "Not because of what they did."
    "But because of where they were born."
    return