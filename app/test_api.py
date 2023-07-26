import asyncio

from app.api.service import ScoreService, TeamService


async def main():
    # score = await ScoreService.profile_score('007a5d87-4350-498c-abc8-1198d234fd37')
    response = await TeamService.list_teams()
    print(response)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
