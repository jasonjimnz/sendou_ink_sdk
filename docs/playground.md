# Playground

Use `playground.py` to run a live API walkthrough with typed outputs.

The script currently:

- Loads `SENDOU_TOKEN` and `SENDOU_USER` from environment variables
- Fetches the user profile with `client.users.get(...)`
- Fetches each team with `client.teams.get(...)`
- Resolves IDs with `client.users.get_ids(...)`
- Looks up an active SendouQ match with `client.sendouq.active_match(...)`

## Requirements

- Python 3.10+
- A valid API token from https://sendou.ink/api
- A user identifier (`SENDOU_USER`) as user ID, Discord ID, or custom URL

## Run on Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
$env:SENDOU_TOKEN="YOUR_TOKEN"
$env:SENDOU_USER="sendou"
python playground.py
```

## Run on macOS/Linux (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SENDOU_TOKEN="YOUR_TOKEN"
export SENDOU_USER="sendou"
python playground.py
```

## Typed variables used in the script

```python
from sendou_sdk import GetTeamResponse, GetUserIdsResponse

_team: GetTeamResponse = await client.teams.get(team.id)
user_ids: GetUserIdsResponse = await client.users.get_ids(SENDOU_USER)
```

If you want to target a local API instance, update `base_url` in `playground.py` when creating `SendouClient`.

