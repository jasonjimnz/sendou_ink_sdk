# Sendou.ink Python SDK

Async Python SDK for the sendou.ink public API.

Current version: `1.0.1`

## Installation

```bash
pip install sendou-ink-sdk
```

## Quick start

```python
import asyncio
from sendou_sdk import SendouClient

async def main() -> None:
    async with SendouClient(token="YOUR_TOKEN") as client:
        user = await client.users.get("sendou")
        print(user.name, user.country)

asyncio.run(main())
```

## Data types

The SDK returns typed Pydantic models. You can add type hints directly in your scripts:

```python
from sendou_sdk import GetUserResponse, GetUserIdsResponse, GetTeamResponse

user: GetUserResponse = await client.users.get("sendou")
user_ids: GetUserIdsResponse = await client.users.get_ids("sendou")
team: GetTeamResponse = await client.teams.get(4)
```

Most commonly used response and request models are exported from `sendou_sdk`.

## Playground

Use `playground.py` to quickly inspect live API responses with your own token and user identifier.

Required environment variables:

- `SENDOU_TOKEN` (API token from https://sendou.ink/api)
- `SENDOU_USER` (user ID, Discord ID, or custom URL)

Run the playground on Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
$env:SENDOU_TOKEN="YOUR_TOKEN"
$env:SENDOU_USER="sendou"
python playground.py
```

Run the playground on macOS/Linux (bash/zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SENDOU_TOKEN="YOUR_TOKEN"
export SENDOU_USER="sendou"
python playground.py
```

See `docs/playground.md` for full platform-specific instructions.

## Local testing

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

Run a quick test against the live API:

```python
import asyncio
from sendou_sdk import SendouClient

async def main() -> None:
    async with SendouClient(token="YOUR_TOKEN") as client:
        user = await client.users.get("sendou")
        print(user.name, user.country)

asyncio.run(main())
```

Build and preview docs locally:

```bash
mkdocs serve
```

## Build wheel

Create a distributable wheel from source:

```powershell
python -m pip install -e ".[build]"
python -m build --wheel
python -m twine check dist/*
```

## Releases

Releases are automated with GitHub Actions:

- `deploy-docs.yml` deploys documentation to GitHub Pages.
- `release-tag-publish.yml` deploys docs for the tag, validates the tag version against `pyproject.toml`, builds distributions, and publishes to PyPI.

Create a release tag (example):

```powershell
git tag [VERSION] # e.g. git tag v1.0.1
git push origin [VERSION] # e.g. git push origin v1.0.1
```

For tagged releases, keep `CHANGELOG.md` updated before pushing the tag.

## Features

- Async-first client built on httpx
- Typed response models powered by Pydantic
- Token-based authentication handling
- Explicit API error types

## Documentation

Full documentation lives in `docs/` and can be published with MkDocs.

Published docs: https://jasonjimnz.github.io/sendou_ink_sdk/

- `docs/usage.md` for typed endpoint examples
- `docs/playground.md` for local playground instructions
- `docs/configuration.md` for runtime configuration
- `docs/reference.md` for method and model reference
- `docs/releasing.md` for release automation and tag flow
- `CHANGELOG.md` for release notes

