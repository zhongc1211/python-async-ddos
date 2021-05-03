import aiohttp
import asyncio
import time


async def get_url(client, i, url):
    async with client.get(url) as resp:
        result = await resp.text()
        return result


async def fetch_html(url, session):
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()
    print(f"Got response [{resp.status}] for URL: {url}")


async def run(i, url, semaphore, client):
    async with semaphore:
        status = await get_url(client, i, url)
        print(f'Request batch {i}:{status} from {url}')
        # await fetch_html(url, client)


async def main(url_list):
    task = []
    # conn = aiohttp.TCPConnector(
    #     family=socket.AF_INET,
    #     verify_ssl=False,
    # )
    semaphore = asyncio.Semaphore(1000)
    async with aiohttp.ClientSession() as client:
        for i, url in enumerate(url_list):
            task.append(run(i, url, semaphore, client))
        await asyncio.gather(*task)


if __name__ == "__main__":
    api_url = ""
    url = api_url + ''
    total_requests = 5000
    url_list = [url]*total_requests
    start1 = time.time()
    asyncio.run(main(url_list))
    print('Time used %.5f seconds' % float(time.time() - start1))