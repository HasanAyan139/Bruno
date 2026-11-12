import psutil

keywords = [
    "lively",
    "copilot",
    "whatsapp",
    "steam",
    "xbox",
    "discord",
    "epic",
    "chatgpt",
    "riot",
    "vanguard",
    "vgtray"
]

for process in psutil.process_iter(["pid", "name"]):
    name = process.info["name"] or ""

    if any(word in name.lower() for word in keywords):
        print(f"{name} - PID: {process.pid}")