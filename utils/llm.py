import json

def process_strategic_data(data_input: str):
    data_map = {
        "idea": [
            "Market-ready SaaS Platform",
            "Local Service Marketplace",
            "Subscription-based Consumer App"
        ],
        "roadmap": [
            "Phase 1: Market Research",
            "Phase 2: Prototype Development",
            "Phase 3: Beta Testing"
        ],
        "default": [
            "Analysis Category A",
            "Analysis Category B",
            "Analysis Category C"
        ]
    }

    key = "default"
    if "Generate 3 business ideas" in data_input:
        key = "idea"
    elif "roadmap" in data_input.lower():
        key = "roadmap"

    return "\n".join(f"- {item}" for item in data_map[key])