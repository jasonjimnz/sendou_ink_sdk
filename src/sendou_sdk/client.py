from __future__ import annotations

"""Top-level async client for the sendou.ink public API."""

from typing import Any

from ._http import SendouHttpClient
from .config import SendouConfig, SendouDefaults
from .resources import (
    CalendarResource,
    OrganizationsResource,
    SendouqResource,
    TeamsResource,
    TournamentsResource,
    UsersResource,
)


class SendouClient:
    """Async SDK client exposing typed resource groups.

    Parameters:
        token: API token from https://sendou.ink/api.
        base_url: API base URL. If omitted, defaults to the production API.
        timeout_seconds: Request timeout in seconds.
    """

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str | None = None,
        timeout_seconds: float | None = None,
    ) -> None:
        config = SendouConfig(
            base_url=base_url or SendouDefaults.base_url,
            timeout_seconds=timeout_seconds or SendouDefaults.timeout_seconds,
            token=token,
        )
        self._http = SendouHttpClient(config)
        self.users = UsersResource(self._http)
        self.teams = TeamsResource(self._http)
        self.calendar = CalendarResource(self._http)
        self.sendouq = SendouqResource(self._http)
        self.tournaments = TournamentsResource(self._http)
        self.organizations = OrganizationsResource(self._http)

    async def request(self, method: str, path: str, *, params: dict[str, Any] | None = None) -> Any:
        """Perform a low-level request against the API.

        Prefer resource helpers when possible, and use this method for endpoints
        not yet wrapped by the SDK.
        """

        return await self._http.request(method, path, params=params)

    async def close(self) -> None:
        """Close the underlying HTTP client and release network resources."""

        await self._http.close()

    async def __aenter__(self) -> "SendouClient":
        """Enter async context manager scope."""

        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        """Exit async context manager scope and close the client."""

        await self.close()
