from __future__ import annotations

"""Organization-related public API endpoints."""

from ..models import GetTournamentOrganizationResponse
from ._base import BaseResource


class OrganizationsResource(BaseResource):
    """Resource wrapper for organization lookups."""

    async def get(self, organization_id: int) -> GetTournamentOrganizationResponse:
        """Fetch tournament organization details by ID."""

        data = await self._get(f"/org/{organization_id}")
        return GetTournamentOrganizationResponse.model_validate(data)
