# Tube Status Discord

A simple Python script that sends live London Tube, Overground, DLR, Elizabeth Line and Tram status updates to a Discord channel using a Discord webhook and TfL live data.

## Features

- Live TfL line status updates
- Sends updates directly to Discord
- Supports `@everyone` mentions
- Automatic daily updates using cron
- Lightweight and easy to self-host
- Works on Debian, Ubuntu, Proxmox containers and VMs

## Requirements

- Python 3
- Discord webhook URL
- Python `requests` package

## Installation

Install dependencies:

```bash
apt update
apt install -y python3 python3-pip python3-venv
```

Create the project directory:

```bash
mkdir -p /opt/tubestatus-discord
cd /opt/tubestatus-discord
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Install requests:

```bash
./venv/bin/pip install requests
```

## Script Setup

Create the script:

```bash
nano tube-discord.py
```

Paste the Python script from this repository into the file.

## Discord Webhook Setup

1. Open Discord
2. Open your server
3. Go to the channel you want alerts in
4. Click **Edit Channel**
5. Go to **Integrations**
6. Open **Webhooks**
7. Create a new webhook
8. Copy the webhook URL

In `tube-discord.py`, replace:

```python
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"
```

with your real Discord webhook URL.

Do not upload your real webhook URL to GitHub.

## Run Manually

```bash
/opt/tubestatus-discord/venv/bin/python /opt/tubestatus-discord/tube-discord.py
```

## Automatic Daily Updates at 6AM

Open cron:

```bash
crontab -e
```

Add this line:

```bash
0 6 * * * /opt/tubestatus-discord/venv/bin/python /opt/tubestatus-discord/tube-discord.py
```

Save and exit.

Check it saved:

```bash
crontab -l
```

## Example Discord Output

```text
🚇 Tube Status - 6AM Update

🟢 Bakerloo - Good Service
🟢 Central - Good Service
🟡 District - Minor Delays
🔴 Jubilee - Severe Delays
```

## TfL API Endpoint

```text
https://api.tfl.gov.uk/line/mode/tube,overground,dlr,elizabeth-line,tram/status
```

## Example Proxmox Setup

Create a Debian container:

```bash
bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/ct/debian.sh)"
```

Then follow the installation steps above.

## Licence

MIT Licence

## Credits

- TfL Unified API
- Discord Webhooks
- Python Requests Library
