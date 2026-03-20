import asyncio
import os
from sendou_sdk import SendouClient, GetUserIdsResponse, GetTeamResponse

SENDOU_TOKEN = os.getenv('SENDOU_TOKEN')
SENDOU_USER = os.getenv('SENDOU_USER')

async def main() -> None:
    async with SendouClient(token=SENDOU_TOKEN, base_url='https://sendou.ink/api') as client:
        user = await client.users.get(SENDOU_USER)
        print(f"User: {user.name} ({user.country})")
        for team in user.teams:
            _team: GetTeamResponse = await client.teams.get(team.id)
            print(f"ID: {team.id} Name: {_team.name} Role: {team.role}")
        user_ids: GetUserIdsResponse = await client.users.get_ids(SENDOU_USER)
        print(f"IDs: {user_ids.id}, DISCORD_ID: {user_ids.discord_id}, CUSTOM_URL: {user_ids.custom_url}")
        active = await client.sendouq.active_match(user.id)
        print(f"Active match: {active.match_id}")


if __name__ == "__main__":
    asyncio.run(main())
