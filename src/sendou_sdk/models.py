from __future__ import annotations

"""Typed request and response models exposed by the SDK."""

from typing import Literal

from pydantic import BaseModel, Field


class SocialLinks(BaseModel):
    """Optional social profile links for a user."""

    twitch: str | None = None
    twitter: None = None
    battlefy: str | None = None
    bsky: str | None = None


class ProfileWeapon(BaseModel):
    """Weapon entry shown on a user's profile."""

    id: int
    name: str
    is_five_star: bool = Field(alias="isFiveStar")


class Badge(BaseModel):
    """Badge metadata shown on a user profile."""

    name: str
    count: int
    image_url: str = Field(alias="imageUrl")
    gif_url: str = Field(alias="gifUrl")


class GlobalTeamMembership(BaseModel):
    """A team membership summary for a user profile."""

    id: int
    role: str | None


class SeasonalRankTier(BaseModel):
    """Tier metadata for a seasonal rank."""

    name: str
    is_plus: bool = Field(alias="isPlus")


class SeasonalRank(BaseModel):
    """Current seasonal rank details."""

    tier: SeasonalRankTier
    season: int


class GetUserResponse(BaseModel):
    """Response model for a user profile lookup."""

    id: int
    name: str
    discord_id: str = Field(alias="discordId")
    url: str
    avatar_url: str | None = Field(alias="avatarUrl")
    country: str | None
    socials: SocialLinks
    plus_server_tier: int | None = Field(alias="plusServerTier")
    weapon_pool: list[ProfileWeapon] = Field(alias="weaponPool")
    badges: list[Badge]
    teams: list[GlobalTeamMembership]
    pronouns: dict | None
    peak_xp: int | None = Field(alias="peakXp")
    current_rank: SeasonalRank | None = Field(alias="currentRank")


class GetUserIdsResponse(BaseModel):
    """Response model for resolving user id variants."""

    id: int
    discord_id: str = Field(alias="discordId")
    custom_url: str | None = Field(alias="customUrl")


class GetTeamResponse(BaseModel):
    """Response model for team details."""

    id: int
    name: str
    team_page_url: str = Field(alias="teamPageUrl")
    logo_url: str | None = Field(alias="logoUrl")


class CalendarWeekItem(BaseModel):
    """Single calendar event returned for a week query."""

    name: str
    tournament_id: int | None = Field(alias="tournamentId")
    tournament_url: str | None = Field(alias="tournamentUrl")
    start_time: str = Field(alias="startTime")


# Collection returned by `client.calendar.week(...)`.
GetCalendarWeekResponse = list[CalendarWeekItem]


class GetUsersActiveSendouqMatchResponse(BaseModel):
    """Response model for a user's active SendouQ match lookup."""

    match_id: int | None = Field(alias="matchId")


class SendouqMatchPlayer(BaseModel):
    """Player entry in a SendouQ match team."""

    user_id: int = Field(alias="userId")
    rank: dict | None


class SendouqMatchTeam(BaseModel):
    """Team data within a SendouQ match."""

    id: int
    score: int
    players: list[SendouqMatchPlayer]


class MapListMap(BaseModel):
    """Map and result metadata used in matches and brackets."""

    map: dict
    source: int | Literal["DEFAULT", "TIEBREAKER", "BOTH", "TO", "COUNTERPICK"]
    winner_team_id: int | None = Field(alias="winnerTeamId")
    participated_user_ids: list[int] | None = Field(alias="participatedUserIds")
    points: tuple[int, int] | None


class GetSendouqMatchResponse(BaseModel):
    """Response model for SendouQ match details."""

    team_alpha: SendouqMatchTeam | None = Field(alias="teamAlpha")
    team_bravo: SendouqMatchTeam | None = Field(alias="teamBravo")
    map_list: list[MapListMap] = Field(alias="mapList")


class TournamentTeamsSummary(BaseModel):
    """Tournament registration and check-in totals."""

    registered_count: int = Field(alias="registeredCount")
    checked_in_count: int = Field(alias="checkedInCount")


class TournamentBracket(BaseModel):
    """Tournament bracket metadata."""

    type: Literal["double_elimination", "single_elimination", "round_robin", "swiss"]
    name: str


class GetTournamentResponse(BaseModel):
    """Response model for tournament overview details."""

    name: str
    url: str
    logo_url: str | None = Field(alias="logoUrl")
    start_time: str = Field(alias="startTime")
    teams: TournamentTeamsSummary
    brackets: list[TournamentBracket]
    organization_id: int | None = Field(alias="organizationId")
    is_finalized: bool = Field(alias="isFinalized")


class TournamentTeamMember(BaseModel):
    """Member entry for a tournament team."""

    user_id: int = Field(alias="userId")
    name: str
    discord_id: str = Field(alias="discordId")
    battlefy: str | None
    avatar_url: str | None = Field(alias="avatarUrl")
    country: str | None
    captain: bool
    in_game_name: str | None = Field(alias="inGameName")
    pronouns: dict | None
    friend_code: str = Field(alias="friendCode")
    joined_at: str = Field(alias="joinedAt")


class TournamentTeamSeedingPower(BaseModel):
    """Computed seeding power values for a tournament team."""

    ranked: float | None
    unranked: float | None


class TournamentTeam(BaseModel):
    """Tournament team details including members and seeding."""

    id: int
    name: str
    registered_at: str = Field(alias="registeredAt")
    checked_in: bool = Field(alias="checkedIn")
    url: str
    team_page_url: str | None = Field(alias="teamPageUrl")
    logo_url: str | None = Field(alias="logoUrl")
    seed: int | None
    map_pool: list[dict] | None = Field(alias="mapPool")
    seeding_power: TournamentTeamSeedingPower = Field(alias="seedingPower")
    members: list[TournamentTeamMember]


# Collection returned by `client.tournaments.teams(...)`.
GetTournamentTeamsResponse = list[TournamentTeam]


class TournamentPlayer(BaseModel):
    """Tournament player summary with participated match ids."""

    user_id: int = Field(alias="userId")
    match_ids: list[int] = Field(alias="matchIds")


# Collection returned by `client.tournaments.players(...)`.
GetTournamentPlayersResponse = list[TournamentPlayer]


class TournamentCastChannel(BaseModel):
    """Broadcast channel details for a casted match."""

    type: Literal["TWITCH"]
    channel_id: str = Field(alias="channelId")


class CastedMatch(BaseModel):
    """Currently casted tournament match entry."""

    match_id: int = Field(alias="matchId")
    channel: TournamentCastChannel


class FutureCastedMatch(BaseModel):
    """Upcoming casted match entry."""

    match_id: int = Field(alias="matchId")
    channel: TournamentCastChannel | None


class GetCastedTournamentMatchesResponse(BaseModel):
    """Response model for current and future casted matches."""

    current: list[CastedMatch]
    future: list[FutureCastedMatch]


class TournamentMatchTeam(BaseModel):
    """Team score details for a tournament match."""

    id: int
    score: int


class GetTournamentMatchResponse(BaseModel):
    """Response model for tournament match details."""

    team_one: TournamentMatchTeam | None = Field(alias="teamOne")
    team_two: TournamentMatchTeam | None = Field(alias="teamTwo")
    bracket_name: str | None = Field(alias="bracketName")
    round_name: str | None = Field(alias="roundName")
    map_list: list[MapListMap] | None = Field(alias="mapList")
    url: str


class TournamentBracketMeta(BaseModel):
    """Bracket-level metadata for structure and grouping."""

    teams_per_group: int | None = Field(alias="teamsPerGroup")
    group_count: int | None = Field(alias="groupCount")
    round_count: int | None = Field(alias="roundCount")


class TournamentBracketTeamsEntry(BaseModel):
    """Minimal team entry returned with bracket payloads."""

    id: int
    checked_in: bool = Field(alias="checkedIn")


class GetTournamentBracketResponse(BaseModel):
    """Response model for tournament bracket data."""

    data: dict
    teams: list[TournamentBracketTeamsEntry]
    meta: TournamentBracketMeta


class TournamentBracketStandingStats(BaseModel):
    """Stat line used in bracket standings."""

    set_wins: int = Field(alias="setWins")
    set_losses: int = Field(alias="setLosses")
    map_wins: int = Field(alias="mapWins")
    map_losses: int = Field(alias="mapLosses")
    points: int
    wins_against_tied: int = Field(alias="winsAgainstTied")
    losses_against_tied: int | None = Field(alias="lossesAgainstTied")
    buchholz_sets: int | None = Field(alias="buchholzSets")
    buchholz_maps: int | None = Field(alias="buchholzMaps")


class TournamentBracketStanding(BaseModel):
    """Single bracket standing entry for a tournament team."""

    tournament_team_id: int = Field(alias="tournamentTeamId")
    placement: int
    stats: TournamentBracketStandingStats | None


class GetTournamentBracketStandingsResponse(BaseModel):
    """Response model for tournament bracket standings."""

    standings: list[TournamentBracketStanding]


class TournamentOrganizationMember(BaseModel):
    """Member details for a tournament organization."""

    user_id: int = Field(alias="userId")
    name: str
    discord_id: str = Field(alias="discordId")
    pronouns: dict | None
    role: str
    role_display_name: str | None = Field(alias="roleDisplayName")


class GetTournamentOrganizationResponse(BaseModel):
    """Response model for tournament organization details."""

    id: int
    name: str
    description: str | None
    url: str
    logo_url: str | None = Field(alias="logoUrl")
    members: list[TournamentOrganizationMember]
    social_link_urls: list[str] = Field(alias="socialLinkUrls")


class TournamentSeedsBody(BaseModel):
    """Request body for tournament seeding updates."""

    tournament_team_ids: list[int] = Field(alias="tournamentTeamIds")


class TournamentStartingBracketsBody(BaseModel):
    """Request body for setting tournament starting brackets."""

    starting_brackets: list[dict] = Field(alias="startingBrackets")


class TournamentTeamMemberBody(BaseModel):
    """Request body for adding or removing a tournament team member."""

    user_id: int = Field(alias="userId")


class TournamentUpdateMemberIgnBody(BaseModel):
    """Request body for updating a member in-game name."""

    user_id: int = Field(alias="userId")
    in_game_name: str = Field(alias="inGameName")
