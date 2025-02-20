from TikTokApi import TikTokApi
import asyncio

ms_token = "yvBZrOKf5MiwH2dDKWDgwbcYF4nRKVNyD8L3eayIRXa23AnRFK-V-sTjh51a6j5Bb1NBzqzTjKFQe_OVnupyXxMmWWgIo9XJl0-KuiIr8rcMOD6gV4gJA2jQf5I-bimG0FSUKjjUIsCI8UPyZaKRcURDm"
async def trending_videos():
    print("Starting")
    async with TikTokApi() as api:
        try:
            await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
            print("Sessions created")
            print(await api.trending.videos(count=30))
            
            async for video in api.trending.videos(count=30):
                print("Got video")
                print(video)
            print("done")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(trending_videos())
