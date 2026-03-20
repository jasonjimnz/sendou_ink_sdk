from __future__ import annotations

"""User-related endpoints for profile and id resolution."""

from ..errors import SendouApiError
from ..models import GetUserIdsResponse, GetUserResponse
from ._base import BaseResource


class UsersResource(BaseResource):
    """Resource wrapper for `/user/*` endpoints."""

    async def get(self, user_id_or_discord_id: str | int) -> GetUserResponse:
        """Fetch a user profile by user ID, Discord ID, or custom URL.

        The API endpoint `/user/{identifier}` resolves user ID and Discord ID
        directly. If a 404 is returned, the SDK attempts ID resolution via
        `/user/{identifier}/ids` and retries with the numeric user ID.
        """

        identifier = str(user_id_or_discord_id)
        try:
            data = await self._get(f"/user/{identifier}")
        except SendouApiError as exc:
            if exc.status_code != 404:
                raise
            # /user/{identifier} does not resolve custom URL values; map to numeric id first.
            ids = await self.get_ids(identifier)
            data = await self._get(f"/user/{ids.id}")

        return GetUserResponse.model_validate(data)

    async def get_ids(self, user_id_discord_id_or_custom: str | int) -> GetUserIdsResponse:
        """Resolve user ID variants (numeric ID, Discord ID, custom URL)."""

        data = await self._get(f"/user/{user_id_discord_id_or_custom}/ids")
        return GetUserIdsResponse.model_validate(data)
