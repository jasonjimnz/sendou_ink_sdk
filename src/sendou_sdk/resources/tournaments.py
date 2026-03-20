from __future__ import annotations

"""Tournament endpoints including read and admin operations."""

from ..models import (
    GetCastedTournamentMatchesResponse,
    GetTournamentBracketResponse,
    GetTournamentBracketStandingsResponse,
    GetTournamentMatchResponse,
    GetTournamentPlayersResponse,
    GetTournamentResponse,
    GetTournamentTeamsResponse,
    TournamentPlayer,
    TournamentSeedsBody,
    TournamentStartingBracketsBody,
    TournamentTeam,
    TournamentTeamMemberBody,
    TournamentUpdateMemberIgnBody,
)
from ._base import BaseResource


class TournamentsResource(BaseResource):
    """Resource wrapper for `/tournament/*` and related endpoints."""

    async def get(self, tournament_id: int) -> GetTournamentResponse:
        """Fetch tournament overview details."""

        data = await self._get(f"/tournament/{tournament_id}")
        return GetTournamentResponse.model_validate(data)

    async def teams(self, tournament_id: int) -> GetTournamentTeamsResponse:
        """Fetch teams registered for a tournament."""

        data = await self._get(f"/tournament/{tournament_id}/teams")
        return [TournamentTeam.model_validate(item) for item in data]

    async def players(self, tournament_id: int) -> GetTournamentPlayersResponse:
        """Fetch players and match participation data for a tournament."""

        data = await self._get(f"/tournament/{tournament_id}/players")
        return [TournamentPlayer.model_validate(item) for item in data]

    async def casted(self, tournament_id: int) -> GetCastedTournamentMatchesResponse:
        """Fetch current and upcoming casted matches for a tournament."""

        data = await self._get(f"/tournament/{tournament_id}/casted")
        return GetCastedTournamentMatchesResponse.model_validate(data)

    async def match(self, match_id: int) -> GetTournamentMatchResponse:
        """Fetch details for a tournament match by match ID."""

        data = await self._get(f"/tournament-match/{match_id}")
        return GetTournamentMatchResponse.model_validate(data)

    async def bracket(self, tournament_id: int, bracket_index: int) -> GetTournamentBracketResponse:
        """Fetch bracket structure data by tournament and bracket index."""

        data = await self._get(f"/tournament/{tournament_id}/brackets/{bracket_index}")
        return GetTournamentBracketResponse.model_validate(data)

    async def bracket_standings(
        self,
        tournament_id: int,
        bracket_index: int,
    ) -> GetTournamentBracketStandingsResponse:
        """Fetch standings for a specific tournament bracket."""

        data = await self._get(f"/tournament/{tournament_id}/brackets/{bracket_index}/standings")
        return GetTournamentBracketStandingsResponse.model_validate(data)

    async def seed(self, tournament_id: int, body: TournamentSeedsBody) -> None:
        """Update tournament seed ordering using team IDs."""

        payload = body.model_dump(by_alias=True)
        await self._post(f"/tournament/{tournament_id}/seeds", payload=payload)

    async def starting_brackets(self, tournament_id: int, body: TournamentStartingBracketsBody) -> None:
        """Set starting bracket assignments for a tournament."""

        payload = body.model_dump(by_alias=True)
        await self._post(f"/tournament/{tournament_id}/starting-brackets", payload=payload)

    async def add_member(self, tournament_id: int, tournament_team_id: int, body: TournamentTeamMemberBody) -> None:
        """Add a member to a tournament team."""

        payload = body.model_dump(by_alias=True)
        await self._post(
            f"/tournament/{tournament_id}/teams/{tournament_team_id}/add-member",
            payload=payload,
        )

    async def remove_member(self, tournament_id: int, tournament_team_id: int, body: TournamentTeamMemberBody) -> None:
        """Remove a member from a tournament team."""

        payload = body.model_dump(by_alias=True)
        await self._post(
            f"/tournament/{tournament_id}/teams/{tournament_team_id}/remove-member",
            payload=payload,
        )

    async def update_member_ign(
        self,
        tournament_id: int,
        tournament_team_id: int,
        body: TournamentUpdateMemberIgnBody,
    ) -> None:
        """Update a tournament team member in-game name."""

        payload = body.model_dump(by_alias=True)
        await self._post(
            f"/tournament/{tournament_id}/teams/{tournament_team_id}/update-member-ign",
            payload=payload,
        )
