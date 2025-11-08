# llm_local.py
import random

# Simple local AI responder for now
def ask_ai(prompt: str) -> str:
    responses = [
        "That’s a good question! Let me break it down for you.",
        "Interesting point — let’s explore that further.",
        "Here’s what I think, from Sainath’s perspective.",
        "That’s something I’d also consider in a real DevOps setup.",
        "Hmm, let’s reason this out like a system architect would."
    ]
    return f"{random.choice(responses)}\n\n💡 {prompt}"
