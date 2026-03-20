# Sendou.ink SDK

Async Python SDK for the sendou.ink public API.

## Install

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

## Authentication

Pass your API token via `SendouClient(token=...)`. Tokens are generated at https://sendou.ink/api.

## Data types

SDK methods return typed Pydantic models (for example `GetUserResponse` and `GetTournamentResponse`).
See `reference.md` for the full method-to-type map.

## Playground

For a live end-to-end example using environment variables, see `playground.py` and `playground.md` (Windows and macOS/Linux instructions included).

## Documentation map

- `usage.md`: typed examples for all resource groups
- `playground.md`: local runnable script instructions
- `configuration.md`: token, base URL, and timeout options
- `reference.md`: method signatures, response/request models, and errors
- `releasing.md`: tag-based release and PyPI publish automation
- `../CHANGELOG.md`: release notes

## Deploying docs

Documentation is deployed automatically by GitHub Actions workflow `deploy-docs.yml`.

For tagged releases, workflow `release-tag-publish.yml` deploys docs and then publishes the package to PyPI.

## Resources

- `client.users` → user profile + IDs
- `client.teams` → team details
- `client.calendar` → weekly tournament calendar
- `client.sendouq` → active SendouQ match + match details
- `client.tournaments` → tournament details + bracket + team ops
- `client.organizations` → organization info
