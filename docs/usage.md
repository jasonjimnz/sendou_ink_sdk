# Usage

All examples below use concrete SDK data types for IDE autocomplete and static checks.

## Users

```python
from sendou_sdk import GetUserIdsResponse, GetUserResponse

user: GetUserResponse = await client.users.get("sendou")
user_ids: GetUserIdsResponse = await client.users.get_ids("sendou")
```

## Teams

```python
from sendou_sdk import GetTeamResponse

team: GetTeamResponse = await client.teams.get(4)
```

## Calendar

```python
from sendou_sdk import GetCalendarWeekResponse

week: GetCalendarWeekResponse = await client.calendar.week(2024, 2)
```

## SendouQ

```python
from sendou_sdk import GetSendouqMatchResponse, GetUsersActiveSendouqMatchResponse

active: GetUsersActiveSendouqMatchResponse = await client.sendouq.active_match(123)
match: GetSendouqMatchResponse = await client.sendouq.match(active.match_id)
```

## Tournaments

```python
from sendou_sdk import (
	GetCastedTournamentMatchesResponse,
	GetTournamentBracketResponse,
	GetTournamentBracketStandingsResponse,
	GetTournamentMatchResponse,
	GetTournamentPlayersResponse,
	GetTournamentResponse,
	GetTournamentTeamsResponse,
)

tournament: GetTournamentResponse = await client.tournaments.get(1)
teams: GetTournamentTeamsResponse = await client.tournaments.teams(1)
players: GetTournamentPlayersResponse = await client.tournaments.players(1)
casted: GetCastedTournamentMatchesResponse = await client.tournaments.casted(1)
match: GetTournamentMatchResponse = await client.tournaments.match(10)
bracket: GetTournamentBracketResponse = await client.tournaments.bracket(1, 0)
standings: GetTournamentBracketStandingsResponse = await client.tournaments.bracket_standings(1, 0)
```

### Tournament admin endpoints

```python
from sendou_sdk import TournamentSeedsBody

await client.tournaments.seed(1, TournamentSeedsBody(tournament_team_ids=[1, 2, 3]))
```
