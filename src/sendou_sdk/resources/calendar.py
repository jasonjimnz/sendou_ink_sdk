from __future__ import annotations

"""Calendar-related public API endpoints."""

from ..models import CalendarWeekItem, GetCalendarWeekResponse
from ._base import BaseResource


class CalendarResource(BaseResource):
    """Resource wrapper for calendar schedule queries."""

    async def week(self, year: int, week: int) -> GetCalendarWeekResponse:
        """Fetch all calendar items for the provided ISO week."""

        data = await self._get(f"/calendar/{year}/{week}")
        return [CalendarWeekItem.model_validate(entry) for entry in data]
