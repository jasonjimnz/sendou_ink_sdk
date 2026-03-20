from __future__ import annotations

"""SendouQ matchmaking endpoints."""

from ..models import GetSendouqMatchResponse, GetUsersActiveSendouqMatchResponse
from ._base import BaseResource


class SendouqResource(BaseResource):
    """Resource wrapper for SendouQ match lookups."""

    async def active_match(self, user_id: int) -> GetUsersActiveSendouqMatchResponse:
        """Get a user's active SendouQ match id, if any."""

        data = await self._get(f"/sendouq/active-match/{user_id}")
        return GetUsersActiveSendouqMatchResponse.model_validate(data)

    async def match(self, match_id: int) -> GetSendouqMatchResponse:
        """Fetch full SendouQ match details by match ID."""

        data = await self._get(f"/sendouq/match/{match_id}")
        return GetSendouqMatchResponse.model_validate(data)
