# ============================================================
#  DecodeLabs | Industrial Training Kit — Batch 2026
#  Project 1  : Rule-Based AI Chatbot
#  Author     : <Your Name>
# ============================================================

# ── KNOWLEDGE BASE (Dictionary / Hash Map — O(1) lookup) ────
RESPONSES = {
    # Greetings
    "hello"        : "Hey there! I'm DecoBot. How can I help you today?",
    "hi"           : "Hi! Good to see you. What's on your mind?",
    "hey"          : "Hey! What can I do for you?",

    # Identity
    "who are you"  : "I'm DecoBot — a rule-based AI chatbot built at DecodeLabs.",
    "what are you" : "I'm a rule-based chatbot. Pure logic, zero hallucinations!",
    "your name"    : "My name is DecoBot. Nice to meet you!",

    # Well-being
    "how are you"  : "I'm running at 100% efficiency. Thanks for asking!",
    "what's up"    : "Just processing rules and serving answers. You?",

    # Help / Capabilities
    "help"         : "I can answer questions about: greetings, my identity, AI, DecodeLabs, and general chat. Try me!",
    "what can you do": "I respond to predefined inputs using rule-based logic. Ask me anything on my topic list!",

    # About AI
    "what is ai"   : "AI is the simulation of human intelligence by machines using logic, learning, and reasoning.",
    "what is ml"   : "Machine Learning is a subset of AI where systems learn patterns from data instead of explicit rules.",
    "difference between ai and ml": "AI is the broad concept; ML is a technique within AI that learns from data automatically.",

    # About DecodeLabs
    "what is decodelabs" : "DecodeLabs is a tech training organisation that provides hands-on project-based AI/tech internships.",
    "about decodelabs"   : "DecodeLabs (Greater Lucknow, India) offers real-world industrial training to aspiring engineers.",

    # Fun / Misc
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "favourite language": "Python, obviously. Clean syntax, powerful libraries — what's not to love?",
    "meaning of life"   : "42. At least, that's what the algorithm says.",

    # Farewell
    "bye"          : "Goodbye! Keep building. 🚀",
    "goodbye"      : "See you next time. Stay curious!",
    "see you"      : "See ya! Come back anytime.",
}

# ── FALLBACK ────────────────────────────────────────────────
FALLBACK = "I don't understand that yet. Try 'help' to see what I can do."

# ── EXIT COMMANDS ────────────────────────────────────────────
EXIT_COMMANDS = {"exit", "quit", "q", "stop", "bye", "goodbye"}


# ── PHASE 1 : INPUT SANITIZATION ────────────────────────────
def sanitize(raw: str) -> str:
    """Lowercase and strip whitespace — normalise the raw feed."""
    return raw.lower().strip()


# ── PHASE 2 : INTENT MATCHING ────────────────────────────────
def get_response(clean_input: str) -> str:
    """O(1) dictionary lookup with a fallback default."""
    return RESPONSES.get(clean_input, FALLBACK)


# ── PHASE 3 : MAIN LOOP (The Heartbeat) ──────────────────────
def run_chatbot():
    print("=" * 55)
    print("  DecoBot — Rule-Based AI Chatbot | DecodeLabs 2026")
    print("  Type 'help' for topics  |  Type 'exit' to quit")
    print("=" * 55)

    while True:                              # ← Infinite loop
        raw_input_text = input("\nYou: ")
        clean_input    = sanitize(raw_input_text)   # Sanitize

        if not clean_input:                  # ignore empty enter
            continue

        if clean_input in EXIT_COMMANDS:     # ← Kill command
            print("DecoBot:", RESPONSES.get(clean_input, "Goodbye! 👋"))
            print("\n[ Session ended. DecoBot signing off. ]\n")
            break                            # ← Clean break

        response = get_response(clean_input)
        print("DecoBot:", response)


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
