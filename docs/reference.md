# API Reference

## Client

```python
SendouClient(token: str | None = None, base_url: str | None = None)
```

- `await client.request(method, path, params=None)` for low-level access to endpoints not yet wrapped.
- `await client.close()` to close the HTTP client explicitly.
- Supports `async with SendouClient(...)` context manager usage.

## Errors

- `SendouSdkError`
- `SendouApiError`
- `SendouAuthError`
- `SendouRateLimitError`

## Resources

### Users

- `await client.users.get(user_id_or_discord_id_or_custom_url)`
  - Accepts user ID, Discord ID, or custom URL string.
  - If direct `/user/{identifier}` lookup returns 404, the SDK resolves IDs via `get_ids(...)` and retries with numeric user ID.
- `await client.users.get_ids(user_id_discord_id_or_custom)`

### Teams

- `await client.teams.get(team_id)`

### Calendar

- `await client.calendar.week(year, week)`

### SendouQ

- `await client.sendouq.active_match(user_id)`
- `await client.sendouq.match(match_id)`

### Tournaments

- `await client.tournaments.get(tournament_id)`
- `await client.tournaments.teams(tournament_id)`
- `await client.tournaments.players(tournament_id)`
- `await client.tournaments.casted(tournament_id)`
- `await client.tournaments.match(match_id)`
- `await client.tournaments.bracket(tournament_id, bracket_index)`
- `await client.tournaments.bracket_standings(tournament_id, bracket_index)`
- `await client.tournaments.seed(tournament_id, TournamentSeedsBody)`
- `await client.tournaments.starting_brackets(tournament_id, TournamentStartingBracketsBody)`
- `await client.tournaments.add_member(tournament_id, tournament_team_id, TournamentTeamMemberBody)`
- `await client.tournaments.remove_member(tournament_id, tournament_team_id, TournamentTeamMemberBody)`
- `await client.tournaments.update_member_ign(tournament_id, tournament_team_id, TournamentUpdateMemberIgnBody)`

### Organizations

- `await client.organizations.get(organization_id)`

## Data types

### Response models

- `client.users.get(...)` -> `GetUserResponse`
- `client.users.get_ids(...)` -> `GetUserIdsResponse`
- `client.teams.get(...)` -> `GetTeamResponse`
- `client.calendar.week(...)` -> `GetCalendarWeekResponse`
- `client.sendouq.active_match(...)` -> `GetUsersActiveSendouqMatchResponse`
- `client.sendouq.match(...)` -> `GetSendouqMatchResponse`
- `client.tournaments.get(...)` -> `GetTournamentResponse`
- `client.tournaments.teams(...)` -> `GetTournamentTeamsResponse`
- `client.tournaments.players(...)` -> `GetTournamentPlayersResponse`
- `client.tournaments.casted(...)` -> `GetCastedTournamentMatchesResponse`
- `client.tournaments.match(...)` -> `GetTournamentMatchResponse`
- `client.tournaments.bracket(...)` -> `GetTournamentBracketResponse`
- `client.tournaments.bracket_standings(...)` -> `GetTournamentBracketStandingsResponse`
- `client.organizations.get(...)` -> `GetTournamentOrganizationResponse`

### Request body models

- `client.tournaments.seed(...)` -> `TournamentSeedsBody`
- `client.tournaments.starting_brackets(...)` -> `TournamentStartingBracketsBody`
- `client.tournaments.add_member(...)` -> `TournamentTeamMemberBody`
- `client.tournaments.remove_member(...)` -> `TournamentTeamMemberBody`
- `client.tournaments.update_member_ign(...)` -> `TournamentUpdateMemberIgnBody`

### Type aliases

- `GetCalendarWeekResponse` -> `list[CalendarWeekItem]`
- `GetTournamentTeamsResponse` -> `list[TournamentTeam]`
- `GetTournamentPlayersResponse` -> `list[TournamentPlayer]`

