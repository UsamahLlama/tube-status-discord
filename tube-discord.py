import requests
from datetime import datetime

WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

url = "https://api.tfl.gov.uk/line/mode/tube,overground,dlr,elizabeth-line,tram/status"
data = requests.get(url, timeout=20).json()

results = []

for line in data:
    name = line["name"]
    status = line["lineStatuses"][0]["statusSeverityDescription"]
    reason = line["lineStatuses"][0].get("reason", "No reported issues")

    if status == "Good Service":
        emoji = "🟢"
    elif "Minor" in status:
        emoji = "🟡"
    elif "Severe" in status or "Suspended" in status:
        emoji = "🔴"
    else:
        emoji = "🟠"

    results.append(f"{emoji} **{name}** - `{status}`\n{reason}")

message = {
    "username": "Tube Status",
    "content": "@everyone",
    "embeds": [{
        "title": "🚇 Tube Status - 6AM Update",
        "description": "\n\n".join(results),
        "color": 3447003,
        "footer": {
            "text": f"Source: TfL live data | Updated {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        }
    }]
}

requests.post(WEBHOOK_URL, json=message, timeout=20).raise_for_status()
