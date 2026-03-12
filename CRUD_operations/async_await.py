import httpx
import time
import asyncio
from fastapi import FastAPI

app = FastAPI()
url = "https://official-joke-api.appspot.com/random_joke"

@app.get('/get_jokes')
def get_jokes_sync():
    start = time.time()
    jokes = []
    with httpx.Client() as client:
        for _ in range(10):
            res = client.get(url)
            data = res.json()
            jokes.append(f"{data['setup']} - {data['punchline']}")
    period = time.time() - start
    return {
        "mode" : "sync",
        "jokes" : jokes,
        "time_period" : round(period,3),
    }

@app.get('/get_jokes_async')
async def get_jokes_async():
    start = time.time()
    jokes = []
    async with httpx.AsyncClient() as client:
        task = [client.get(url) for _ in range(10)]
        response = await asyncio.gather(*task)
        for res in response:
            data = res.json()
            jokes.append(f"{data['setup']} - {data['punchline']}")
    period = time.time() - start
    return {
        "mode" : "async",
        "jokes" : jokes,
        "time_period" : round(period,3),
    }
