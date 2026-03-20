from __future__ import annotations

"""Team-related public API endpoints."""

from ..models import GetTeamResponse
from ._base import BaseResource


class TeamsResource(BaseResource):
    """Resource wrapper for `/team/*` endpoints."""

    async def get(self, team_id: int) -> GetTeamResponse:
        """Fetch team details by numeric team ID."""

        data = await self._get(f"/team/{team_id}")
        return GetTeamResponse.model_validate(data)
